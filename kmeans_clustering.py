"""
K-means Clustering for Commuter Demand Analysis
Thesis: Gusa-Bugo Corridor, Cagayan de Oro City

Two separate K-means:
  A) Boarding points (385) - where passengers come from
  B) Alighting points (385) - where passengers go to

Points use WEIGHTED HOTSPOTS: more passengers at a coordinate = higher density = high demand.
All points are within ~250m of the National Highway corridor.
"""

import csv
import random
import math
import os
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Jitter in degrees (~10m at this latitude) so points arent perfectly stacked
JITTER = 0.00009

# Weighted hotspots along the National Highway corridor (6 barangays + Cogon)
# More passengers per hotspot = higher K-means density
BOARDING_HOTSPOTS = [
    # (label, barangay, lat, lon, weight)  total = 385
    ('Bugo Public Market',        'Bugo',   8.5055, 124.7540, 65),
    ('Bugo Highway',              'Bugo',   8.5070, 124.7535, 50),
    ('Puerto National Highway',   'Puerto', 8.5005, 124.7505, 55),
    ('Puerto Junction',           'Puerto', 8.5015, 124.7495, 25),
    ('Agusan Crossing',           'Agusan', 8.4885, 124.7380, 20),
    ('Agusan Highway',            'Agusan', 8.4895, 124.7370, 15),
    ('Tablon Crossing',           'Tablon', 8.4820, 124.7285, 25),
    ('Tablon Highway',            'Tablon', 8.4810, 124.7295, 10),
    ('Cugman Highway',            'Cugman', 8.4700, 124.7050, 20),
    ('Cugman Crossing',           'Cugman', 8.4690, 124.7060, 10),
    ('Gusa National Highway',     'Gusa',   8.4760, 124.6820, 50),
    ('Gusa Crossing',             'Gusa',   8.4750, 124.6830, 40),
]

ALIGHTING_HOTSPOTS = [
    # (label, barangay, lat, lon, weight)  total = 385
    ('Cogon Market',              'Cogon',  8.4775, 124.6460, 130),
    ('Cogon Downtown',            'Cogon',  8.4770, 124.6470, 65),
    ('Cogon Terminal',            'Cogon',  8.4765, 124.6455, 30),
    ('Bugo Public Market',        'Bugo',   8.5055, 124.7540, 30),
    ('Puerto National Highway',   'Puerto', 8.5005, 124.7505, 25),
    ('Puerto Junction',           'Puerto', 8.5015, 124.7495, 15),
    ('Agusan Crossing',           'Agusan', 8.4885, 124.7380, 15),
    ('Tablon Crossing',           'Tablon', 8.4820, 124.7285, 15),
    ('Cugman Highway',            'Cugman', 8.4700, 124.7050, 12),
    ('Gusa National Highway',     'Gusa',   8.4760, 124.6820, 15),
    ('Gusa Crossing',             'Gusa',   8.4750, 124.6830, 13),
    ('Bugo Highway',              'Bugo',   8.5070, 124.7535, 10),
    ('Tablon Highway',            'Tablon', 8.4810, 124.7295,  5),
    ('Agusan Highway',            'Agusan', 8.4895, 124.7370,  3),
    ('Cugman Crossing',           'Cugman', 8.4690, 124.7060,  2),
]

WAITING_TIME_CATS = ['<5 min', '5-10 min', '11-15 min', '16-20 min', '>20 min']
WAITING_TIME_WEIGHTS = [0.12, 0.35, 0.30, 0.15, 0.08]

WAITING_LOCATIONS = [
    'Waiting Shed', 'Sidewalk', 'Road Shoulder',
    'In Front of Establishment', 'Under a Tree', 'Others'
]
WAITING_LOC_WEIGHTS = [0.05, 0.35, 0.30, 0.15, 0.10, 0.05]

STOPPING_PATTERNS = ['Designated Stop', 'Anywhere Along Road', 'Informal Common Spot']
STOPPING_WEIGHTS = [0.25, 0.45, 0.30]


def jitter(lat, lon, sigma=JITTER):
    return round(lat + random.gauss(0, sigma), 6), round(lon + random.gauss(0, sigma), 6)


def generate_survey_csv(n=385, path=None):
    if path is None:
        path = os.path.join(DATA_DIR, 'mock_commuter_survey.csv')

    total_board_weight = sum(h[4] for h in BOARDING_HOTSPOTS)
    total_alight_weight = sum(h[4] for h in ALIGHTING_HOTSPOTS)

    fields = [
        'respondent_id', 'boarding_barangay', 'boarding_lat', 'boarding_lon', 'boarding_hotspot',
        'alighting_barangay', 'alighting_lat', 'alighting_lon', 'alighting_hotspot',
        'waiting_time_cat', 'waiting_location', 'stopping_pattern', 'is_route_endpoint',
    ]

    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i in range(n):
            # Pick boarding hotspot by weight
            r = random.random() * total_board_weight
            cumul = 0
            for label, brgy, lat, lon, wt in BOARDING_HOTSPOTS:
                cumul += wt
                if r <= cumul:
                    blat, blon = jitter(lat, lon)
                    b_brgy = brgy
                    b_label = label
                    break

            # Pick alighting hotspot by weight
            r = random.random() * total_alight_weight
            cumul = 0
            for label, brgy, lat, lon, wt in ALIGHTING_HOTSPOTS:
                cumul += wt
                if r <= cumul:
                    alat, alon = jitter(lat, lon)
                    a_brgy = brgy
                    a_label = label
                    break

            wt_idx = random.choices(range(5), weights=WAITING_TIME_WEIGHTS, k=1)[0]
            wl_idx = random.choices(range(6), weights=WAITING_LOC_WEIGHTS, k=1)[0]
            sp_idx = random.choices(range(3), weights=STOPPING_WEIGHTS, k=1)[0]
            ep = 1 if a_brgy in ('Bugo', 'Cogon') and random.random() < 0.7 else 0

            w.writerow({
                'respondent_id': f'R{i+1:03d}',
                'boarding_barangay': b_brgy,
                'boarding_lat': blat,
                'boarding_lon': blon,
                'boarding_hotspot': b_label,
                'alighting_barangay': a_brgy,
                'alighting_lat': alat,
                'alighting_lon': alon,
                'alighting_hotspot': a_label,
                'waiting_time_cat': WAITING_TIME_CATS[wt_idx],
                'waiting_location': WAITING_LOCATIONS[wl_idx],
                'stopping_pattern': STOPPING_PATTERNS[sp_idx],
                'is_route_endpoint': ep,
            })

    print(f'[1/6] Survey data -> {path} ({n} rows)')
    return path


def load_coords(csv_path):
    board, alight = [], []
    with open(csv_path, 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            board.append([float(row['boarding_lat']), float(row['boarding_lon'])])
            alight.append([float(row['alighting_lat']), float(row['alighting_lon'])])
    return np.array(board), np.array(alight)


def run_kmeans(X, k=3, label=''):
    km = KMeans(n_clusters=k, random_state=RANDOM_SEED, n_init=10)
    labels = km.fit_predict(X)
    sil = silhouette_score(X, labels)
    counts = {}
    for lbl in labels:
        counts[lbl] = counts.get(lbl, 0) + 1
    sorted_ids = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    demand_map = {
        sorted_ids[0]: 'High Demand',
        sorted_ids[1]: 'Moderate Demand',
        sorted_ids[2]: 'Low Demand',
    }
    demand_labels = [demand_map[l] for l in labels]

    print(f'\n  [{label}] K-means k=3 - Silhouette: {sil:.4f}')
    for cid in sorted_ids:
        print(f'    Cluster {cid}: {demand_map[cid]} - {counts[cid]} pts')
    print(f'    Centroids:')
    for cid in sorted_ids:
        c = km.cluster_centers_[cid]
        print(f'      C{cid+1} ({demand_map[cid]}): Lat={c[0]:.5f}, Lon={c[1]:.5f}')

    return km, labels, demand_labels, demand_map, sil


def export_csv(csv_path, coords, labels, demand, label, output_dir):
    out_path = os.path.join(output_dir, f'kmeans_{label}.csv')
    with open(csv_path, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    fields = [
        'respondent_id', 'lat', 'lon', 'point_type', 'kmeans_cluster',
        'demand_level', 'boarding_barangay', 'alighting_barangay',
        'boarding_hotspot', 'alighting_hotspot',
        'waiting_time_cat', 'waiting_location', 'stopping_pattern', 'is_route_endpoint',
    ]
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, row in enumerate(rows):
            w.writerow({
                'respondent_id': row['respondent_id'],
                'lat': coords[i, 0], 'lon': coords[i, 1],
                'point_type': label,
                'kmeans_cluster': int(labels[i]),
                'demand_level': demand[i],
                'boarding_barangay': row['boarding_barangay'],
                'alighting_barangay': row['alighting_barangay'],
                'boarding_hotspot': row['boarding_hotspot'],
                'alighting_hotspot': row['alighting_hotspot'],
                'waiting_time_cat': row['waiting_time_cat'],
                'waiting_location': row['waiting_location'],
                'stopping_pattern': row['stopping_pattern'],
                'is_route_endpoint': row['is_route_endpoint'],
            })
    print(f'  [Export] {out_path}')
    return out_path


def export_combined(csv_path, board_coords, board_labels, board_demand,
                    alight_coords, alight_labels, alight_demand, output_dir):
    out_path = os.path.join(output_dir, 'kmeans_all_points.csv')
    with open(csv_path, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    fields = [
        'respondent_id', 'lat', 'lon', 'point_type', 'kmeans_cluster',
        'demand_level', 'boarding_barangay', 'alighting_barangay',
        'boarding_hotspot', 'alighting_hotspot',
        'waiting_time_cat', 'waiting_location', 'stopping_pattern', 'is_route_endpoint',
    ]
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, row in enumerate(rows):
            w.writerow({
                'respondent_id': row['respondent_id'], 'point_type': 'boarding',
                'lat': board_coords[i, 0], 'lon': board_coords[i, 1],
                'kmeans_cluster': int(board_labels[i]),
                'demand_level': board_demand[i],
                **{k: row[k] for k in fields if k in row},
            })
            w.writerow({
                'respondent_id': row['respondent_id'], 'point_type': 'alighting',
                'lat': alight_coords[i, 0], 'lon': alight_coords[i, 1],
                'kmeans_cluster': int(alight_labels[i]),
                'demand_level': alight_demand[i],
                **{k: row[k] for k in fields if k in row},
            })
    print(f'  [Export] {out_path}')


def plot_clusters(coords, labels, demand_labels, centroids, demand_map, title, filename, output_dir):
    color_map = {'High Demand': '#e63946', 'Moderate Demand': '#f4a261', 'Low Demand': '#2a9d8f'}
    fig, ax = plt.subplots(figsize=(10, 8))

    for dl in ['High Demand', 'Moderate Demand', 'Low Demand']:
        mask = np.array(demand_labels) == dl
        if np.any(mask):
            ax.scatter(coords[mask, 1], coords[mask, 0],
                       c=color_map[dl], label=dl, alpha=0.6, s=20)

    ax.scatter(centroids[:, 1], centroids[:, 0],
               c='black', marker='X', s=200, edgecolors='white', linewidths=1.5,
               label='Centroids', zorder=5)

    for cid, dn in demand_map.items():
        c = centroids[cid]
        short = dn.replace(' Demand', '')
        ax.annotate(f'  {short}', (c[1], c[0]),
                    fontsize=10, fontweight='bold', color='black', zorder=6)

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(title)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, filename)
    fig.savefig(path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'  [Plot] {path}')


def plot_elbow(X, output_dir, max_k=10):
    ks = range(2, max_k + 1)
    inertias, sils = [], []
    for k in ks:
        km = KMeans(n_clusters=k, random_state=RANDOM_SEED, n_init=10)
        labels = km.fit_predict(X)
        inertias.append(km.inertia_)
        sils.append(silhouette_score(X, labels))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ax1.plot(ks, inertias, 'o-', color='#457b9d', linewidth=2)
    ax1.axvline(x=3, color='#e63946', linestyle='--', alpha=0.5, label='k=3')
    ax1.set_xlabel('k'); ax1.set_ylabel('Inertia'); ax1.set_title('Elbow Method')
    ax1.legend(); ax1.grid(alpha=0.3)

    ax2.plot(ks, sils, 's-', color='#2a9d8f', linewidth=2)
    ax2.axvline(x=3, color='#e63946', linestyle='--', alpha=0.5, label='k=3')
    ax2.set_xlabel('k'); ax2.set_ylabel('Silhouette'); ax2.set_title('Silhouette Analysis')
    ax2.legend(); ax2.grid(alpha=0.3)

    fig.suptitle('Optimal k Determination', fontsize=14, fontweight='bold')
    path = os.path.join(output_dir, 'elbow_plot.png')
    fig.savefig(path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'  [Plot] {path}')


def create_qml(output_dir):
    qml = r"""<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology" version="3.28">
  <renderer-v2 type="categorizedSymbol" attr="demand_level" label="">
    <categories>
      <category value="High Demand" symbol="0" label="High Demand"/>
      <category value="Moderate Demand" symbol="1" label="Moderate Demand"/>
      <category value="Low Demand" symbol="2" label="Low Demand"/>
    </categories>
    <symbols>
      <symbol name="0" type="marker" alpha="1"><layer pass="0" class="SimpleMarker" enabled="1"><prop k="color" v="230,57,70,255"/><prop k="name" v="circle"/><prop k="size" v="3"/></layer></symbol>
      <symbol name="1" type="marker" alpha="1"><layer pass="0" class="SimpleMarker" enabled="1"><prop k="color" v="244,162,97,255"/><prop k="name" v="circle"/><prop k="size" v="3"/></layer></symbol>
      <symbol name="2" type="marker" alpha="1"><layer pass="0" class="SimpleMarker" enabled="1"><prop k="color" v="42,157,143,255"/><prop k="name" v="circle"/><prop k="size" v="3"/></layer></symbol>
    </symbols>
  </renderer-v2>
</qgis>"""
    path = os.path.join(output_dir, 'kmeans_qgis_layer.qml')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(qml)
    print(f'  [QML] {path}')


def main():
    print('=' * 60)
    print('K-MEANS CLUSTERING - Gusa-Bugo Corridor, CDO')
    print('Weighted hotspots along National Highway')
    print('=' * 60)

    csv_path = generate_survey_csv(385)
    board_coords, alight_coords = load_coords(csv_path)

    # K-means A: BOARDING
    print('\n--- K-MEANS A: BOARDING (origins) ---')
    km_b, labels_b, demand_b, demand_map_b, sil_b = run_kmeans(board_coords, 3, 'BOARDING')
    export_csv(csv_path, board_coords, labels_b, demand_b, 'boarding', OUTPUT_DIR)
    plot_clusters(board_coords, labels_b, demand_b, km_b.cluster_centers_, demand_map_b,
                  'K-means: Boarding Locations (Origins)\nGusa-Bugo Corridor, CDO',
                  'kmeans_boarding_map.png', OUTPUT_DIR)

    # K-means B: ALIGHTING
    print('\n--- K-MEANS B: ALIGHTING (destinations) ---')
    km_a, labels_a, demand_a, demand_map_a, sil_a = run_kmeans(alight_coords, 3, 'ALIGHTING')
    export_csv(csv_path, alight_coords, labels_a, demand_a, 'alighting', OUTPUT_DIR)
    plot_clusters(alight_coords, labels_a, demand_a, km_a.cluster_centers_, demand_map_a,
                  'K-means: Alighting Locations (Destinations)\nGusa-Bugo Corridor, CDO',
                  'kmeans_alighting_map.png', OUTPUT_DIR)

    # Combined
    export_combined(csv_path, board_coords, labels_b, demand_b,
                    alight_coords, labels_a, demand_a, OUTPUT_DIR)

    all_coords = np.vstack([board_coords, alight_coords])
    plot_elbow(all_coords, OUTPUT_DIR)
    create_qml(OUTPUT_DIR)

    print('\n' + '=' * 60)
    print('ALL OUTPUTS GENERATED')
    print('=' * 60)
    print(f'\nOutputs in: {OUTPUT_DIR}')


if __name__ == '__main__':
    main()

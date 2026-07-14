"""
K-means Clustering by Barangay — Hierarchical Approach
Thesis: Gusa-Bugo Corridor, Cagayan de Oro City

6 per-barangay K-means (k=3) + 1 overall K-means on top 18 modal hotspot candidates.

Per-barangay: identifies 3 cluster centroids + modal hotspot per cluster.
Overall:      K-means (k=3) on 18 modal hotspot coordinates, weighted by demand.
Ranking:      composite score = cluster_size x demand_multiplier -> facility type.
"""

import csv
import os
import sys
import random
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
import kmeans_clustering as kmc

RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

OUTPUT_DIR = kmc.OUTPUT_DIR
DATA_DIR = kmc.DATA_DIR

BARANGAYS = ['Gusa', 'Cugman', 'Tablon', 'Agusan', 'Puerto', 'Bugo']
DEMAND_MULT = {'High Demand': 3, 'Moderate Demand': 2, 'Low Demand': 1}

BRGY_COLORS = {
    'Gusa': '#00b4d8', 'Cugman': '#9b5de5', 'Tablon': '#457b9d',
    'Agusan': '#2a9d8f', 'Puerto': '#f4a261', 'Bugo': '#e63946',
}
DEMAND_COLORS = {
    'High Demand': '#e63946',
    'Moderate Demand': '#f4a261',
    'Low Demand': '#2a9d8f',
}
FACILITY_COLORS = {
    'Terminal': '#e63946',
    'Waiting Station': '#f4a261',
    'Loading/Unloading Zone': '#2a9d8f',
}


def get_hotspots_by_brgy():
    """Build lookup: barangay -> list of (label, lat, lon, weight)."""
    lookup = {}
    for h in kmc.BOARDING_HOTSPOTS:
        label, brgy, lat, lon, wt = h
        lookup.setdefault(brgy, []).append((label, lat, lon, wt))
    return lookup


HOTSPOT_BY_BRGY = get_hotspots_by_brgy()


def filter_by_barangay(csv_path, barangay):
    """Load boarding rows for a specific barangay."""
    coords, rows = [], []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['boarding_barangay'] == barangay:
                coords.append([float(row['boarding_lat']), float(row['boarding_lon'])])
                rows.append(row)
    return np.array(coords), rows


def find_modal_hotspot(cluster_coords, barangay_hotspots):
    """
    Given the coordinates of points in one cluster and the list of hotspot
    entries for that barangay, return the hotspot (label, lat, lon, weight)
    whose coordinate is closest to the mean of the cluster points.
    """
    if len(cluster_coords) == 0:
        return barangay_hotspots[0]
    mean_lat = np.mean(cluster_coords[:, 0])
    mean_lon = np.mean(cluster_coords[:, 1])
    best = None
    best_dist = float('inf')
    for label, hlat, hlon, hwt in barangay_hotspots:
        d = (hlat - mean_lat) ** 2 + (hlon - mean_lon) ** 2
        if d < best_dist:
            best_dist = d
            best = (label, hlat, hlon, hwt)
    return best


def run_kmeans_brgy(X, rows, barangay):
    """Run K-means on one barangay's boarding points. Returns result dict or None."""
    n = len(X)
    if n < 2:
        print(f'  [{barangay}] Skipped — only {n} point(s)')
        return None

    k = min(3, n)
    km = KMeans(n_clusters=k, random_state=RANDOM_SEED, n_init=10)
    labels = km.fit_predict(X)
    sil = silhouette_score(X, labels) if len(set(labels)) > 1 else 0.0

    counts = {}
    for lbl in labels:
        counts[lbl] = counts.get(lbl, 0) + 1
    sorted_ids = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    demand_map = {}
    demand_levels = ['High Demand', 'Moderate Demand', 'Low Demand']
    for i, cid in enumerate(sorted_ids):
        demand_map[cid] = demand_levels[i] if i < 3 else f'Cluster {cid}'
    demand_labels = [demand_map[l] for l in labels]

    # For each cluster, find modal hotspot
    brgy_hotspots = HOTSPOT_BY_BRGY.get(barangay, [])
    cluster_hotspots = {}
    for cid in range(k):
        mask = labels == cid
        if np.any(mask):
            cluster_hotspots[cid] = find_modal_hotspot(X[mask], brgy_hotspots)
        else:
            cluster_hotspots[cid] = brgy_hotspots[0] if brgy_hotspots else ('Unknown', 0, 0, 0)

    print(f'\n  [{barangay}] K-means k={k} — Silhouette: {sil:.4f} — Points: {n}')
    for cid in sorted_ids:
        hs = cluster_hotspots[cid]
        print(f'    Cluster {cid}: {demand_map[cid]} — {counts[cid]} pts — Modal: {hs[0]}')
    print(f'    Centroids:')
    for cid in range(k):
        c = km.cluster_centers_[cid]
        print(f'      C{cid+1}: Lat={c[0]:.5f}, Lon={c[1]:.5f}')

    return {
        'km': km, 'labels': labels, 'demand_labels': demand_labels,
        'demand_map': demand_map, 'sil': sil, 'counts': counts,
        'cluster_hotspots': cluster_hotspots, 'k': k,
    }


def export_brgy_csv(csv_path, coords, result, barangay, output_dir):
    """Export per-barangay K-means results to CSV."""
    out = os.path.join(output_dir, f'kmeans_brgy_{barangay.lower()}.csv')
    with open(csv_path, 'r', encoding='utf-8') as f:
        all_rows = list(csv.DictReader(f))
    brgy_rows = [r for r in all_rows if r['boarding_barangay'] == barangay]

    fields = [
        'respondent_id', 'lat', 'lon', 'kmeans_cluster', 'demand_level',
        'modal_hotspot', 'alighting_barangay',
        'waiting_time_cat', 'waiting_location', 'stopping_pattern',
    ]
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, row in enumerate(brgy_rows):
            w.writerow({
                'respondent_id': row['respondent_id'],
                'lat': coords[i, 0], 'lon': coords[i, 1],
                'kmeans_cluster': int(result['labels'][i]),
                'demand_level': result['demand_labels'][i],
                'modal_hotspot': result['cluster_hotspots'][result['labels'][i]][0],
                'alighting_barangay': row['alighting_barangay'],
                'waiting_time_cat': row['waiting_time_cat'],
                'waiting_location': row['waiting_location'],
                'stopping_pattern': row['stopping_pattern'],
            })
    print(f'  [Export] {out}')
    return out


def plot_all_brgy(per_brgy_data, output_dir):
    """Plot all 6 barangays in a 2x3 grid with centroids + modal hotspots."""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    axes = axes.flatten()

    for idx, brgy in enumerate(BARANGAYS):
        ax = axes[idx]
        data = per_brgy_data.get(brgy)
        if data is None or len(data['coords']) < 2:
            ax.text(0.5, 0.5, f'{brgy}\nInsufficient data', ha='center', va='center', fontsize=12)
            ax.set_title(brgy)
            continue

        coords = data['coords']
        result = data['result']
        demand_labels = result['demand_labels']
        centroids = result['km'].cluster_centers_
        cluster_hotspots = result['cluster_hotspots']

        for dl in ['High Demand', 'Moderate Demand', 'Low Demand']:
            mask = np.array(demand_labels) == dl
            if np.any(mask):
                ax.scatter(coords[mask, 1], coords[mask, 0],
                           c=DEMAND_COLORS[dl], label=dl, alpha=0.6, s=18)

        # Centroids
        ax.scatter(centroids[:, 1], centroids[:, 0],
                   c='black', marker='X', s=150, edgecolors='white', linewidths=1.5, zorder=5,
                   label='Centroids')

        # Modal hotspot markers
        for cid, hs in cluster_hotspots.items():
            label, hlat, hlon, hwt = hs
            dl = result['demand_map'].get(cid, 'Unknown')
            color = DEMAND_COLORS.get(dl, '#888')
            ax.scatter(hlon, hlat, marker='*', s=200,
                       c=color, edgecolors='black', linewidths=1.2, zorder=6)
            ax.annotate(f'{label}', (hlon, hlat),
                        textcoords='offset points', xytext=(5, 5),
                        fontsize=7, fontweight='bold', zorder=7)

        ax.set_title(f'{brgy} (n={len(coords)})', fontweight='bold')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.grid(True, alpha=0.3)
        if idx == 0:
            ax.legend(fontsize=7, loc='upper right')

    fig.suptitle('Per-Barangay K-means Clustering — Boarding Points\n'
                 'Gusa-Bugo Corridor, CDO',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    path = os.path.join(output_dir, 'kmeans_per_brgy_map.png')
    fig.savefig(path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'\n[Plot] {path}')


def classify_facility(demand_level, is_endpoint, stopping_pattern, waiting_time):
    """Thesis Section 3.7 facility type logic."""
    high = demand_level == 'High Demand'
    mod = demand_level in ('High Demand', 'Moderate Demand')
    endpoint = is_endpoint == '1'
    organized = stopping_pattern == 'Designated Stop'
    chaotic = stopping_pattern in ('Anywhere Along Road', 'Informal Common Spot')
    long_wait = waiting_time in ('11-15 min', '16-20 min', '>20 min')

    if endpoint and high:
        return 'Terminal'
    if mod and chaotic and not endpoint:
        return 'Loading/Unloading Zone'
    if high and long_wait and not organized:
        return 'Waiting Station'
    if mod:
        return 'Waiting Station'
    return 'Waiting Station'


def build_candidates(per_brgy_data, csv_path):
    """
    Build list of 18 candidate dicts (one per cluster across all barangays).

    Each candidate:
      barangay, modal_hotspot, lat, lon, weight, demand_level,
      composite_score, is_endpoint, stopping_pattern, waiting_time
    """
    candidates = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        all_rows = list(csv.DictReader(f))

    for brgy in BARANGAYS:
        data = per_brgy_data.get(brgy)
        if data is None:
            continue
        result = data['result']
        brgy_rows = [r for r in all_rows if r['boarding_barangay'] == brgy]

        for cid in range(result['k']):
            hs = result['cluster_hotspots'][cid]
            label, hlat, hlon, hwt = hs
            weight = result['counts'][cid]
            dl = result['demand_map'][cid]
            score = weight * DEMAND_MULT.get(dl, 1)

            # Get a representative survey row from this cluster
            mask = result['labels'] == cid
            cluster_indices = np.where(mask)[0]
            rep_row = brgy_rows[cluster_indices[0]] if len(cluster_indices) > 0 else brgy_rows[0]

            candidates.append({
                'barangay': brgy,
                'modal_hotspot': label,
                'lat': hlat,
                'lon': hlon,
                'weight': weight,
                'demand_level': dl,
                'composite_score': score,
                'is_endpoint': rep_row.get('is_route_endpoint', '0'),
                'stopping_pattern': rep_row.get('stopping_pattern', ''),
                'waiting_time': rep_row.get('waiting_time_cat', ''),
                'cluster_id': cid,
            })

    # Sort by composite score descending
    candidates.sort(key=lambda c: c['composite_score'], reverse=True)
    return candidates


def run_overall_kmeans(candidates, output_dir):
    """Run overall K-means (k=3) on 18 candidate points weighted by composite score."""
    if len(candidates) < 3:
        print('Not enough candidates for overall K-means.')
        return None, None, None, None

    X = np.array([[c['lat'], c['lon']] for c in candidates])
    W = np.array([c['composite_score'] for c in candidates], dtype=float)
    k_overall = min(3, len(candidates))

    km = KMeans(n_clusters=k_overall, random_state=RANDOM_SEED, n_init=10)
    km.fit(X, sample_weight=W)
    labels = km.predict(X)

    # Determine demand levels by cluster size
    counts = {}
    for lbl in labels:
        counts[lbl] = counts.get(lbl, 0) + 1
    sorted_ids = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    dl_map = {}
    dlv = ['High Demand', 'Moderate Demand', 'Low Demand']
    for i, cid in enumerate(sorted_ids):
        dl_map[cid] = dlv[i] if i < 3 else f'Cluster {cid}'
    demand_labels = [dl_map[l] for l in labels]

    sil = silhouette_score(X, labels) if len(set(labels)) > 1 else 0.0

    print(f'\n  Overall K-means k={k_overall} — Silhouette: {sil:.4f}')
    for cid in sorted_ids:
        names = [candidates[i]['modal_hotspot'] for i in range(len(candidates)) if labels[i] == cid]
        print(f'    Cluster {cid}: {dl_map[cid]} — {counts[cid]} candidates')
        for n in names:
            print(f'      — {n}')
    print(f'    Centroids:')
    for cid in range(k_overall):
        c = km.cluster_centers_[cid]
        print(f'      C{cid+1} ({dl_map.get(cid, "N/A")}): Lat={c[0]:.5f}, Lon={c[1]:.5f}')

    return km, labels, demand_labels, sil


def export_candidates_csv(candidates, overall_labels, overall_demand_labels, output_dir):
    """Export ranked candidates with overall cluster + facility type."""
    for i, c in enumerate(candidates):
        c['overall_cluster'] = int(overall_labels[i]) if overall_labels is not None else -1
        c['overall_demand'] = overall_demand_labels[i] if overall_demand_labels is not None else ''
        c['facility_type'] = classify_facility(
            c['demand_level'], c['is_endpoint'],
            c['stopping_pattern'], c['waiting_time'],
        )

    # Ranked candidates CSV
    path1 = os.path.join(output_dir, 'top18_candidates_ranked.csv')
    fields = [
        'rank', 'barangay', 'modal_hotspot', 'lat', 'lon',
        'weight', 'demand_level', 'composite_score',
        'overall_cluster', 'overall_demand', 'facility_type',
        'is_endpoint', 'stopping_pattern', 'waiting_time',
    ]
    with open(path1, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, c in enumerate(candidates):
            w.writerow({
                'rank': i + 1,
                'barangay': c['barangay'],
                'modal_hotspot': c['modal_hotspot'],
                'lat': c['lat'], 'lon': c['lon'],
                'weight': c['weight'],
                'demand_level': c['demand_level'],
                'composite_score': c['composite_score'],
                'overall_cluster': c['overall_cluster'],
                'overall_demand': c['overall_demand'],
                'facility_type': c['facility_type'],
                'is_endpoint': c['is_endpoint'],
                'stopping_pattern': c['stopping_pattern'],
                'waiting_time': c['waiting_time'],
            })
    print(f'\n[Export] {path1}')

    # Per-facility-type breakdown
    path2 = os.path.join(output_dir, 'top18_facilities.csv')
    ffields = ['rank', 'barangay', 'modal_hotspot', 'lat', 'lon',
               'demand_level', 'composite_score', 'overall_demand', 'facility_type']
    with open(path2, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=ffields)
        w.writeheader()
        for i, c in enumerate(candidates):
            w.writerow({
                'rank': i + 1,
                'barangay': c['barangay'],
                'modal_hotspot': c['modal_hotspot'],
                'lat': c['lat'], 'lon': c['lon'],
                'demand_level': c['demand_level'],
                'composite_score': c['composite_score'],
                'overall_demand': c['overall_demand'],
                'facility_type': c['facility_type'],
            })
    print(f'[Export] {path2}')

    # Summary
    print(f'\nFacility type distribution:')
    type_counts = {}
    for c in candidates:
        ft = c['facility_type']
        type_counts[ft] = type_counts.get(ft, 0) + 1
    for t, n in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f'  {t}: {n}')

    return path1, path2


def plot_overall(candidates, overall_km, overall_labels, overall_demand_labels, output_dir):
    """Plot overall K-means on 18 candidate points."""
    if overall_km is None:
        return

    fig, ax = plt.subplots(figsize=(12, 9))

    X = np.array([[c['lat'], c['lon']] for c in candidates])

    # Draw overall cluster regions via a mesh
    lat_min, lat_max = X[:, 0].min() - 0.005, X[:, 0].max() + 0.005
    lon_min, lon_max = X[:, 1].min() - 0.005, X[:, 1].max() + 0.005
    xx, yy = np.meshgrid(
        np.linspace(lon_min, lon_max, 200),
        np.linspace(lat_min, lat_max, 200),
    )
    Z = overall_km.predict(np.c_[yy.ravel(), xx.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot decision regions
    cmap_reg = {0: '#fee5d9', 1: '#fdd0a2', 2: '#e5f5e0'}
    for cid in range(overall_km.n_clusters):
        color = cmap_reg.get(cid, '#f0f0f0')
        mask = Z == cid
        ax.contourf(xx, yy, Z, levels=[cid - 0.5, cid + 0.5], colors=[color], alpha=0.3)

    # Plot centroids
    centroids = overall_km.cluster_centers_
    ax.scatter(centroids[:, 1], centroids[:, 0],
               c='black', marker='X', s=300, edgecolors='white',
               linewidths=2, zorder=8, label='Overall Centroids')

    # Plot each candidate
    for i, c in enumerate(candidates):
        dl = overall_demand_labels[i] if overall_demand_labels else c['demand_level']
        ft = c.get('facility_type', 'Waiting Station')
        fc = FACILITY_COLORS.get(ft, '#888')
        size = 50 + c['composite_score'] * 3
        edge = 'black' if c['composite_score'] >= 100 else '#666'
        ax.scatter(c['lon'], c['lat'], c=fc, s=size,
                   edgecolors=edge, linewidths=1.2, zorder=6, alpha=0.85)
        ax.annotate(f'{c["barangay"]}:{c["modal_hotspot"][:12]}',
                    (c['lon'], c['lat']),
                    textcoords='offset points', xytext=(6, 6),
                    fontsize=7, fontweight='bold', zorder=7)

    # Legend for facility types
    for ft, fc in FACILITY_COLORS.items():
        ax.scatter([], [], c=fc, label=f'Facility: {ft}', alpha=0.8, s=40)
    ax.scatter([], [], c='white', edgecolors='black', s=60, label='Size = composite score')
    ax.scatter([], [], marker='X', c='black', s=150, label='Overall centroids')

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Overall K-means on Top 18 Candidate Points\n'
                 'Gusa-Bugo Corridor, CDO',
                 fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, 'kmeans_overall_map.png')
    fig.savefig(path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'[Plot] {path}')


def print_ranking_table(candidates, overall_labels, overall_demand_labels):
    """Print a terminal summary table of the top 18 ranked candidates."""
    print('\n' + '=' * 100)
    print('RANKED CANDIDATES (by composite score)')
    print('=' * 100)
    header = f'{"Rank":<5} {"Barangay":<10} {"Modal Hotspot":<30} {"Wt":<6} {"Demand":<16} {"Score":<8} {"OvrCluster":<12} {"Facility":<22}'
    print(header)
    print('-' * 100)
    for i, c in enumerate(candidates):
        ol = overall_labels[i] if overall_labels is not None else -1
        od = overall_demand_labels[i] if overall_demand_labels is not None else ''
        ft = c.get('facility_type', '')
        print(
            f'{i + 1:<5} {c["barangay"]:<10} {c["modal_hotspot"]:<30} '
            f'{c["weight"]:<6} {c["demand_level"]:<16} {c["composite_score"]:<8} '
            f'C{ol} {od:<8} {ft:<22}'
        )


def main():
    print('=' * 60)
    print('K-MEANS BY BARANGAY — Hierarchical Clustering')
    print('6 per-barangay -> 18 modal hotspot candidates -> overall K-means')
    print('=' * 60)

    # 1. Generate mock survey data
    csv_path = kmc.generate_survey_csv(385)

    # 2. Per-barangay K-means
    print('\n' + '=' * 60)
    print('PER-BARANGAY K-MEANS')
    print('=' * 60)

    per_brgy_data = {}

    for brgy in BARANGAYS:
        coords, rows = filter_by_barangay(csv_path, brgy)
        if len(coords) < 2:
            print(f'  [{brgy}] Skipped — only {len(coords)} point(s)')
            continue

        result = run_kmeans_brgy(coords, rows, brgy)
        if result is None:
            continue

        export_brgy_csv(csv_path, coords, result, brgy, OUTPUT_DIR)
        per_brgy_data[brgy] = {'coords': coords, 'result': result}

    # 3. Plot per-barangay grid
    plot_all_brgy(per_brgy_data, OUTPUT_DIR)

    # 4. Build 18 candidates
    print('\n' + '=' * 60)
    print('BUILDING TOP 18 CANDIDATES (modal hotspots)')
    print('=' * 60)
    candidates = build_candidates(per_brgy_data, csv_path)
    print(f'  Total candidates: {len(candidates)}')
    for i, c in enumerate(candidates):
        print(f'  {i+1:>2}. [{c["barangay"]:<8}] {c["modal_hotspot"]:<30} '
              f'wt={c["weight"]:<3} {c["demand_level"]:<15} score={c["composite_score"]}')

    # 5. Overall K-means on 18 points
    print('\n' + '=' * 60)
    print('OVERALL K-MEANS (18 candidates)')
    print('=' * 60)
    overall_km, overall_labels, overall_demand_labels, overall_sil = run_overall_kmeans(
        candidates, OUTPUT_DIR
    )

    # 6. Export with facility type
    export_candidates_csv(candidates, overall_labels, overall_demand_labels, OUTPUT_DIR)

    # 7. Plot overall
    plot_overall(candidates, overall_km, overall_labels, overall_demand_labels, OUTPUT_DIR)

    # 8. Terminal ranking table
    print_ranking_table(candidates, overall_labels, overall_demand_labels)

    print('\n' + '=' * 60)
    print(f'ALL OUTPUTS IN: {OUTPUT_DIR}')
    print('=' * 60)


if __name__ == '__main__':
    main()

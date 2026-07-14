"""
Facility Type Recommender
Uses K-means cluster outputs + survey data to assign facility types per POINT.

Decision logic (per thesis Section 3.7):
  TERMINAL        = route endpoint + high demand + jeepneys start/end here
  WAITING STATION = high demand + prolonged waiting + no organized stop
  LOADING ZONE    = moderate-high demand + frequent boarding/alighting + irregular stopping

Note: facility type is assigned PER BOARDING POINT, not per barangay.
Multiple types may exist in one barangay.
"""

import csv
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
SURVEY_PATH = os.path.join(os.path.dirname(__file__), 'data', 'mock_commuter_survey.csv')
BOARDING_CSV = os.path.join(OUTPUT_DIR, 'kmeans_boarding.csv')

FACILITY_COLORS = {
    'Terminal': '#e63946',
    'Waiting Station': '#f4a261',
    'Loading/Unloading Zone': '#2a9d8f',
}


def classify_facility(demand_level, is_endpoint, stopping_pattern, waiting_time):
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


def main():
    print('=' * 60)
    print('FACILITY TYPE RECOMMENDER')
    print('Per-point classification using thesis Section 3.7 criteria')
    print('=' * 60)

    with open(SURVEY_PATH, 'r', encoding='utf-8') as f:
        survey_rows = list(csv.DictReader(f))
    survey_lookup = {r['respondent_id']: r for r in survey_rows}

    with open(BOARDING_CSV, 'r', encoding='utf-8') as f:
        boarding_rows = list(csv.DictReader(f))

    facilities = []
    for br in boarding_rows:
        rid = br['respondent_id']
        sr = survey_lookup[rid]

        ft = classify_facility(
            demand_level=br['demand_level'],
            is_endpoint=sr['is_route_endpoint'],
            stopping_pattern=sr['stopping_pattern'],
            waiting_time=sr['waiting_time_cat'],
        )

        facilities.append({
            'respondent_id': rid,
            'lat': br['lat'],
            'lon': br['lon'],
            'boarding_hotspot': br.get('boarding_hotspot', ''),
            'boarding_barangay': br['boarding_barangay'],
            'alighting_barangay': sr['alighting_barangay'],
            'demand_level': br['demand_level'],
            'facility_type': ft,
            'is_route_endpoint': sr['is_route_endpoint'],
            'stopping_pattern': sr['stopping_pattern'],
            'waiting_time': sr['waiting_time_cat'],
        })

    # Distribution
    type_counts = {}
    for f in facilities:
        type_counts[f['facility_type']] = type_counts.get(f['facility_type'], 0) + 1

    print(f'\nFacility type distribution (per boarding point, n={len(facilities)}):')
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f'  {t}: {c}')

    # Per hotspot breakdown
    print(f'\nFacility type per boarding hotspot:')
    print(f'  {"Hotspot":<35} {"Terminal":<10} {"Wait Stn":<10} {"Load Zone":<10} {"Majority":<20}')
    hotspots = {}
    for f in facilities:
        h = f['boarding_hotspot'] or f['boarding_barangay']
        if h not in hotspots:
            hotspots[h] = {'Terminal': 0, 'Waiting Station': 0, 'Loading/Unloading Zone': 0}
        hotspots[h][f['facility_type']] += 1

    for h, data in sorted(hotspots.items()):
        best = max(['Terminal', 'Waiting Station', 'Loading/Unloading Zone'], key=lambda t: data[t])
        print(f'  {h:<35} {data["Terminal"]:<10} {data["Waiting Station"]:<10} {data["Loading/Unloading Zone"]:<10} {best:<20}')

    # Export per-point
    fields = list(facilities[0].keys())
    path = os.path.join(OUTPUT_DIR, 'proposed_facilities.csv')
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(facilities)
    print(f'\n[Export] {path} ({len(facilities)} rows)')

    # Plot map
    fig, ax = plt.subplots(figsize=(10, 8))
    for ft, color in FACILITY_COLORS.items():
        pts = [f for f in facilities if f['facility_type'] == ft]
        if pts:
            lats = [float(p['lat']) for p in pts]
            lons = [float(p['lon']) for p in pts]
            ax.scatter(lons, lats, c=color, label=ft, alpha=0.6, s=20)

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Proposed Facility Types per Boarding Point\nGusa-Bugo Corridor, CDO')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)

    map_path = os.path.join(OUTPUT_DIR, 'proposed_facilities_map.png')
    fig.savefig(map_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'[Plot] {map_path}')

    print('\n' + '=' * 60)
    print('DONE')
    print('=' * 60)


if __name__ == '__main__':
    main()

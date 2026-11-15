#!/usr/bin/env python3
"""Outdoor air by the ASHRAE 62.1 Ventilation Rate Procedure (zone level)."""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ventilation-rates.json")))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--space", required=True, choices=sorted(D["rates_cfm"]))
    p.add_argument("--people", type=float, default=0, help="design occupants; 0 = use default density")
    p.add_argument("--area", type=float, required=True, help="zone area, ft2")
    p.add_argument("--ez", type=float, default=1.0)
    a = p.parse_args()
    r = D["rates_cfm"][a.space]
    pz = a.people if a.people > 0 else r["density_per_1000ft2"] * a.area / 1000
    vbz = r["rp"] * pz + r["ra"] * a.area
    print(f"{r['label']}: Rp {r['rp']} CFM/person, Ra {r['ra']} CFM/ft2")
    print(f"Zone population Pz = {pz:.1f}, area Az = {a.area:g} ft2")
    print(f"Breathing-zone outdoor air Vbz = {vbz:.0f} CFM")
    print(f"Zone outdoor airflow Voz = Vbz / Ez({a.ez:g}) = {vbz / a.ez:.0f} CFM")
    print("Zone-level result; multi-zone systems need the system ventilation efficiency step of 62.1 Section 6.2.5.")

if __name__ == "__main__":
    main()

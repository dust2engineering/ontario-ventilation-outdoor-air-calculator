# Ontario Ventilation Outdoor Air Calculator

Calculates zone outdoor air by the ASHRAE Standard 62.1 Ventilation Rate Procedure (Vbz = Rp x Pz + Ra x Az, Voz = Vbz / Ez) for the space types small commercial projects use most, with the Table 6.2.2.1 rates and default occupant densities included as data.

**Live web tool:** https://dust2engineering.github.io/ontario-ventilation-outdoor-air-calculator/web/

## How it works

- Pick the space type; enter the design population or leave it at 0 to use the 62.1 default density.
- Exhaust minimums (Table 6.2) are listed separately: public toilets, commercial kitchens, parking garages.

## Data in this repository

- ventilation-rates.json — Rp, Ra and default density for every space type, plus exhaust rates, machine-readable.

## Command line

```bash
python3 ventilation.py --space restaurant_dining --people 100 --area 2000
```

## Worked examples

- [restaurant-dining-2000-sqft.md](examples/restaurant-dining-2000-sqft.md)
- [office-5000-sqft.md](examples/office-5000-sqft.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: HVAC / mechanical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering

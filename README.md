# Studio1-BDM-F26
Studio 1 for F26 in the BDM Class

Studio 1 (Wed Sept 9) — Data ER + Retirement
Monte Carlo

GitHub on-ramp (20 min). Open the starter notebook from the course repo in Colab → work
→ File → Save a copy in GitHub → your opim5641-work repo. That one loop is the habit —
nothing about branches tonight. Your repo becomes your portfolio for the whole course.

Part 1 — Data ER: PPP loans in Connecticut (~40 min). 117,888 real SBA PPP loans, dirt
included: missing industry codes, suspicious job counts, cities spelled three ways. In pairs we
triage: shape → missing-value census → duplicates → describe the money → who got it,
where, and how many dollars per job. Deliverable: three findings, each one plot or table plus
two sentences.

📚 Open the PPP Data ER notebook in Colab
📖 PPP data dictionary — what all 53 columns mean (official SBA descriptions), plus
which columns to distrust and why missing ≠ zero.

Part 2 — Retirement Monte Carlo (~35 min). The flip side: your balance in 35 years is data
you don’t have. We build the simulation in three escalations — one path, then 10,000, then
the twist: bootstrap 98 years of real S&P 500 returns instead of a made-up normal
distribution, and watch what fat tails do to P(you retire comfortably).

🎲 Open the Retirement Monte Carlo notebook in Colab
Wrap (10 min). Save your notebooks to GitHub (the loop, again). The pairing that drives this
course: when you have data, explore it; when you don’t, simulate it. Preview of Week 3 (brute
force — feel the explosion).

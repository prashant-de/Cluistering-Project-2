# Clustering Project 2

This repository contains our team’s full submission for the vertiport clustering project. We organized the work into three tasks and documented the methodology, intermediate outputs, and final comparison results.

## Our Approach

We solved the project in a staged way rather than jumping directly to the final vertiport sites.

1. **Task 1**: we first implemented K-means manually on a small toy dataset to demonstrate that we understood the algorithm itself.
2. **Task 2**: we then used the South Korea territory boundary to generate evenly distributed points inside the polygon so that we could simulate a practical spatial placement strategy.
3. **Task 3**: finally, we built a scoring pipeline for candidate vertiports using traffic, hospital, and tourist attraction data. We ranked all candidates, kept the top candidates, and compared two final-selection approaches:
   - K-means on the full candidate list, and
   - K-means only on the top-ranked candidate list.

We prefer the top-candidate approach as the final recommendation because it combines multiple datasets before clustering, which makes the result more efficient and easier to justify.

## Repository Structure

```text
.
├─ Project_2_description.pdf
├─ data/
├─ task1/
│  ├─ task1.py
│  └─ README.md
├─ task2/
│  ├─ even_distribution.py
│  ├─ task2.py                  # legacy/archived script (not used in final workflow)
│  └─ README.md
├─ task3/
│  ├─ task3.1/
│  │  ├─ build_candidate_scores.py
│  │  ├─ kmeans_17_vertiports.py
│  │  ├─ kmeans_on_top_candidates.py
│  │  ├─ produced_data/
│  │  └─ README.md
│  └─ task3.2/
│     ├─ find_optimal_k.py
│     ├─ produced_data/
│     └─ README.md
└─ requirements.txt
```

## Requirement Coverage (Project_2_description.pdf -> Evidence)

| Requirement from PDF | Implementation | Output Evidence |
|---|---|---|
| Task 1: Manual K-means on toy Cartesian points with given initial centroids and iteration logic | `task1/task1.py` | `task1/task1_figure.webp`, Task 1 README answers |
| Task 2: Generate evenly distributed points inside South Korea territory | `task2/even_distribution.py` | `task2/task2_centroids_N17.csv`, `task2/task2_centroids_N17.png` |
| Task 3: Build scoring model from traffic/hospital/tourist data and compare final site selection approaches | `task3/task3.1/build_candidate_scores.py`, `task3/task3.1/kmeans_17_vertiports.py`, `task3/task3.1/kmeans_on_top_candidates.py` | `task3/task3.1/produced_data/Processed_Data_vertiport_candidates_scores.csv`, `Top_400_Candidates.csv`, `allcandidate_final_vertiport_sites.csv`, `topcandidate_final_vertiport_sites.csv`, comparison plots |
| (Optional analysis) k selection support | `task3/task3.2/find_optimal_k.py` | `task3/task3.2/produced_data/k_sweep_*.csv`, `k_sweep_*.png` |

## Environment Setup

- Python 3.10+ recommended
- Install dependencies:

### Windows (PowerShell)

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Linux/macOS (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run

### Task 1: Manual K-means (toy problem)

Windows:

```powershell
py -3 task1\task1.py
```

Linux/macOS:

```bash
python3 task1/task1.py
```

Expected console output (example):
- `Total iterations taken: <number>`
- final cluster assignment lines
- final centroid coordinates

### Task 2: Even distribution inside territory polygon

Windows:

```powershell
py -3 task2\even_distribution.py data\Data_South_Korea_territory.csv --n-points 17
```

Linux/macOS:

```bash
python3 task2/even_distribution.py data/Data_South_Korea_territory.csv --n-points 17
```

Expected outputs:
- `task2/task2_centroids_N17.csv`
- `task2/task2_centroids_N17.png`

### Task 3A: Build candidate scores

Windows:

```powershell
py -3 task3\task3.1\build_candidate_scores.py --top-n 400
```

Linux/macOS:

```bash
python3 task3/task3.1/build_candidate_scores.py --top-n 400
```

Expected outputs:
- `task3/task3.1/produced_data/Processed_Data_vertiport_candidates_scores.csv`
- `task3/task3.1/produced_data/Top_400_Candidates.csv`

### Task 3B: K-means on all candidates

Windows:

```powershell
py -3 task3\task3.1\kmeans_17_vertiports.py data\Data_vertiport_candidates.csv data\Data_South_Korea_territory.csv --k 17 --random-state 42
```

Linux/macOS:

```bash
python3 task3/task3.1/kmeans_17_vertiports.py data/Data_vertiport_candidates.csv data/Data_South_Korea_territory.csv --k 17 --random-state 42
```

Expected outputs:
- `task3/task3.1/produced_data/allcandidate_kmeans_centroids_k17.csv`
- `task3/task3.1/produced_data/allcandidate_final_vertiport_sites.csv`
- `task3/task3.1/produced_data/allcandidate_kmeans_plot.png`

### Task 3C: K-means on top candidates

Windows:

```powershell
py -3 task3\task3.1\kmeans_on_top_candidates.py --k 17 --random-state 42
```

Linux/macOS:

```bash
python3 task3/task3.1/kmeans_on_top_candidates.py --k 17 --random-state 42
```

Expected outputs:
- `task3/task3.1/produced_data/topcandidate_kmeans_centroids_k17.csv`
- `task3/task3.1/produced_data/topcandidate_final_vertiport_sites.csv`
- `task3/task3.1/produced_data/topcandidate_kmeans_plot.png`

## Main Outputs

- `task1/task1_figure.webp`
- `task2/task2_centroids_N17.csv`
- `task2/task2_centroids_N17.png`
- `task3/task3.1/produced_data/Processed_Data_vertiport_candidates_scores.csv`
- `task3/task3.1/produced_data/Top_400_Candidates.csv`
- `task3/task3.1/produced_data/allcandidate_final_vertiport_sites.csv`
- `task3/task3.1/produced_data/topcandidate_final_vertiport_sites.csv`

## Results Summary

- Both methods produce 17 final sites.
- The all-candidate method is a geometry-first baseline.
- The top-candidate method is data-informed (traffic/hospital/tourist) before clustering.
- **Recommended final approach:** top-candidate pipeline (`build_candidate_scores.py` -> `kmeans_on_top_candidates.py`).

## Limitations & Assumptions

- The provided territory boundary is imperfect in some regions (notably Jeju), so some points can appear outside the plotted boundary.
- K-means is distance-based and sensitive to `k` and seed; reproducibility is handled with fixed `random_state`.
- Scoring is a weighted heuristic model and depends on selected weights/decay parameters.

## Task-Specific Documentation

- [Task 1 README](task1/README.md)
- [Task 2 README](task2/README.md)
- [Task 3.1 README](task3/task3.1/README.md)
- [Task 3.2 README](task3/task3.2/README.md)

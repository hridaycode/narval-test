from pathlib import Path

import numpy as np
import pandas as pd


DATA_DIR = Path("/lustre07/scratch/codehri/ScaledSM/Data")
OUTPUT_DIR = Path("/lustre07/scratch/codehri/ScaledSM/Results")
OUTPUT_FILE = OUTPUT_DIR / "graph_summary.csv"


def get_graph_stats(A):
    """Return number of nodes and edges for an undirected graph."""
    num_nodes = A.shape[0]
    num_edges = np.count_nonzero(A) // 2

    return num_nodes, num_edges


def main():

    graphs = [
        "Cora",
        "Citeseer",
        "Pubmed",
        "Wiki",
        "Sinanet",
        "American75",
        "Auburn71",
        "BU10",
        "Bucknell39",
        "Colgate88",
        "Yale4",
    ]

    results = []

    for graph in graphs:

        if graph in ["Cora", "Citeseer", "Pubmed"]:
            path = DATA_DIR / "CitationNetworks" / f"{graph}_connected_comp.npz"

        elif graph == "Sinanet":
            path = DATA_DIR / "Sinanet" / f"{graph}.npz"

        elif graph in [
            "American75",
            "Auburn71",
            "BU10",
            "Bucknell39",
            "Colgate88",
            "Yale4",
        ]:
            path = DATA_DIR / "FacebookNetworks" / f"{graph}.npz"

        elif graph == "Wiki":
            path = DATA_DIR / "Wiki" / f"{graph}.npz"

        data = np.load(path)
        adj = data["adj"]

        num_nodes, num_edges = get_graph_stats(adj)

        results.append(
            {
                "Graph": graph,
                "Num Nodes": num_nodes,
                "Num Edges": num_edges,
            }
        )

    results_df = pd.DataFrame(results)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results_df.to_csv(OUTPUT_FILE, index=False)

    print(results_df)
    print(f"\nSaved results to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
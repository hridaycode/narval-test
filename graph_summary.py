from pathlib import Path

import numpy as np
import pandas as pd
import scipy.sparse as sp


# -----------------------------
# Paths
# -----------------------------
DATA_DIR = Path("/lustre07/scratch/codehri/ScaledSM/Data")
OUTPUT_DIR = Path("/lustre07/scratch/codehri/ScaledSM/Results")
OUTPUT_FILE = OUTPUT_DIR / "graph_summary.csv"


def get_graph_stats(A):
    """
    Return number of nodes and edges.

    Assumes an undirected graph, so each edge appears twice
    in the adjacency matrix.
    """
    num_nodes = A.shape[0]
    num_edges = A.nnz // 2
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

    reults_df = pd.DataFrame(columns=["Graph", "Num Nodes", "Num Edges"])

    for graph in graphs:
        if graph in ["Cora", "Citeseer", "Pubmed"]:
            data = np.load(DATA_DIR / "CitationNetworks" / f"{graph}_connected_comp.npz")
            adj = data["adj"]
            num_nodes, num_edges = get_graph_stats(adj)
        elif graph in ["Sinanet"]:
            data = np.load(DATA_DIR / "Sinanet" / f"{graph}.npz")
            adj = data["adj"]
            num_nodes, num_edges = get_graph_stats(adj)
        elif graph in ["American75", "Auburn71", "BU10", "Bucknell39", "Colgate88", "Yale4"]:
            data = np.load(DATA_DIR / "FacebookNetworks" / f"{graph}.npz")
            adj = data["adj"]
            num_nodes, num_edges = get_graph_stats(adj)
        elif graph in ["Wiki"]:
            data = np.load(DATA_DIR / "Wiki" / f"{graph}.npz")
            adj = data["adj"]
            num_nodes, num_edges = get_graph_stats(adj)

        reults_df = pd.concat(
            [
                reults_df,
                pd.DataFrame(
                    {
                        "Graph": [graph],
                        "Num Nodes": [num_nodes],
                        "Num Edges": [num_edges],
                    }
                ),
            ],
            ignore_index=True,
        )

    reults_df.to_csv(OUTPUT_FILE, index=False)

if __name__ == "__main__":
    main()
import networkx as nx

def compare_with_networkx(pages, d=0.85):
    # Build the identical graph
    G = nx.DiGraph()
    for p in pages:
        G.add_node(p.name)
    for p in pages:
        for link in p.links:
            G.add_edge(p.name, link.target.name, weight=link.weight)

    # Reference result, with a tight tolerance so it's effectively exact
    nx_rank = nx.pagerank(G, alpha=d, weight="weight", tol=1e-12, max_iter=1000)

    # Page-by-page table
    print(f"\n{'Page':<10}{'Mine':>12}{'NetworkX':>12}{'Abs diff':>14}")
    max_diff = 0.0
    for p in sorted(pages, key=lambda p: p.rank, reverse=True):
        diff = abs(p.rank - nx_rank[p.name])
        max_diff = max(max_diff, diff)
        print(f"{p.name:<10}{p.rank:>12.6f}{nx_rank[p.name]:>12.6f}{diff:>14.2e}")

    # Summary metrics
    my_order = [p.name for p in sorted(pages, key=lambda p: p.rank, reverse=True)]
    nx_order = sorted(nx_rank, key=nx_rank.get, reverse=True)
    print(f"\nMax absolute difference: {max_diff:.2e}")
    print(f"Sum of mine: {sum(p.rank for p in pages):.6f}  "
          f"Sum of NetworkX: {sum(nx_rank.values()):.6f}")
    print(f"Identical ranking order: {my_order == nx_order}")
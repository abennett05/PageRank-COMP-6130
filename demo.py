from page import Page
from compare import compare_with_networkx
from visualizer import make_visualizer
import random
import matplotlib.pyplot as plt

# PageRank algorithm implementation
def compute_pagerank(pages, d=0.85, tol=1e-6, max_iter=100, on_iteration=None):
    n = len(pages)
    for p in pages:
        p.rank = 1 / n
    if on_iteration:
        on_iteration(0, None)

    for iteration in range(1, max_iter + 1):
        new_rank = {p: (1 - d) / n for p in pages}

        # Dangling pages (no outlinks) spread their rank evenly to everyone
        dangling = sum(p.rank for p in pages if not p.links)
        for p in pages:
            new_rank[p] += d * dangling / n

        # Each page sends rank along its links in proportion to weight
        for p in pages:
            for link in p.links:
                new_rank[link.target] += d * p.rank * link.weight

        

        diff = sum(abs(new_rank[p] - p.rank) for p in pages)
        for p in pages:
            p.rank = new_rank[p]

        # Callback for visualizer
        if on_iteration:
            on_iteration(iteration, diff)

        print(f"Iteration {iteration}: change = {diff:.8f}")
        if diff < tol:
            break
    return iteration

if __name__ == "__main__":
    # SETTINGS - Configurable
    PAGE_COUNT = 50
    LINK_RANGE_LOW = 30
    LINK_RANGE_HIGH = 70
    USE_HIGH = True

    # RUNTIME - Do not edit
    pages = list()
    link_count = LINK_RANGE_HIGH if USE_HIGH else random.randrange(LINK_RANGE_LOW, LINK_RANGE_HIGH + 1)
    total_links = 0

    # Print settings
    print(f"Page Rank Demo - COMP-6130")
    print(f"Created by Adrian Bennett -- aab0125")
    print(f"--- Settings ---")
    print(f"- Pages: {PAGE_COUNT}")
    print(f"- Links: {link_count}")
    print(" --- Starting ---")
    print()

    # Create pages
    for i in range(PAGE_COUNT):
        new_page = Page(f"Page {i}")
        pages.append(new_page)
    # Form page links
    while total_links < link_count and len(pages) > 1:
        # Get pages
        source_page: Page = random.choice(pages)
        dest_page: Page = random.choice(pages)

        while total_links < link_count:
            source = random.choice(pages)
            candidates = [p for p in pages if p is not source and p not in source.link_by_dest]
            if not candidates:
                continue
            source.add_link(random.choice(candidates), random.uniform(0.1, 1))
            total_links += 1

    # Normalize all pages after graph has been made
    for p in pages:
        p.normalize_weights()

    # Print each page with their links
    for page in pages:
        print(f"--- {page.name} ---")
        if (len(page.links) < 1):
            print(f"-- No Outgoing Links")
        else:
            print(f"-- Links")
        for link in page.links:
            print(f"- Links to {link.target.name} ({link.weight})")
        print(f"------------")

    draw=make_visualizer(pages)
    iterations = compute_pagerank(pages, on_iteration=draw)
    
    print(f"\nConverged in {iterations} iterations")
    print(f"Sum of ranks: {sum(p.rank for p in pages):.6f}")  # should be 1.0

    for p in sorted(pages, key=lambda p: p.rank, reverse=True):
        print(f"{p.name}: {p.rank:.4f}")

    print(f"--- COMPARSION ---")
    print(f"-- Performance compared against networkx PageRank function")
    compare_with_networkx(pages)

    plt.ioff()
    plt.show()
import math
from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        return [[int(x) for x in row.split(',')] for row in f.read().strip().splitlines()]
    
def merge_sort(points, k, last):
    edges = []
    n = len(points)

    # Build all pairwise edges
    for i in range(n):
        for j in range(i + 1, n):   # no duplicates, no self-pairs
            p = points[i]
            q = points[j]
            dist = math.dist(p, q)
            edges.append((dist, i, j))

    edges.sort()

    # DSU
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    def current_components():
        comp = {}
        for v in range(n):
            r = find(v)
            comp.setdefault(r, set()).add(v)
        return [len(s) for s in comp.values()]

    processed = 0

    # PROCESS FIRST k CLOSEST PAIRS
    for dist, i, j in edges:
        union(i, j)
        processed += 1

        if processed == k:
            sizes = sorted(current_components(), reverse=True)
            return math.prod(sizes[:last])

    # If k >= number of possible edges (rare), still compute
    sizes = sorted(current_components(), reverse=True)
    return math.prod(sizes[:last])
    

def merge_sort_wrong(points: List[List[int]], k: int, last: int) -> int:
    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if i == j:
                continue
            first = points[i]
            second = points[j]
            dist = math.sqrt((first[0] - second[0])**2 + (first[1] - second[1])**2 + (first[2] - second[2])**2)
            edges.append((dist, i, j))
    edges.sort()

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a,b):
        ra, rb = find(a), find(b)
        if ra == rb: return False
        parent[rb] = ra
        return True

    def current_components():
        comp = {}
        for v in range(len(points)):
            r = find(v)
            comp.setdefault(r, set()).add(v)
        # return list of components sorted by size desc
        return sorted([sorted(list(s)) for s in comp.values()], key=lambda x:-len(x))

    parent = list(range(len(points)))
    count = 0
    for dist, i, j in edges:
        if union(i, j):
            count += 1
            comps = current_components()
            if count == k-1:
                result = [len(group) for group in comps]
                result.sort(reverse=True)
                ans = math.prod(result[:last])
                return ans

if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = merge_sort(test_data, 10, 3)
    print(test_ans)

    data1 = parse_input("input.txt")
    ans1 = merge_sort(data1, 1000, 3)
    print(ans1)
            
from collections import defaultdict
from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        rows = f.read().strip().splitlines()
        sep_rows = [text.split(": ") for text in rows]
        ans = defaultdict(list)
        for x, y in sep_rows:
            values = y.split(" ")
            ans[x].extend(values)
        return ans

def find_device_path(graph) -> int:
    def dfs(node):
        nonlocal total
        new_neighbors = graph[node]
        for new_neighbor in new_neighbors:
            if new_neighbor == "out":
                total += 1
                continue
            dfs(new_neighbor)
        return 
    
    total = 0
    start = graph["you"]
    for i in start:
        neighbors = graph[i]
        for neighbor in neighbors:
            if neighbor == "out":
                total += 1
                continue
            dfs(neighbor)

    return total

def find_device_path2(graph) -> int:
    def dfs(node, paths):
        new_neighbors = graph[node]
        for new_neighbor in new_neighbors:
            new_paths = paths + [new_neighbor]
            if new_neighbor == "out":
                groups.append(new_paths)
                continue
            dfs(new_neighbor, new_paths)
        return

    start = graph["svr"]
    groups = []
    for i in start:
        neighbors = graph[i]
        for neighbor in neighbors:
            temp = [i, neighbor]
            if neighbor == "out":
                groups.append(temp)
                continue
            dfs(neighbor, temp)
    
    total = 0
    for group in groups:
        if 'fft' in group and 'dac' in group:
            total += 1
    return total

def find_device_path2_dfs(graph) -> int:
    total = 0 
    def dfs(node, has_fft, has_dac):
        nonlocal total

        if node == "fft":
            has_fft = True
        if node == "dac":
            has_dac == True

        if node == "out":
            if has_fft and has_dac:
                total += 1
            return
        
        for neighbor in graph[node]:
            dfs(neighbor, has_fft, has_dac)
    
    for neighbor in graph["svr"]:
        dfs(neighbor, False, False)

    return total


if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = find_device_path(test_data)
    print(test_ans)

    data = parse_input("input.txt")
    ans1 = find_device_path(data)
    print(ans1)

    test_data2 = parse_input("input_test2.txt")
    test_ans2 = find_device_path2(test_data2)
    print(test_ans2)

    # data2 = parse_input("input.txt")
    # ans2 = find_device_path2_dfs(data2)
    # print(ans2)

    data2 = parse_input("input.txt")
    ans2 = find_device_path2(data2)
    print(ans2)

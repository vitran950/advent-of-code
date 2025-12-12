from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        return f.read().strip().splitlines()

def count_beam_split(manifolds: List[str]) -> int:
    def check_inbounds(c: int) -> bool:
        if 0 <= c < n:
            return True
        return False

    m = len(manifolds)
    n = len(manifolds[0])
    total = 0
    seen = set()
    
    # pre-process first row to find S
    prev = []
    for index, element in enumerate(manifolds[0]):
        if element == 'S':
            prev.append(index)
            seen.add(index)
            break

    for i in range(1, m):
        # need to create a brand new temp set
        temp = seen.copy()
        for j in range(n): # (0,1), (0,2) ..
            curr = manifolds[i][j]
            if curr == '^' and j in seen:
                total += 1
                curr1 = j-1
                curr2 = j+1
                
                if check_inbounds(curr1):
                    temp.add(curr1)
                if check_inbounds(curr2):
                    temp.add(curr2)
                temp.remove(j)
        seen = temp
    return total

def count_timelines_dfs(grid):
    m = len(grid)
    n = len(grid[0])

    # Find starting S
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 'S':
                start_r, start_c = r, c

    def dfs(r, c):
        # Exited grid → 1 timeline branch
        if r < 0 or r >= m or c < 0 or c >= n:
            return 1

        cell = grid[r][c]

        if cell == '^':   # splitter
            return dfs(r + 1, c - 1) + dfs(r + 1, c + 1)
        else:             # empty or S
            return dfs(r + 1, c)

    # Start below S (same convention as your DP code)
    return dfs(start_r + 1, start_c)

def count_timelines(grid):
    def find_S(grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    return r, c
        raise ValueError("No S in grid")
    
    m = len(grid)
    n = len(grid[0])
    start_r, start_c = find_S(grid)

    memo = {}

    def f(r, c):
        # exited
        if r < 0 or r >= m or c < 0 or c >= n:
            return 1
        key = (r, c)
        if key in memo:
            return memo[key]
        cell = grid[r][c]
        if cell == '^':
            # splitter: spawn left and right (same convention as Part 1)
            left_count = f(r + 1, c - 1)   # careful with indices
            right_count = f(r + 1, c + 1)
            memo[key] = left_count + right_count
            return memo[key]
        else:
            # empty or S: just proceed down one row same column
            memo[key] = f(r + 1, c)
            return memo[key]

    return f(start_r + 1, start_c)  # or f(start_r, start_c) depending how you defined S handling

# def count_beam_split2(manifolds: List[str]) -> int:
#     def check_inbounds(c: int) -> bool:
#         if 0 <= c < n:
#             return True
#         return False
    
#     def backtrack(curr, y):
#         if y == m: 
#             ans.append(curr)
#             return
        
#         for i in range(n):
#             element = manifolds[y][i]
#             if element == '^':
#                 x1 = i - 1
#                 x2 = i + 1
#                 if check_inbounds(x1):
#                     curr.append(x1)
#                     backtrack(curr, y + 1)
#                     curr.pop()
#                 if check_inbounds(x2):
#                     curr.append(x2)
#                     backtrack(curr, y + 1)
#                     curr.pop()
        
#     m = len(manifolds)
#     n = len(manifolds[0])
#     ans = []

#     prev = []
#     for index, element in enumerate(manifolds[0]):
#         if element == 'S':
#             prev.append(index)
#             break

#     backtrack(prev, 0)
#     return len(ans)

# def count_beam_split2(manifolds: List[str]) -> int:
#     def check_inbounds(c: int) -> bool:
#         return 0 <= c < n

#     m = len(manifolds)
#     n = len(manifolds[0])
#     # seen now maps position to timeline count
#     seen = {}
#     for index, element in enumerate(manifolds[0]):
#         if element == 'S':
#             seen[index] = 1
#             break

#     for i in range(1, m):
#         temp = {}
#         for j in range(n):
#             curr = manifolds[i][j]
#             if j in seen:
#                 if curr == '^':
#                     # split timelines
#                     if check_inbounds(j-1):
#                         temp[j-1] = temp.get(j-1, 0) + seen[j]
#                     if check_inbounds(j+1):
#                         temp[j+1] = temp.get(j+1, 0) + seen[j]
#                 else:
#                     temp[j] = temp.get(j, 0) + seen[j]
#         seen = temp
#     return sum(seen.values())                

if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = count_beam_split(test_data)
    print(test_ans)

    data1 = parse_input("input.txt")
    ans1 = count_beam_split(data1)
    print(ans1)

    test_data2 = parse_input("input_test.txt")

    # test_ans2 = count_timelines_dfs(data1)
    # print(test_ans2)

    test_ans22 = count_timelines(data1)
    print(test_ans22)
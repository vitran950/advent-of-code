from typing import List, Tuple

def parse_input(file_path):
    with open(file_path) as f:
        text = f.read().strip().splitlines()
        # convert to 2D array 
        return [list(row) for row in text]

def count_liftable_papers(papers: List[List[str]]) -> int:
    def check_inbounds(x, y):
        if x < 0 or x >= m:
            return False
        if y < 0 or y >= n:
            return False
        return True

    m = len(papers)
    n = len(papers[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count = 0

    for i in range(m):
        for j in range(n):
            curr = papers[i][j]
            if curr == '@':
                neighbors = 0
                for dir in directions:
                    new_x = i + dir[0]
                    new_y = j + dir[1]
                    if check_inbounds(new_x, new_y) and papers[new_x][new_y] == '@':
                        neighbors += 1
                if neighbors < 4:
                    count += 1
    return count

def count_liftable_papers2(papers: List[List[str]]) -> int:
    def remove_space(grid) -> Tuple[List[List[str]], int]:
        def check_inbounds(x, y):
            if x < 0 or x >= m:
                return False
            if y < 0 or y >= n:
                return False
            return True
        
        new_grid = grid
        temp_count = 0
        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                if curr == '@':
                    neighbors = 0
                    for dir in directions:
                        new_x = i + dir[0]
                        new_y = j + dir[1]
                        if check_inbounds(new_x, new_y) and papers[new_x][new_y] == '@':
                            neighbors += 1
                    if neighbors < 4:
                        temp_count += 1
                        new_grid[i][j] = '.'
        return (new_grid, temp_count)

    m = len(papers)
    n = len(papers[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count = 0
    grid = papers

    while True:
        new_grid, num = remove_space(grid)
        if num == 0:
            break
        count += num
        grid = new_grid
    
    return count


if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = count_liftable_papers(test_data)
    print(test_ans)

    data = parse_input("input.txt")
    ans = count_liftable_papers(data)
    print(ans)

    test_data2 = parse_input("input_test.txt")
    test_ans2 = count_liftable_papers2(test_data2)
    print(test_ans2)

    data2 = parse_input("input.txt")
    ans2 = count_liftable_papers2(data2)
    print(ans2)

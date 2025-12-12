from collections import defaultdict
from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        pairs = f.read().strip().splitlines()
        return [[int(x) for x in pair.split(",")] for pair in pairs]
    
def find_big_red(tiles: List[List[int]]) -> int:
    largest = 0
    m = len(tiles)
    for i in range(m):
        for j in range(i + 1, m):
            area = (abs(tiles[i][0] - tiles[j][0]) + 1)*(abs(tiles[i][1] - tiles[j][1]) + 1)
            largest = max(area, largest)
    return largest

def find_big_red2_wrong(tiles: List[List[int]]) -> int:
    largest = 0
    y_dict = defaultdict(list)
    x_dict = defaultdict(list)

    for col,row in tiles:
        y_dict[col].append(row)
        x_dict[row].append(col)

    m = len(tiles)
    for i in range(m):
        for j in range(i + 1, m):
            spot1 = tiles[j]
            spot2 = tiles[i]
            print(spot1, spot2)
            spot3 = [spot2[0], spot1[1]]
            spot4 = [spot1[0], spot2[1]]

            # check y first
            range_y1 = y_dict[spot3[0]]
            if min(range_y1) < spot3[1] > max(range_y1):
                continue
            range_y2 = y_dict[spot4[0]]
            if min(range_y2) < spot4[1] > max(range_y2):
                continue

            # check x
            range_x1 = x_dict[spot3[1]]
            if min(range_x1) < spot3[0] > max(range_x1):
                continue
            range_x2 = x_dict[spot4[1]]
            if min(range_x2) < spot4[0] > max(range_x2):
                continue  

            area = (abs(tiles[i][0] - tiles[j][0]) + 1)*(abs(tiles[i][1] - tiles[j][1]) + 1)
            largest = max(area, largest)

    return largest

if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = find_big_red(test_data)
    print(test_ans)

    data1 = parse_input("input.txt")
    ans1 = find_big_red(data1)
    print(ans1)

    test_ans2 = find_big_red2_wrong(test_data)
    print(test_ans2)
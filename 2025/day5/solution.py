from typing import List

"""
TODO: try it with binary tree since we are sorting it
"""

def parse_input(file_path):
    with open(file_path) as f:
        all = f.read().strip().splitlines()
        
        i = 0
        while i < len(all):
            curr = all[i]
            if curr == '':
                break
            i += 1

        ranges = [[int(x) for x in y.split('-')] for y in all[:i]]
        ids = [int(x) for x in all[i+1:]]

        return (ranges, ids)
        
def find_fresh_ingredients(ranges: List[List[int]], ids: List[int]) -> int:
    # sort ranges by the first element in asc
    ranges.sort()

    # handle overlapping ranges and reduce it down
    stack = [ranges[0]]
    for i in range(1, len(ranges)):
        start = ranges[i][0]
        end = ranges[i][1]
        if stack[-1][1] >= start:
            # need to look for max of stack and end 
            # e.g. stack = [1,6] and ranges[i] = [2,4] 
            # we need to change to [1,6]
            stack[-1][1] = max(end, stack[-1][1])
        else:
            stack.append([start,end])

    count = 0
    for id in ids:
        for span in stack:
            if span[0] <= id <= span[1]:
                count += 1
                break
    return count
    
        
def find_fresh_ingredients_dumb(ranges: List[List[int]], ids: List[int]) -> int:
    count = 0
    for id in ids:
        for span in ranges:
            if span[0] <= id <= span[1]:
                count += 1
                break
    return count

def find_fresh_ingredients2(ranges: List[List[int]]) -> int:
    # sort ranges by the first element in asc
    ranges.sort()
    stack = [ranges[0]]
    for i in range(1, len(ranges)):
        start = ranges[i][0]
        end = ranges[i][1]
        if stack[-1][1] >= start:
            # need to look for max of stack and end 
            # e.g. stack = [1,6] and ranges[i] = [2,4] 
            # we need to change to [1,6]
            stack[-1][1] = max(end, stack[-1][1])
        else:
            stack.append([start,end])
    
    count = 0
    for space in stack:
        count += (space[1] - space[0] + 1)
    return count


if __name__ == "__main__":
    test_ranges, test_ids = parse_input("input_test.txt")
    test_ans = find_fresh_ingredients(test_ranges, test_ids)
    print(test_ans)

    ranges1, ids1 = parse_input("input.txt")
    ans1 = find_fresh_ingredients_dumb(ranges1, ids1)
    ans1_smart = find_fresh_ingredients(ranges1, ids1)
    print(ans1)
    print(ans1_smart)

    test_ans2 = find_fresh_ingredients2(test_ranges)
    print(test_ans2)
    ans2 = find_fresh_ingredients2(ranges1)
    print(ans2)
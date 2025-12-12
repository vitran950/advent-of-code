import math
from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        all = f.read().strip().splitlines()
        all_2d = [[x for x in row.split()] for row in all]
        numbers = [[int(b) for b in a] for a in all_2d[:-1]]
        symbols = all_2d[-1]
        return (numbers, symbols)
    
def parse_input2(file_path):
    with open(file_path) as f:
        all = f.read().strip().splitlines()
        numbers = [row for row in all[:-1]]
        symbols = all[-1].split()
        return (numbers, symbols)

def do_math_homework(numbers: List[List[int]], symbols: List[str]) -> int:    
    count = 0
    m = len(numbers)
    n = len(numbers[0])

    for j in range(n):
        nums = []
        for i in range(m):
            curr = numbers[i][j]
            nums.append(curr)
        
        if symbols[j] == "+":
            count += sum(nums)
        else:
            count += math.prod(nums) 

    return count

def do_math_homework2(numbers: List[str], symbols: List[str]) -> int:    
    total = 0 
    k = 0 
    m = len(numbers)
    n = len(numbers[0])
    collect = []

    for j in range(n):
        temp = []
        for i in range(m):
            curr = numbers[i][j]
            if curr != ' ':
                temp.append(curr)
        
        # if it is the last, then we need to manually inject it into collect
        if j == n-1 and len(temp) != 0:
            last_element = "".join(temp)
            converted_last = int(last_element)
            collect.append(converted_last)

        # if temp == 0, we know it's ready to be applied to the total
        if len(temp) == 0 or j == n-1:
            if symbols[k] == "+":
                total += sum(collect)
            else:
                total += math.prod(collect)
            k += 1
            collect = []
        else:
            converted = "".join(temp)
            converted_int = int(converted)
            collect.append(converted_int)
    return total

if __name__ == "__main__":
    test_numbers, test_symbols = parse_input("input_test.txt")
    test_ans = do_math_homework(test_numbers, test_symbols)
    print(test_ans)

    numbers, symbols = parse_input("input.txt")
    ans1 = do_math_homework(numbers, symbols)
    print(ans1)

    test_numbers2, test_symbols2 = parse_input2("input_test.txt")
    test_ans2 = do_math_homework2(test_numbers2, test_symbols2)
    print(test_ans2)
    
    numbers2, symbols2 = parse_input2("input.txt")
    ans2 = do_math_homework2(numbers2, symbols2)
    print(ans2)
    
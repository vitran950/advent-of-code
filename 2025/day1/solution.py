from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        return f.read().strip().splitlines()
    
def rotate_lock(rotations: List[int], start: int, circle: int) -> int:
    count = 0
    for dial in rotations:
        # extract first letter for direction + remaining characters for turn number         
        dir = dial[0]
        num = dial[1:]  

        # determine if negative or positive based on direction + convert to integer + take mod 100
        # we're making the assumption that L and R are the ONLY first char
        start = (start + int('-' + num if dir == "L" else num)) % circle

        if start == 0:
            count += 1

    return count

# this is the right answer - it gives us 6770
def rotate_lock2(rotations: List[int], start: int, circle: int) -> int:
    count = 0
    for dial in rotations:
        # extract first letter for direction + remaining characters for turn number         
        dir = dial[0]
        num = int(dial[1:])
        move = -num if dir == "L" else num
        steps = abs(move)
        for i in range(1, steps + 1):
            if dir == "R":
                pos = (start + i) % circle
            else:
                pos = (start - i) % circle
            if pos == 0:
                count += 1
        start = (start + move) % circle
    return count

if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = rotate_lock(test_data, 50, 100)
    print(test_ans)

    data = parse_input("input.txt")
    ans1 = rotate_lock(data, 50, 100)
    print(ans1)

    test_ans2 = rotate_lock2(test_data, 50, 100)
    print(test_ans2)

    ans2 = rotate_lock2(data, 50, 100)
    print(ans2)
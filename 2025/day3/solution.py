from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        return f.read().strip().splitlines()
    
def largest_jolt(banks: List[str]) -> int:
    count = 0
    for bank in banks:
        # get list of the bank excluding last character
        first = [int(c) for c in list(bank)[:-1]]
        largest_first = max(first)

        # find the insertion point of where we can look for the rest of the list
        insertion_index = first.index(largest_first)

        second = [int(c) for c in list(bank)[insertion_index+1:]]
        largest_second = max(second)
        
        # arithmetic trick to combine 2 digits instead of converting to string
        count += largest_first * 10 + largest_second
    return count       

def largest_jolt2(banks: List[str]) -> int:
    count = 0

    # TODO: convert this to be passed as arg to the function? 12 can easily change
    size = 12
    for bank in banks:
        insertion = 0
        storage = []
        
        # enumerate until storage reaches size (12)
        while len(storage) < size:
            
            # iterate from ranges from (insertion_index, to the position that will ensure we'll have enough digits remaining to fill storage to 'size')
            curr = [int(c) for c in list(bank)[insertion:len(bank)-(size-len(storage)-1)]]
            largest = max(curr)
            storage.append(largest)

            # get index of largest and always add by 1 to move to the next range of the list
            insertion += curr.index(largest) + 1

        # convert the list of int to str first -> concatenate all prior to converting back to int
        jolt = "".join(map(str, storage))
        count += int(jolt)
    return count

if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = largest_jolt(test_data)
    print(test_ans)

    data = parse_input("input.txt")
    ans = largest_jolt(data)
    print(ans)

    test_ans2 = largest_jolt2(test_data)
    print(test_ans2)

    ans2 = largest_jolt2(data)
    print(ans2)
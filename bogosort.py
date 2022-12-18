import random


# This function takes in a list of integers and returns them sorted from least to greatest, in
# the most efficient manner that humanity has ever dared to attempt.
def bogosort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst


# This function takes in a list and returns a sorted list in O(1) time. Provided list must be sorted.
def instantsort(lst):
    return lst


# This function is nihilistic.
def entropysort(lst):
    print("The heat death of the universe is inevitable as maximum entropy is reached and all becomes disordered, no reason to sort now")
    return lst


# This function returns true if the given list is sorted, otherwise returns false
def is_sorted(lst):
    for i in range(1, len(lst)):
        prev_num, num = lst[i - 1], lst[i]
        if prev_num > num:
            return False
    return True


def main():
    # Test bogosort
    bogo_list = [1, 5, 3, 4, 7, 9, 1, 0, 4, 6]
    bogo_list_sorted = bogosort(bogo_list)
    print(f"Bogosorted List: {bogo_list_sorted}")

    # Test instantsort
    instant_list = [1, 2, 3, 4, 5]
    instant_list_sorted = instantsort(instant_list)
    print(f"Instantsorted List: {instant_list_sorted}")

    # Test entropysort
    entropy_list = [1, 2, 3, 4, 5]
    entropy_list_sorted = entropysort(entropy_list)


if __name__ == "__main__":
    main()

"""Demonstration of sorting."""
from typing import List
from cs110 import expect, summarize

lon = [2, 1, 3]
lon.sort()
print(lon)


lod = [
    {"k1": 1, "k2": 2},
    {"k1": 3, "k2": 3},
    {"k1": 2, "k2": 1}    
]

lod.sort(key=lambda d: d["k1"])
print(lod)

lod.sort(key=lambda d: d["k2"])
print(lod)

los = ["a", "aaa", "aa"]
los.sort(key=lambda s: len(s))
print(los)

lot = [
    (1, 2, "b"),
    (3, 1, "a"),
    (2, 3, "c")
]
lot.sort(key=lambda t: t[1])
print(lot)



def min_index(lon: List[int]) -> int:
    """
    Purpose: Find the index of the minimum value of the list.
    Assume: List is non-empty
    Example:
        min_index([2, 1]) -> 1
        min_index([2, 5]) -> 0
    """
    minimum_value = lon[0]
    minimum_index = 0
    for i in range(len(lon)):
        if lon[i] < minimum_value:
            minimum_index = i
    return minimum_index

expect(min_index([2, 1]), 1)
expect(min_index([2, 5]), 0)


def swap(lon: List[int], i: int, j: int) -> List[int]:
    """
    Purpose: Swap the values at the given indices
    Assume: List is non-empty, indices < len(list)
    Examples:
        swap([1, 2], 0, 1) -> [2, 1]
        swap([1, 2, 3], 0, 2) -> [3, 2, 1]
    """
    lon[i], lon[j] = lon[j], lon[i]
    return lon

expect(swap([1, 2], 0, 1), [2, 1])
expect(swap([1, 2, 3], 0, 2), [3, 2, 1])


def selection(lon: List[int]) -> List[int]:
    """
    Purpose: Sort a list of numbers
    Examples:
        selection([3, 1, 2]) -> [1, 2, 3]
    """
    for i in range(len(lon)):
        min_i = min_index(lon[i:])
        lon = swap(lon, i, min_i)
    return lon
        
expect(selection([3, 1, 2]), [1, 2, 3])

# summarize()

## Timing
import time

# Timing Tests
print()
print("="*80)
print("Timing Tests")
print("="*80)



def timing_test(func, list_input, *args, description=""):
    """
    Times how long it takes to execute a function on a list and prints the result.
    
    Parameters:
    - func: The function to time.
    - list_input: The list to use as input to the function.
    - args: Additional arguments for the function.
    - description: A string to describe the function being timed (e.g., 'swap').
    
    Returns:
    - Execution time for the function.
    """
    start = time.perf_counter()
    func(list_input, *args)
    end = time.perf_counter()
    fmt = f"{description}({len(list_input)}):"
    print(f"{fmt:>20} {end - start:<40.6}")
    return end - start

def average_timing(func, lengths, *args, description="", repetitions=5):
    """
    Runs timing_test for each list size in lengths multiple times and computes the average time.
    
    Parameters:
    - func: The function to time.
    - lengths: List of list sizes.
    - args: Additional arguments for the function.
    - description: Description of the test (e.g., 'swap').
    - repetitions: Number of times to repeat each test for averaging.
    """
    for size in lengths:
        times = []
        for _ in range(repetitions):
            lon = [1, 2, 3] * size
            times.append(timing_test(func, lon, *args, description=description))
        
        avg_time = sum(times) / repetitions
        print(f"Average time for {description}({size * 3} elements): {avg_time:.6f} seconds\n")



# Swap timing tests with averages
lengths = [1, 2, 20, 200, 2000, 20000]
print("Swap Timing Tests (Averages)")
average_timing(swap, lengths, 0, 1, description="swap")

print("\nMin Index Timing Tests (Averages)")
average_timing(min_index, lengths, description="min_index")

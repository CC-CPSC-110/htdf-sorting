# How to Design Tasks: Sorting and Complexity Analysis

Sorting is one of the most common Computer Science problems that you will come across. Even though it seems simple, ordering a list of items is key to even areas of research like AI. 

```python
[2, 1, 3] -> [1, 2, 3]
```

At the same time, we want to sort quickly. Today we will learn how to sort, and to figure out how long it takes to sort something.

## Python built-in sorting
Python offers an easy built-in sorting function:
```python
>>> lon = [2, 1, 3]
>>> lon.sort()
>>> lon
[1, 2, 3]
>>> lon.sort(reverse=True)
>>> lon
[3, 2, 1]
```
Python sorting is in-place, so you modify original list when you sort.

## Python built-in sorting using a key
You can sort a list of dictionaries based on their keys:
```python
>>> lod = [
    {"k1": 1, "k2": 2},
    {"k1": 3, "k2": 3},
    {"k1": 2, "k2": 1}    
]
>>> lod.sort(key=lambda d: d["k1"])
>>> lod
[
    {'k1': 1, 'k2': 2}, 
    {'k1': 2, 'k2': 1}, 
    {'k1': 3, 'k2': 3}
]
>>> lod.sort(key=lambda d: d["k2"])
>>> lod
[
    {'k1': 2, 'k2': 1}, 
    {'k1': 1, 'k2': 2}, 
    {'k1': 3, 'k2': 3}
]
```

## Python built-in sorting using a key
You can use the key function to perform any operation on your items:
```python
>>> los = ["a", "aaa", "aa"]
>>> los.sort(key=lambda s: len(s))
>>> los
['a', 'aa', 'aaa']
```


## Exercise: Sort a list of tuples by the second element
Given the any list of tuples, create a function that will sort them by their second element.
```python
>>> lot = [
    (1, 2, "b"),
    (3, 1, "a"),
    (2, 3, "c")
]
```

## Solution: Sort a list of tuples by the second element
Given the any list of tuples, create a function that will sort them by their second element.
```python
>>> lot = [
    (1, 2, "b"),
    (3, 1, "a"),
    (2, 3, "c")
]
>>> lot.sort(key=lambda t: t[1])
>>> lot
[
    (3, 1, 'a'), 
    (1, 2, 'b'), 
    (2, 3, 'c')
]
```

## Making your classes comparable
Classes can be made comparable in Python by implementing the following:
- `__eq__`: Equal to
- `__lt__`: Less than
- `__gt__`: Greater than
`__le__`: Less than or equal to
`__ge__`: Greater than or equal to


## Extending Latitude
We can make it possible to compare `Latitudes` by implementing the `__eq__` and `__lt__` functions, as well as the rest of the comparison functions.
```python
@dataclass
class Latitude():
    """Class to validate and normalize the latitude value."""
    lat: float
    
    def __eq__(self, other: Self) -> bool:
        """Check if Latitudes are equal."""
        return self.lat == other.lat

    def __lt__(self, other: Self) -> bool:
        """Check if this Latitude is less than other."""
        return self.lat < other.lat
```

## Exercise: Implement the rest of the comparison functions
Implement the following for `Latitude`:
- `__gt__`: Greater than
- `__le__`: Less than or equal to
- `__ge__`: Greater than or equal to

Bonus: does it make sense to have a comparable `Longitude`? Why or why not?

## Sorting a list of Latitudes
Now we can implement our built-in sorting methods.

```python
>>> lats = [Latitude(20), Latitude(90), Latitude(-3)]
>>> lats.sort()
>>> lats
[Latitude(lat=-3), Latitude(lat=20), Latitude(lat=90)]
```

## Your projects
Your projects will need some kind of ordering. You'll have to implement comparisons in one of your iterable classes.

## Selection Sort
One of the easiest sorting algorithms to understand is selection sort. Now that we have access to the built-in sorting functions for comparison, we can design our own sorting functions.

The Selection sort algorithm is simply traversing a list for the next over and over again.

```python
for each index in a list of numbers:
    find the index of the smallest item in the rest of the list
    swap the items at index and index of smallest
```

## Selection Sort: Min Index
```python
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

```

## Selection Sort: Swap
```python
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
```

## Selection Sort: Algorithm
```python

def selection(lon: List[int]) -> List[int]:
    """
    Purpose: Sort a list of numbers
    Examples:
        selection([3, 1, 2]) -> [1, 2, 3]
    """
    for i in range(len(lon)):
        min_i = min_index(lon[1:])
        lon = swap(lon, i, min_i)
    return lon
        
expect(selection([3, 1, 2]), [1, 2, 3])
```

## Selection Sort: Analysis of Swap
```python
def swap(lon, i, j):                # ignore definition
    lon[i], lon[j] = lon[j], lon[i] # two changes (mutations)
    return lon                      # ignore return unless there's a mutation
```

## Selection Sort: Swap Big-O Analysis
Order means the class of problems that run in a certain time frame that depends on input length. We say that something is in the Order(1) when it takes a constant amount of time to run. It doesn't change depending on input length.
```python
def swap(lon, i, j):                # ignore definition
    lon[i], lon[j] = lon[j], lon[i] # two changes (mutations)
    return lon                      # ignore return unless there's a mutation
# Swap takes 2 steps, no matter how long lon is.
# Therefore, it is in the Order of 2, a.k.a., O(2)
# By definition, for any c where c is constant, O(c) = O(1)
# Therefore, Swap is O(1)
```

## Selection Sort: Swap Empirical Results
Let's prove it with our timing library.
```python
>>> lon = [1, 2, 3]
>>> start = time.perf_counter()
>>> swap(lon, 0, 1)
>>> end = time.perf_counter()
>>> print(end - start)
2.9199873097240925e-07

>>> lon = [1, 2, 3]*200
>>> start = time.perf_counter()
>>> swap(lon, 0, 1)
>>> end = time.perf_counter()
>>> print(end - start)
2.079978003166616e-07
```

## Exercise: Min Index complexity analysis
Analyze `min_index` using a Big-O analysis.
Then, use our timing pattern for empirical results.
Does `min_index` take longer when the list gets longer?

```python
def min_index(lon: List[int]) -> int:
    minimum_value = lon[0]
    minimum_index = 0
    for i in range(len(lon)):
        if lon[i] < minimum_value:
            minimum_index = i
    return minimum_index
```

## Solution: Min Index analysis
Analyze `min_index` using a Big-O analysis.
Then, use our timing pattern for empirical results.
Does `min_index` take longer when the list gets longer?

```python
def min_index(lon: List[int]) -> int:
    minimum_value = lon[0]         # 1 mutation
    minimum_index = 0              # 1 mutation
    for i in range(len(lon)):      # len(lon) mutations
        if lon[i] < minimum_value: # no mutation, could count
            minimum_index = i      # 1 mutation
    return minimum_index
# 4 + n -> O(4 + n) = O(n)

>>> lon = [1, 2, 3]
>>> start = time.perf_counter()
>>> min_index(lon)
>>> end = time.perf_counter()
>>> print(end - start)
2.9199873097240925e-07

>>> lon = [1, 2, 3]*20000
>>> start = time.perf_counter()
>>> min_index(lon)
>>> end = time.perf_counter()
>>> print(end - start)
5.274374998407438e-03    # much bigger number
```

## Selection Sort: Min Index analysis
Hopefully you can see that as `len(lon)` grows, it will be the dominant factor in our analysis. Therefore, we just say that `O(n) = O(c + n)`.

```python
def min_index(lon: List[int]) -> int:
    minimum_value = lon[0]         # 1 mutation
    minimum_index = 0              # 1 mutation
    for i in range(len(lon)):      # len(lon) mutations
        if lon[i] < minimum_value: # no mutation, could count
            minimum_index = i      # 1 mutation
    return minimum_index
```


## Selection Sort: Big-O Analysis
We can put together our previous analyses to finally analyze our sorting algorithm.

```python
def selection(lon):
    for i in range(len(lon)):          # This outer loop runs n times.
        min_i = i + min_index(lon[i:]) # Finding the min is O(n - i) in each iteration.
        swap(lon, i, min_i)            # Each swap is O(1)
    return lon
# Multiply outer loop by inner complexity:
# O(n) + O(n-1) + O(n-2) ... + O(1) = O(n^2)  
# O(n^2) + O(n) = O(n^2)
# Note that 1 + 2 + 3 ... n = n(n+1)*(1/2)
```

## Analysis of Built-ins
Most Python sorting algorithms will be closer to `O(nlogn)`, which is beyond the scope of this course. You should be able to do basic analysis of functions that use for-loops.

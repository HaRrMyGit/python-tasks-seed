#!/usr/bin/env -S python3
"""
Sortings demo
"""

from beartype import beartype
import random
from counting_container import CountingList, CountingOrdered
import sortings

if __name__ == "__main__":
    raw_data = list(range(1000))
    random.shuffle(raw_data)
    
    
    data_builtin: CountingList[CountingOrdered[int]] = CountingList(
        [CountingOrdered(e) for e in raw_data]
    )
    sortings.builtin_sort(data_builtin)
    print(
        f"Builtin Comps: {CountingOrdered.comparisons()}, Swaps: {CountingList.likely_swaps()}"
    )
    
    
    data_bubble: CountingList[CountingOrdered[int]] = CountingList(
        [CountingOrdered(e) for e in raw_data]
    )
    sortings.bubble_sort(data_bubble)
    print(
        f"Bubble Comps: {CountingOrdered.comparisons()}, Swaps: {CountingList.likely_swaps()}"
    )


    data_merge: CountingList[CountingOrdered[int]] = CountingList(
        [CountingOrdered(e) for e in raw_data]
    )
    sortings.merge_sort(data_merge)
    print(
        f"Merge Comps: {CountingOrdered.comparisons()}, Swaps: {CountingList.likely_swaps()}"
    )
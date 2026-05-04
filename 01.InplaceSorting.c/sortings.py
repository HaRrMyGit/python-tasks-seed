"""
Sorting algorithms
"""


def builtin_sort(data):
    """
    Standard library sorting algorithm


    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """
    if isinstance(data, list):
        data.sort()
    else:  # assume it is counting container
        # TODO: скормить корректно, или оставить эту идею, и
        # сделать less & swap
        data._array.sort()


def bubble_sort(data):
    """
    Bubble sort

    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """


    def bubble(data):
        isSorted = False
        while not isSorted:
            isSorted = True
            for i in range(len(data)-1):
                if data[i] > data[i + 1]: 
                    data[i], data[i + 1] = data[i + 1], data[i]
                    isSorted = False
    if isinstance(data, list):
        bubble(data)
    else:
        bubble(data._array)

def merge_sort(data):
    """
    Merge sort
    
    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """


    def _merge(left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    

    if len(data) <= 1:
        return data[:]
    
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return _merge(left, right)

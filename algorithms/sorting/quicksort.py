def quicksort(xs: list, lo: int, hi: int):
    """
    Quicksort is a recursive algorithm that swaps items around
    a pivot value. The items to the left of the pivot are all smaller
    and the items to the right are larger.
    This is done for each left/right partition until reaching a single item list,
    where no swapping occurs.
    :param xs: sequence to sort in-place
    :param lo: the starting index of partition
    :param hi: the exclusive right index of partition (usually length of xs)
    """
    if lo < hi:
        pivot_location = _partition(xs, lo, hi)

        quicksort(xs, lo, pivot_location)
        quicksort(xs, pivot_location + 1, hi)


def _partition(xs: list, lo: int, hi: int) -> int:
    """
    Iterates through partition from lo to hi indices.
    Pivot is leftmost value on start.
    As smaller elements than pivot are encountered, they are swapped with
    the left value, advancing its index.

    :param xs: full sequence
    :param lo: left index
    :param hi: exclusive right index
    :return: pivot location (index of a value for which all items to left are smaller,
        and all to right are larger)
    """
    pivot = xs[lo]
    leftwall = lo

    for i in range(lo + 1, hi):
        if xs[i] < pivot:
            # swap xs[i] with xs[leftwall] around pivot
            t = xs[i]
            xs[i] = xs[leftwall]
            xs[leftwall] = t

            # advance leftwall
            leftwall += 1

    return leftwall


def quicksort_immutable(xs: list) -> list:
    """
    Quicksort implementation without relying on mutation.
    It returns the sorted list as a result without changing the input list.

    :param xs: sequence to sort
    :return: sorted list
    """
    if not xs:
        return []

    pivot = xs[0]  # leftmost item is the pivot

    left_partition = [x for x in xs[1:] if x <= pivot]  # smaller or equal items, not including pivot
    right_partition = [x for x in xs[1:] if x > pivot]  # greater items, not including pivot

    # recursive call to sort left partition, the pivot element itself, and sort right partition,
    # concatenating the results, and returning.
    return quicksort_immutable(left_partition) + [pivot] + quicksort_immutable(right_partition)

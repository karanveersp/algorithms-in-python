
def bubblesort(xs: list):
    """
    Bubble sort algorithm implementation.
    Worst case time complexity is O(N^2).

    A loop within a loop, where the outer loop index i goes to n - 1,
    and the inner loop index j runs till n - 1 - i.
    This optimization prevents repetitive comparisons of values
    which have "bubbled" to the right.

    The inner loop compares the current value with its successor.
    If the value is smaller, a swap occurs.

    If an iteration of the inner loop happens without any swaps, the list is sorted.

    :param xs: sequence to sort in-place
    """
    n = len(xs)

    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if xs[j] > xs[j + 1]:
                # swap
                t = xs[j]
                xs[j] = xs[j + 1]
                xs[j + 1] = t
                swapped = True

        if not swapped:
            break

from algorithms import __version__
import algorithms.sorting as sorting


def test_bubblesort():
    items = [0, 3, 1, 2]
    sorting.bubblesort(items)
    assert items == [0, 1, 2, 3]


def test_quicksort():
    items = [2, 3, 2, 1, 0]
    sorting.quicksort(items, 0, len(items))
    assert items == [0, 1, 2, 2, 3]


def test_quicksort_immutable():
    items = [2, 3, 1, 2, 0]
    actual = sorting.quicksort_immutable(items)
    assert actual == [0, 1, 2, 2, 3]


def test_version():
    assert __version__ == '0.1.0'

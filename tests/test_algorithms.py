from algorithms import __version__
import algorithms.sorting as sorting


def test_bubblesort():
    items = [0, 3, 1, 2]
    sorting.bubblesort(items)
    assert items == [0, 1, 2, 3]


def test_version():
    assert __version__ == '0.1.0'

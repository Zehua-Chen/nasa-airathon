import os


_root = os.path.dirname(__file__)
_root = os.path.dirname(_root)
_root = os.path.dirname(_root)

_dataset = os.path.join(_root, "dataset")
_dataset_metadata = os.path.join(_dataset, "metadata")


def root() -> str:
    return _root


def dataset() -> str:
    return _dataset


def dataset_metadata() -> str:
    return _dataset_metadata


from importlib import metadata


# Export the version defined in project metadata
__version__ = metadata.version(__package__)
del metadata


def add_one(x):
    return x + 1

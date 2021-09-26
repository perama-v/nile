"""StarkNet/Cairo development toolbelt."""
from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version("nile")
except PackageNotFoundError:
    # package is not installed
    __version__ = None

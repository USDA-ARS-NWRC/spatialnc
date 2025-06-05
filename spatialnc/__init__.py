# -*- coding: utf-8 -*-

"""Top-level package for spatialnc."""


from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("spatialnc")
except PackageNotFoundError:
    __version__ = "unknown"

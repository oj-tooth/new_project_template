"""
<project-name>

Description of the project.
"""
__author__ = "Ollie Tooth (oliver.tooth@noc.ac.uk)"
__credits__ = "National Oceanography Centre (NOC), Southampton, UK"

from importlib.metadata import version as _version

from project import (
    cli,
    module,
)

try:
    __version__ = _version("project")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "9999.0.0"

__all__ = ("cli", "module")
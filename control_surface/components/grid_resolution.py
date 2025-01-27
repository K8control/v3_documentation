# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/grid_resolution.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3997 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import NamedTuple
from Live.Clip import GridQuantization
from ...base import listenable_property
from .. import Component
from ..controls import FixedRadioButtonGroup

class GridResolution(NamedTuple):
    """
    Documentation for GridResolution.
    """
    """
    Documentation for GridResolution.
    """
    name: str
    step_length: float
    grid: int
    is_triplet: bool


GRID_RESOLUTIONS = (
 GridResolution("1/32t", 0.08333333333333333, GridQuantization.g_thirtysecond, True),
 GridResolution("1/32", 0.125, GridQuantization.g_thirtysecond, False),
 GridResolution("1/16t", 0.16666666666666666, GridQuantization.g_sixteenth, True),
 GridResolution("1/16", 0.25, GridQuantization.g_sixteenth, False),
 GridResolution("1/8t", 0.3333333333333333, GridQuantization.g_eighth, True),
 GridResolution("1/8", 0.5, GridQuantization.g_eighth, False),
 GridResolution("1/4t", 0.6666666666666666, GridQuantization.g_quarter, True),
 GridResolution("1/4", 1.0, GridQuantization.g_quarter, False))
DEFAULT_INDEX = 3

class GridResolutionComponent(Component):
    """
    Documentation for GridResolutionComponent.
    """
    """
    Documentation for GridResolutionComponent.
    """
    resolution_buttons = FixedRadioButtonGroup(checked_color="NoteEditor.Resolution.Selected",
      unchecked_color="NoteEditor.Resolution.NotSelected",
      control_count=8)

    def __init__(self, name="Grid_Resolution", resolutions=None, default_index=DEFAULT_INDEX, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._resolutions = resolutions or GRID_RESOLUTIONS
        self._index = default_index
        self._update_resolution_buttons()

    @property
    def step_length(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._resolutions[self.index].step_length

    @property
    def clip_grid(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        resolution = self._resolutions[self.index]
        return (resolution.grid, resolution.is_triplet)

    @property
    def is_triplet(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._resolutions[self.index].is_triplet

    @listenable_property
    def index(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if index != self._index:
            self._index = index
            self._update_resolution_buttons()
            self.notify_index()

    def set_to(self, name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        name = name.lower()
        for index, grid_resolution in enumerate(self._resolutions):
            if grid_resolution.name == name:
                self.index = index
                return

        raise AssertionError("{} is not a valid GridResolution name".format(name))

    @resolution_buttons.checked
    def resolution_buttons(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.index = button.index

    def _update_resolution_buttons(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.resolution_buttons.checked_index = self._index

# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/color.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 3823 bytes
from __future__ import absolute_import, print_function, unicode_literals
from abc import ABC, abstractmethod
from typing import NamedTuple, Optional
from ...base import memoize, old_hasattr

@memoize
def create_rgb_color(values):
        """
        Documentation for create_rgb_color.
        """
        """
        Documentation for create_rgb_color.
        """
    if values is not None:
        return RgbColor(*values)


class Color(ABC):
    """
    Documentation for Color.
    """
    """
    Documentation for Color.
    """

    @abstractmethod
    def draw(self, interface):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        pass

    @property
    def midi_value(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        raise NotImplementedError


class SimpleColor(Color):
    """
    Documentation for SimpleColor.
    """
    """
    Documentation for SimpleColor.
    """

    def __init__(self, value, channel=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._value = value
        self._channel = channel

    @property
    def midi_value(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._value

    def draw(self, interface):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        interface.send_value((self._value), channel=(self._channel))


class RgbColor(Color):
    """
    Documentation for RgbColor.
    """
    """
    Documentation for RgbColor.
    """

    def __init__(self, *values, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(**k)
        self._values = values

    def draw(self, interface):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (interface.send_value)(*self._values)


class ColorPart(NamedTuple):
    """
    Documentation for ColorPart.
    """
    """
    Documentation for ColorPart.
    """
    value: int
    channel = None
    channel: Optional[int]


class ComplexColor(Color):
    """
    Documentation for ComplexColor.
    """
    """
    Documentation for ComplexColor.
    """

    def __init__(self, color_parts, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._color_parts = color_parts

    def draw(self, interface):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        for part in self._color_parts:
            interface.send_value((part.value), channel=(part.channel))


class FallbackColor(Color):
    """
    Documentation for FallbackColor.
    """
    """
    Documentation for FallbackColor.
    """

    def __init__(self, rgb_color, fallback_color):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._rgb_color = rgb_color
        self._fallback_color = fallback_color

    @property
    def midi_value(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._rgb_color.midi_value

    def draw(self, interface):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if old_hasattr(interface, "is_rgb") and interface.is_rgb:
            self._rgb_color.draw(interface)
        else:
            self._fallback_color.draw(interface)

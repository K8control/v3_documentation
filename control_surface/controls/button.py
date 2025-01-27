# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/controls/button.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3019 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import listenable_property
from ..display import Renderable
from elements.touch import TouchElement
from . import ButtonControlBase, control_color

class ButtonControl(ButtonControlBase):
    """
    Documentation for ButtonControl.
    """
    """
    Documentation for ButtonControl.
    """

    class State(ButtonControlBase.State, Renderable):
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        is_held = listenable_property.managed(False)
        color = control_color("DefaultButton.On")
        on_color = control_color(None)

        def __init__(self, color='DefaultButton.On', on_color=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            (super().__init__)(*a, **k)
            self.color = color
            self.on_color = on_color
            self._is_on = False

        @listenable_property
        def is_pressed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            return self._is_pressed

        @property
        def is_on(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            return self._is_on

        @is_on.setter
        def is_on(self, is_on):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            if is_on != self._is_on:
                self._is_on = is_on
                self._send_current_color()

        def _send_button_color(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            if self.on_color is not None and self.is_on:
                self._control_element.set_light(self.on_color)
            else:
                if self.color is not None:
                    self._control_element.set_light(self.color)

        def _has_delayed_event(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            return True

        def _call_listener(self, listener_name, *a):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            (super()._call_listener)(listener_name, *a)
            if listener_name == "pressed":
                self.notify_is_pressed()
            else:
                if listener_name == "pressed_delayed":
                    self.is_held = True
                else:
                    if listener_name == "released":
                        self.is_held = False
                        self.notify_is_pressed()


class TouchControl(ButtonControl):
    """
    Documentation for TouchControl.
    """
    """
    Documentation for TouchControl.
    """

    class State(ButtonControl.State):
    """
    Documentation for .
    """
    """
    Documentation for .
    """

        def set_control_element(self, control_element):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            super().set_control_element(control_element)

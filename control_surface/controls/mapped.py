# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/controls/mapped.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 4608 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import MappedSensitivitySettingControl as MappedSensitivitySettingControlBase
from ...base import EventObject, listens
from ...live import action, liveobj_valid
from .. import ABSOLUTE_MAP_MODES, EnumWrappingParameter
from . import ButtonControl as ButtonControlBase
from . import is_internal_parameter

class MappableButton(EventObject):
    """
    Documentation for MappableButton.
    """
    """
    Documentation for MappableButton.
    """

    def __init__(self, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._parameter = None

    def disconnect(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._parameter = None
        super().disconnect()

    @property
    def mapped_parameter(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._parameter

    @mapped_parameter.setter
    def mapped_parameter(self, parameter):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._parameter = parameter if liveobj_valid(parameter) else None
        self.enabled = self._parameter is not None
        self._MappableButton__on_parameter_value_changed.subject = self._parameter
        self._MappableButton__on_parameter_value_changed()

    @listens("value")
    def __on_parameter_value_changed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.is_on = liveobj_valid(self._parameter) and self._parameter.value


class MappedButtonControl(ButtonControlBase):
    """
    Documentation for MappedButtonControl.
    """
    """
    Documentation for MappedButtonControl.
    """

    class State(ButtonControlBase.State, MappableButton):
    """
    Documentation for .
    """
    """
    Documentation for .
    """

        def __init__(self, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            (super().__init__)(*a, **k)
            self.enabled = False

        def _call_listener(self, listener_name, *_):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            if listener_name == "pressed":
                action.toggle_or_cycle_parameter_value(self.mapped_parameter)


class MappedSensitivitySettingControl(MappedSensitivitySettingControlBase):
    """
    Documentation for MappedSensitivitySettingControl.
    """
    """
    Documentation for MappedSensitivitySettingControl.
    """

    class State(MappedSensitivitySettingControlBase.State):
    """
    Documentation for .
    """
    """
    Documentation for .
    """

        def __init__(self, default_sensitivity=None, fine_sensitivity=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            (super().__init__)(*a, **k)
            self.default_sensitivity = default_sensitivity or self.default_sensitivity
            self.fine_sensitivity = fine_sensitivity or self.fine_sensitivity

        def _update_direct_connection(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            self._control_value.subject = None
            self._absolute_control_value.subject = None
            self._quantized_stepper.reset()
            if self._control_element:
                if is_internal_parameter(self.mapped_parameter):
                    self._connect_internal_parameter()
                else:
                    self._update_control_element()

        @staticmethod
        def _is_parameter_valid(parameter):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            return not is_internal_parameter(parameter) or isinstance(parameter, EnumWrappingParameter)

        def _connect_internal_parameter(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            self._control_element.release_parameter()
            self._control_element.connect_to(self.mapped_parameter)
            if self._control_element.message_map_mode() in ABSOLUTE_MAP_MODES:
                self._absolute_control_value.subject = self._control_element
            else:
                self._control_value.subject = self._control_element
            self._update_control_sensitivity()

        @listens("value")
        def _absolute_control_value(self, value):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            step_size = self._control_element.max_value() / (self.mapped_parameter.max + 1)
            self.mapped_parameter.value = int(value / step_size)

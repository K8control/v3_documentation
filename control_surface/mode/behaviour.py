# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/mode/behaviour.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3733 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import mixin
from . import ModeButtonBehaviour, pop_last_mode

def make_reenter_behaviour(base_behaviour, on_reenter=None, *a, **k):
        """
        Documentation for make_reenter_behaviour.
        """
        """
        Documentation for make_reenter_behaviour.
        """
    return (mixin(ReenterBehaviourMixin, base_behaviour))(a, on_reenter=on_reenter, **k)


class ReenterBehaviourMixin:
    """
    Documentation for ReenterBehaviourMixin:
.
    """
    """
    Documentation for ReenterBehaviourMixin:
.
    """

    def __init__(self, on_reenter=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._on_reenter = on_reenter

    def press_immediate(self, component, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        was_active = component.selected_mode == mode
        super().press_immediate(component, mode)
        if was_active:
            self._on_reenter()


class ToggleBehaviour(ModeButtonBehaviour):
    """
    Documentation for ToggleBehaviour.
    """
    """
    Documentation for ToggleBehaviour.
    """

    def __init__(self, return_to_default=False, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._return_to_default = return_to_default

    def press_immediate(self, component, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if component.selected_mode == mode:
            if self._return_to_default:
                component.push_mode(component.modes[0])
                component.pop_unselected_modes()
            else:
                pop_last_mode(component, mode)
        else:
            component.push_mode(mode)


class MomentaryBehaviour(ModeButtonBehaviour):
    """
    Documentation for MomentaryBehaviour.
    """
    """
    Documentation for MomentaryBehaviour.
    """

    def __init__(self, entry_delay=None, exit_delay=None, immediate_exit_delay=None):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._entry_delay = entry_delay
        self._exit_delay = exit_delay
        self._immediate_exit_delay = self._exit_delay if immediate_exit_delay is None else immediate_exit_delay

    def press_immediate(self, component, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        component.push_mode(mode, delay=(self._entry_delay))

    def release_immediate(self, component, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        component.pop_mode(mode, delay=(self._immediate_exit_delay))

    def release_delayed(self, component, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        component.pop_mode(mode, delay=(self._exit_delay))

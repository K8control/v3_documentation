# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/mode/modes.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 12552 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from typing import cast
from ableton.v2.control_surface import StackingResource
from ableton.v2.control_surface.mode import _ModeEntry, tomode
from ...base import listenable_property, task
from .. import Component
from ..controls import ButtonControl, SendValueInputControl
from ..display import Renderable
from . import ImmediateBehaviour, make_mode_button_control

class ModesComponent(Component, Renderable):
    """
    Documentation for ModesComponent.
    """
    """
    Documentation for ModesComponent.
    """
    mode_selection_control = SendValueInputControl()
    cycle_mode_button = ButtonControl()
    default_behaviour = ImmediateBehaviour()
    previous_mode = listenable_property.managed(None)

    def __init__(self, name=None, support_momentary_mode_cycling=True, default_behaviour=None, is_private=False, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, is_private=is_private, **k)
        self._support_momentary_mode_cycling = support_momentary_mode_cycling
        self._mode_list = []
        self._mode_map = {}
        self._last_selected_mode = None
        self._mode_stack = StackingResource(self._do_enter_mode, self._do_leave_mode)
        self._push_mode_tasks = {}
        self._pop_mode_tasks = {}
        if default_behaviour is not None:
            self.default_behaviour = default_behaviour

    def disconnect(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._mode_stack.release_all()
        super().disconnect()

    @property
    def modes(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._mode_list

    @property
    def active_modes(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._mode_stack.clients

    @listenable_property
    def selected_mode(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._mode_stack.owner or self._last_selected_mode

    @selected_mode.setter
    def selected_mode(self, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.previous_mode = self.selected_mode
        if self.is_enabled():
            if self.selected_mode != mode:
                if mode is not None:
                    self.push_mode(mode)
                    self.pop_unselected_modes()
                    self.notify(self.notifications.Modes.select, cast(str, self.name), cast(str, mode))
                else:
                    self._mode_stack.release_all()
        else:
            self._last_selected_mode = mode

    def get_mode(self, name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        entry = self._mode_map.get(name, None)
        return entry and entry.mode

    def get_mode_button(self, name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return getattr(self, "%s_button" % name)

    def get_mode_groups(self, name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        entry = self._mode_map.get(name, None)
        if entry:
            return entry.groups
        return set()

    def push_mode(self, mode, delay=0):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._cancel_push_mode_task(mode)
        if mode in self._pop_mode_tasks:
            self._cancel_pop_mode_task(mode)
        else:
            if not delay:
                self._do_push_mode(mode)
            else:
                self._push_mode_tasks[mode] = self._tasks.add(task.sequence(task.wait(delay), task.run(partial(self._do_push_mode, mode))))

    def _do_push_mode(self, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._cancel_push_mode_task(mode)
        self._mode_stack.grab(mode)

    def _cancel_push_mode_task(self, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if mode in self._push_mode_tasks:
            self._push_mode_tasks[mode].kill()
            self._tasks.remove(self._push_mode_tasks[mode])
            del self._push_mode_tasks[mode]

    def pop_mode(self, mode, delay=0):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._cancel_pop_mode_task(mode)
        if mode in self._push_mode_tasks:
            self._cancel_push_mode_task(mode)
        else:
            if not delay:
                self._do_pop_mode(mode)
            else:
                self._pop_mode_tasks[mode] = self._tasks.add(task.sequence(task.wait(delay), task.run(partial(self._do_pop_mode, mode))))

    def _do_pop_mode(self, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._cancel_pop_mode_task(mode)
        if len(self.active_modes) <= 1:
            return
        self._mode_stack.release(mode)

    def _cancel_pop_mode_task(self, mode):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if mode in self._pop_mode_tasks:
            self._pop_mode_tasks[mode].kill()
            self._tasks.remove(self._pop_mode_tasks[mode])
            del self._pop_mode_tasks[mode]

    def pop_unselected_modes(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._mode_stack.release_stacked()

    def pop_groups(self, groups):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if not isinstance(groups, set):
            groups = set(groups)
        for client in self._mode_stack.clients:
            if self.get_mode_groups(client) & groups:
                self._mode_stack.release(client)

    def cycle_mode(self, delta=1):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        current_index = self._mode_list.index(self.selected_mode) if self.selected_mode else -delta
        current_index = (current_index + delta) % len(self._mode_list)
        self.selected_mode = self._mode_list[current_index]

    def add_mode(self, name, mode_or_component, groups=None, behaviour=None, selector=None):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if not isinstance(groups, set):
            groups = set(groups) if groups is not None else set()
        mode = tomode(mode_or_component)
        behaviour = behaviour or self.default_behaviour
        self._mode_list.append(name)
        self._mode_map[name] = _ModeEntry(mode=mode,
          cycle_mode_button_color=("{}.On".format(self._get_mode_color_base_name(name))),
          behaviour=behaviour,
          groups=groups)
        self.add_mode_button_control(name, behaviour)
        if callable(selector):
            selector(self, name)

    def add_mode_button_control(self, mode_name, behaviour):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        mode_color_basename = self._get_mode_color_base_name(mode_name)
        colors = {'mode_selected_color':("{}.On".format)(mode_color_basename), 
         'mode_unselected_color':("{}.Off".format)(mode_color_basename), 
         'mode_group_active_color':("{}.On".format)(mode_color_basename)}
        button_control = make_mode_button_control(self, mode_name, behaviour, **colors)
        self.add_control("{}_button".format(mode_name), button_control)
        self._update_mode_buttons(self.selected_mode)

    @mode_selection_control.value
    def mode_selection_control(self, value, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        modes = self.modes
        if value < len(modes):
            self.selected_mode = modes[value]

    @cycle_mode_button.pressed
    def cycle_mode_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self._mode_list:
            self.cycle_mode(1)

    @cycle_mode_button.released_delayed
    def cycle_mode_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self._mode_list:
            if self._support_momentary_mode_cycling:
                self.cycle_mode(-1)

    def _do_enter_mode(self, name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        entry = self._mode_map[name]
        entry.mode.enter_mode()
        self._update_mode_buttons(name)
        self._update_cycle_mode_button(name)
        self.notify_selected_mode(name)

    def _do_leave_mode(self, name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._mode_map[name].mode.leave_mode()
        if self._mode_stack.stack_size == 0:
            self._update_mode_buttons(None)
            self._update_cycle_mode_button(None)
            self.notify_selected_mode(None)

    def _get_mode_behaviour(self, name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        entry = self._mode_map.get(name, None)
        if entry is not None:
            return entry.behaviour
        return self.default_behaviour

    def _get_mode_color_base_name(self, mode_name):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return "{}.{}".format(self.name.title().replace("_", ""), mode_name.title().replace("_", ""))

    def on_enabled_changed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().on_enabled_changed()
        if not self.is_enabled():
            self._last_selected_mode = self.selected_mode
            self._mode_stack.release_all()
        else:
            if self._last_selected_mode:
                self.push_mode(self._last_selected_mode)

    def _update_mode_buttons(self, selected):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.is_enabled():
            for name in self._mode_map:
                self._get_mode_behaviour(name).update_button(self, name, selected)

        if selected in self._mode_list:
            self.mode_selection_control.value = self._mode_list.index(selected)

    def _update_cycle_mode_button(self, selected):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        entry = self._mode_map.get(selected)
        color = entry.cycle_mode_button_color if entry else None
        if color is not None:
            self.cycle_mode_button.color = color

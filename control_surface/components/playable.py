# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/playable.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 4887 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ...base import listenable_property
from .. import Component
from ..controls import ButtonControl, PlayableControl, control_matrix

class PlayableComponent(Component):
    """
    Documentation for PlayableComponent.
    """
    """
    Documentation for PlayableComponent.
    """
    matrix = control_matrix(PlayableControl, color=None)
    select_button = ButtonControl(color=None)
    pressed_pads = listenable_property.managed([])

    def __init__(self, name='Playable', matrix_always_listenable=False, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._takeover_pads = False
        self._default_playable_mode = PlayableControl.Mode.playable_and_listenable if matrix_always_listenable else PlayableControl.Mode.playable
        self.matrix._control_type = partial(PlayableControl,
          mode=(self._default_playable_mode))

    @property
    def width(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.matrix.width:
            return self.matrix.width
        return 4

    @property
    def height(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.matrix.height:
            return self.matrix.height
        return 4

    def set_matrix(self, matrix):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.matrix.set_control_element(matrix)
        self._reset_selected_pads()
        self._update_led_feedback()
        self._update_note_translations()

    def _set_control_pads_from_script(self, takeover_pads):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if takeover_pads != self._takeover_pads:
            self._takeover_pads = takeover_pads
            self._update_control_from_script()

    def _update_control_from_script(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        takeover_pads = self._takeover_pads or len(self.pressed_pads) > 0
        mode = PlayableControl.Mode.listenable if takeover_pads else self._default_playable_mode
        for button in self.matrix:
            button.set_mode(mode)

    @matrix.pressed
    def matrix(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._on_matrix_pressed(button)

    @matrix.released
    def matrix(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._on_matrix_released(button)

    def _on_matrix_pressed(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.pressed_pads = self.pressed_pads + [button]
        if len(self.pressed_pads) == 1:
            self._update_control_from_script()

    def _on_matrix_released(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if button in self.pressed_pads:
            self.pressed_pads = [p for p in self.pressed_pads if p is not button]
            if not self.pressed_pads:
                self._update_control_from_script()
        self._update_led_feedback()

    @select_button.value
    def select_button(self, _, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._set_control_pads_from_script(button.is_pressed)

    def _update_led_feedback(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        for button in self.matrix:
            self._update_button_color(button)

    def _update_button_color(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        pass

    def _update_note_translations(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        for button in self.matrix:
            if self._button_should_be_enabled(button):
                self._set_button_control_properties(button)
                button.enabled = True
            else:
                button.enabled = False

    def _reset_selected_pads(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.pressed_pads:
            self.pressed_pads = []
            self._update_control_from_script()

    def _set_button_control_properties(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        identifier, channel = self._note_translation_for_button(button)
        button.identifier = identifier
        button.channel = channel

    def _button_should_be_enabled(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        identifier, _ = self._note_translation_for_button(button)
        return identifier is None or isinstance(identifier, int) and identifier < 128

    def _note_translation_for_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return (
         button.identifier, button.channel)

    def update(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().update()
        if self.is_enabled():
            self._set_control_pads_from_script(False)

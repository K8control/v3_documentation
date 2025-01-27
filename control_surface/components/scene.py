# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/scene.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 5236 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import depends, listens
from ...live import action, display_name, liveobj_changed, liveobj_valid, scene_index
from .. import Component
from ..controls import ButtonControl
from ..display import Renderable
from ..skin import LiveObjSkinEntry
from . import ClipSlotComponent

class SceneComponent(Component, Renderable):
    """
    Documentation for SceneComponent.
    """
    """
    Documentation for SceneComponent.
    """
    launch_button = ButtonControl()
    select_button = ButtonControl(color=None)
    delete_button = ButtonControl(color=None)
    duplicate_button = ButtonControl(color=None)
    include_in_top_level_state = False

    @depends(session_ring=None)
    def __init__(self, session_ring=None, clip_slot_component_type=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._session_ring = session_ring
        self._scene = None
        clip_slot_component_type = clip_slot_component_type or ClipSlotComponent
        self._clip_slots = [clip_slot_component_type(parent=self) for _ in range(session_ring.num_tracks)]
        self.register_slot(session_ring, self._reassign_clip_slots, "tracks")

    @property
    def scene(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._scene

    def set_scene(self, scene):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if liveobj_changed(scene, self._scene):
            self._scene = scene
            self._SceneComponent__on_is_triggered_changed.subject = scene
            self._SceneComponent__on_scene_color_changed.subject = scene
            self.update()

    def clip_slot(self, index):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._clip_slots[index]

    def set_launch_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.launch_button.set_control_element(button)
        self.update()

    @launch_button.pressed
    def launch_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._on_launch_button_pressed()

    def _on_launch_button_pressed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        scene_name = display_name(self._scene) if liveobj_valid(self._scene) else ""
        if self.select_button.is_pressed:
            if action.select(self._scene):
                self.notify(self.notifications.Scene.select, scene_name)
        elif self.duplicate_button.is_pressed:
            action.duplicate(self._scene)
        else:
            if self.delete_button.is_pressed:
                if action.delete(self._scene):
                    self.notify(self.notifications.Scene.delete, scene_name)
            else:
                self._do_launch_scene()

    def _do_launch_scene(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        action.fire((self._scene), button_state=True)

    @launch_button.released
    def launch_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._on_launch_button_released()

    def _on_launch_button_released(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.launch_button.is_momentary:
            if not self._any_modifier_pressed():
                action.fire((self._scene), button_state=False)

    def _any_modifier_pressed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self.select_button.is_pressed or self.delete_button.is_pressed or self.duplicate_button.is_pressed

    def update(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().update()
        self._reassign_clip_slots()
        self._update_launch_button_color()

    def _update_launch_button_color(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        value_to_send = "Session.NoScene"
        if liveobj_valid(self._scene):
            value_to_send = self._feedback_value()
        self.launch_button.color = value_to_send

    def _feedback_value(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        value = "Session.Scene"
        if self._scene.is_triggered:
            value = "Session.SceneTriggered"
        return LiveObjSkinEntry(value, self._scene)

    def _reassign_clip_slots(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if liveobj_valid(self._scene) and self.is_enabled():
            scene_offset = scene_index(self._scene)
            regular_tracks = self.song.tracks
            for slot_wrapper, track in zip(self._clip_slots, self._session_ring.tracks):
                if track in regular_tracks:
                    slot_wrapper.set_clip_slot(track.clip_slots[scene_offset])
                else:
                    slot_wrapper.set_non_player_track(track)

        else:
            for slot in self._clip_slots:
                slot.set_clip_slot(None)

    @listens("is_triggered")
    def __on_is_triggered_changed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_launch_button_color()

    @listens("color")
    def __on_scene_color_changed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_launch_button_color()

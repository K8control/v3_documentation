# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/auto_arm.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 3482 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import depends, listens, listens_group, task
from ...live import any_track_armed, liveobj_changed, liveobj_valid
from .. import Component

def track_can_be_auto_armed(track):
        """
        Documentation for track_can_be_auto_armed.
        """
        """
        Documentation for track_can_be_auto_armed.
        """
    return liveobj_valid(track) and track.can_be_armed and track.has_midi_input


class AutoArmComponent(Component):
    """
    Documentation for AutoArmComponent.
    """
    """
    Documentation for AutoArmComponent.
    """

    @depends(target_track=None)
    def __init__(self, name='Auto_Arm', target_track=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._target_track = target_track
        self._auto_arm_target = None
        self._update_auto_arm_task = self._tasks.add(task.run(self._update_auto_arm))
        self.register_slot(self._target_track, self.update, "target_track")
        self._AutoArmComponent__on_tracks_changed.subject = self.song
        self._AutoArmComponent__on_tracks_changed()

    def disconnect(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._setup_new_auto_arm_target(None)
        super().disconnect()

    def update(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().update()
        self._update_auto_arm()

    def _can_auto_arm(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self.is_enabled() and not any_track_armed()

    def _auto_arm_target_changed(self, target_track):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return liveobj_changed(target_track, self._auto_arm_target) or not track_can_be_auto_armed(self._auto_arm_target)

    def _set_auto_arm_state(self, state):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if liveobj_valid(self._auto_arm_target):
            if self._auto_arm_target.implicit_arm != state:
                self._auto_arm_target.implicit_arm = state

    def _setup_new_auto_arm_target(self, target_track):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        new_target = target_track if track_can_be_auto_armed(target_track) else None
        self._AutoArmComponent__on_implicit_arm_changed.subject = new_target
        self._set_auto_arm_state(False)
        self._auto_arm_target = new_target

    def _update_auto_arm(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_auto_arm_task.kill()
        if self._can_auto_arm():
            target_track = self._target_track.target_track
            if self._auto_arm_target_changed(target_track):
                self._setup_new_auto_arm_target(target_track)
            self._set_auto_arm_state(True)
        else:
            self._setup_new_auto_arm_target(None)

    @listens("implicit_arm")
    def __on_implicit_arm_changed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_auto_arm()

    @listens_group("arm")
    def __on_arm_changed(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_auto_arm_task.restart()

    @listens_group("input_routing_type")
    def __on_input_routing_type_changed(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_auto_arm_task.restart()

    @listens_group("is_frozen")
    def __on_frozen_state_changed(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_auto_arm_task.restart()

    @listens("tracks")
    def __on_tracks_changed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        tracks = list(filter((lambda t: t.can_be_armed), self.song.tracks))
        self._AutoArmComponent__on_arm_changed.replace_subjects(tracks)
        self._AutoArmComponent__on_input_routing_type_changed.replace_subjects(tracks)
        self._AutoArmComponent__on_frozen_state_changed.replace_subjects(tracks)

# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/recording.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 8921 bytes
from __future__ import absolute_import, print_function, unicode_literals
from abc import ABC, abstractmethod
from Live.Song import SessionRecordStatus
from ...base import depends
from ...live import is_track_armed, is_track_recording, liveobj_valid, playing_clip_slot, prepare_new_clip_slot
from .. import Component
from ..controls import ButtonControl, ToggleButtonControl
from ..display import Renderable

class RecordingMethod(ABC):
    """
    Documentation for RecordingMethod.
    """
    """
    Documentation for RecordingMethod.
    """

    @depends(song=None, target_track=None)
    def __init__(self, song=None, target_track=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self.song = song
        self.target_track = target_track

    @abstractmethod
    def trigger_recording(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        pass

    def start_recording(self, *_):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.song.session_record = True

    def stop_recording(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        status = self.song.session_record_status
        was_recording = status != SessionRecordStatus.off or self.song.session_record
        if was_recording:
            self.song.session_record = False
        return was_recording

    @staticmethod
    def can_record_into_clip_slot(clip_slot):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return liveobj_valid(clip_slot) and is_track_armed(clip_slot.canonical_parent)


class BasicRecordingMethod(RecordingMethod):
    """
    Documentation for BasicRecordingMethod.
    """
    """
    Documentation for BasicRecordingMethod.
    """

    def trigger_recording(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if not self.stop_recording():
            self.start_recording()


class NextSlotRecordingMethod(RecordingMethod):
    """
    Documentation for NextSlotRecordingMethod.
    """
    """
    Documentation for NextSlotRecordingMethod.
    """

    def trigger_recording(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if not self.stop_recording():
            slot = prepare_new_clip_slot(self.target_track.target_track)
            if self.can_record_into_clip_slot(slot):
                slot.fire()
            else:
                self.start_recording()


class NextSlotWithOverdubRecordingMethod(NextSlotRecordingMethod):
    """
    Documentation for NextSlotWithOverdubRecordingMethod.
    """
    """
    Documentation for NextSlotWithOverdubRecordingMethod.
    """

    def trigger_recording(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        track = self.target_track.target_track
        playing_slot = playing_clip_slot(track)
        if (is_track_recording(track) or playing_slot) is not None:
            self.song.overdub = not self.song.overdub
            self.song.is_playing = self.song.is_playing or True
        else:
            super().trigger_recording()


class RecordingComponent(Component, Renderable):
    """
    Documentation for RecordingComponent.
    """
    """
    Documentation for RecordingComponent.
    """
    session_record_button = ButtonControl()
    session_overdub_button = ToggleButtonControl(color="Recording.SessionOverdubOff",
      on_color="Recording.SessionOverdubOn")
    arrangement_record_button = ToggleButtonControl(color="Recording.ArrangementRecordOff",
      on_color="Recording.ArrangementRecordOn")
    arrangement_overdub_button = ToggleButtonControl(color="Recording.ArrangementOverdubOff",
      on_color="Recording.ArrangementOverdubOn")
    new_button = ButtonControl(color="Recording.New",
      pressed_color="Recording.NewPressed")

    @depends(target_track=None)
    def __init__(self, target_track=None, recording_method_type=None, name='Recording', *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        recording_method_type = recording_method_type or BasicRecordingMethod
        self._recording_method = recording_method_type()
        song = self.song
        self.session_overdub_button.connect_property(song, "overdub")
        self.arrangement_record_button.connect_property(song, "record_mode")
        self.arrangement_overdub_button.connect_property(song, "arrangement_overdub")
        self.register_slot(song, self._update_session_record_button, "session_record_status")
        self.register_slot(song, self._update_session_record_button, "session_record")
        self._update_session_record_button()
        self._target_track = target_track
        self.register_slot(target_track, self._update_new_button, "target_clip")
        self._update_new_button()

    @session_record_button.pressed
    def session_record_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._recording_method.trigger_recording()

    @new_button.pressed
    def new_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if prepare_new_clip_slot((self._target_track.target_track), stop=True):
            self.notify(self.notifications.Recording.new)

    def _update_session_record_button(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        song = self.song
        status = song.session_record_status
        if status == SessionRecordStatus.transition:
            self.session_record_button.color = "Recording.SessionRecordTransition"
        else:
            if status == SessionRecordStatus.on or song.session_record:
                self.session_record_button.color = "Recording.SessionRecordOn"
            else:
                self.session_record_button.color = "Recording.SessionRecordOff"

    def _update_new_button(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.new_button.enabled = liveobj_valid(self._target_track.target_clip)


class ViewBasedRecordingComponent(RecordingComponent):
    """
    Documentation for ViewBasedRecordingComponent.
    """
    """
    Documentation for ViewBasedRecordingComponent.
    """

    def __init__(self, name='View_Based_Recording', *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._record_button = None
        self._overdub_button = None
        self.register_slot(self.application.view, self.update, "focused_document_view")

    def disconnect(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().disconnect()
        self._record_button = None
        self._overdub_button = None

    def set_record_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._record_button = button
        self._update_record_button_assignments()

    def set_overdub_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._overdub_button = button
        self._update_overdub_button_assignments()

    def update(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().update()
        self._update_record_button_assignments()
        self._update_overdub_button_assignments()

    def _update_record_button_assignments(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.arrangement_record_button.set_control_element(None)
        self.session_record_button.set_control_element(None)
        if self.application.view.focused_document_view == "Session":
            self.session_record_button.set_control_element(self._record_button)
        else:
            self.arrangement_record_button.set_control_element(self._record_button)

    def _update_overdub_button_assignments(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.arrangement_overdub_button.set_control_element(None)
        self.session_overdub_button.set_control_element(None)
        if self.application.view.focused_document_view == "Session":
            self.session_overdub_button.set_control_element(self._overdub_button)
        else:
            self.arrangement_overdub_button.set_control_element(self._overdub_button)

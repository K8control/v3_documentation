# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/all.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 8711 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from typing import NewType
import Live.ClipSlot as ClipSlot
from ....base import pitch_index_to_string
from ....live import display_name, major_version
from .type_decl import Fn, Notification, _DefaultText, _TransformDefaultText
from .util import toggle_text_generator
SceneName = NewType("SceneName", str)
TrackName = NewType("TrackName", str)
ClipName = NewType("ClipName", str)
DeviceName = NewType("DeviceName", str)
DeviceBank = NewType("DeviceBank", str)
PadName = NewType("PadName", str)
ComponentName = NewType("ComponentName", str)
ModeName = NewType("ModeName", str)
Subdivision = NewType("Subdivision", str)
Resolution = NewType("Resolution", str)
Range = NewType("Range", str)
RangeName = NewType("RangeName", str)

class Notifications:
    """
    Documentation for Notifications:
.
    """
    """
    Documentation for Notifications:
.
    """
    identify = lambda: "Live {}\nConnected".format(major_version())
    identify: "Notification"
    full_velocity = toggle_text_generator("Full Velocity\n{}")
    full_velocity: "Notification[Fn[bool]]"
    note_repeat = toggle_text_generator("Note Repeat\n{}")
    note_repeat: "Notification[Fn[bool]]"
    controlled_range = "{}\n{}".format
    controlled_range: "Notification[Fn[RangeName, Range]]"
    generic = "{}".format
    generic: "Notification[Fn[str]]"

    class Element:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        button_lock = lambda name, state: "{}\n{}".format(name.replace("_", " "), "locked" if state else "unlocked")
        button_lock: "Notification[Fn[str, bool]]"

    class Clipboard:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        clear = "Clipboard\ncleared"
        clear: "Notification"

    class UndoRedo:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        undo = "{}".format
        undo: "Notification[Fn[str]]"
        error_undo_no_action = "No Action To Undo"
        error_undo_no_action: "Notification"
        redo = "{}".format
        redo: "Notification[Fn[str]]"
        error_redo_no_action = "No Action To Redo"
        error_redo_no_action: "Notification"

    class Transport:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        metronome = toggle_text_generator("Metronome\n{}")
        metronome: "Notification[Fn[bool]]"
        midi_capture = lambda tempo_set_by_capture, tempo:         if tempo_set_by_capture:
"Captured\n{} BPM".format(int(tempo)) # Avoid dead code: "Captured"
        midi_capture: "Notification[Fn[bool, float]]"
        loop = toggle_text_generator("Loop\n{}")
        loop: "Notification[Fn[bool]]"
        tap_tempo = lambda tempo: "Tap Tempo\n{}".format(int(tempo))
        tap_tempo: "Notification[Fn[float]]"
        record_quantize = toggle_text_generator("Record Quantize\n{}")
        record_quantize: "Notification[Fn[bool]]"

    class Recording:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        new = "New Clip Slot\nselected"
        new: "Notification"

    class Automation:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        delete = "Automation\ndeleted"
        delete: "Notification"

    class Scene:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        select = "{}\nselected".format
        select: "Notification[Fn[SceneName]]"
        delete = "{}\ndeleted".format
        delete: "Notification[Fn[SceneName]]"

    class Track:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        lock = lambda name, state: "{}\n{}".format(name, "locked" if state else "unlocked")
        lock: "Notification[Fn[TrackName, bool]]"
        select = "{}".format
        select: "Notification[Fn[TrackName]]"
        delete = "{}\ndeleted".format
        delete: "Notification[Fn[TrackName]]"
        duplicate = "{}\nduplicated".format
        duplicate: "Notification[Fn[TrackName]]"
        mute = lambda name, state: "{}\n{}".format(name, "muted" if state else "unmuted")
        mute: "Notification[Fn[TrackName, bool]]"

    class Clip:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        select = "{}\nselected".format
        select: "Notification[Fn[ClipName]]"
        delete = "{}\ndeleted".format
        delete: "Notification[Fn[ClipName]]"
        duplicate = "{}\nduplicated".format
        duplicate: "Notification[Fn[ClipName]]"
        error_delete_empty_slot = "Clip Slot\nalready empty"
        error_delete_empty_slot: "Notification"
        quantize = "{} {}\nquantized".format
        quantize: "Notification[Fn[ClipName, Subdivision]]"
        error_quantize_invalid_resolution = "Cannot quantize to {}".format
        error_quantize_invalid_resolution: "Notification[Fn[Resolution]]"
        double_loop = "Loop\ndoubled"
        double_loop: "Notification"

        class CopyPaste:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            error_copy_from_group_slot = "Cannot copy from Group Slot"
            error_copy_from_group_slot: "Notification"
            error_copy_from_empty_slot = "Cannot copy from empty Slot"
            error_copy_from_empty_slot: "Notification"
            error_copy_recording_clip = "Cannot copy recording Clip"
            error_copy_recording_clip: "Notification"
            copy = lambda slot: "{}\ncopied".format(display_name(slot))
            copy: "Notification[Fn[ClipSlot]]"
            error_paste_to_group_slot = "Cannot paste into Group Slot"
            error_paste_to_group_slot: "Notification"
            error_paste_audio_to_midi = "Cannot paste an audio Clip into a MIDI Track"
            error_paste_audio_to_midi: "Notification"
            error_paste_midi_to_audio = "Cannot paste a MIDI Clip into an audio Track"
            error_paste_midi_to_audio: "Notification"
            paste = lambda slot: "{}\npasted".format(display_name(slot))
            paste: "Notification[Fn[ClipSlot]]"

    class Device:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        lock = lambda name, state: "{}\n{}".format(name, "locked" if state else "unlocked")
        lock: "Notification[Fn[DeviceName, bool]]"
        select = "{}".format
        select: "Notification[Fn[DeviceName]]"
        bank = "{}".format
        bank: "Notification[Fn[DeviceBank]]"

    class DrumGroup:
    """
    Documentation for .
    """
    """
    Documentation for .
    """

        class Pad:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            select = "{}\nselected".format
            select: "Notification[Fn[PadName]]"
            delete = "{}\ndeleted".format
            delete: "Notification[Fn[PadName]]"
            mute = lambda name, state: "{}\n{}".format(name, "muted" if state else "unmuted")
            mute: "Notification[Fn[PadName]]"
            delete_notes = "{}\nnotes deleted".format
            delete_notes: "Notification[Fn[PadName]]"

            class CopyPaste:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
                error_copy_from_empty_pad = "Cannot copy from empty Pad"
                error_copy_from_empty_pad: "Notification"
                copy = "{}\ncopied".format
                copy: "Notification[Fn[PadName]]"
                error_paste_to_source_pad = "Cannot paste to source Pad"
                error_paste_to_source_pad: "Notification"
                paste = "{}\npasted".format
                paste: "Notification[Fn[PadName]]"

        class Page:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            up = "Page up"
            up: "Notification"
            down = "Page down"
            down: "Notification"

        class Scroll:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            up = "Scroll up"
            up: "Notification"
            down = "Scroll down"
            down: "Notification"

    class Simpler:
    """
    Documentation for .
    """
    """
    Documentation for .
    """

        class Slice:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            select = "Slice {}\nselected".format
            select: "Notification[Fn[int]]"
            delete = "Slice {}\ndeleted".format
            delete: "Notification[Fn[int]]"
            delete_notes = "Slice {}\nnotes deleted".format
            delete_notes: "Notification[Fn[int]]"

        class Page:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            up = "Page up"
            up: "Notification"
            down = "Page down"
            down: "Notification"

        class Scroll:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            up = "Scroll up"
            up: "Notification"
            down = "Scroll down"
            down: "Notification"

    class Notes:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        delete = "Notes\ndeleted"
        delete: "Notification"
        error_no_notes_to_delete = "No notes\nto delete"
        error_no_notes_to_delete: "Notification"
        nudge = "Notes\nnudged"
        nudge: "Notification"

        class Pitch:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            select = lambda index: "Pitch {}\nselected".format(pitch_index_to_string(index))
            select: "Notification[Fn[int]]"
            delete = lambda index: "{}\nnotes deleted".format(pitch_index_to_string(index))
            delete: "Notification[Fn[int]]"

        class Octave:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            up = "Octave up"
            up: "Notification"
            down = "Octave down"
            down: "Notification"

        class ScaleDegree:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            up = "Scale degree\nup"
            up: "Notification"
            down = "Scale degree\ndown"
            down: "Notification"

    class Modes:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        select = None
        select: "Notification[Fn[ComponentName, ModeName]]"

    class DefaultText(_DefaultText):
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        pass

    class TransformDefaultText(_TransformDefaultText):
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        pass

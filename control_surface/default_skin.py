# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/default_skin.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 9123 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .colors import BasicColors
from .skin import Skin, merge_skins

def create_skin(skin=None, colors=None):
        """
        Documentation for create_skin.
        """
        """
        Documentation for create_skin.
        """
    skins = [
     default_skin]
    if skin:
        skins.append(Skin(skin))
    if colors:
        skins.append(Skin(colors))
    return merge_skins(*skins)


class DefaultColors:
    """
    Documentation for DefaultColors:
.
    """
    """
    Documentation for DefaultColors:
.
    """

    class DefaultButton:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        On = BasicColors.ON
        Off = BasicColors.OFF
        Disabled = BasicColors.OFF

    class TargetTrack:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        LockOn = BasicColors.ON
        LockOff = BasicColors.OFF

    class Transport:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        PlayOn = BasicColors.ON
        PlayOff = BasicColors.OFF
        StopOn = BasicColors.ON
        StopOff = BasicColors.OFF
        AutomationArmOn = BasicColors.ON
        AutomationArmOff = BasicColors.OFF
        LoopOn = BasicColors.ON
        LoopOff = BasicColors.OFF
        MetronomeOn = BasicColors.ON
        MetronomeOff = BasicColors.OFF
        PunchOn = BasicColors.ON
        PunchOff = BasicColors.OFF
        TapTempoPressed = BasicColors.ON
        TapTempo = BasicColors.OFF
        NudgePressed = BasicColors.ON
        Nudge = BasicColors.OFF
        SeekPressed = BasicColors.ON
        Seek = BasicColors.OFF
        CanReEnableAutomation = BasicColors.ON
        CanCaptureMidi = BasicColors.ON
        CanJumpToCue = BasicColors.ON
        CannotJumpToCue = BasicColors.OFF
        SetCuePressed = BasicColors.ON
        SetCue = BasicColors.OFF
        RecordQuantizeOn = BasicColors.ON
        RecordQuantizeOff = BasicColors.OFF

    class Recording:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        ArrangementRecordOn = BasicColors.ON
        ArrangementRecordOff = BasicColors.OFF
        ArrangementOverdubOn = BasicColors.ON
        ArrangementOverdubOff = BasicColors.OFF
        SessionRecordOn = BasicColors.ON
        SessionRecordTransition = BasicColors.ON
        SessionRecordOff = BasicColors.OFF
        SessionOverdubOn = BasicColors.ON
        SessionOverdubOff = BasicColors.OFF
        NewPressed = BasicColors.ON
        New = BasicColors.OFF

    class UndoRedo:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        UndoPressed = BasicColors.ON
        Undo = BasicColors.OFF
        RedoPressed = BasicColors.ON
        Redo = BasicColors.OFF

    class ViewControl:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        TrackPressed = BasicColors.ON
        Track = BasicColors.ON
        ScenePressed = BasicColors.ON
        Scene = BasicColors.ON

    class ViewToggle:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        SessionOn = BasicColors.ON
        SessionOff = BasicColors.OFF
        DetailOn = BasicColors.ON
        DetailOff = BasicColors.OFF
        ClipOn = BasicColors.ON
        ClipOff = BasicColors.OFF
        BrowserOn = BasicColors.ON
        BrowserOff = BasicColors.OFF

    class Mixer:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        ArmOn = BasicColors.ON
        ArmOff = BasicColors.OFF
        ImplicitArmOn = BasicColors.ON
        MuteOn = BasicColors.ON
        MuteOff = BasicColors.OFF
        SoloOn = BasicColors.ON
        SoloOff = BasicColors.OFF
        Selected = BasicColors.ON
        NotSelected = BasicColors.OFF
        CrossfadeA = BasicColors.ON
        CrossfadeB = BasicColors.ON
        CrossfadeOff = BasicColors.OFF
        CycleSendIndexPressed = BasicColors.OFF
        CycleSendIndex = BasicColors.ON
        CycleSendIndexDisabled = BasicColors.OFF
        NoTrack = BasicColors.OFF

    class Session:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        Slot = BasicColors.OFF
        SlotRecordButton = BasicColors.OFF
        NoSlot = BasicColors.OFF
        ClipStopped = BasicColors.OFF
        ClipTriggeredPlay = BasicColors.ON
        ClipTriggeredRecord = BasicColors.ON
        ClipPlaying = BasicColors.ON
        ClipRecording = BasicColors.ON
        Scene = BasicColors.OFF
        SceneTriggered = BasicColors.ON
        NoScene = BasicColors.OFF
        StopClipTriggered = BasicColors.ON
        StopClip = BasicColors.OFF
        StopClipDisabled = BasicColors.OFF
        StopAllClipsPressed = BasicColors.ON
        StopAllClips = BasicColors.OFF
        NavigationPressed = BasicColors.ON
        Navigation = BasicColors.ON

    class Zooming:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        Selected = BasicColors.OFF
        Stopped = BasicColors.ON
        Playing = BasicColors.ON
        Empty = BasicColors.OFF

    class ClipActions:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        Delete = BasicColors.OFF
        DeletePressed = BasicColors.ON
        Double = BasicColors.OFF
        DoublePressed = BasicColors.ON
        Duplicate = BasicColors.OFF
        DuplicatePressed = BasicColors.ON
        Quantize = BasicColors.OFF
        QuantizedPressed = BasicColors.ON

    class Device:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        On = BasicColors.ON
        Off = BasicColors.OFF
        LockOn = BasicColors.ON
        LockOff = BasicColors.OFF
        NavigationPressed = BasicColors.ON
        Navigation = BasicColors.OFF

        class Bank:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            Selected = BasicColors.ON
            NotSelected = BasicColors.OFF
            NavigationPressed = BasicColors.ON
            Navigation = BasicColors.ON

    class Accent:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        On = BasicColors.ON
        Off = BasicColors.OFF

    class DrumGroup:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        PadEmpty = BasicColors.OFF
        PadFilled = BasicColors.OFF
        PadSelected = BasicColors.ON
        PadMuted = BasicColors.ON
        PadMutedSelected = BasicColors.ON
        PadSoloed = BasicColors.ON
        PadSoloedSelected = BasicColors.ON
        PadAction = BasicColors.ON
        ScrollPressed = BasicColors.ON
        Scroll = BasicColors.ON

    class SlicedSimpler:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        NoSlice = BasicColors.OFF
        SliceNotSelected = BasicColors.OFF
        SliceSelected = BasicColors.ON
        NextSlice = BasicColors.ON
        PadAction = BasicColors.ON
        ScrollPressed = BasicColors.ON
        Scroll = BasicColors.ON

    class NoteEditor:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        NoClip = BasicColors.OFF
        StepDisabled = BasicColors.OFF
        StepEmpty = BasicColors.OFF
        StepFilled = BasicColors.ON
        StepMuted = BasicColors.OFF

        class Resolution:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            Selected = BasicColors.ON
            NotSelected = BasicColors.OFF

    class LoopSelector:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        InsideLoopSelected = BasicColors.ON
        InsideLoop = BasicColors.OFF
        OutsideLoopSelected = BasicColors.ON
        OutsideLoop = BasicColors.OFF
        Playhead = BasicColors.OFF
        PlayheadRecord = BasicColors.OFF
        NavigationPressed = BasicColors.ON
        Navigation = BasicColors.OFF

    class Clipboard:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
        Empty = BasicColors.OFF
        Filled = BasicColors.ON

    class Translation:
    """
    Documentation for .
    """
    """
    Documentation for .
    """

        class Channel:
    """
    Documentation for .
    """
    """
    Documentation for .
    """
            Selected = BasicColors.ON
            NotSelected = BasicColors.OFF


default_skin = Skin(DefaultColors)

# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/instrument_finder.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3943 bytes
from __future__ import absolute_import, print_function, unicode_literals
from itertools import chain
import Live
from ..base import depends, listenable_property, listens_group
from ..live import liveobj_changed
from . import Component, find_instrument_devices, find_instrument_meeting_requirement
from .display import Renderable

def find_drum_group_device(track_or_chain):
        """
        Documentation for find_drum_group_device.
        """
        """
        Documentation for find_drum_group_device.
        """

    def requirement(instrument):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return instrument.can_have_drum_pads

    return find_instrument_meeting_requirement(requirement, track_or_chain)


def find_sliced_simpler(track_or_chain):
        """
        Documentation for find_sliced_simpler.
        """
        """
        Documentation for find_sliced_simpler.
        """

    def requirement(instrument):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return getattr(instrument, "playback_mode", None) == Live.SimplerDevice.PlaybackMode.slicing

    return find_instrument_meeting_requirement(requirement, track_or_chain)


class InstrumentFinderComponent(Component, Renderable):
    """
    Documentation for InstrumentFinderComponent.
    """
    """
    Documentation for InstrumentFinderComponent.
    """
    __events__ = ('instrument', )
    drum_group = listenable_property.managed(None)
    sliced_simpler = listenable_property.managed(None)
    any_instrument = listenable_property.managed(None)

    @depends(target_track=None)
    def __init__(self, name='Instrument_Finder', target_track=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._target_track = target_track
        self.register_slot(target_track, self.update, "target_track")
        self.update()

    @listens_group("devices")
    def __on_devices_changed(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.update()

    @listens_group("chains")
    def __on_chains_changed(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.update()

    @listens_group("playback_mode")
    def __on_slicing_changed(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.update()

    def update(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().update()
        if self.is_enabled():
            self._update_listeners()
            self._update_instruments()

    def _update_listeners(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        track = self._target_track.target_track
        devices = list(find_instrument_devices(track))
        racks = list(filter((lambda d: d.can_have_chains), devices))
        simplers = list(filter((lambda d: hasattr(d, "playback_mode")), devices))
        chains = list(chain([track], *[d.chains for d in racks]))
        self._InstrumentFinderComponent__on_chains_changed.replace_subjects(racks)
        self._InstrumentFinderComponent__on_devices_changed.replace_subjects(chains)
        self._InstrumentFinderComponent__on_slicing_changed.replace_subjects(simplers)

    def _update_instruments(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        track = self._target_track.target_track
        do_notify = False
        drum_group = find_drum_group_device(track)
        if liveobj_changed(drum_group, self.drum_group):
            self.drum_group = drum_group
            do_notify = True
        sliced_simpler = find_sliced_simpler(track)
        if liveobj_changed(sliced_simpler, self.sliced_simpler):
            self.sliced_simpler = sliced_simpler
            do_notify = True
        any_instrument = list(find_instrument_devices(track))
        any_instrument = any_instrument[0] if any_instrument else None
        if liveobj_changed(any_instrument, self.any_instrument):
            self.any_instrument = any_instrument
            do_notify = True
        if do_notify:
            self.notify_instrument()

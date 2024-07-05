# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/session_navigation.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 7277 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ...base import clamp, depends, listens
from .. import Component
from . import Scrollable, ScrollComponent

class SessionRingScroller(Scrollable):
    """
    Documentation for SessionRingScroller.
    """
    """
    Documentation for SessionRingScroller.
    """

    def __init__(self, session_ring, respect_borders, snap_track_offset=False, scroll_scenes=False, page_size=1, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self.session_ring = session_ring
        self.respect_borders = respect_borders
        self.snap_track_offset = snap_track_offset
        self.page_size = page_size
        can_scroll = self._can_scroll_scenes if scroll_scenes else self._can_scroll_tracks
        self.can_scroll_up = partial(can_scroll, -1)
        self.can_scroll_down = partial(can_scroll, 1)
        self._do_scroll = self._scroll_scenes if scroll_scenes else self._scroll_tracks

    def scroll_up(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.can_scroll_up():
            self._do_scroll(-self.page_size)

    def scroll_down(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.can_scroll_down():
            self._do_scroll(self.page_size)

    def _max_track_offset(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.respect_borders:
            return len(self.session_ring.tracks_to_use()) - self.session_ring.num_tracks
        return len(self.session_ring.tracks_to_use()) - 1

    def _max_scene_offset(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.respect_borders:
            return len(self.session_ring.scenes_to_use()) - self.session_ring.num_scenes
        return len(self.session_ring.scenes_to_use()) - 1

    def _can_scroll_tracks(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        offset = self.session_ring.track_offset
        if self.snap_track_offset:
            if delta > 0:
                return offset < len(self.session_ring.tracks_to_use()) - self.page_size
        return delta < 0 < offset or offset + delta in range(self._max_track_offset() + 1)

    def _can_scroll_scenes(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        offset = self.session_ring.scene_offset
        return delta < 0 < offset or offset + delta in range(self._max_scene_offset() + 1)

    def _scroll_tracks(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        new_offset = self.session_ring.track_offset + delta
        self.session_ring.set_offsets(clamp(new_offset, 0, self._max_track_offset()), self.session_ring.scene_offset)

    def _scroll_scenes(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        new_offset = self.session_ring.scene_offset + delta
        self.session_ring.set_offsets(self.session_ring.track_offset, clamp(new_offset, 0, self._max_scene_offset()))


class SessionNavigationComponent(Component):
    """
    Documentation for SessionNavigationComponent.
    """
    """
    Documentation for SessionNavigationComponent.
    """

    @depends(session_ring=None)
    def __init__(self, name='Session_Navigation', session_ring=None, respect_borders=False, snap_track_offset=False, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)

        def scroller_factory(**k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            component = ScrollComponent(SessionRingScroller(session_ring, respect_borders, **k),
              parent=self,
              scroll_skin_name="Session.Navigation")
            return component

        self._vertical_banking = scroller_factory(scroll_scenes=True)
        self._horizontal_banking = scroller_factory()
        self._vertical_paging = scroller_factory(scroll_scenes=True,
          page_size=(session_ring.num_scenes))
        self._horizontal_paging = scroller_factory(page_size=(session_ring.num_tracks),
          snap_track_offset=snap_track_offset)
        self.register_slot(self.song, self._update_vertical, "scenes")
        self.register_slot(session_ring, self._update_horizontal, "tracks")
        self._SessionNavigationComponent__on_offset_changed.subject = session_ring

    def set_up_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._vertical_banking.set_scroll_up_button(button)

    def set_down_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._vertical_banking.set_scroll_down_button(button)

    def set_left_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._horizontal_banking.set_scroll_up_button(button)

    def set_right_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._horizontal_banking.set_scroll_down_button(button)

    def set_page_up_button(self, page_up_button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._vertical_paging.set_scroll_up_button(page_up_button)

    def set_page_down_button(self, page_down_button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._vertical_paging.set_scroll_down_button(page_down_button)

    def set_page_left_button(self, page_left_button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._horizontal_paging.set_scroll_up_button(page_left_button)

    def set_page_right_button(self, page_right_button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._horizontal_paging.set_scroll_down_button(page_right_button)

    def set_vertical_encoder(self, control):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._vertical_banking.set_scroll_encoder(control)

    def set_horizontal_encoder(self, control):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._horizontal_banking.set_scroll_encoder(control)

    def _update_vertical(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.is_enabled():
            self._vertical_banking.update()
            self._vertical_paging.update()

    def _update_horizontal(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.is_enabled():
            self._horizontal_banking.update()
            self._horizontal_paging.update()

    @listens("offset")
    def __on_offset_changed(self, *_):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._update_vertical()
        self._update_horizontal()

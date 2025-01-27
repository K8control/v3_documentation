# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/view_control.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 7308 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from typing import cast
from ...base import EventObject, ObservablePropertyAlias, clamp, depends
from ...live import all_visible_tracks, scene_index, track_index
from .. import Component
from ..display import Renderable
from . import Scrollable, ScrollComponent

class NotifyingViewScroller(Scrollable, EventObject):
    """
    Documentation for NotifyingViewScroller.
    """
    """
    Documentation for NotifyingViewScroller.
    """
    __events__ = ('scrolled', )

    def __init__(self, song, scroll_scenes=False, page_size=1, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self.song = song
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

    @staticmethod
    def _can_scroll_tracks(delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        tracks = all_visible_tracks()
        return track_index(track_list=tracks) + delta in range(len(tracks))

    def _can_scroll_scenes(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return scene_index() + delta in range(len(self.song.scenes))

    def _scroll_tracks(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        tracks = all_visible_tracks()
        new_index = track_index(track_list=tracks) + delta
        self.song.view.selected_track = tracks[clamp(new_index, 0, len(tracks) - 1)]
        self.notify_scrolled()

    def _scroll_scenes(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        scenes = list(self.song.scenes)
        new_index = scene_index() + delta
        self.song.view.selected_scene = scenes[clamp(new_index, 0, len(scenes) - 1)]
        self.notify_scrolled()


class ViewControlComponent(Component, Renderable):
    """
    Documentation for ViewControlComponent.
    """
    """
    Documentation for ViewControlComponent.
    """
    __events__ = ('track_selection_scrolled', 'scene_selection_scrolled')

    @depends(session_ring=None)
    def __init__(self, name='View_Control', session_ring=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._session_ring = session_ring

        def scroller_factory(scroll_scenes=False, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            scroller_type = "Scene" if scroll_scenes else "Track"
            scroller = NotifyingViewScroller(self.song, scroll_scenes=scroll_scenes, **k)
            self.register_disconnectable(ObservablePropertyAlias(self,
              property_host=scroller,
              property_name="scrolled",
              alias_name=("{}_selection_scrolled".format(scroller_type.lower()))))
            component = ScrollComponent(scroller,
              parent=self,
              scroll_skin_name=("ViewControl.{}".format(scroller_type)))
            return component

        self._scroll_tracks = scroller_factory()
        self._page_tracks = scroller_factory(page_size=(self._session_ring.num_tracks))
        self._scroll_scenes = scroller_factory(scroll_scenes=True)
        self._page_scenes = scroller_factory(scroll_scenes=True,
          page_size=(self._session_ring.num_scenes))
        song = self.song
        view = song.view
        self.register_slot(self._session_ring, self._update_track_scrollers, "tracks")
        self.register_slot(song, self._update_track_scrollers, "visible_tracks")
        self.register_slot(song, self._update_track_scrollers, "return_tracks")
        self.register_slot(view, self._update_track_scrollers, "selected_track")
        self.register_slot(song, self._update_scene_scrollers, "scenes")
        self.register_slot(view, self._update_scene_scrollers, "selected_scene")

        def notify_tracks_scrolled():
        """
        Documentation for .
        """
        """
        Documentation for .
        """
            self.notify(self.notifications.Track.select, cast(str, self.song.view.selected_track.name))

        self.register_slot(self, notify_tracks_scrolled, "track_selection_scrolled")

    def set_next_track_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_tracks.set_scroll_down_button(button)

    def set_prev_track_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_tracks.set_scroll_up_button(button)

    def set_next_track_page_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_tracks.set_scroll_down_button(button)

    def set_prev_track_page_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_tracks.set_scroll_up_button(button)

    def set_track_encoder(self, control):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_tracks.set_scroll_encoder(control)

    def set_track_page_encoder(self, control):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_tracks.set_scroll_encoder(control)

    def set_next_scene_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_scenes.set_scroll_down_button(button)

    def set_prev_scene_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_scenes.set_scroll_up_button(button)

    def set_next_scene_page_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_scenes.set_scroll_down_button(button)

    def set_prev_scene_page_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_scenes.set_scroll_up_button(button)

    def set_scene_encoder(self, control):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_scenes.set_scroll_encoder(control)

    def set_scene_page_encoder(self, control):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_scenes.set_scroll_encoder(control)

    def _update_track_scrollers(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_tracks.update()
        self._page_tracks.update()

    def _update_scene_scrollers(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_scenes.update()
        self._page_scenes.update()

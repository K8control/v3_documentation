# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/page.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 4703 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import EventObject, clamp, listens
from .. import Component
from .scroll import Scrollable, ScrollComponent

class Pageable(EventObject):
    """
    Documentation for Pageable.
    """
    """
    Documentation for Pageable.
    """
    __events__ = ('position', )
    position_count = NotImplemented
    position = NotImplemented
    page_offset = NotImplemented
    page_length = NotImplemented


class PageComponent(Component, Scrollable):
    """
    Documentation for PageComponent.
    """
    """
    Documentation for PageComponent.
    """

    def __init__(self, pageable=None, scroll_skin_name=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._pageable = pageable or self
        self._position_scroll = ScrollComponent(self,
          parent=self, scroll_skin_name=scroll_skin_name)
        self._page_scroll = ScrollComponent(parent=self,
          scroll_skin_name=scroll_skin_name)
        self._page_scroll.can_scroll_up = self.can_scroll_page_up
        self._page_scroll.can_scroll_down = self.can_scroll_page_down
        self._page_scroll.scroll_down = self.scroll_page_down
        self._page_scroll.scroll_up = self.scroll_page_up
        self._PageComponent__on_position_changed.subject = self._pageable

    def set_scroll_up_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._position_scroll.set_scroll_up_button(button)

    def set_scroll_down_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._position_scroll.set_scroll_down_button(button)

    def set_scroll_encoder(self, encoder):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._position_scroll.set_scroll_encoder(encoder)

    def set_scroll_page_up_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_scroll.set_scroll_up_button(button)

    def set_scroll_page_down_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_scroll.set_scroll_down_button(button)

    def set_scroll_page_encoder(self, encoder):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._page_scroll.set_scroll_encoder(encoder)

    def scroll_page_up(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_page(1)

    def scroll_page_down(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_page(-1)

    def scroll_up(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_position(1)

    def scroll_down(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._scroll_position(-1)

    def can_scroll_page_up(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        model = self._pageable
        return model.position < model.position_count - model.page_length

    def can_scroll_page_down(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._pageable.position > 0

    def can_scroll_up(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self.can_scroll_page_up()

    def can_scroll_down(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self.can_scroll_page_down()

    def _scroll_position(self, delta):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.is_enabled():
            model = self._pageable
            model.position = clamp(model.position + delta, 0, model.position_count - model.page_length)

    def _scroll_page(self, sign):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.is_enabled():
            model = self._pageable
            remainder = (model.position - model.page_offset) % model.page_length
            if sign > 0:
                delta = model.page_length - remainder
            else:
                if remainder == 0:
                    delta = -model.page_length
                else:
                    delta = -remainder
            self._scroll_position(delta)

    def update(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().update()
        self._position_scroll.update()
        self._page_scroll.update()

    @listens("position")
    def __on_position_changed(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._position_scroll.update()
        self._page_scroll.update()

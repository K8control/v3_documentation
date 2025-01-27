# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/clipboard.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 3070 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import listenable_property
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.control_surface.display import Renderable

class ClipboardComponent(Component, Renderable):
    """
    Documentation for ClipboardComponent.
    """
    """
    Documentation for ClipboardComponent.
    """
    copy_button = ButtonControl(color="Clipboard.Empty", on_color="Clipboard.Filled")
    has_content = listenable_property.managed(False)

    def __init__(self, name='Clipboard', *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._source_obj = None
        self._did_paste = False
        self._pending_clear = False

    def set_copy_button(self, button):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.clear()
        self.copy_button.set_control_element(button)

    def copy_or_paste(self, obj):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self.has_content:
            if self._is_source_valid():
                self._did_paste = self._do_paste(obj)
                if self._did_paste:
                    if not self.copy_button.is_pressed:
                        self.clear()
                    else:
                        self.clear(notify=True)
            else:
                pass
        else:
            self._source_obj = self._do_copy(obj)
            self.update()

    def clear(self, notify=False):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._source_obj = None
        self._pending_clear = False
        self.update()
        if notify:
            self.notify(self.notifications.Clipboard.clear)

    @copy_button.pressed
    def copy_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._pending_clear = self.has_content

    @copy_button.released
    def copy_button(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if self._did_paste or self._pending_clear:
            self.clear(notify=True)

    def update(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().update()
        self._did_paste = False
        self.has_content = self._source_obj is not None
        self.copy_button.is_on = self.has_content

    def _do_copy(self, obj):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._source_obj = obj
        return self._source_obj

    def _do_paste(self, obj):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._did_paste = obj is not None
        return self._did_paste

    def _is_source_valid(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._source_obj is not None

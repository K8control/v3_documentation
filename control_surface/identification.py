# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/identification.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 9099 bytes
from __future__ import absolute_import, print_function, unicode_literals
import logging
from abc import ABC, abstractmethod
from ..base import depends, listenable_property, nop, task
from . import MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE, Component, InputControlElement, midi
from .controls import InputControl
from .display import Renderable
from .elements import SysexElement
logger = logging.getLogger(__name__)
NON_REALTIME_HEADER = (
 midi.SYSEX_START, midi.SYSEX_NON_REALTIME)
STANDARD_RESPONSE_BYTES = (midi.SYSEX_GENERAL_INFO, midi.SYSEX_IDENTITY_RESPONSE_ID)
PRODUCT_ID_BYTES_START_INDEX = 3

def status_byte_to_msg_type(status_byte):
        """
        Documentation for status_byte_to_msg_type.
        """
        """
        Documentation for status_byte_to_msg_type.
        """
    status_byte = 240 & status_byte
    msg_type = MIDI_CC_TYPE
    if status_byte == midi.NOTE_ON_STATUS:
        msg_type = MIDI_NOTE_TYPE
    else:
        if status_byte == midi.PB_STATUS:
            msg_type = MIDI_PB_TYPE
    return msg_type


def create_responder(identity_response_id_bytes, custom_identity_response):
        """
        Documentation for create_responder.
        """
        """
        Documentation for create_responder.
        """
    if identity_response_id_bytes is not None:
        return StandardResponder(identity_response_id_bytes)
    if custom_identity_response[0] == midi.SYSEX_START:
        return CustomSysexResponder(custom_identity_response)
    return PlainMidiResponder(custom_identity_response)


class Responder(ABC):
    """
    Documentation for Responder.
    """
    """
    Documentation for Responder.
    """

    def __init__(self, response_bytes, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(*a, **k)
        self._response_bytes = tuple(response_bytes)

    @abstractmethod
    def create_response_element(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        pass

    @abstractmethod
    def is_valid_response(self, response_bytes):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        pass


class CustomSysexResponder(Responder):
    """
    Documentation for CustomSysexResponder.
    """
    """
    Documentation for CustomSysexResponder.
    """

    def create_response_element(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return SysexElement(sysex_identifier=(self._response_bytes))

    def is_valid_response(self, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return True


class PlainMidiResponder(Responder):
    """
    Documentation for PlainMidiResponder.
    """
    """
    Documentation for PlainMidiResponder.
    """

    def __init__(self, response_bytes, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(response_bytes, *a, **k)
        self._expected_response_value_bytes = midi.extract_value(response_bytes) if len(response_bytes) == 3 else None

    def create_response_element(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        first_byte = self._response_bytes[0]
        element = InputControlElement(msg_type=(status_byte_to_msg_type(first_byte)),
          channel=(15 & first_byte),
          identifier=(self._response_bytes[1]))
        element.reset = nop
        return element

    def is_valid_response(self, response_bytes):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return self._expected_response_value_bytes is None or self._expected_response_value_bytes == response_bytes


class StandardResponder(Responder):
    """
    Documentation for StandardResponder.
    """
    """
    Documentation for StandardResponder.
    """

    def create_response_element(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return SysexElement(sysex_identifier=NON_REALTIME_HEADER)

    def is_valid_response(self, response_bytes):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        if response_bytes[1[:PRODUCT_ID_BYTES_START_INDEX]] == STANDARD_RESPONSE_BYTES:
            product_id_bytes = self._extract_product_id_bytes(response_bytes)
            if product_id_bytes != self._response_bytes:
                raise IdentityResponseError(expected_bytes=(self._response_bytes),
                  actual_bytes=product_id_bytes)
            return True
        return False

    def _extract_product_id_bytes(self, midi_bytes):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        return midi_bytes[PRODUCT_ID_BYTES_START_INDEX[:PRODUCT_ID_BYTES_START_INDEX + len(self._response_bytes)]]


class IdentityResponseError(Exception):
    """
    Documentation for IdentityResponseError.
    """
    """
    Documentation for IdentityResponseError.
    """

    def __init__(self, expected_bytes=None, actual_bytes=None):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        super().__init__("Hardware controller responded with wrong identity bytes: ({} != {}).".format(expected_bytes, actual_bytes))


class IdentificationComponent(Component, Renderable):
    """
    Documentation for IdentificationComponent.
    """
    """
    Documentation for IdentificationComponent.
    """
    identity_response_control = InputControl()
    is_identified = listenable_property.managed(False)
    received_response_bytes = listenable_property.managed(None)

    @depends(send_midi=None)
    def __init__(self, name="Identification", identity_request=midi.SYSEX_IDENTITY_REQUEST_MESSAGE, identity_request_delay=0.0, identity_response_id_bytes=None, custom_identity_response=None, send_midi=None, *a, **k):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        (super().__init__)(a, name=name, **k)
        self._send_midi = send_midi
        self._identity_request = identity_request
        self._responder = create_responder(identity_response_id_bytes, custom_identity_response)
        response_element = self._responder.create_response_element()
        response_element.name = "identity_control"
        response_element.is_private = True
        self.identity_response_control.set_control_element(response_element)
        self._request_task = self._tasks.add(task.sequence(task.run(self._send_identity_request), task.wait(identity_request_delay), task.run(self._send_identity_request)))
        self._request_task.kill()

    @identity_response_control.value
    def identity_response_control(self, response_bytes, _):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        try:
            if self._responder.is_valid_response(response_bytes):
                self._request_task.kill()
                self.identity_response_control.enabled = False
                self.received_response_bytes = response_bytes
                self.is_identified = True
                self.notify(self.notifications.identify)
        except IdentityResponseError as e:
            try:
                logger.error(e)
            finally:
                e = None
                del e

    def request_identity(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self._request_task.restart()
        self.received_response_bytes = None
        self.is_identified = False

    def _send_identity_request(self):
        """
        Documentation for .
        """
        """
        Documentation for .
        """
        self.identity_response_control.enabled = True
        self._send_midi(self._identity_request)

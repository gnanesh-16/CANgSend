# __init__.py

"""
CAN Message Sender Module

This module allows users to send CAN messages for acceleration control. It provides functions to:
- Send a single CAN message with specific data.
- Continuously send CAN messages with incremental changes.

Functions:
- send_acceleration_message(bus, arbitration_id, data): Sends a single CAN message.
- continuous_acceleration_send(channel, interface, bitrate, arbitration_id, data_accel, seventh_byte): Continuously sends CAN messages with updated data.
- main(): Parses command-line arguments and starts sending CAN messages based on user input.

Example usage:
    from can_message_sender import send_acceleration_message, continuous_acceleration_send, main

    # Send a single CAN message
    bus = can.interface.Bus(channel='can0', interface='socketcan', bitrate=500000)
    send_acceleration_message(bus, arbitration_id=0x123, data=[0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])

    # Continuously send CAN messages
    continuous_acceleration_send(
        channel='can0',
        interface='socketcan',
        bitrate=500000,
        arbitration_id=0x123,
        data_accel=[0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x00, 0x00],
        seventh_byte=0x00
    )
"""

from .CANgSend import send_acceleration_message, continuous_acceleration_send, main
from.version import __version__

__all__ = [
    "send_acceleration_message",
    "continuous_acceleration_send",
    "main"
]

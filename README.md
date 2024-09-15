# CANgSend

[![Version](https://img.shields.io/badge/version-0.1.1-blue)](https://github.com/gnanesh-16/CANgSend)

**CANgSend** is a Python package designed for sending and managing CAN (Controller Area Network) messages, specifically tailored for applications like vehicle acceleration control. This package allows for the easy creation and transmission of CAN messages using both the PCAN and SocketCAN interfaces, making it ideal for automotive and industrial systems where CAN communication is essential.

## Features

- **CAN Communication Support**: Send CAN frames using PCAN and SocketCAN interfaces.
- **Flexible API**: Easily configure CAN channels, bitrate, and message data.
- **Vehicle Control**: Specifically designed for handling vehicle acceleration control through CAN messages.
- **Checksum Calculation**: Automatically handles XOR checksum for message integrity.
- **Customizable**: User-specified parameters for message creation, including channels, interfaces, and byte values.

## Installation

You can install CANgSend via `pip`:

```bash
pip install CANgSend

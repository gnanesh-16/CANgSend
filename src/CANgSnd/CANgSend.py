import time
import can
import argparse

def send_acceleration_message(bus, arbitration_id, data):
    message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
    try:
        bus.send(message)
        print(f"Acceleration Message sent: ID=0x{arbitration_id:X}, Data: {' '.join(f'{byte:02X}' for byte in data)}")
    except can.CanError as e:
        print(f"Message not sent: {e}")

def continuous_acceleration_send(channel, interface, bitrate, arbitration_id, data_accel, seventh_byte):
    try:
        bus = can.interface.Bus(channel=channel, interface=interface, bitrate=bitrate)
    except can.CanError as e:
        print(f"Failed to initialize CAN bus: {e}")
        return

    try:
        while True:
            # Calculate checksum for Byte 7
            data_accel[7] = data_accel[0] ^ data_accel[1] ^ data_accel[2] ^ data_accel[3] ^ data_accel[4] ^ data_accel[5] ^ data_accel[6]
            
            # Send the CAN message
            send_acceleration_message(bus, arbitration_id, data_accel)

            # Increment the seventh byte from 0x00 to 0x0F
            seventh_byte = (seventh_byte + 1) % 0x10
            data_accel[6] = seventh_byte
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Exiting Acceleration Control...")
    finally:
        bus.shutdown()

def main():
    parser = argparse.ArgumentParser(description="Send CAN messages for acceleration control.")
    parser.add_argument('--channel', type=str, required=True, help='CAN bus channel (e.g., PCAN_USBBUS2)')
    parser.add_argument('--interface', type=str, required=True, help='CAN interface type (e.g., pcan)')
    parser.add_argument('--bitrate', type=int, required=True, help='CAN bitrate in bps (e.g., 500000)')
    parser.add_argument('--arbitration_id', type=lambda x: int(x, 0), required=True, help='CAN message arbitration ID (hexadecimal)')
    parser.add_argument('--data', type=lambda x: [int(b, 0) for b in x.split(',')], required=True, help='CAN message data bytes (comma-separated hexadecimal)')
    parser.add_argument('--seventh_byte', type=lambda x: int(x, 0), required=True, help='Initial value for the seventh byte (hexadecimal)')

    args = parser.parse_args()

    continuous_acceleration_send(
        channel=args.channel,
        interface=args.interface,
        bitrate=args.bitrate,
        arbitration_id=args.arbitration_id,
        data_accel=args.data,
        seventh_byte=args.seventh_byte
    )

if __name__ == "__main__":
    main()

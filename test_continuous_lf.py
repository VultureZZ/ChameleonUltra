#!/usr/bin/env python3
"""
Test script for continuous LF card reading feature
"""

import sys
import time
from chameleon_com import ChameleonCom
from chameleon_enum import ButtonPressFunction, ButtonType

def test_continuous_lf_read():
    """Test the continuous LF reading feature"""

    print("Testing Continuous LF Card Reading Feature")
    print("=" * 50)

    try:
        # Connect to device
        print("Connecting to ChameleonUltra...")
        device = ChameleonCom()
        device.open()

        # Check if device supports the feature
        print("Checking device capabilities...")
        resp = device.send_cmd_sync(0x1030)  # GET_DEVICE_CAPABILITIES
        if resp.status != 0x68:  # SUCCESS
            print("Failed to get device capabilities")
            return False

        # Set button A to continuous LF reading
        print("Setting button A to continuous LF reading...")
        data = bytes([ButtonType.A, ButtonPressFunction.CONTINUOUS_LF_READ])
        resp = device.send_cmd_sync(0x1027, data)  # SET_BUTTON_PRESS_CONFIG
        if resp.status != 0x68:  # SUCCESS
            print("Failed to set button function")
            return False

        # Save settings
        print("Saving settings...")
        resp = device.send_cmd_sync(0x1013)  # SAVE_SETTINGS
        if resp.status != 0x68:  # SUCCESS
            print("Failed to save settings")
            return False

        print("✓ Settings saved successfully")
        print("\nInstructions:")
        print("1. Press button A on the device")
        print("2. Watch for LED sequence: RED → GREEN → GREEN (steady)")
        print("3. Place LF cards near the device")
        print("4. Check logs for detected UIDs")
        print("5. Power cycle to stop continuous reading")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        if 'device' in locals():
            device.close()

if __name__ == "__main__":
    success = test_continuous_lf_read()
    sys.exit(0 if success else 1)

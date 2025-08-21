# Continuous LF Card UUID Reading Feature

## Overview

This feature adds a new button function that allows continuous reading of LF (Low Frequency) card UUIDs and automatically saves them to slot 7. When activated, the device will:

1. Turn the LED RED for 500ms
2. Turn the LED GREEN for 500ms
3. Start continuously scanning for LF cards
4. Automatically save detected UIDs to slot 7
5. Log detected card UUIDs to the console
6. Flash the LED when a new card is detected and saved
7. Stop reading when any button is pressed

## Hardware Requirements

- ChameleonUltra device (this feature is only available on Ultra models)
- LF reader hardware must be properly connected

## Usage

### Setting up the Button Function

1. Connect to the device via USB or BLE
2. Use the CLI to set the button function:

```bash
# Set button A to continuous LF reading
hw settings btnpress --a --function CONTINUOUS_LF_READ

# Set button B to continuous LF reading
hw settings btnpress --b --function CONTINUOUS_LF_READ

# Save settings to flash
hw settings save
```

### Using the Feature

1. Press the configured button (A or B)
2. Watch the LED sequence: RED → GREEN → GREEN (steady)
3. The device will start continuously scanning for LF cards
4. When a card is detected:
   - The LED will flash BLUE briefly
   - The UID will be automatically saved to slot 7
   - Card UUIDs will be logged to the console/logs
5. Press any button to stop the scanning
6. When stopped, the LED will flash CYAN then GREEN to indicate completion

### Accessing Saved UIDs

The detected UIDs are automatically saved to slot 7 and can be accessed using:

```bash
# Switch to slot 7
hw slot --set 7

# Get the UID from slot 7
hw lf em410x --get
```

## LED Indicators

- **RED (500ms)**: Initializing
- **GREEN (500ms)**: Ready to start
- **GREEN (steady)**: Scanning for cards
- **BLUE (200ms)**: Card detected and saved
- **YELLOW (50ms)**: Heartbeat (every 100 scans)
- **CYAN (300ms)**: Stopping (when button pressed)
- **GREEN (300ms)**: Complete

## Supported Card Types

Currently supports:
- EM410X cards (125kHz)

## Technical Details

- Scanning interval: 100ms between reads
- Heartbeat indicator: Every 100 scans
- UID format: 8-byte hexadecimal
- Logging: All detected UIDs are logged via NRF_LOG

## Limitations

- Only works on ChameleonUltra devices
- Requires LF reader hardware
- Only detects EM410X cards currently
- Automatically configures slot 7 for EM410X emulation

## Troubleshooting

1. **No cards detected**: Ensure LF reader is properly connected and powered
2. **LED not responding**: Check button configuration and save settings
3. **UID not saved**: Check if slot 7 is properly configured for EM410X
4. **No logs**: Check USB/BLE connection and log level settings
5. **Button not stopping**: Ensure button is properly configured and not disabled

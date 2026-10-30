# Atomic Time

A Python-based TCP client that retrieves the current time from NIST (National Institute of Standards and Technology) and compares it with the local system clock.

## Overview

The program connects to the NIST Time Server using TCP on port `37`, receives a 4-byte timestamp, and converts it into an integer representing the number of seconds elapsed since January 1, 1900, 00:00 UTC.

It then calculates the system time using Python's `time` module and compares both timestamps to determine the difference in seconds.

## Features

- Connects to the NIST Time Server (`time.nist.gov`) using TCP sockets.
- Receives and processes binary timestamp data.
- Decodes Big-Endian integers using `int.from_bytes()`.
- Converts Unix time (1970 epoch) into NIST's 1900 epoch.
- Calculates the difference between NIST time and system time.
- Handles socket connection timeouts.

## Implementation

### NIST Time

- Server: `time.nist.gov`
- Port: `37`
- Protocol: TCP
- Data format: 4-byte Big-Endian unsigned integer.
- Epoch: January 1, 1900, 00:00 UTC.

### System Time

Python's `time.time()` returns the number of seconds since January 1, 1970, 00:00 UTC.

To convert it into the NIST epoch, the program adds `2,208,988,800` seconds.

### Time Difference

The program calculates the absolute difference between the two timestamps:

`abs(NIST time - System time)`

## Requirements

- Python 3
- Internet connection

## Usage

Run the program:

```bash
python timeclient.py
```

## Sample Output

```bash
Connecting to time.nist.gov on port 37...
Time (in seconds) received from NIST: 4002349369
Time (in seconds) from the system: 4002349370
Error between the two (in seconds): 1
```

## Concepts Learned

- TCP socket communication
- Receiving binary data over a network
- Big-Endian byte ordering
- Bytes-to-integer conversion
- Unix epoch and alternative time epochs
- Working with external time servers
- Measuring differences between two clocks

## Important Note

NIST requests that clients do not query its Time Server more than once every 4 seconds. Avoid making frequent requests while testing.

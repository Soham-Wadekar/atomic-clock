import time
import socket


def get_time_from_nist(domain="time.nist.gov", port=37):
    with socket.socket() as s:
        s.settimeout(10)
        print(f"Connecting to {domain} on port {port}...")
        s.connect((domain, port))

        response = bytearray()
        while True:
            try:
                data = s.recv(4096)
            except socket.timeout:
                print("Connection timed out.")
                return

            if not data:
                break

            response.extend(data)

        seconds_from_nist = int.from_bytes(response, "big")
        return seconds_from_nist


def get_system_time():
    seconds_delta = 2_208_988_800
    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta
    return seconds_since_1900_epoch


if __name__ == "__main__":
    nist_time = get_time_from_nist()
    sys_time = get_system_time()
    print(f"Time (in seconds) received from NIST: {nist_time}")
    print(f"Time (in seconds) from the system: {sys_time}")

    print(f"Error between the two (in seconds): {abs(nist_time - sys_time)}")

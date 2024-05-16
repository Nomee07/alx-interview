#!/usr/bin/python3
import sys
import signal

# Global variables to store the total file size and the count of each status code
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
line_counter = 0

def print_stats():
    """Print the accumulated statistics."""
    global total_size, status_count
    print(f"File size: {total_size}")
    for status in sorted(status_count.keys()):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")

def signal_handler(sig, frame):
    """Signal handler to print stats on keyboard interruption."""
    print_stats()
    sys.exit(0)

# Attach the signal handler for keyboard interruption (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        try:
            ip = parts[0]
            date = parts[3] + " " + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[8])
            file_size = int(parts[9])
        except (IndexError, ValueError):
            continue
        
        # Only process lines matching the exact format
        if request != '"GET /projects/260 HTTP/1.1"':
            continue
        
        # Accumulate the file size
        total_size += file_size
        
        # Increment the count for the status code if it's valid
        if status_code in valid_status_codes:
            status_count[status_code] += 1

        # Increment the line counter and print stats every 10 lines
        line_counter += 1
        if line_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats when a keyboard interruption occurs
    print_stats()
    sys.exit(0)

# Ensure to print stats if the input ends without interruption
print_stats()

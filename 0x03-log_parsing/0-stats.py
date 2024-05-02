#!/usr/bin/python3
import sys

total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                     404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) != 7:
        continue
    try:
        file_size = int(parts[6])
        status_code = int(parts[5])
        if status_code in status_code_count:
            total_size += file_size
            status_code_count[status_code] += 1
    except ValueError:
        continue

    if line_count % 10 == 0:
        print(f"File size: {total_size}")
        for code in sorted(status_code_count.keys()):
            if status_code_count[code] > 0:
                print(f"{code}: {status_code_count[code]}")

try:
    while True:
        pass
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

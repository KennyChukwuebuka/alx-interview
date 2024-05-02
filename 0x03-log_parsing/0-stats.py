#!/usr/bin/python3
import sys
import re

total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    line_count += 1
    match = re.match(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$',
        line)
    if match:
        ip, date, status_code, file_size = match.groups()
        total_size += int(file_size)
        if int(status_code) in status_code_count:
            status_code_count[int(status_code)] += 1
    if line_count == 10 or (line_count > 10 and line_count % 10 == 0):
        print(f"File size: {total_size}")
        for code in sorted(status_code_count):
            if status_code_count[code] > 0:
                print(f"{code}: {status_code_count[code]}")
    if line_count > 10 and line_count % 10 == 0:
        try:
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print(f"File size: {total_size}")
            for code in sorted(status_code_count):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")
            break

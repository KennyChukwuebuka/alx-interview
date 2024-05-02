#!/usr/bin/python3
"""function that parses apache log files
"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """function that prints statistics
    """
    print("File size:", total_size)
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")


def parse_line(line):
    """function that parses line"""
    parts = line.split()
    if len(parts) != 7:
        return None
    ip, date, request, status_code, size = parts[0], parts[3][1:],
    parts[5], parts[6], int(parts[8])
    if request != "GET /projects/260 HTTP/1.1":
        return None
    return ip, status_code, size


def main():
    """main function
    """
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for i, line in enumerate(sys.stdin, 1):
            parsed_line = parse_line(line.strip())
            if parsed_line:
                ip, status_code, size = parsed_line
                total_size += size
                status_counts[status_code] += 1
            if i % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()

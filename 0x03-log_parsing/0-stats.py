#!/usr/bin/python3
"""Script that reads stdin"""

# Import necessary modules
import sys

def parseLogs():
    """
    Parses logs from standard input and calculates
    the file size and status codes.

    Args:
        None

    Returns:
        None
    """
    # Read from standard input
    stdin = sys.stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    # List of HTTP status codes to track
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        # Loop through each line in standard input
        for line in stdin:
            lineNumber += 1
            # Split the line into tokens
            line = line.split()
            try:
                # Extract file size from the last token of the line
                fileSize += int(line[-1])
                # Check if the second last token is a valid status code
                if line[-2] in codes:
                    try:
                        # Increment the count of the status code
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        # If status code doesn't exist, initialize it
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                # Ignore lines that cannot be processed due to missing or invalid data
                pass
            # If 10 lines have been processed, generate report and reset counter
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        # Generate report for the remaining lines
        report(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        # In case of KeyboardInterrupt, generate report and re-raise the exception
        report(fileSize, statusCodes)
        raise
    except BrokenPipeError:
        # Handle the BrokenPipeError explicitly
        pass


def report(fileSize, statusCodes):
    """
    Prints generated report to standard output

    Args:
        fileSize (int): total log size after every 10 successfully read lines
        statusCodes (dict): dictionary of status codes and counts
    """
    # Print total file size
    print("File size: {}".format(fileSize))
    # Print each status code and its count, sorted alphabetically by status code
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    try:
        # Call the main function to parse logs
        parseLogs()
    except BrokenPipeError:
        # Handle the BrokenPipeError at the top level
        pass

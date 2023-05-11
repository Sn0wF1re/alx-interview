#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metric
"""
import sys


total_size = 0
counter = 0
code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
try:
    for line in sys.stdin:
        data_list = line.split()
        if len(data_list) > 3:
            total_size += int(data_list[-1])
            status_code = data_list[-2]
            if status_code in code_count:
                code_count[status_code] += 1
            counter += 1

        if counter == 10:
            print("File size: {}".format(total_size))
            for k, v in sorted(code_count.items()):
                if v > 0:
                    print("{}: {}".format(k, v))
            counter = 0

except Exception:
    pass

finally:
    print("File size: {}".format(total_size))
    for k, v in sorted(code_count.items()):
        if v > 0:
            print("{}: {}".format(k, v))

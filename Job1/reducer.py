#!/usr/bin/env python
import sys


# to filter and splits incoming lines form stdin
def splitter(data, separator='\t'):
    line_striped = data.strip()
    line_splited = line_striped.split(separator)
    return line_splited


# conversion and emitting ot stdout
def format_data(data, location, separator='\t'):
    map(str, data)
    for product_id in data:
        emit((product_id, location))


# emitting to stdout
def emit(data, separator='\t'):
    print data[0], separator, data[1]


def reducer():
    current_user_id = None
    current_location = None
    prev_user_id = None
    product_list = []
    for line in sys.stdin:
        current_user_id, product_id, location = splitter(line)
        if current_user_id != prev_user_id and len(product_list) == 0:
            prev_user_id = current_user_id
            if (product_id == '-'):
                current_location = location
            else:
                product_list.append(product_id)
        elif current_user_id != prev_user_id and len(product_list) != 0:
            format_data(product_list, current_location)
            prev_user_id = current_user_id
            del product_list[:]
            if (product_id != '-'):
                product_list.append(product_id)
            else:
                current_location = location
        else:
            if (product_id != '-'):
                product_list.append(product_id)
                prev_user_id = current_user_id


if __name__ == '__main__':
    reducer()

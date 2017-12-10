#!/usr/bin/env python

import sys


# filter and split incoming lines from stdin
def splitter(line, separator='\t'):
    line_striped = line.strip()
    line_splited = line_striped.split(separator)
    return line_splited


# to check if a given location is existing in the passed array or not
def location_exist(locations, location):
    if location in locations:
        return True
    else:
        return False


# print data to stdout
def emit(locations, prod_id):
    print '|     ', prod_id, '    |       ', len(locations), '         |'
    print '-----------------------------------'


# visualizing data
def emit_top_bar():
    print '-----------------------------------'
    print '| product_id  |  no. of locations |'
    print '-----------------------------------'


def reducer():
    locations = []
    current_location = None
    prev_location = None
    current_product_id = None
    prev_product_id = None
    emit_top_bar()
    for line in sys.stdin:
        current_product_id, current_location = splitter(line)
        if current_product_id != prev_product_id and len(locations) == 0:
            locations.append(current_location)
            prev_product_id = current_product_id
            prev_location = current_location
            continue
        elif current_product_id == prev_product_id and current_location == prev_location and len(locations) != 0:
            continue
        elif current_product_id == prev_product_id and current_location != prev_location and len(locations) != 0:
            if location_exist(locations, current_location):
                continue
            else:
                locations.append(current_location)
                prev_product_id = current_product_id
                prev_location = current_location

        elif current_product_id != prev_location and current_product_id != 'end':
            emit(locations, prev_product_id)
            prev_location = current_location
            prev_product_id = current_product_id


if __name__ == '__main__':
    reducer()

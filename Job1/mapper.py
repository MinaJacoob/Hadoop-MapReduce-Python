#!/usr/bin/env python
import sys


# filter and split incoming lines from stream
def splitter(line, separator=','):
    line_striped = line.strip()
    line_splited = line_striped.split(separator)
    return line_splited


# converting data to string before printing to stream
def emit(data, separator='\t'):
    output = data[0] + '\t' + data[1] + '\t' + data[2]
    print output


def mapper():
    for line in sys.stdin:
        line_content = splitter(line)
        if (len(line_content) == 4):  # i.e record is for user
            user_id, email, language, location = line_content
            emit([user_id, '-', location])
        else:
            trans_id, product_id, user_id, purchase_amount, product_desc = line_content
            emit([user_id, product_id, '-'])


if __name__ == '__main__':
    mapper()

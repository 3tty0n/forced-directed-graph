# coding:utf-8

import sys
from utils.util import create_json_from_file

args = sys.argv
argc = len(args)

def generate_json():
    create_json_from_file(args[1], int(args[2]))

generate_json()

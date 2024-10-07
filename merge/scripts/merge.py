#!/usr/bin/env python3
import argparse
from merge.modules.merge_func import merge


parser = argparse.ArgumentParser(
    description='Compares two configuration files and merger them.')
parser.add_argument(
    'first_file', type=str,
    help='Input first file for comparison')
parser.add_argument(
    'second_file', type=str,
    help='Input second file for comparison')
parser.add_argument(
    'output_file', type=str,
    help='Input second file for comparison')
args = parser.parse_args()


def main():
    merge(args.first_file, args.second_file, args.output_file)


if __name__ == '__main__':
    main()
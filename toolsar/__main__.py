#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------
# dependencies
# -------------------------------------------------------------------------------------------------
from argparse    import ArgumentParser
from check_uuids import main as check_uuids
from sar_viewer  import main as sar_view
from sar_parser  import main as sar_parse
from sar_filter  import main as sar_filter
# -------------------------------------------------------------------------------------------------
# parsers
# -------------------------------------------------------------------------------------------------
# head
# -----------------------------------------------------------------------------
head = ArgumentParser(prog='toolsar')
sub  = head.add_subparsers(title='sub-command')
# -----------------------------------------------------------------------------
# check uuid
# -----------------------------------------------------------------------------
parser = sub.add_parser('check-uuids')
# arguments
parser.add_argument('path', type=str, help='search path')
# function
parser.set_defaults(func=check_uuids)
# -----------------------------------------------------------------------------
# parse sar
# -----------------------------------------------------------------------------
parser = sub.add_parser('parse')
# arguments
parser.add_argument('path', type=str, help='search path')
# function
parser.set_defaults(func=sar_parse)
# -----------------------------------------------------------------------------
# filter sar
# -----------------------------------------------------------------------------
parser = sub.add_parser('filter')
# arguments
parser.add_argument(
	'path', type=str, help='search path')
parser.add_argument(
	'--target', type=str, help='target key', nargs='+', default='.*')
parser.add_argument(
	'--filter', type=str, help='filter key', nargs='+', default='')
# function
parser.set_defaults(func=sar_filter)
# -----------------------------------------------------------------------------
# view sar
# -----------------------------------------------------------------------------
parser = sub.add_parser('view')
# arguments
parser.add_argument(
	'path', type=str, help='search path')
parser.add_argument(
	'--target', type=str, help='target key', nargs='+', default='.*')
parser.add_argument(
	'--filter', type=str, help='filter key', nargs='+', default='')
# function
parser.set_defaults(func=sar_view)
# -------------------------------------------------------------------------------------------------
# execute
# -------------------------------------------------------------------------------------------------
from colorlog import basicConfig as config_logger
from logging  import INFO
from sys      import stdout
# logger configuration
config_logger(
	format = '%(log_color)s%(asctime)s %(levelname)-8s %(reset)s| %(message)s',
	stream = stdout,
	level  = INFO,
	datefmt='%H:%M:%S')
# call method
opt = head.parse_args()
try:
	opt.func(opt)
except:
	head.print_help()
# -------------------------------------------------------------------------------------------------
# end
# -------------------------------------------------------------------------------------------------
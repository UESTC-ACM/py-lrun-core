#! /usr/bin/env python2.7
#
# command line entrance for py-lrun-core.
#
import argparse
import util
import runner


parser = argparse.ArgumentParser(description='New judge core for CDOJ.')
parser.add_argument('-l', '--language', required = True, type = str, dest = 'language_token',
                    choices = util.judge_languages.keys(),
                    help='the language of source')
parser.add_argument('-w', '--work_dir', required = True, type = str, dest = 'work_dir',
                    help='the work path')
parser.add_argument('-d', '--data_dir', required = True, type = str, dest = 'data_dir',
                    help='the data path')
parser.add_argument('-s', '--source_file', required = True, type = str, dest = 'source_file',
                    help='the source file name, without extension')
parser.add_argument('-t', '--time_limit', required = True, type = int, dest = 'time_limit',
                    help='the time limit, formatted as millisecond')
parser.add_argument('-m', '--memory_limit', required = True, type = int, dest = 'memory_limit',
                    help='the memory limit, formatted as Kilobyte')
parser.add_argument('-f', '--test_file', required = True, type = str, dest = 'test_case',
                    help='the input and output file, without extension')
parser.add_argument('-o', '--output_limit', required = True, type = int, dest = 'output_limit',
                    help='the output limit, formatted as Kilobyte')
parser.add_argument('-c', '--compile', action = 'store_true', dest = 'compile',
                    help='needs compile the source code or not')

args = parser.parse_args()
print runner.Judge(work_dir = args.work_dir, \
                   data_dir = args.data_dir, \
                   language_token = args.language_token, \
                   source_file = args.source_file, \
                   time_limit = args.time_limit, \
                   memory_limit = args.memory_limit, \
                   test_case = args.test_case, \
                   output_limit = args.output_limit, \
                   compile = args.compile)


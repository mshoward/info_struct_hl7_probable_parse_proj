#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parser_utilities.py
#
#  Copyright 2017 mason <mason.howard.15@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

"""
Version 0.0.1.3
"""



class parser_utilities:
    """Helper class for parse_things_msh"""
    log_file_name = "parser_debug.log"
    exit_codes = {'io_error'}

    @staticmethod
    def graceful_exception_handler(accepted_exception):
        """
        Graceful handling of exceptions.
        """
        loggit(accepted_exception)
        printerr

    @staticmethod
    def loggit(*log_these):
        with open(log_file_name, 'a') as log_file:
            parser_utilities.printerr(datetime.datetime.now(), log_these, file=sys.stderr)
            print(datetime.datetime.now(), log_these, file=log_file)

    @staticmethod
    def insert_into_dicts(dict_one, dict_two, key, val):
        try:
            dict_one[key] = val
            dict_two[val] = key
        except Exception as insert_failure:


    @staticmethod
    def printerr(*e_objects, e_sep=' ', e_end='\n', e_file=sys.stderr,
                 e_flush=True):
        """
        Wrapper around print() to print to stderr by default.

        Formats with timestamps, resolves 'verbose' flag.
        """
        #global PARSED_GLOBALS
        if PARSED_GLOBALS['verbose']:
            print(datetime.datetime.now(), sep=e_sep, end=e_sep, file=e_file,
                  flush=e_flush)
            print(*e_objects, sep=e_sep, end=e_end, file=e_file, flush=e_flush)

    @staticmethod
    def curr_fname(whole_path=False):
        """
        Wrapper for __file__ if whole_path else os.path.basename(__file__)
        """
        return __file__ if whole_path else os.path.basename(__file__)

    @staticmethod
    def log_msg(*l_objects, l_sep=' ', l_end='\n', l_flush=True):
        #sol_util.notimp()
        """
        print() to the logfile, default debugging.log in the current working
        directory.
        """
        with open(sol_util.log_file_name, 'a') as logfile:
            print(datetime.datetime.now(), sep=l_sep, file=logfile,
                  flush=l_flush)
            print(*l_objects, sep=l_sep, end=l_end, file=logfile, flush=l_flush)

    @staticmethod
    def notimp(loggit=False):
        """
        Raises a NotImplemented exception.  Logs if loggit.
        """
        if loggit:
            sol_util.log_msg("todo logging caller")
        raise NotImplementedError()


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

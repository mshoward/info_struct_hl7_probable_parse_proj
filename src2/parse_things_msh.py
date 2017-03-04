#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parse_things_msh.py
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
Version:
    0.0.1
Description:
    parse_things_msh does things
"""

import datetime
import sys



class io_err(Exception):
    def __init__(self, caller='', message='Default message for io error.  \
                 Fill this out', prev=None


class parse_things_msh:
    """
    flexible parser thing
    """
    class utils:
        """Helper class for parse_things_msh"""
        log_file_name = "parser_debug.log"
        exit_codes = {'io_error'}
        @staticmethod
        def graceful_exception_handler(accepted_exception):
            """
            Graceful handling of exceptions.
            """
            loggit(accepted_exception)

        @staticmethod
        def loggit(*log_these):
            with open(log_file_name, 'a') as log_file:
                print(datetime.datetime.now(), log_these, file=sys.stderr)
                print(datetime.datetime.now(), log_these, file=log_file)

        @staticmethod
        def insert_into_dicts(dict_one, dict_two, key, val):


    name_to_single_char_delims = {}
    single_char_delims_to_name = {}

    name_to_multi_char_delims = {}
    multi_char_delims_to_name = {}

    name_to_key_words = {}
    key_words_to_name = {}

    name_to_data_type = {}
    data_type_to_name = {}


    @staticmethod
    def add_single_char_delim(name, delim):
        """
        Inserts name and delim into the dicts.
        """
        name_to_single_char_delims


        pass

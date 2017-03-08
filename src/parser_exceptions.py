#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parser_exceptions.py
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
Version 0.0.3.

Description
"""


class parser_exception(Exception):
    """
    Base handling funcs.

    todo.
    """


class io_err(parser_exception):
    """IO error specific to the module."""

    def __init__(self, p_caller='', p_message='Default message for error.  \
                 Fill this out', p_prev=None):
        """Standard exception chaining."""
        self.message = p_message
        self.caller = p_caller
        self.prev = p_prev


class dict_insertion_err(parser_exception):
    """Tried to insert things into the dictionary, but was not able to."""

    import parser_utilities

    def __init__(self, p_caller='', p_message='Default message for error.  \
                 Fill this out', p_prev=None, **failed_mappings):
        """Todo doc."""
        self.message = p_message
        self.caller = p_caller
        self.prev = p_prev
        parser_utilities.loggit(self.message)
        for key, val in failed_mappings:
            parser_utilities.loggit("Failure to insert key: '", key,
                                    "' and value: '", val,
                                    "' into dictionary.")

# def main(args):
#     return 0

# if __name__ == '__main__':
#     import sys
#     sys.exit(main(sys.argv))

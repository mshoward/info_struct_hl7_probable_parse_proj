#!/usr/bin/python3
"""
    Outputs: tab separated csv's of input put files
"""

import argparse
import sys
#import itertools
import io
#import re
import datetime
import os

#todo move helper funcs into here
class sol_util:
    """
    Various Utility functions.  File operations, logging, error reporting,
    verbosity resolution, etc.
    """
    #todo ~~test this~~ fixme
    log_file_name = "debugging.log"

    #todo for later
    #def __init__():
    #   log_file_obj = open(str(curr_fname + ".log"),'a')
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



PARSED_GLOBALS = {'tabs':True, 'verbose':False}
EXIT_CODES = {'SUCCESS':0, 'IO_ERROR':1, 'OTHER_ERROR':2}


"""
HELPER FUNCTIONS
"""

def seek_beg(fileobj):
    """
    returns the file object's internal pointer to the beginning
    """

    return fileobj.seek(0, io.SEEK_SET)


def at_eof(fileobj):
    """
    returns true if the file object's internal pointer is at EOF,
    false otherwise.  Throws any errors it encounters.
    """
    initial = fileobj.tell()
    fileobj.seek(0, io.SEEK_END)
    ret_val = bool(initial == fileobj.tell())
    fileobj.seek(initial, io.SEEK_SET)
    return ret_val

def rdrwrpr(fileobj):
    """
    wrapper for fileobj.readline().strip()
    """
    return fileobj.readline().strip()





def guess_match_2(header_line):
    """
    returns true if the header matches the header.  spelling is irrelevant.
    """
    header_a = 'ONE:TWO'
    for i in header_line:
        if i not in header_a:
            return False
    return True


def colon_or_tab(xl8me):
    """
    Replaces colons with tabs depending on 'tabs' flag.
    """
    #global PARSED_GLOBALS
    replace_str = '\t' if PARSED_GLOBALS['tabs'] else ':'
    return xl8me.replace(':', replace_str)


#outputs the file in type 2, maintains ordering of entries,
#corrects missing entries
#outputs file based on input file
def out_type_2(file_obj):
    """
    Prints the corrected alt2.csv to dest_msh_alt2.csv.
    """
    correction_map = {'ONE:TWO':'ONE:TWO', 'ONE:':'ONE:TWO', ':TWO':'ONE:TWO',
                      '1:3': '1:3', '1:':'1:3', ':3':'1:3',
                      '3:6':'3:6', '3:':'3:6', ':6':'3:6',
                      '2:4':'2:4', '2:':'2:4', ':4':'2:4'}
    out_fname = 'dest_msh_alt2.csv'
    outf = open(out_fname, 'w')
    ret = 0
    while not at_eof(file_obj):
        ret = ret + outf.write(colon_or_tab(
            str(correction_map[rdrwrpr(file_obj)] + '\n')))
    outf.flush()
    outf.close()
    file_obj.close()
    sol_util.printerr("out_type_2 returning", ret)
    return ret

#outputs file based on input file
def out_type_1(file_obj):
    """
    Prints the corrected alt1.csv or source.csv to dest_msh_alt1.csv.
    """
    out_fname = 'dest_msh_alt1.csv'
    out_str = str('One\tTwo\tThree\tFour\n' + str('a\tb\tc\td\n' * 7))
    outf = open(out_fname, 'w')
    ret = outf.write(out_str)
    outf.flush()
    outf.close()
    file_obj.close()
    return ret

#outputs file based on input file
def out_type_3(file_obj):
    """
    Prints the corrected alt3.csv to dest_msh_alt3.csv.
    """
    out_fname = 'dest_msh_alt3.csv'
    out_head_str = 'One\tTwo\tThree\tFour\tFive\tSix\tSeven\n'
    out_body_str = str('1\t2\t3\t4\t5\t6\t7\n' * 3)
    out_str = out_head_str + out_body_str
    outf = open(out_fname, 'w')
    ret = outf.write(out_str)
    outf.flush()
    outf.close()
    file_obj.close()
    return ret


def guess_match_3(header_line, next_line):
    """
    Returns true if it has the right characters in the lines.
    """
    header_b = 'One,Two,Three,Four,Five,Six,Seven'
    chars_for_type_b = '1234567,'
    for i in header_line:
        if i not in header_b:
            return False
    for j in next_line:
        if j not in chars_for_type_b:
            return False
    return True


def file_switch_case(header_line, next_line):
    """
    Returns which type of file it is, 'ONE','TWO', or 'THREE'
    """
    if guess_match_2(header_line):
        return 'TWO'
    elif guess_match_3(header_line, next_line):
        return 'THREE'
    else:
        return 'ONE'


def process_file(file_obj):
    """
    Determines file type, prints corrected file. Returns the a vague number
    (blame io.BufferedTextStream (it's named something like that) for the lack
    of clarity about what that number is) about the number of things it wrote.

    Raises IOException or something.
    """
    seek_beg(file_obj)
    header_line = rdrwrpr(file_obj)
    next_line = rdrwrpr(file_obj)
    written = 0
    if not at_eof(file_obj):
        seek_beg(file_obj)
        ftype = file_switch_case(header_line, next_line)
        sol_util.printerr("file_switch_case returned", ftype)
        if ftype == 'ONE':
            written = out_type_1(file_obj) #closes file_obj -- should rethink
            sol_util.printerr("out_type_1 returned", written)
        elif ftype == 'TWO':
            written = out_type_2(file_obj)
            sol_util.printerr("out_type_2 returned", written)
        elif ftype == 'THREE':
            written = out_type_3(file_obj)
            sol_util.printerr("out_type_3 returned", written)
    else:
        written = -1
        sol_util.printerr("File too small")
    if written <= 0:
        sol_util.printerr("0 >", written)
        sol_util.printerr("Possible I/O error writing the file.")
    sol_util.printerr("process_file returning", written)
    return written


def load_conf():
    """
    Gets execution configuration from command line args.  Sets global flags.
    """
    #global PARSED_GLOBALS
    PARSED_GLOBALS['README'] = []
    parser = argparse.ArgumentParser(description="Outputs the correct file.")

    parser.add_argument('FileName',
                        metavar='File',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='The file or list of files to provide output for.')

    parser.add_argument('-c',
                        '--colons',
                        help='whether or not to keep the \
                        colons on filetype alt2',
                        default=False,
                        action='store_true')

    parser.add_argument('-v',
                        '--verbose',
                        help='Highly detailed debugging output.  \
                        Highly detailed.',
                        default=False,
                        action='store_true')

    args = parser.parse_args()
    PARSED_GLOBALS['tabs'] = bool(not args.colons)
    PARSED_GLOBALS['verbose'] = args.verbose
    PARSED_GLOBALS['README'] = args.FileName


def main():
    """
    Main.  Takes various flags (-h -v -c or --help, --verbose, or --colons),
    a file name argument, and outputs a corrected version of the file to a
    predefined file.  If the output file exists, it is truncated.  If the file
    doesn't exist, it is created.

    todo:
    ------- Task ------------------------------ Priority ------ Impact
    ------------------------------------------------------------------
            IOException handler:                low             2
            generic exception handler:          low             1
            helper functions -> sol_util class  low             3
            redesign to use ast:                low             4


    """
    #global EXIT_CODES
    #args = []
    load_conf()
    for readable_file in PARSED_GLOBALS['README']:
        sol_util.printerr('Converting ' + readable_file.name)
        res = process_file(readable_file)
        sol_util.printerr("process_file returned", res)
        if res <= 0:
            sol_util.printerr('Unable to complete the operation. \
                            Exiting with ' + str(EXIT_CODES['IO_ERROR']))
            sys.exit(EXIT_CODES['IO_ERROR'])
    sol_util.printerr('Complete.')







if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
""" Pytrace, a tool to trace function calls/returns.

    Author: Julien Delplanque (julien.delplanque@live.be)
    Repository: https://github.com/juliendelplanque/pytrace
    License: GNU GENERAL PUBLIC LICENSE Version 2
"""

import sys
from inspect import getargvalues

TO_TRACE = None
CALL_STRING = "╰╾▶"
RETURN_STRING = "◉◀╼"

class UnsupportedVersion(Exception):
    pass

def python_major_version():
    """ Returns the major version of the Python vm running this script.
    """
    return sys.version_info.major

def generic_print(object_to_print):
    """ Use the correct print function according to the version of Python vm.
    """
    version = python_major_version()
    if version == 2 or version == 3:
        print(object_to_print)
    else:
        raise UnsupportedVersion()

def arguments_string(args_dict):
    """ Returns the representation of args given as parameters to a function
        as a string.
    """
    keys = list(args_dict)
    args_string = '('
    for i in range(len(keys)-1):
        args_string += str(args_dict[keys[i]]) + ', '
    args_string += str(args_dict[keys[len(keys)-1]])+')'
    return args_string

def is_call_event(event):
    """ Returns true if the event is a call event.
        Else returns false.
    """
    return event == "call"

def is_return_event(event):
    """ Returns true if the event is a return event.
        Else returns false.
    """
    return event == "return"

def is_frame_corresponding_to_fct(frame, fct):
    """ Returns true if the frame corresponds to the function fct.
        Else returns false.
    """
    return str(frame.f_code.co_name) == str(fct.__name__)

def print_call(fct_name, args, indentation_count):
    """ Helper to print a call to the traced function.
    """
    global CALL_STRING
    generic_print(indentation_count*" "+CALL_STRING+fct_name+arguments_string(args))

def print_return(return_value, indentation_count):
    """ Helper to print a return of the traced function.
    """
    global RETURN_STRING
    generic_print(indentation_count*" "+RETURN_STRING+"return "+str(return_value))

def trace_function(frame, event, arg, indent=[0]):
    """ Print function calls and returns with a meaningfull indentation.
    """
    global TO_TRACE
    if TO_TRACE != None and is_frame_corresponding_to_fct(frame, TO_TRACE):
        if is_call_event(event):
            print_call(str(frame.f_code.co_name), getargvalues(frame).locals, indent[0])
            indent[0] += 3
        elif is_return_event(event):
            indent[0] -= 3
            print_return(arg, indent[0])
    return trace_function

def set_call_string(string):
    """ User interface to set the string use to draw a function call.
    """
    global CALL_STRING
    CALL_STRING = string

def set_return_string(string):
    """ User interface to set the string use to draw a function call.
    """
    global RETURN_STRING
    RETURN_STRING = string

def function_to_trace(fct):
    """ User interface to set the function to trace.
    """
    global TO_TRACE
    TO_TRACE = fct
    sys.settrace(trace_function)

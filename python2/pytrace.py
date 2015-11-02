#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from inspect import getargvalues

TO_TRACE = None

def arguments_string(args_dict):
    """ Returns the representation of args given as parameters to a function
        as a string.
    """
    keys = args_dict.keys()
    args_string = '('
    for i in range(len(keys)-1):
        args_string += str(args_dict[keys[i]]) + ', '
    args_string += str(args_dict[keys[len(keys)-1]])+')'
    return args_string

def trace_function(frame, event, arg, indent=[0]):
    """ Print function calls and returns with a meaningfull indentation.
    """
    global TO_TRACE
    if event == "call" and TO_TRACE != None and str(frame.f_code.co_name) == str(TO_TRACE.__name__):
        indent[0] += 2
        print "-" * indent[0]+">",str(frame.f_code.co_name)+arguments_string(getargvalues(frame).locals)
    elif event == "return" and TO_TRACE != None and str(frame.f_code.co_name) == str(TO_TRACE.__name__):
        print "<" + "-" * indent[0], "return", arg
        indent[0] -= 2
    return trace_function

def function_to_trace(f):
    global TO_TRACE
    TO_TRACE = f
    sys.settrace(trace_function)

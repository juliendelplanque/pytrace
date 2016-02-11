# -*- coding: utf-8 -*-
""" Pytrace, a tool to trace function calls/returns.
    Some examples.

    Author: Julien Delplanque (julien.delplanque@live.be)
    Repository: https://github.com/juliendelplanque/pytrace
    License: GNU GENERAL PUBLIC LICENSE Version 2
"""

from pytrace import function_to_trace, set_call_string, set_return_string

def count(n):
    if n == 0:
        return n
    else:
        count(n-1)
        return n

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

if __name__ == '__main__':
    print("Example with count function")
    print("===========================")
    function_to_trace(count)
    count(5)

    print("\nExample with fibo function")
    print("==========================")
    set_call_string("-->") # Change the string used to represent function calls.
    set_return_string("o<-") # Change the string used to represent returns.
    function_to_trace(fibo)
    fibo(4)



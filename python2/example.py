#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pytrace import *

def count(n):
    if n == 0:
        return n
    else:
        count(n-1)
        return n
function_to_trace(count)

count(5)

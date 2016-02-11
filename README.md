# pytrace
A function calls/returns tracker for Python.

[![asciicast](https://asciinema.org/a/36177.png)](https://asciinema.org/a/36177)

## How to use me?
Simply download the script pytrace.py and put it in your project
directory.

Then add the following lines in the file where is located the function
you want to trace.
~~~
from pytrace import function_to_trace
function_to_trace(the_function_you_will_track)
~~~

This will print function calls/returns in the console!

## Examples
See examples.py

## What if your terminal does not support UTF-8?
You can change the strings used to represent function calls/returns
using **set_call_string** and **set_return_string**.

For example:
~~~
from pytrace import function_to_trace, set_call_string, set_return_string

set_call_string("-->")
set_return_string("o<-")

...
~~~

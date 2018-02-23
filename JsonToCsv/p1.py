import datetime
from Logs import logpart
import sys
import time

def Addition(a, b):
    global add1, add2
    now1 = datetime.datetime.now()
    add1=str(now1)

    print(a, "+", b, "=", a + b); this_line_number1 = sys._getframe().f_lineno;
    this_function_name1 = sys._getframe().f_code.co_name
    this_filename1 = sys._getframe().f_code.co_filename
    logpart(this_line_number1, this_function_name1, this_filename1,add1)



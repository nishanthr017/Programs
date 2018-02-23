import datetime
from Logs import logpart
import sys
import time

def Subtraction(a, b):
    global sub1,sub2
    now2 = datetime.datetime.now()
    sub1=str(now2)

    print(b, "-", a, "=", b - a);this_line_number3 = sys._getframe().f_lineno;
    this_function_name3 = sys._getframe().f_code.co_name
    this_filename3 = sys._getframe().f_code.co_filename
    logpart(this_line_number3, this_function_name3, this_filename3,sub1)

import datetime
from logss import logpart
import sys
import time

def Subtraction(a, b):
    global sub1,sub2
    now3 = datetime.datetime.now()
    sub1=str(now3)
    time.sleep(0.020)
    print(b, "-", a, "=", b - a);this_line_number3 = sys._getframe().f_lineno;
    now4 = datetime.datetime.now()
    sub2 = str(now4)
    this_function_name3 = sys._getframe().f_code.co_name
    this_filename3 = sys._getframe().f_code.co_filename
    logpart(this_line_number3, this_function_name3, this_filename3,sub1,sub2)

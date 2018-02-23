import datetime
from logss import logpart
import sys
import time

def Multiplication(a, b):
    global mul1,mul2
    now5 = datetime.datetime.now()
    mul1=str(now5)
    time.sleep(0.150)
    print(a, "*", b, "=", a * b);this_line_number2 = sys._getframe().f_lineno;
    now6 = datetime.datetime.now()
    mul2=str(now6)
    this_function_name2 = sys._getframe().f_code.co_name
    this_filename2 = sys._getframe().f_code.co_filename
    logpart(this_line_number2,this_function_name2,this_filename2,mul1,mul2)

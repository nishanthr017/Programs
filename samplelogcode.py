import os
from collections import OrderedDict
from logging import Formatter, FileHandler,getLogger, INFO
from json import dumps
from pythonjsonlogger import jsonlogger

recordfields=[]
record1 = OrderedDict((('logger','aaa'),('application','logger-test'),('profile','prd')))
record2 = OrderedDict((('logger','aaa'),('application','logger-test'),('profile','prd')))
record3 = OrderedDict((('logger','aaa'),('application','logger-test'),('profile','prd')))
record4 = OrderedDict((('logger','aaa'),('application','logger-test'),('profile','prd')))


def filelogger(name, filname, level=INFO, recordfields=[]):

    handler = FileHandler(filename='/Users/nishrame/PycharmProjects/calc/Progr.json')
    log = getLogger('Calculation')
    textformatter = jsonlogger.JsonFormatter('%(method)s %(filename)s %(lineno)s')
    handler.setFormatter(textformatter)
    log.addHandler(handler)
    log.setLevel(INFO)
    return log

class JSONFormatter(Formatter):

    def __init__(self, recordfields=[], datefmt=None, customjson=None):

        Formatter.__init__(self, None, datefmt)
        self.recordfields = recordfields
        self.customjson = customjson


    def usesTime(self):

        return 'asctime' in self.recordfields

    def _formattime(self, record):
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)



    def _getjsondata(self, record):

        if (len(self.recordfields) > 0):
            fields = []
            for x in self.recordfields:
                fields.append((x, getattr(record, x)))
            fields.append(('message', record.msg))
            return OrderedDict(fields)
        else:
            return record.msg


    def format(self, record):

        self._formattime(record)
        jsondata = self._getjsondata(record)
        formattedjson = dumps(jsondata, cls=self.customjson)
        return formattedjson

flog = filelogger('testfilelog','/var/log/xxx.json',INFO,recordfields)
flog.info(record1)
flog.info(record2)
flog.info(record3)
flog.info(record4)

import logging
import arrow

def logpart(lineno,fnname,file_name,time1,time2):
    lno=str(lineno)
    dateformat = arrow.now().format('_YYYY_MM_DD')
    filename = "/Math/out" + dateformat+".json"
    finame=str(file_name)
    y=finame.replace("C:\Math\\","")
    stri=" { \""+fnname+"\" : \n\t\t\t{ \"Start time\" : \""+time1+"\",\n\t\t\t \"End time\" : \""+time2+"\",\n\t\t\t \"Function name\" : \""+fnname+"\",\n\t\t\t \"File name\" : \""+y+"\",\n\t\t\t \"Line no.\" : \""+lno+"\"\n\t\t\t } , "
    textformatter = logging.Formatter(stri)
    handler = logging.FileHandler(filename)
    handler.setFormatter(textformatter)
    log = logging.getLogger('Calculation')
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info('Hello1')
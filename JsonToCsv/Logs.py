import logging
import arrow

def logpart(lineno,fnname,file_name,time1):
    lno=str(lineno)
    dateformat = arrow.now().format('_YYYY_MM_DD')
    filename = "/Log/out" + dateformat+".json"
    finame=str(file_name)
    log = logging.getLogger('Calculation')
    y=finame.replace("C:\Log\\","")
    stri=" { \"timestamp\" : \""+time1+"\",\n   \"level\" : \"%(levelname)s\",\n   \"thread\" : \"%(thread)s\",\n   \"msg\" : \"%(message)s\",\n   \"Source\" : {\n\t\t   \"file\" : \""+y+"\",\n\t\t   \"method\" : \""+fnname+"\",\n\t\t   \"lineno\" : \""+lno+"\"},\n   \"module\" : \"%(module)s\"} , "
    textformatter = logging.Formatter(stri)
    handler = logging.FileHandler(filename)
    handler.setFormatter(textformatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info('Message to display')
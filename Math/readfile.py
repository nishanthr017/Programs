import json
from datetime import datetime

json_file=open('out_2018_02_23.json','r')
data = json.load(json_file)

startadd=data['Addition']['Start time']
startsub=data['Subtraction']['Start time']
startmul=data['Multiplication']['Start time']
endadd=data['Addition']['End time']
endsub=data['Subtraction']['End time']
endmul=data['Multiplication']['End time']

fmt = '%Y-%m-%d %H:%M:%S.%f'
tstamp1 = datetime.strptime(startadd, fmt)
tstamp2 = datetime.strptime(endadd, fmt)
tstamp3 = datetime.strptime(startsub, fmt)
tstamp4 = datetime.strptime(endsub, fmt)
tstamp5 = datetime.strptime(startmul, fmt)
tstamp6 = datetime.strptime(endmul, fmt)
td1=tstamp2-tstamp1
td2=tstamp4-tstamp3
td3=tstamp6-tstamp5

print("\n Addition-> \n\t Start time: ",startadd,"\n\t End time: ",endadd,"\n\t Running time: ",td1)
print("\n Subtraction-> \n\t Start time: ",startsub,"\n\t End time: ",endsub,"\n\t Running time: ",td2)
print("\n Multiplication-> \n\t Start time: ",startmul,"\n\t End time: ",endmul,"\n\t Running time: ",td3)
json_file.close()
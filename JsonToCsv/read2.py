import csv
import json

json_file='input.json'
with open(json_file, 'r') as json_data:
    x = json.load(json_data)


with open("oa5g2.csv","w",newline="") as f:  # python 2: open("output.csv","wb")
    title = ["timestamp","level","thread","msg","source_lineno","source_method","source_file","module"] # quick hack
    cw = csv.DictWriter(f,fieldnames=title,extrasaction='ignore')
    cw.writeheader()
    cw.writerows(x)
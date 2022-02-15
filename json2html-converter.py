from json2html import *
import json
''' 
please install 

json2html and json '''

ifile = 'api.json'
converted = 'sample1.html'

input = json.load(open(ifile))
out = json2html.convert(json = input)

file = open(converted,"w")
file.write(out)
file.close()

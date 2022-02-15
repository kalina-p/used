import json

data = json.load(open('api.json'))

z = (data['locations'])
za =z[0]
zb = (za['measurement'])

zc = zb.get('volts')
print('Volts:', zc)



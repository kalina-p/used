import json
import pandas as pd

'''flaten nested  jsons'''

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


jsonObj = json.loads(jsonStr)
flat = flatten_json(jsonObj)
df = pd.json_normalize(flat)
#print(df)
# print(df.locations_0_alarm)
#print(df.locations_0_measurement_volts)

import json
import sys
import pandas as pd
from datetime import datetime
from datetime import date

def detection(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        x = 0
        bb = False
        for features in file_data['features']:
            
            if bb == False:
                bb = True
                
            else:
                if bb == True :
                    x = x + 1
                    bb = False
                else:
                    bb = True
        print(x)
        
detection()
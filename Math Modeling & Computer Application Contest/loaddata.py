import os
import pandas as pd

def walk(path):
    paths = []
    name = []
    if not os.path.exists(path):
        return -1

    for root,dirs,names in os.walk(path):
        for filename in names:
            name.append(filename)
            paths.append(os.path.join(root,filename))
    
    return paths,name



def loaddata(path):
    df = pd.read_csv(path)
    
    return df
    
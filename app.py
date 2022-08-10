import pandas as pd
import gzip
import re
import os 

def concatinate():
    fp = open("output.txt", "a")
    dir_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(dir_path,'data')
    ls = [os.path.join(data_path, path) for path in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, path))]        

    for file in ls:
        with gzip.open(file,'rt') as f:
            for line in f:
                fp.write(line)


def get_url():
    with open("output.txt", 'r') as file:
        data = {}
        mention_counter = 0
        for line in file:
            if re.match("URL", line):
                url = re.search("(?P<url>(ftp|http|https)?://[^\s]+)", line)["url"]
                data[url] = 0
                mention_counter = 0

            if re.match("MENTION", line):
                mention_counter += 1
                data[url] = mention_counter
                
    df = pd.DataFrame(data.items()) 
    df.sort_index(inplace=True, ascending = False)
    print(df.head(50))


concatinate()
get_url()

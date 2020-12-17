import pandas as pd 

df = pd.read_csv("data\endpoint_dataset_final.csv")

count=0
with open("data\options.txt",mode="w") as text_file:
    for index,row in df.iterrows():
        count+=1
        s = '<option value="{}">{}</option>\n'.format(row['appid'],row['o_name'])
        text_file.write(s)

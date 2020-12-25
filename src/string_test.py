# intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# outtab = "abcdefghijklmnopqrstuvwxyz"
# trantab = str.maketrans(intab, outtab)

# str = "The Witcher 3: Wild Hunt"
# print (str.translate(trantab))

import re,string,csv
import pandas as pd

regex = re.compile('[%s]' % re.escape(string.punctuation))
s = "The Witcher 3: Wild Hunt"
# print(regex.sub('', s).lower())

def test_re(s):  # From Vinko's solution, with fix.
    return regex.sub('', s).lower()

def join(s):
    print(s)
    return ''.join([i if ord(i) < 128 else '' for i in s]).strip()

print(test_re(s))
# with open(r"./testing_ground/ratings.csv") as csv_file:
#     reader = csv.reader(csv_file,delimiter=",")
#     lines = 0
#     for row in reader:
#         if lines>0:
#             row[1] = regex.sub('', row[1]).lower()
#             print(row)
#         lines+=1
# print(test_re(s))

# df = pd.read_csv("data\endpoint_dataset.csv")
# df['o_name'] = df['o_name'].apply(join)
# print(df.shape)
# df.to_csv("data\endpoint_dataset_final.csv",index=False)
# df.to_csv("testing_ground/sanitized_steam_using_join.csv",index=False)
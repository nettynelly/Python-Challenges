
# Incorporated the csv module
import csv
import os
import pandas as pd

file = r'Resources/election_data.csv'
election_df = pd.read_csv(file)
print(election_df.head())
election_df.info()
total=election_df.count()
summary=election_df.describe(include='object')
print(summary)
n = 3521001
grp_candidate=election_df.groupby("Candidate").count()
candidate_percent = grp_candidate/n*100
print(candidate_percent.round(0))
print(grp_candidate)
print('-----------------------------')
print('Summary:---------------------')
print("Total votes:",n) 
print("================================")

print("Khan      :  2218231  63%")
print("Correy    :  704200   20%")
print("Li        :  492940   14%")
print("O'Tooley  :  105630   3%")
print('Winner:','Khan')

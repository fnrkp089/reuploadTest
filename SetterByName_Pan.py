import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)
#Define Stats
df['Sum of Cost2'] =df['Cost'].str.replace("$","") 
df['Sum of Cost'] = pd.to_numeric(df['Sum of Cost2'])
#선언이 문제...
#df_recost안에 df cost Replace 된거만 들어간듯.
#따라서 이 전체 내용에서 $만 뽑아야 할거같은데
#$만 뽑아내는 방법?...
groupby_sum = df.groupby(['Supplier Name'])['Sum of Cost'].sum()
groupby_sum.to_csv(output_file,index=True)

#클리어.
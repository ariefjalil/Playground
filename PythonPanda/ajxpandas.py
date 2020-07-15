import pandas as pd

def header(msg):
	print('-' * 50)
	print('[' + msg + ' ]')

filename = "potato_test.csv"
df = pd.read_csv(filename)
print(df)

'''header(" Remove columns")
df.drop('Time', axis=1, inplace =True)
print (df)'''

header ("remove unwanted columns")
df = df.drop(df.columns[[0,1,2]], axis=1)
print(df)



header(" write to csv file")
df.to_csv('potato_test123.csv', mode='w', index=False)


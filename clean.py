import pandas as pd

df = pd.read_csv("dataset.csv",index_col=0) # means that dont read col 1,2

arr_delay = df['ArrDelay']
class_list = []

for i in arr_delay:
	if i > 15:
		class_list.append(0)
	else:
		class_list.append(1)
print("Length of arr_delay is ",len(arr_delay))
print("Length of class_list is ",len(class_list))
print("Length of df is ",len(df))
#lenght = len(df)
#data = []
#for i in range(0,lenght):
#	data.append(0)

new_column = pd.DataFrame({'Class':class_list})
df = df.merge(new_column, left_index = True, right_index = True)
df.to_csv('model1.csv')


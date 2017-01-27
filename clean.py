# clea.py reads the csv file,creates a new col called Class and populates it according to value of arr_delay
# Class col is populated by using the list class_list
import pandas as pd

df = pd.read_csv("dataset.csv",index_col=0) # means that dont read col 1,2

arr_delay = df['ArrDelay'] # this list contains all the values of arr_delay from dataframe
class_list = [] # empty list

# if arr_delay > 15 assign class => 0 ( delayed ) else assign class => 1 ( not delayed )

for i in arr_delay:
	if i > 15:
		class_list.append(0)
	else:
		class_list.append(1)
#checking to ensure correct merge of 2 dataframes new_col and df
print("Length of arr_delay is ",len(arr_delay))
print("Length of class_list is ",len(class_list))
print("Length of df is ",len(df))
 
new_column = pd.DataFrame({'Class':class_list}) # dataframe with one col called 'Class'
df = df.merge(new_column, left_index = True, right_index = True) # dataframe which has the rest of the attributes
df.to_csv('model1.csv') # wrtie merged df to new csv file


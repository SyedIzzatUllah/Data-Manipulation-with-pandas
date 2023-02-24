#DataFrames
#Introducing DataFrames  
#Inspecting a DataFrame in the set    
# Print the head of the homelessness data
print(homelessness.head( ))    

#  Print information about homelessness
print(homelessness.info( ))  
 
# Print the shape  of  homelessness  
print(homelessness.shape)   

#  Print a description of  homelessness
print(homelessness.describe( ))

#Parts of a DataFrame in the  set    

# Import pandas using the alias pd  
import pandas as pd 

# Print a 2D NumPy array of the values in homelessness.
print(homelessness.values) 

# Print the column  names of homelessness
print(homelessness.columns)

#  Print the row index of homelessness
print(homelessness.index) 

#Sorting and subsetting

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values('individuals') 

# Sort  homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members',ascending=False)
 
# Sort homelessness by region, then descending family members
homelessness_reg_fam =  homelessness.sort_values(['region','family_members'], ascending = [True, False])

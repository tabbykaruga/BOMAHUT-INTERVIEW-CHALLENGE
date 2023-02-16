# A function called "find_max_min" that takes in a matrix as its argument.
# Initialize an empty list called "max_values" 
# Loop through each row in the matrix:
# a. Find the maximum number in the row and append them to our list "max_values".
# b. Find the minimum number of all the maximum numbers in our list "max_values".

def find_max_min(mat):
    m = len(mat)   
    max_values = []

    # loop through each row of the matrix
    for i in range(m):
        n = mat[i]

        max_in_row = max(n)
      
        # add all the maximum values to a list
        max_values.append(max_in_row)
        
        # find the minimun out of all the maximum values
        min_value =min(max_values)
          
    return min_value
    


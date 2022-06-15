import csv
with open( "Height-Weight.csv" , newline ="") as f:
     #reader() reads and returns the current row and then moves on to the next.
     r = csv.reader( f )
     file_data = list( r )

#print(file_data)
file_data.pop( 0 )

new_data = []
for i in range( len( file_data) ):
     num = file_data[i][1]
     #type casting to float or else the value after point will not be there
     new_data.append( float(num) )

n = len(new_data)
sum = 0
for x in new_data:
    sum = sum+x

mean = sum/n

print(mean)
print(f"Mean of the data is : { mean }")

import statistics
#mean1 = statistics.mean(new_data)
print(f"Using the predefined method, the mean is : { statistics.mean(new_data) }")
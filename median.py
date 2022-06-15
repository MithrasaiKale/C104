import csv
with open( "Height-Weight.csv" , newline ="") as f:
     #reader() reads and returns the current row and then moves on to the next.
     r = csv.reader( f )
     file_data = list( r )

#print(file_data)
file_data.pop( 0 )

new_data = []
for i in range( len( file_data) ):
     num = file_data[i][2]
     #type casting to float or else the value after point will not be there
     new_data.append( float(num) )

n = len(new_data)
new_data.sort()
#modulo symbol : %
            
#using floor division to get the nearest whole number
# floor division is shown by //
if( n%2 == 0 ):
    m1 = float(new_data[n //2])
    m2 = float(new_data[n // 2 -1])
    median=(m1+m2)/2
else:
    median=float(new_data[n // 2])
    
print(f"\nMedian of Data is={median}")
import statistics
print(f"\nUsing the predefined method, the median is : {statistics.median(new_data)}")
print(f"\nUsing the predefined method, the mode is:{statistics.mode(new_data)}")
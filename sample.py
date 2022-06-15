from collections import Counter
#Counter is a sub class in dictionary, using Counter tool you can count key-value pair
new_data = "Hellocoder"
data = Counter( new_data )
#print(data)

#return the list with all dictionary keys with values. It returns a tuple of key value pairs
print( data.items() )

#returns the list of all the values in the dictionary. 
print( data.values() )
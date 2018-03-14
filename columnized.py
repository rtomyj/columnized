#!/usr/local/bin/python3
import math

'''
	Method takes a list and specified number of columns to attempt and make
	even rows for the specified column constraints
'''
def getTable(numCols: int, contents: list):
	lineHeight = math.ceil(len(contents) / numCols)		# the max num of elments in a column

	rows = list()		# new list of rows
	start = 0			# starting number

	'''
		Cycles through the list user wants columnized and pairs elements that have
		the same modulus result. Possible modulus results are [0 (start) - lineheight)
	'''
	while start != lineHeight:
		# gets row where every element have the same modulus
		# results -- using list comprehensions
		tempRow = \
		[element for index, element in enumerate(contents) \
		if ((index )  % lineHeight == start)]

		rows.append(tempRow)		# adds the previously found row to list of rows
		start += 1
	return rows		# returns the rows


'''
	List of rows will be converted into a table. numRows is the constaint on the table. getTable
	will be called to try and make a table that has the same number of 
'''
def printTable(rows: list, numRows = 5, header = None, printFormator = None, headerFormator = None \
	, columnSeperator = '\t'):
	table = getTable(numRows, rows)
	numColumns = len(table[0])		# gets the number of columns for table

	# prints the column headers if user specified them
	if header is not None:
		i = 0
		for i in range(numColumns):
			if headerFormator is not None:
				print(headerFormator.format(header), end=columnSeperator)
			else:
				print(header, end=columnSeperator)
		print('')	# blank line

	# prints rows of table with their corresponding dict values
	for row in table:
		for element in row:
			print(element, end=columnSeperator)
		print('')		# seperates rows

	print('\n')		# seperates table from future output



import numpy as np
import pandas as pd

def read_data(file_name):
	print(file_name)
	df  =  pd.read_csv(file_name)
	npMatrix = df.as_matrix()
	print(npMatrix[2][2:4])
	return npMatrix
	
def read_data2(file_name):
	file_object  = open(file_name, "r")
	table = []
	next(file_object)
	for line in file_object:
		values = [float(x) for x in line.split()]
		if len(values) == 6:
			table.append(values)			
	#new_table = np.array(table).T
	t, ad_id, country, app_id, net, click  = np.array(table).T
	return t, ad_id, country, app_id, net, click
    
	

def distinct_values_and_top5(npMatrix):
	# to calculate N of diff val in each column
	i = 0
	v1 = []
	length = len(npMatrix[:,0])
	length = 30
	for i in range(length):
		i = i + 1	
		#print(npMatrix[i,1])
		v1.append(int(npMatrix[i,1]))
	y1 = np.bincount(v1)
	ii1 = np.nonzero(y1)[0]
	fn1 = np.vstack((ii1,y1[ii1])).T
	#fn1_sorted = fn1.sort(axis=0)
	fn1.sort(axis=0)
	print(fn1[0:5,:])
	
	
	
def feature_comb_per_impression(npMatrix):
	# to calculate N of diff rows in the matrix according to day and hour
	i = 0
	length = len(npMatrix[:,0])
	length = 30
	v1 = []
	y1_hours = np.bincount(npMatrix[0])
	
	#for i in range(length):
	#	i = i + 1	
	#	print(npMatrix[i,1:6])
	#	v1.append(int(npMatrix[i,1:4]))
	#pass
	
	
def top_five():
	# sort by diffrent columns and to take frist 5
	pass
	

def identical_in_top_five():
	# a.to calculate top N diff. for top 5
	# b. percentage from all data
	pass
	
	
def question():
	pass
	

def combination_per_click_75():
	# deterministic, probability?
	pass
	
	
def correlation_among_features():
	# correlation between features
	pass

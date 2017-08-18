import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pylab import *


file_name = "extracted.csv" # my file is in the same folder than the script so I can just give the name
df = pd.read_csv(file_name)


lat = df["latitude"] # storing the column latitude in a new variable called lat
longit = df["longitude"]
elev = df["elevation"]
flow_dist = df["flow distance"]
drainage = df["drainage area"]
m_chi = df["m_chi"]
b_chi = df["b_chi"]
key = df["source_key"]
basin = df["basin_key"]
seg_elev = df["segmented_elevation"]
seg_num = df["segment_number"]
Geology = df["Geology"]

lithology_name = "lithology.csv"
df_litho = pd.read_csv(lithology_name, sep = ';', encoding = "ISO-8859-1")


Geol = df_litho["Geology"]
litho = df_litho["Lithology"]
age = df_litho["Age"]


l = list(df["Geology"].unique())
df["GeoCode"] = pd.Series(np.zeros(df.shape[0]))

for i in range(len(l)):
	df["GeoCode"][df["Geology"] == l[i]] = i

GeoCode = df["GeoCode"]


df_no_data = df 
df_no_data = df_no_data[df_no_data["Geology"] == "NoData"]



df3 = df.merge(df_litho, on='Geology', how='inner')


############################### GRAPHS ####################################


#plt.scatter(df["longitude"], df["latitude"], c = "red")

#plt.scatter(df_no_data["longitude"], df_no_data["latitude"], c = "green")

#df2 = pd.DataFrame(data =[ df["m_chi"], df["Geology"]])

#print (df2)

### plot m_chi by geology


#l = list (df["Geology"].unique())
#d  = {}

#for i in range(len(l)):
	#d[l[i]] = df["m_chi"][df["Geology"] == l[i]]
	
#print(d.keys())

#df2 = pd.DataFrame([d], ["m_chi", "Geology"])

#print(df2)

#print(df.groupby("Geology").GeoCode.count())

#df.groupby("Geology").GeoCode.count().plot(kind ="bar")


#plt.boxplot(list(d.values()), list(d.keys()), '')
#legend(loc='upper left')


#new_list = []
#for item in list(d.keys()):
    #new_list.append(str(item))

#print(new_list)



#fig, ax = plt.subplots()



#ax.boxplot(list(d.values()), new_list,'')

#ax.set_xticks(range(1,len(d)+1))

#ax.set_xticklabels(new_list, rotation ="vertical")
#ax.set_xlabel ("Geology")
#ax.set_ylabel("m_chi")
#ax.set_title("BOXPLOT", fontsize = 18)
#plt.show()


### plot age by litho

# print(df3.groupby("Age").GeoCode.count())

l = list (df3["Age"].unique())
dictio  = {}
count = list(df3.groupby("Age").GeoCode.count())
for i in range(len(l)):

	mchi = df3["m_chi"][df3["Age"] == l[i]]
	titre = "(n= " + str(count[i])+") " + l[i]
	dictio[titre] = [(mchi)]


new_list = []
for i in list(dictio.keys()):
    new_list.append(str(i))


fig, ax = plt.subplots(1,1)

ax.boxplot(list(dictio.values()), new_list,'')

ax.set_xticks(range(1,len(dictio)+1))

ax.set_xticklabels(new_list, rotation ="vertical", fontsize = 7)

ax.set_xlabel ("Age")
ax.set_ylabel("m_chi")
ax.set_title("BOXPLOT", fontsize = 18)

# for i in range(len(l)):
# 	ax.annotate(list(etiq.values()))

#df.groupby("Geology").GeoCode.count().plot(kind ="bar")

plt.show()
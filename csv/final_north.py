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


# jaune

df2 = df[(df["Geology"] == "al+vr") & (df["longitude"] > 25.7) & (df["latitude"] > 46.2)]
df2bis = df[(df["Geology"] == "ne") & (df["longitude"] > 25.7) & (df["latitude"] > 46.2)]
df2ter = df[(df["Geology"] == "al+tu") & (df["longitude"] > 25.7) & (df["latitude"] > 46.2)]
df2quat = df[(df["Geology"] == "vr+cm") & (df["longitude"] > 25.7) & (df["latitude"] > 46.2)]
df2cinq = df[(df["Geology"] == "ne+ap") & (df["longitude"] > 25.7) & (df["latitude"] > 46.2)]


df2ter = df2bis.append(df2ter)
df2quat = df2ter.append(df2quat)
df2cinq = df2quat.append(df2cinq)
df2 = df2cinq.append(df2)

# df2.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv_df2_north.txt', index = False)


# beige fonce

df3 = df[(df["Geology"] == "Pg1-lt") & (df["longitude"] > 25.8) & (df["longitude"] < 26.60) & (df["latitude"] > 46.2)]
df3bis = df[(df["Geology"] == "Pr") & (df["longitude"] > 25.8) & (df["longitude"] < 26.60) & (df["latitude"] > 46.2)]
df3ter = df[(df["Geology"] == "If-ch") & (df["longitude"] > 25.8) & (df["longitude"] < 26.60) & (df["latitude"] > 46.2)]
df3quat = df[(df["Geology"] == "sm") & (df["longitude"] > 25.8) & (df["longitude"] < 26.60) & (df["latitude"] > 46.2)]
df3cinq = df[(df["Geology"] == "sm+Pg1") & (df["longitude"] > 25.8) & (df["longitude"] < 26.60) & (df["latitude"] > 46.2)]




df3ter = df3bis.append(df3ter)
df3quat = df3ter.append(df3quat)
df3cinq = df3quat.append(df3cinq)
df3 = df3cinq.append(df3)

# df3.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv_df3_north.txt', index = False)


# beige clair

df4 = df[(df["Geology"] == "he")& (df["longitude"] > 26.40) & (df["latitude"] > 46.2)]
df4bis = df[(df["Geology"] == "bd")& (df["longitude"] > 26.40) & (df["latitude"] > 46.2)]
df4ter = df[(df["Geology"] == "to")& (df["longitude"] > 26.40) & (df["latitude"] > 46.2)]

df4ter = df4bis.append(df4ter)
df4 = df4ter.append(df4)
# df4.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv_df4_north.txt', index = False)
# bleu clair

df5 = df[(df["Geology"] == "br-al") & (df["longitude"] < 26.10) & (df["longitude"] > 25.30) & (df["latitude"] > 46.2)]

df5bis = df[(df["Geology"] == "ne") & (df["longitude"] < 26.10) & (df["longitude"] > 25.30) & (df["latitude"] > 46.2)]
df5ter = df[(df["Geology"] == "al") & (df["longitude"] < 26.10) & (df["longitude"] > 25.30) &  (df["latitude"] > 46.2)]

df5ter = df2bis.append(df5ter)
df5 = df5ter.append(df5)
# df5.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv_df5_north.txt', index = False)

df_list = [df2, df3, df4, df5]

df_final = pd.concat(df_list)

# df_final.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv_north.txt', index = False)

print(df_final)


plt.clf()
plt.scatter(df2["longitude"], df2["latitude"])
plt.scatter(df3["longitude"], df3["latitude"], color = 'red')
plt.scatter(df4["longitude"], df4["latitude"], color = 'green')
plt.scatter(df5["longitude"], df5["latitude"], color = 'purple')

plt.xlabel ("longitude")
plt.ylabel("latitude")
plt.title("Points/Structures")


show()
quit()

Structure_A = list(df5["m_chi"])
Structure_B = list(df2["m_chi"])
Structure_C = list(df3["m_chi"])
Structure_D = list(df4["m_chi"])


fig, ax = plt.subplots()

ax.boxplot((Structure_A, Structure_B, Structure_C, Structure_D), showfliers=False)

boxColor = ["blue", "green", "red", "black"]


label = ax.set_xticklabels(("Structure_A", "Structure_B", "Structure_C", "Structure_D"), rotation = 'vertical', fontsize = 8)


ax.set_ylim(-10, 180)
ax.set_xlabel ("Structures")
ax.set_ylabel("m_chi")
ax.set_title("BOXPLOT", fontsize = 18)

fig.set_size_inches(15, 15)
plt.show()


show()
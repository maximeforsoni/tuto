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

df2 = df[(df["Geology"] == "al+vr") & (df["longitude"] > 25.9) & (df["latitude"] > 46.2)]
df2bis = df[(df["Geology"] == "ne") & (df["longitude"] > 25.9) & (df["latitude"] > 46.2)]
df2ter = df[(df["Geology"] == "al+tu") & (df["longitude"] > 25.9) & (df["latitude"] > 46.2)]
df2quat = df[(df["Geology"] == "vr+cm") & (df["longitude"] > 25.9) & (df["latitude"] > 46.2)]
df2cinq = df[(df["Geology"] == "ne+ap") & (df["longitude"] > 25.9) & (df["latitude"] > 46.2)]


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

df5 = df[(df["Geology"] == "br-al") & (df["longitude"] < 26.10) & (df["latitude"] > 46.2) & (df["longitude"] > 25.80)]

df5bis = df[(df["Geology"] == "ne") & (df["longitude"] < 26.10) & (df["latitude"] > 46.2) & (df["longitude"] > 25.80)]
df5ter = df[(df["Geology"] == "al") & (df["longitude"] < 26.10) & (df["latitude"] > 46.2) & (df["longitude"] > 25.80)]


df5bis = df5.append(df5bis)
df5ter = df5bis.append(df5ter)
df5ter.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv\csv_df5_north.txt', index = False)

df6 = df[(df["Geology"] == "qp2-qp3") & (df["longitude"] > 26.40)  & (df["longitude"] < 27)  & (df["latitude"] > 46.2)]
df6bis = df[(df["Geology"] == "Iv") & (df["longitude"] > 26.40)  & (df["longitude"] < 27)   & (df["latitude"] > 46.2)]
df6ter = df[(df["Geology"] == "qpi") &  (df["longitude"] > 26.40)  & (df["longitude"] < 27)   & (df["latitude"] > 46.2)]
df6quat = df[(df["Geology"] == "qp3") &  (df["longitude"] > 26.55)  & (df["longitude"] < 27)   & (df["latitude"] > 46.2)]
df6cinq = df[(df["Geology"] == "p") &  (df["longitude"] > 26.55)  & (df["longitude"] < 27)  & (df["latitude"] > 46.2)]
df6six = df[(df["Geology"] == "dc") &  (df["longitude"] > 26.40)  & (df["longitude"] < 27)   & (df["latitude"] > 46.2)]
df6seven = df[(df["Geology"] == "qh2") & (df["longitude"] > 26.40)  & (df["longitude"] < 27)   & (df["latitude"] > 46.2)]
df6eight = df[(df["Geology"] == "bs") & (df["longitude"] > 26.40)  & (df["longitude"] < 27)  & (df["latitude"] > 46.2)]
df6nine = df[(df["Geology"] == "ks+m") &  (df["longitude"] > 26.40)  & (df["longitude"] < 27)  & (df["latitude"] > 46.2)]
df6ten = df[(df["Geology"] == "vh") &  (df["longitude"] > 26.80)  & (df["longitude"] < 27)  & (df["latitude"] > 46.2)]


df6bis = df6.append(df6bis)
df6ter = df6bis.append(df6ter)
df6quat = df6ter.append(df6quat)
df6cinq = df6quat.append(df6cinq)
df6six = df6cinq.append(df6six)
df6seven = df6six.append(df6seven)
df6eight = df6seven.append(df6eight)
df6nine = df6eight.append(df6nine)
df6ten = df6nine.append(df6ten)
df6ele= df6ten.append(df6)

df6ele.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv\csv_df6_north.txt', index = False)

df_list = [df2, df3, df4, df5ter, df6ele]

df_final = pd.concat(df_list)

df_final.to_csv('C:\Users\Maxime\Desktop\UniED\Scripts\csv\csv_north.txt', index = False)

# print(df_final)
quit()
plt.clf()
plt.scatter(df2["longitude"], df2["latitude"])
plt.scatter(df3["longitude"], df3["latitude"], color = 'red')
plt.scatter(df4["longitude"], df4["latitude"], color = 'green')
plt.scatter(df5ter["longitude"], df5ter["latitude"], color = 'purple')
plt.scatter(df6ele["longitude"], df6ele["latitude"], color = 'cyan')

plt.xlabel ("longitude")
plt.ylabel("latitude")
plt.title("Points/Structures")


Structure_A = list(df5ter["m_chi"])
Structure_B = list(df2["m_chi"])
Structure_C = list(df3["m_chi"])
Structure_D = list(df4["m_chi"])
Structure_E = list(df6ele["m_chi"])


fig, ax = plt.subplots()

ax.boxplot((Structure_A, Structure_B, Structure_C, Structure_D, Structure_E), showfliers=False)

boxColor = ["blue", "green", "red", "black"]


label = ax.set_xticklabels(("Structure_A", "Structure_B", "Structure_C", "Structure_D", "Structure_E"), rotation = 'vertical', fontsize = 8)


ax.set_ylim(-10, 180)
ax.set_xlabel ("Structures")
ax.set_ylabel("m_chi")
ax.set_title("BOXPLOT", fontsize = 18)

fig.set_size_inches(15, 15)
plt.show()


show()
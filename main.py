import pandas
import pandas as pd

df = pd.read_csv("./Data/Squirrel_Data.csv")
df_count = df["Primary Fur Color"].value_counts()
df_dict = df_count.to_dict()
count = df_count.to_list()
# print(count)
colors = []
for i in df_dict:
    colors.append(i)
# print(colors)

data_dict ={
    "Colors": colors,
    "Count": count
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./Data/data.csv")
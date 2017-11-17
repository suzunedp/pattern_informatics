import numpy as np
import random

#csv読み込み
import csv
list_row = []
raw_data = [] #元のデータを格納

with open("Iris.csv","r") as f:
    reader = csv.reader(f)

    for row in reader:
        map_row = map(float, row)  # 各要素をfloatに変換
        list_row = list(map_row)
        raw_data.append(list_row)

iris_raw_data = np.array(raw_data)

    

import numpy as np

#最初の座標を設定
def init_centre(k):
    pass

#各クラスタの重心を取る
def get_centre(k,iris_position_data,claster_data):



#中心点との距離を計算
def get_distance(iris_position_data,centre):
    return np.sum(iris_position_data - centre)**2

#最も近い座標を見つける
def get_nearest_centre(distance):
    return np.where(np.min(distance))

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

# iris_raw_data = np.array(raw_data)

# #品種データと答えのデータを分割
# iris_position_data, iris_answer_data = np.hsplit(iris_raw_data, [4])
# iris_answer_data = iris_answer_data.astype(np.int)
# print(iris_answer_data)

group1 = []
group2 = []

for data in iris_raw_data
    initial_number = random.randint(0,1)
    if initial_number == 0:
        group1.append(data)
    else:
        group2.append(data)

group1 = np.array(group1)
group2 = np.array(gronp2)

centre1 = np.avarage(group1, axis = 1)
centre2 = np.avarage(group2, axis = 1)


while prev_centre == centre:

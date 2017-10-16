from operator import itemgetter, attrgetter
#定義した関数

#距離を計算
def culculate_dist(test,teacher):
   dist = (tester[0]-teacher[0])**2 + (tester[1]-teacher[1])**2 + (tester[2]-teacher[2])**2 + (tester[3]-teacher[3])**2
   result = [dist, teacher[4]]
   return result

#一つ抜き法用の教師データの作成
def create_teacher_data(number,data):
    del data[number]
    return data

#k番目までの配列に入っている花の種類を数える
def count_frequent_spices(k,result):
    count = 0
    spices_count = [0,0,0]
    while count < k:
        if result[k][1] == 0.0:
            spices_count[0] += 1
        elif result[k][1] == 1.0:
            spices_count[1] += 1
        else:
            spices_count[2] += 1
        count += 1
    return spices_count

#k近傍法で求めた品種と本当の品種の照合
def data_check(spices_list,answer):
    spices = spices_list.index(max(spices_list))
    if int(answer) == spices:
        return True
    else:
        return False

#ここからメイン

import csv
list_row = []
raw_data = [] #元のデータを格納

with open("Iris.csv","r") as f:
    reader = csv.reader(f)

    for row in reader:
        map_row = map(float, row)  # 各要素をfloatに変換
        list_row = list(map_row)
        raw_data.append(list_row)

#k近傍法のkの初期値
k = 3

#テストデータの番号
test_number = 0

while test_number < len(raw_data):

    #教師用データとテスト用データに分割
    tester = raw_data[test_number] #テストデータ
    test_answer = tester[4] #テストデータの品種
    teacher = create_teacher_data(test_number,raw_data) #教師用データ

    result = []  #距離の計算結果格納用配列
    teacher_number = 0 #教師データの番号

    while teacher_number < len(teacher):
        #ここでそれぞれの教師用データとテストデータの距離を計算する
        each_result = culculate_dist(tester,teacher[teacher_number])
        result.append(each_result)
        teacher_number += 1

    #result配列を距離に応じて並び替える
    sorted(result, key=itemgetter(0), reverse = True)

    #k番目までの配列に入っている花の種類を数える
    count_spices = []
    count_spices = count_frequent_spices(k,result)

    #テストデータとあってるか確認
    print(data_check(count_spices,test_answer))

    if test_number == 0:
        break
    test_number += 1

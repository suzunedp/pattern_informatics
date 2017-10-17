#定義した関数

#距離を計算
def culculate_dist(test,teacher):
   dist = (tester[0]-teacher[0])**2 + (tester[1]-teacher[1])**2 + (tester[2]-teacher[2])**2 + (tester[3]-teacher[3])**2
   result = [dist, teacher[4]]
   return result

#一つ抜き法用の教師データの作成
# def create_teacher_data(number,data):
#     del data[number]
#     return data

#k番目までの配列に入っている花の種類を数える
def count_frequent_spices(k,result):
    count = 1
    spices_count = [0,0,0]
    while count < k:
        if result[count][1] == 0.0:
            spices_count[0] += 1
        elif result[count][1] == 1.0:
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

#csvの読み込み------------------------------------------------------------
import csv
list_row = []
raw_data = [] #元のデータを格納

with open("Iris.csv","r") as f:
    reader = csv.reader(f)

    for row in reader:
        map_row = map(float, row)  # 各要素をfloatに変換
        list_row = list(map_row)
        raw_data.append(list_row)

#csvの読み込みここまで------------------------------------------------------

total_result = [] #最終結果が吐かれる配列

k = 2 #k近傍法のkの初期値
result = []  #距離の計算結果
sorted_result = [] #ソート済み距離の計算結果
count_spices = [] #品種
# teacher_number = 0

while k <= 31:

    k_and_success_rate = [k,0] #各kの時に何回成功したか
    test_data_number = 0 #何番目のデータをテスト用データとして使うか

    while test_data_number < len(raw_data):

        #教師用データとテスト用データに分割
        tester = raw_data[test_data_number] #テストデータ
        test_answer = tester[4] #テストデータの品種

        teacher = raw_data #教師用データ
        # teacher = create_teacher_data(test_data_number,raw_data) #教師用データ

        teacher_number = 0

        while teacher_number < len(teacher):
            #ここでそれぞれの教師用データとテストデータの距離を計算する
            each_result = culculate_dist(tester,teacher[teacher_number])
            result.append(each_result)
            teacher_number += 1

        #result配列を距離に応じて並び替える
        sorted_result = sorted(result)
        #k番目までの配列に入っている花の種類を数える

        count_spices = count_frequent_spices(k,sorted_result)

         #テストデータとあってるか確認
        if data_check(count_spices,test_answer) == True:
            k_and_success_rate[1] += 1

        # if test_data_number == 0:
        #     break

        result.clear()
        test_data_number += 1



    total_result.append(k_and_success_rate)

    if k == 1:
        break

    k += 1

with open("total_result.csv", "w")as fout:
    csvout = csv.writer(fout)
    csvout.writerows(total_result)

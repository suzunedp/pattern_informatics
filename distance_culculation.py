#一旦教師用データをp,テスト用データをqとする
#
# import csv
#
# with open("Iris.csv","r") as f:
#     reader = csv.reader(f)
#
#     for row in reader:
#         data.append(row)
#
# print(data)

result = [[4.0,1][3.5,1][3.0,0][2.5,1][2.0,0]]

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
    return spices_count

print(count_frequent_spices(3,result))
#p = data[1]
#q = data[2]

#def distance_culc(p,q):
#dist = (p[1]-q[1])^2 + (p[2]-q[2])^2 + (p[3]-q[3])^2
#print([dist,p(4)])

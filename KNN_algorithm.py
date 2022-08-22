import pandas as pd
import numpy as np

target_point = list(map(int, input().split(' ')))

print(target_point)
data = pd.read_csv('C:/Users/Tan Vu/Downloads/KNN_dataset.csv')
# print(data)
data = data.iloc[:,1:]
# print(data)

dataset = data.iloc[:,:-1].values.tolist()
label = data.iloc[:,-1].values.tolist()

# print(dataset)
# print(label)
# target_point = [2,4,6,8]

def E_distance(point_A, point_B):
    dis = 0
    for i in range(len(point_A)):
        dis = dis + (point_A[i] - point_B[i])**2
    # print(np.sqrt(dis))
    return np.sqrt(dis)

E_distance(point_A= [1, 2], point_B= [3,4])

def prediction(data_feature, label_list, target_point, k_num):
    distance_list = []
    for i in range(len(data_feature)):
        dis = E_distance(data_feature[i], target_point)
        distance_list.append([dis, label_list[i]])
    # print('old distance list', distance_list)
    distance_list.sort(key= lambda sub_list: sub_list[0])
    # print('new distance list', distance_list)
    k_shortest_list = []
    for j in range(k_num):
        k_shortest_list.append(distance_list[j][1])
    # print(k_shortest_list)
    prediction = max(k_shortest_list, key=k_shortest_list.count)
    print(prediction)

# K = 5

prediction(data_feature=dataset, label_list= label, target_point= target_point , k_num=5)









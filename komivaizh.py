distances = [
    [0, 712, 673, 1075, 875, 1622, 423],
    [712, 0, 1385, 1800, 1577, 2348, 1128],
    [673, 1385, 0, 1499, 239, 2046, 244],
    [1075, 1800, 1499, 0, 1287, 551, 1266],
    [875, 1577, 239, 1287, 0, 1835, 442],
    [1622, 2348, 2046, 551, 1835, 0, 1813],
    [423, 1128, 244, 1266, 442, 1813, 0]
]

def find_maximum_distance(distances):
    num_cities = len(distances)
    max_distance = 0
    path_temp = []
    path_max = []
    for i in range(num_cities):
        for j in range(num_cities):
            if i == j:
                continue
            distance = distances[i][j]
            path_temp.append(distances[i][j])
            for k in range(num_cities):
                if k == i or k == j:
                    continue
                distance += distances[j][k]
                path_temp.append(distances[j][k])
            if max_distance < distance:
                max_distance = distance
                path_max = path_temp.copy()
                path_temp = []
            else:
                path_temp = []

    return max_distance, path_max


max_distance, path = find_maximum_distance(distances)
print("Максимальное расстояние:", max_distance, path)

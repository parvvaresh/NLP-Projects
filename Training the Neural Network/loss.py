from calendar import c


def loss(data):
    cross_entropy = 1

    for element in data:
        for target , predict in element.items():
            if target == 1:
                cross_entropy *= predict
            elif target == 0:
                cross_entropy *= (1 - predict)
    
    return cross_entropy

data = [{1 : 0.8}, {0 : 0.1}, {0 : 0.3}, {1 : 0.9}]


cross_entropy = loss(data)

print(cross_entropy)
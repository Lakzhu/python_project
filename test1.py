def get_pins(observed):
    dic = {'1': '124', '2': '1235', '3': '236',
             '4': '1457', '5': '24568', '6': '3569',
             '7': '478', '8': '57890', '9': '689',
             '0': '08'}
    observed = list(observed)
    for i in range(len(observed)):
        observed[i] = dic[observed[i]]
    observed[0] = list(observed[0])
    while len(observed) != 1:
        tmp = list(observed[1])
        observed.pop(1)
        p = set()
        for i in observed[0]:
            for j in tmp:
                p.add(i+j)
        observed[0] = list(p)
    return observed[0]
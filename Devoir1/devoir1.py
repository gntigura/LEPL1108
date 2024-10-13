def devoir1(trajets_train, durees_train, ville_depart, durees_voldirect, sacrifice):
    count_train = 0; l = []; rerD = {}; d ={}
    for k in range(len(durees_train)):
        rerD[trajets_train[k]] = durees_train[k]
    ### Liste de villes dans l'ordre ###

    for i in trajets_train:
        cities = i.split('-')
        if cities[0] == ville_depart:
            l.append(cities[1])
        elif cities[1] == ville_depart:
            l.append(cities[0])
        else:
            l.append(cities[0])
            l.append(cities[1])
    ville = list(set(l))
    ville.sort()
    ville.append(ville_depart)
    for l in ville:
        d[l] = {}
    for key in rerD:
        d[key.split('-')[0]][key.split('-')[1]] = rerD[key]
        d[key.split('-')[1]][key.split('-')[0]] = rerD[key]
    report = {vortex: float('inf') for vortex in d}
    report[ville_depart] = 0
    ### Calcul de trajet pour avion ###

    min_distances_avion = []
    for i in durees_voldirect:
        min_distances_avion.append(i + 180)
    
    ### Calcul de trajet pour train ###
    min_distances_train = []
    for _ in range(len(d)-1):
        for i in d:
            for j,k in d[i].items():
                if report[i] != float('inf') and report[i] + k + 15 < report[j]:
                    report[j] = report[i] + k + 15
    for k in report.values():
        min_distances_train.append(k + 15)
    min_distances_train.pop(-1)
    ville.pop(-1)

    for train,avion in zip(min_distances_train, min_distances_avion):
        if train <= avion + sacrifice:
            count_train += 1
    return ville, min_distances_train, min_distances_avion, count_train


print('Aude')
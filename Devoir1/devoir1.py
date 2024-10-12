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
                if report[i] != float('inf') and report[i] + k < report[j]:
                    report[j] = report[i] + k + 15
    for k in report.values():
        min_distances_train.append(k + 15)
    min_distances_train.pop(-1)
    ville.pop(-1)

    for t in range(len(min_distances_avion)):
        if min_distances_train[t] <= min_distances_avion[t] + sacrifice:
            count_train += 1
    return ville, min_distances_train, min_distances_avion, count_train

routes = [
    'BRU-PAR', 'BRU-AMS', 'BRU-LON', 'BRU-COL', 'PAR-BOR', 'PAR-LYO', 'PAR-FRA', 
    'PAR-LON', 'PAR-REN', 'AMS-BER', 'AMS-COL', 'AMS-HAM', 'COL-HAM', 'COL-FRA', 
    'COL-BER', 'LYO-MAR', 'LYO-ZUR', 'FRA-HAM', 'FRA-BER', 'FRA-MUN', 'FRA-ZUR', 
    'BER-MUN', 'BER-HAM', 'BER-PRA', 'MUN-ZUR', 'MIL-LYO', 'MIL-ZUR', 'LYO-BAR', 
    'BAR-MAR', 'BOR-TLS', 'TLS-BAR', 'TLS-MAR', 'LON-BIR', 'LON-MAN', 'MAN-BIR', 
    'MAN-EDI', 'EDI-GLW', 'LYO-TLS', 'HAM-COP', 'PAR-TLS'
]

dureestrain = [80, 95, 120, 105, 120, 110, 230, 140, 90, 385, 180, 300, 215, 60, 280, 110,
240, 280, 275, 200, 235, 255, 175, 265, 210, 270, 240, 330, 285, 120, 195, 225, 95, 140, 80, 190,
50, 250, 280, 260]

dureesvoldirect = [65, 120, 85, 80, 100, 60, 90, 100, 60, 105, 75, 80, 85, 85, 100, 90, 80,
65, 90, 95, 100, 75]

print(devoir1(routes, dureestrain, 'BRU', dureesvoldirect, 60))
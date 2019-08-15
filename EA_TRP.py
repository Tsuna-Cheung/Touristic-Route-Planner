import random
import pandas as pd
import numpy as np
import math

data = pd.read_csv('chinacity_33.csv')
dt = np.array(data)
Lat = np.array(data.iloc[:, 2]).tolist()
Long = np.array(data.iloc[:, 1]).tolist()


def evolutionaryAlg(cities):
    num_cities = len(cities)
    init_list = list(cities)
    POPULATION_SIZE = (num_cities - 1) * (num_cities - 2)
    if num_cities > 11:
        POPULATION_SIZE = 100
    OFFSPRING_SIZE = round(POPULATION_SIZE / 2)
    TOURNAMENT_SIZE = 2
    mr = 0.5
    iteration = 0
    max_iter = 1500

    # generate initial population
    p0 = [1] * POPULATION_SIZE
    d0 = [0] * POPULATION_SIZE
    for i in range(len(p0)):
        individual = list(init_list)
        # print('individual : ',individual)
        temp = individual[1:]
        # print('temp1 : ',temp)
        random.shuffle(temp)
        # print('temp2 : ',temp)
        individual[1:] = temp
        # print('individual2 : ',individual)
        p0[i] = list(individual)
        # print('item: ',p0[i])
        d0[i] = geoDistance(individual)
    # print('p0:', p0)
    # print('d0:', d0)

    # find minimum
    idx_sorted = sorted(range(len(d0)), key=lambda k: d0[k])
    # print('idx_sorted:', idx_sorted)
    # print('d0:', d0)
    best_idx = idx_sorted[0]

    # best route
    best_route = p0[best_idx]
    best_distance = d0[best_idx]
    # print('best_route:', best_route)
    # print('best_distance:', best_distance)

    while iteration < max_iter:
        iteration += 1
        p_t = p0
        d_t = d0
        # print('length of population__:',len(p_t))
        # print('new iteration begin')
        no_offspring = 0
        while no_offspring != OFFSPRING_SIZE:
            # print('selection begin')
            # selection
            [p1, p2] = selection(list(p0), list(d0), POPULATION_SIZE, TOURNAMENT_SIZE)
            # print('selection done')
            # variation
            [c1, c2] = crossover(list(p1), list(p2))
            # print('crossover done')
            # print('child:', child)
            c1 = mutation(list(c1), mr)
            d1 = geoDistance(c1)
            p_t.append(c1)
            d_t.append(d1)
            no_offspring += 1
            # print('no_offspring:',no_offspring)
            # print('size of generation:',len(p_t))

            if no_offspring == OFFSPRING_SIZE:
                break
            else:
                c2 = mutation(list(c2), mr)
                d2 = geoDistance(c2)
                p_t.append(c2)
                d_t.append(d2)
                no_offspring += 1
        [p_t, d_t] = sort_population(p_t, d_t)
        # print('p_t_sorted:', p_t)
        # print('p_t_sorted:', d_t)
        # print('lenth:', len(d_t))
        iter_best_route = p_t[0]
        iter_best_distance = d_t[0]
        if iter_best_distance < best_distance:
            best_distance = iter_best_distance
            best_route = iter_best_route
        print('iteration', iteration, ':', best_distance, '-----------', best_route)
        # reproduction
        p0 = p_t[:POPULATION_SIZE]
        d0 = d_t[:POPULATION_SIZE]
        # print('new_P_T:', p0)
        # print('new_D_T:', d0)
        # print('lenth:', len(d0))
        if checkEqual(d0):
            print('early stop.')
            break

    return best_distance, best_route

def checkEqual(l):
    return len(set(l)) <= 1

def sort_population(population, distance):
    p = list(population)
    d = list(distance)
    p_size = len(d)
    for j in range(p_size):
        swapped = 0
        for i in range(1, p_size):
            if d[i] < d[i - 1]:
                d = swap(d, i, i - 1)
                p = swap(p, i, i - 1)
                swapped = 1
        if swapped == 0:
            break
    return p, d


def swap(d, i, j):
    val = d[i]
    d[i] = d[j]
    d[j] = val
    return d


def selection(p0, d0, POPULATION_SIZE, TOURNAMENT_SIZE):
    p = list(p0)
    d = list(d0)
    candidates = [1] * TOURNAMENT_SIZE
    f = [1] * TOURNAMENT_SIZE
    parents = [1] * 2
    # print(' selection begin1')
    for j in range(2):
        # print('for j',j)
        for i in range(TOURNAMENT_SIZE):
            # print('for i ',i)
            rand = random.randint(0, (POPULATION_SIZE - 1))
            candidates[i] = p[rand]
            # print('candidates ',i,':',candidates[i])
            f[i] = d[rand]
            # print('f ',i,':',f[i])
        idx = f.index(min(f))
        parents[j] = candidates[idx]
        # print('parents ',j,':',parents)
    count = 0
    while parents[0] == parents[1]:
        # print('while')
        # print('p:',p)
        for i in range(TOURNAMENT_SIZE):
            rand = random.randint(0, (POPULATION_SIZE - 1))
            # print('rand:',rand)
            candidates[i] = p[rand]
            # print('candidates ',i,':',candidates[i])
            f[i] = d[rand]
            # print('f ', i, ':', f[i])
        idx = f.index(min(f))
        parents[1] = candidates[idx]
        # print('parents new',parents[1])
        count += 1
        if count == 100:
            break

    p1 = parents[0]
    p2 = parents[1]
    return p1, p2


def crossover(p1, p2):
    num_cities = len(p1)
    c1 = [0] * num_cities
    c2 = [0] * num_cities
    c1[0] = p1[0]
    c2[0] = p2[0]
    c1[1] = p1[1]
    c2[1] = p2[1]

    # c1
    value1 = p2[1]
    idx1 = p1.index(value1)
    c1[idx1] = value1
    mapping_value1 = p2[idx1]
    while mapping_value1 not in c1:
        value1 = mapping_value1
        idx1 = p1.index(value1)
        c1[idx1] = value1
        mapping_value1 = p2[idx1]
    # print('c1:', c1)

    if 0 in c1:
        for i in range(1, num_cities):
            if c1[i] == 0:
                c1[i] = p2[i]

    value2 = p1[1]
    idx2 = p2.index(value2)
    c2[idx2] = value2
    mapping_value2 = p1[idx2]
    while mapping_value2 not in c2:
        value2 = mapping_value2
        idx2 = p2.index(value2)
        c2[idx2] = value2
        mapping_value2 = p1[idx2]

    if 0 in c2:
        for i in range(1, num_cities):
            if c2[i] == 0:
                c2[i] = p1[i]
    return c1,c2


def mutation(individual, mr):
    num_cities = len(individual)
    c = list(individual)
    for i in range(1, num_cities):
        if mr > random.random():
            idx = random.randint(1, (num_cities - 1))
            temp = c[i]
            c[i] = c[idx]
            c[idx] = temp
    return c

def rad(d):
    PI = math.pi
    return d * PI / 180


def geoDistance(solution):
    l = list(solution)
    num_cities = len(l)
    EARTH_RADIUS = 6378.137
    d = 0

    for i in range(num_cities):
        if i != (num_cities - 1):
            idx1 = l[i] - 1
            idx2 = l[i + 1] - 1
            radLat1 = rad(Lat[idx1])
            radLat2 = rad(Lat[idx2])
            a = radLat1 - radLat2
            b = rad(Long[idx1]) - rad(Long[idx2])
            s = 2 * math.asin(math.sqrt(
                math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))
            s = s * EARTH_RADIUS
            s = round(s * 10000) / 10000
            d += s
        else:
            idx1 = l[i] - 1
            idx2 = l[0] - 1
            radLat1 = rad(Lat[idx1])
            radLat2 = rad(Lat[idx2])
            a = radLat1 - radLat2
            b = rad(Long[idx1]) - rad(Long[idx2])
            s = 2 * math.asin(math.sqrt(
                math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))
            s = s * EARTH_RADIUS
            s = round(s * 10000) / 10000
            d += s
    d = round(d)
    return d


# x4 = [3, 2, 4, 5]
# x2 = [2, 3, 7, 9, 10, 26]
# x3 = [2, 7, 3, 26, 9, 10]
# x1 = [2, 3, 4, 7, 8, 10, 22, 25, 29, 31]
# evolutionaryAlg(x1)

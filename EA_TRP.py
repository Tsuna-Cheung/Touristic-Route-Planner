import random
import pandas as pd
import numpy as np
import math

# dataset about location of Chinese 33 cities
data = pd.read_csv('chinacity_33.csv')
dt = np.array(data)
Lat = np.array(data.iloc[:, 2]).tolist()
Long = np.array(data.iloc[:, 1]).tolist()

# dataset about travelling cost between Chinese 33 cities
data1 = pd.read_csv('moneycost_china33.csv')
dt1 = np.array(data1)


def ea_distance(cities):
    num_cities = len(cities)
    init_list = list(cities)
    POPULATION_SIZE = (num_cities - 1) * (num_cities - 2)
    if num_cities > 11:
        POPULATION_SIZE = 100
    OFFSPRING_SIZE = round(POPULATION_SIZE / 2)
    TOURNAMENT_SIZE = 2
    mr = 0.25
    iteration = 1
    max_iter = 1500

    # generate initial population
    p0 = [1] * POPULATION_SIZE
    d0 = [0] * POPULATION_SIZE
    for i in range(len(p0)):
        individual = list(init_list)
        temp = individual[1:]
        random.shuffle(temp)
        individual[1:] = temp
        p0[i] = list(individual)
        d0[i] = geoDistance(individual)

    # find minimum
    idx_sorted = sorted(range(len(d0)), key=lambda k: d0[k])
    best_idx = idx_sorted[0]

    # best route
    best_route = p0[best_idx]
    best_distance = d0[best_idx]

    print('iteration', iteration, '-----------Distance:', best_distance, '-----------Route:', best_route)

    while iteration < max_iter:
        iteration += 1
        p_t = p0
        d_t = d0

        # count for the number of offspring
        no_offspring = 0
        while no_offspring != OFFSPRING_SIZE:
            # selection
            [p1, p2] = selection(list(p0), list(d0), POPULATION_SIZE, TOURNAMENT_SIZE)
            # breeding
            [c1, c2] = crossover_cx(list(p1), list(p2))
            # mutation
            c1 = mutation_inversion(list(c1), mr)
            # evaluation
            d1 = geoDistance(c1)
            # adding the child into new population
            p_t.append(c1)
            d_t.append(d1)
            no_offspring += 1
            if no_offspring == OFFSPRING_SIZE:
                break
            else:
                c2 = mutation_inversion(list(c2), mr)
                d2 = geoDistance(c2)
                p_t.append(c2)
                d_t.append(d2)
                no_offspring += 1
        # Elitism
        [p_t, d_t] = sort_population(p_t, d_t)
        iter_best_route = p_t[0]
        iter_best_distance = d_t[0]
        if iter_best_distance < best_distance:
            best_distance = iter_best_distance
            best_route = iter_best_route
        print('iteration', iteration, '-----------Distance:', best_distance, '-----------Route:', best_route)

        # reproduction
        p0 = p_t[:POPULATION_SIZE]
        d0 = d_t[:POPULATION_SIZE]
        # if all individuals in population are same, then terminate iteration
        if checkEqual(d0):
            # print('early stop.')
            break

    return best_distance, best_route

def ea_cost(cities):
    num_cities = len(cities)
    init_list = list(cities)
    POPULATION_SIZE = (num_cities - 1) * (num_cities - 2)
    if num_cities > 11:
        POPULATION_SIZE = 100
    OFFSPRING_SIZE = round(POPULATION_SIZE / 2)
    TOURNAMENT_SIZE = 2
    mr = 0.25
    iteration = 1
    max_iter = 1500

    # generate initial population
    p0 = [1] * POPULATION_SIZE
    m0 = [0] * POPULATION_SIZE
    for i in range(len(p0)):
        individual = list(init_list)
        temp = individual[1:]
        random.shuffle(temp)
        individual[1:] = temp
        p0[i] = list(individual)
        m0[i] = moneyCost(individual)

    # find minimum
    idx_sorted = sorted(range(len(m0)), key=lambda k: m0[k])
    best_idx = idx_sorted[0]

    # best route
    best_route = p0[best_idx]
    best_moneycost = m0[best_idx]

    print('iteration', iteration, '-----------Cost:', best_moneycost, '-----------Route:', best_route)

    while iteration < max_iter:
        iteration += 1
        p_t = p0
        m_t = m0

        # count for the number of offspring
        no_offspring = 0
        while no_offspring != OFFSPRING_SIZE:
            # selection
            [p1, p2] = selection(list(p0), list(m0), POPULATION_SIZE, TOURNAMENT_SIZE)
            # breeding
            [c1, c2] = crossover_cx(list(p1), list(p2))
            # mutation
            c1 = mutation_inversion(list(c1), mr)
            # evaluation
            m1 = moneyCost(c1)
            # adding the child into new population
            p_t.append(c1)
            m_t.append(m1)
            no_offspring += 1
            if no_offspring == OFFSPRING_SIZE:
                break
            else:
                c2 = mutation_inversion(list(c2), mr)
                m2 = moneyCost(c2)
                p_t.append(c2)
                m_t.append(m2)
                no_offspring += 1
        # Elitism
        [p_t, m_t] = sort_population(p_t, m_t)
        iter_best_route = p_t[0]
        iter_best_moneycost = m_t[0]
        if iter_best_moneycost < best_moneycost:
            best_moneycost = iter_best_moneycost
            best_route = iter_best_route
        print('iteration', iteration, '-----------Cost:', best_moneycost, '-----------Route:', best_route)

        # reproduction
        p0 = p_t[:POPULATION_SIZE]
        m0 = m_t[:POPULATION_SIZE]
        # if all individuals in population are same, then terminate iteration
        if checkEqual(m0):
            # print('early stop.')
            break

    return best_moneycost, best_route

# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
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
    for j in range(2):
        for i in range(TOURNAMENT_SIZE):
            rand = random.randint(0, (POPULATION_SIZE - 1))
            candidates[i] = p[rand]
            f[i] = d[rand]
        idx = f.index(min(f))
        parents[j] = candidates[idx]
    count = 0
    while parents[0] == parents[1]:
        for i in range(TOURNAMENT_SIZE):
            rand = random.randint(0, (POPULATION_SIZE - 1))
            candidates[i] = p[rand]
            f[i] = d[rand]
        idx = f.index(min(f))
        parents[1] = candidates[idx]

        # if repeat tournament too much time, then break
        count += 1
        if count == 100:
            break

    p1 = parents[0]
    p2 = parents[1]
    return p1, p2


def crossover_pmx(p1, p2):
    num_cities = len(p1)
    c1 = [0] * num_cities
    c2 = [0] * num_cities
    a = random.randint(1, num_cities)
    b = random.randint(1, num_cities)
    while a == b:
        b = random.randint(1, num_cities)
    if a < b:
        cutpoint_a = a
        cutpoint_b = b
    else:
        cutpoint_a = b
        cutpoint_b = a

    c1[0] = p1[0]
    c2[0] = p2[0]
    c1[cutpoint_a:cutpoint_b] = p2[cutpoint_a:cutpoint_b]
    c2[cutpoint_a:cutpoint_b] = p1[cutpoint_a:cutpoint_b]
    for i in range(1, num_cities):
        if p1[i] not in c1 and c1[i] == 0:
            c1[i] = p1[i]
        if p2[i] not in c2 and c2[i] == 0:
            c2[i] = p2[i]
    if 0 in c1:
        for i in range(1, num_cities):
            if c1[i] == 0:
                shouldbe_value = p1[i]
                idx = p2.index(shouldbe_value)
                mapping_value = p1[idx]
                while mapping_value in c1:
                    shouldbe_value = mapping_value
                    idx = p2.index(shouldbe_value)
                    mapping_value = p1[idx]
                c1[i] = mapping_value
    if 0 in c2:
        for i in range(1, num_cities):
            if c2[i] == 0:
                shouldbe_value = p2[i]
                idx = p1.index(shouldbe_value)
                mapping_value = p2[idx]
                while mapping_value in c2:
                    shouldbe_value = mapping_value
                    idx = p1.index(shouldbe_value)
                    mapping_value = p2[idx]
                c2[i] = mapping_value
    return c1, c2


def crossover_ox(p1, p2):
    num_cities = len(p1)
    c1 = [0] * num_cities
    c2 = [0] * num_cities
    c1_tempA = []
    c1_tempB = []
    c2_tempA = []
    c2_tempB = []

    a = random.randint(1, num_cities)
    b = random.randint(1, num_cities)
    while a == b:
        b = random.randint(1, num_cities)
    if a < b:
        startPoint = a
        endPoint = b
    else:
        startPoint = b
        endPoint = a


    for i in range(startPoint, endPoint):
        c1_tempA.append(p1[i])
        c2_tempA.append(p2[i])

    for i in range(endPoint, num_cities):
        c1_tempB.append(p2[i])
        c2_tempB.append(p1[i])
    for i in range(1, endPoint):
        c1_tempB.append(p2[i])
        c2_tempB.append(p1[i])
    for item in c1_tempA:
        if item in c1_tempB:
            c1_tempB.remove(item)

    for item in c2_tempA:
        if item in c2_tempB:
            c2_tempB.remove(item)

    c1[startPoint:endPoint] = c1_tempA[:]
    c2[startPoint:endPoint] = c2_tempA[:]

    tail = num_cities - endPoint
    c1[endPoint:num_cities] = c1_tempB[0:tail]
    c2[endPoint:num_cities] = c2_tempB[0:tail]
    c1[1:startPoint] = c1_tempB[tail:]
    c2[1:startPoint] = c2_tempB[tail:]

    c1[0] = p1[0]
    c2[0] = p2[0]
    return c1, c2


def crossover_cx(p1, p2):
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

    if 0 in c1:
        for i in range(1, num_cities):
            if c1[i] == 0:
                c1[i] = p2[i]

    # c2
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
    return c1, c2


def mutation_inversion(individual, mr):
    num_cities = len(individual)
    c = list(individual)
    if mr > random.random():
        a = random.randint(1, num_cities)
        b = random.randint(1, num_cities)
        while a == b:
            b = random.randint(1, num_cities)
        if a < b:
            gen_a = a
            gen_b = b
        else:
            gen_a = b
            gen_b = a
        c_temp = c[gen_a:gen_b]
        c_temp = list(reversed(c_temp))
        c[gen_a:gen_b] = c_temp[:]
    return c


def mutation_scramble(individual, mr):
    num_cities = len(individual)
    c = list(individual)
    temp = []
    for i in range(1, num_cities):
        if mr > random.random():
            temp.append(c[i])
            c[i] = 0
    random.shuffle(temp)
    if 0 in c:
        for i in range(1, num_cities):
            if c[i] == 0:
                c[i] = temp[0]
                temp.remove(temp[0])
    return c


def mutation_swap(individual, mr):
    num_cities = len(individual)
    c = list(individual)
    for i in range(1, num_cities):
        if mr > random.random():
            idx = random.randint(1, (num_cities - 1))
            temp = c[i]
            c[i] = c[idx]
            c[idx] = temp
    return c

# https://blog.csdn.net/yl2isoft/article/details/16367901
def rad(d):
    PI = math.pi
    return d * PI / 180

# https://blog.csdn.net/yl2isoft/article/details/16367901
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

def moneyCost(solution):
    l = list(solution)
    lenth_solution = len(l)
    total_cost = 0
    # departure =  city_code -1 ，destination = city_code
    for i in range(lenth_solution):
        if i != (lenth_solution - 1):
            departure = l[i]
            destination = l[i + 1]
            cost = dt1[departure - 1][destination]
            total_cost += cost
        else:
            departure = l[i]
            destination = l[0]
            cost = dt1[departure - 1][destination]
            total_cost += cost
    return total_cost

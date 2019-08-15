import random
import pandas as pd
import numpy as np
import math

data1 = pd.read_csv('moneycost_china33.csv')
dt1 = np.array(data1)


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
    m0 = [0] * POPULATION_SIZE
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
        m0[i] = moneyCost(individual)
    # print('p0:', p0)
    # print('d0:', d0)

    # find minimum
    idx_sorted = sorted(range(len(m0)), key=lambda k: m0[k])
    # print('idx_sorted:', idx_sorted)
    # print('d0:', d0)
    best_idx = idx_sorted[0]

    # best route
    best_route = p0[best_idx]
    best_moneycost = m0[best_idx]
    # print('best_route:', best_route)
    # print('best_distance:', best_distance)

    while iteration < max_iter:
        iteration += 1
        p_t = p0
        m_t = m0
        # print('length of population__:',len(p_t))
        # print('new iteration begin')
        for i in range(OFFSPRING_SIZE):
            # print('selection begin')
            # selection
            [p1, p2] = selection(list(p0), list(m0), POPULATION_SIZE, TOURNAMENT_SIZE)
            # print('selection done')
            # variation
            child = crossover(list(p1), list(p2))
            # print('crossover done')
            # print('child:', child)
            child = mutation(list(child), mr)
            # print('muatation done')
            # evaluation
            m = moneyCost(child)
            p_t.append(child)
            m_t.append(m)
            # print('adding done')
            # print('length of population',i,':',len(p_t))
            # print(p_t)
        # print('p_t:', p_t)
        # print('d_t:', d_t)
        [p_t, m_t] = sort_population(p_t, m_t)
        # print('p_t_sorted:', p_t)
        # print('p_t_sorted:', d_t)
        # print('lenth:', len(d_t))
        iter_best_route = p_t[0]
        iter_best_moneycost = m_t[0]
        if iter_best_moneycost < best_moneycost:
            best_moneycost = iter_best_moneycost
            best_route = iter_best_route
        print('iteration', iteration, ':', best_moneycost, '-----------', best_route)
        # reproduction
        p0 = p_t[:POPULATION_SIZE]
        m0 = m_t[:POPULATION_SIZE]
        # print('new_P_T:', p0)
        # print('new_D_T:', d0)
        # print('lenth:', len(d0))
        if checkEqual(m0):
            print('early stop.')
            break

    return best_moneycost, best_route

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
    # print(num_cities)
    c = [1] * num_cities
    c_tempA = []
    c_tempB = []

    a = random.randint(1, num_cities)
    b = random.randint(1, num_cities)
    while a == b:
        b = random.randint(1, num_cities)
    # print('a: ',a)
    # print('b: ',b)
    if a < b:
        startPoint = a
        endPoint = b
    else:
        startPoint = b
        endPoint = a

    # print('start Point: ', startPoint)
    # print('end Point: ', endPoint)

    for i in range(startPoint, endPoint):
        c_tempA.append(p1[i])

    # print('c_tempA: ', c_tempA)
    for i in range(endPoint, num_cities):
        c_tempB.append(p2[i])
    # print('c_tempB_1: ', c_tempB)
    for i in range(1, endPoint):
        c_tempB.append(p2[i])
    # print('c_tempB_2: ', c_tempB)
    for item in c_tempA:
        if item in c_tempB:
            c_tempB.remove(item)
    # print('c_tempB_3: ', c_tempB)

    c[startPoint:endPoint] = c_tempA[:]
    # print('c1: ', c)
    tail = num_cities - endPoint
    c[endPoint:num_cities] = c_tempB[0:tail]
    # print('c2: ', c)
    c[1:startPoint] = c_tempB[tail:]
    # print('c: ', c)
    c[0] = p1[0]
    return c


def mutation(individual, mr):
    num_cities = len(individual)
    c = list(individual)
    for i in range(1, num_cities):
        if mr > random.random():
            idx = random.randint(1, (num_cities - 1))
            # print('idx:', idx)
            temp = c[i]
            c[i] = c[idx]
            c[idx] = temp
    # print('c2:', c)
    return c

def moneyCost(solution):
    l = list(solution)
    lenth_solution = len(l)
    total_cost = 0
    # departure =  city_code -1 ，destination= city_code
    for i in range(lenth_solution):
        if i != (lenth_solution - 1):
            departure = l[i]
            destination = l[i + 1]
            cost = dt1[departure - 1][destination]
            # print('cost:',cost)
            total_cost += cost
        else:
            departure = l[i]
            destination = l[0]
            cost = dt1[departure - 1][destination]
            # print('cost1:',cost)
            total_cost += cost
        # print('total_cost',total_cost)
    return total_cost



# x4 = [3, 2, 4, 5]
# x2 = [2, 3, 7, 9, 10, 26]
# x3 = [2, 7, 3, 26, 9, 10]
# x1 = [2, 3, 4, 7, 8, 10, 22, 25, 29, 31]
# evolutionaryAlg(x2)

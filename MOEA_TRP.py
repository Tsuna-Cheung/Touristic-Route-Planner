import random
import pandas as pd
import numpy as np
import math

data = pd.read_csv('chinacity_33.csv')
dt = np.array(data)
Lat = np.array(data.iloc[:, 2]).tolist()
Long = np.array(data.iloc[:, 1]).tolist()

data1 = pd.read_csv('moneycost_china33.csv')
dt1 = np.array(data1)


def evolutionaryAlg(cities):
    num_cities = len(cities)
    init_list = list(cities)
    POPULATION_SIZE = (num_cities - 1) * (num_cities - 2)
    print('POPULATION_SIZE:', POPULATION_SIZE)
    if num_cities > 11:
        POPULATION_SIZE = 100
    OFFSPRING_SIZE = round(POPULATION_SIZE / 2)
    mr = 0.5
    iteration = 0
    max_iter = 1500

    # generate initial population
    p0 = [1] * POPULATION_SIZE
    d0 = [0] * POPULATION_SIZE
    m0 = [0] * POPULATION_SIZE
    for i in range(POPULATION_SIZE):
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
        m0[i] = moneyCost(individual)

    best_solution = p0[0]
    best_moneycost = m0[0]
    best_distance = d0[0]

    while iteration < max_iter:
        print('------------', iteration, '------------')
        print('p0:', p0)
        print('d0:', d0)
        print('m0:', m0)
        # domniated sorting for selection
        [Fa, Fb, rank] = non_domninated_sorting(p0, d0, m0)
        # print('Fa:', Fa)
        # print('Fb:', Fb)
        # print('rank:', rank)
        cd = []
        # last front is empty list
        for i in range(len(Fa) - 1):
            cd_front = crowding_distance(d0, m0, Fa[i])
            cd.append(cd_front)
        # print('cd:', cd)

        for i in range(OFFSPRING_SIZE):
            [p1, p2] = selection(p0, rank, Fa, cd, POPULATION_SIZE)
            child = crossover(p1, p2)
            child = mutation(child, mr)
            d = geoDistance(child)
            m = moneyCost(child)
            p0.append(child)
            d0.append(d)
            m0.append(m)
        # print('p0:', p0)
        # print('d0:', d0)
        # print('m0:', m0)
        [F1, F2, rank1] = non_domninated_sorting(p0, d0, m0)
        # print('F1:', F1)
        # print('F2:', F2)
        # print('rank1:', rank1)
        idx = 0
        p_t = []
        d_t = []
        m_t = []
        while len(p_t) + len(F1[idx]) <= POPULATION_SIZE:
            p_t = p_t + F2[idx]
            d_temp = adding_to_list(d0, F1[idx])
            d_t = d_t + d_temp
            m_temp = adding_to_list(m0, F1[idx])
            m_t = m_t + m_temp
            idx += 1
            # print('p_t:', p_t)
            # print('d_t:', d_t)
            # print('m_t:', m_t)
        remain_len = POPULATION_SIZE - len(p_t)
        # print('remain_len:', remain_len)
        if remain_len > 0:
            cd_last_front = crowding_distance(d0, m0, F1[idx])
            # print('last front:',F1[idx])
            # print('cd_last_front:',cd_last_front)
            last_front_sorted = sort_front_by_crowding_distance(F1[idx], cd_last_front)
            # print('last_front_sorted:',last_front_sorted)
            for i in range(remain_len):
                p_t.append(p0[last_front_sorted[i]])
                d_t.append(d0[last_front_sorted[i]])
                m_t.append(m0[last_front_sorted[i]])
            # print('p_t:', p_t)
            # print('d_t:', d_t)
            # print('m_t:', m_t)
        p0 = p_t
        d0 = d_t
        m0 = m_t
        best_solution = p0[0]
        best_moneycost = m0[0]
        best_distance = d0[0]
        print('best solution is:', best_solution, '--------------distance:', best_distance, '------------cost:', best_moneycost,'---------------')
        print('p0:', p0)
        print('d0:', d0)
        print('m0:', m0)
        if checkEqual(m0) or checkEqual(d0):
            print('early stop.')
            break
        iteration += 1

    return best_solution,best_distance,best_moneycost


def checkEqual(l):
    return len(set(l)) <= 1


def adding_to_list(objective, front):
    f = list(front)
    f_size = len(f)
    v = list(objective)
    l = [0] * f_size
    for i in range(f_size):
        l[i] = v[f[i]]
    return l


def non_domninated_sorting(population, distance, moneyCost):
    p = list(population)
    d = list(distance)
    m = list(moneyCost)
    population_size = len(p)
    # i 支配的个体集合
    s1 = [[] for _ in range(population_size)]
    s2 = [[] for _ in range(population_size)]
    # i 被支配的个体数
    n = [0] * population_size
    rank = [0] * population_size

    front = 0
    # index of front
    F1 = [[]]
    # chromosome of front
    F2 = [[]]

    for i in range(population_size):
        for j in range(population_size):
            dom_less = 0
            dom_equal = 0
            dom_more = 0
            if i != j:
                if d[i] < d[j]:
                    dom_less += 1
                elif d[i] == d[j]:
                    dom_equal += 1
                elif d[i] > d[j]:
                    dom_more += 1

                if m[i] < m[j]:
                    dom_less += 1
                elif m[i] == m[j]:
                    dom_equal += 1
                elif m[i] > m[j]:
                    dom_more += 1
                # print(i,'-------',j)
                # print('less',dom_less)
                # print('equal',dom_equal)
                # print('more',dom_more)
                # i dominites j
                if dom_more == 0 and dom_equal != 2:
                    if j not in s1[i]:
                        s1[i].append(j)
                        s2[i].append(p[j])
                # j dominites i
                if dom_less == 0 and dom_equal != 2:
                    n[i] += 1

        # print('s1',s1)
        # print('s2',s2)
        # print('n',n)

        if n[i] == 0:
            if i not in F1[front]:
                rank[i] = 0
                F1[front].append(i)
                F2[front].append(p[i])

    while (F1[front] != []):
        Q1 = []
        Q2 = []
        for i in F1[front]:
            for j in s1[i]:
                n[j] = n[j] - 1
                if n[j] == 0:
                    rank[j] = front + 1
                    Q1.append(j)
                    Q2.append(p[j])
        front += 1
        F1.append(Q1)
        F2.append(Q2)

    return F1, F2, rank


def crowding_distance(distance, moneyCost, F):
    lenth_front = len(F)
    # print('lenth of f', lenth_front)
    cd = [0] * lenth_front
    d = list(distance)
    m = list(moneyCost)
    f = list(F)
    if lenth_front < 3:
        for i in range(lenth_front):
            cd[i] = float('inf')
        # print('break')
        return cd

    f_sorted_by_d = sort_front(f, d)
    f_sorted_by_m = sort_front(f, m)
    # print('f_sorted_by_d:', f_sorted_by_d)
    # print('f_sorted_by_m:', f_sorted_by_m)
    cd[0] = 4444444444444444
    cd[lenth_front - 1] = 4444444444444444
    for i in range(1, lenth_front - 1):
        cd[i] = cd[i] + (d[f_sorted_by_d[i + 1]] - d[f_sorted_by_d[i - 1]]) / (max(d) - min(d))
    for i in range(1, lenth_front - 1):
        cd[i] = cd[i] + (m[f_sorted_by_m[i + 1]] - m[f_sorted_by_m[i - 1]]) / (max(m) - min(m))
    return cd


def sort_front(front, objective):
    f = list(front)
    v = list(objective)
    f_size = len(f)
    f_v = [0] * f_size
    for i in range(f_size):
        f_v[i] = v[f[i]]
    # print('f_v1:',f_v)
    # print('f1:',f)

    for j in range(f_size):
        swapped = 0
        for i in range(1, f_size):
            if f_v[i] < f_v[i - 1]:
                f = swap(f, i, i - 1)
                f_v = swap(f_v, i, i - 1)
                swapped = 1
                # print('swap')
        if swapped == 0:
            break
    # print('f_v2:',f_v)
    # print('f2:',f)
    return f


def sort_front_by_crowding_distance(front, crowding_distance):
    f = list(front)
    cd = list(crowding_distance)
    f_size = len(f)

    for j in range(f_size):
        swapped = 0
        for i in range(1, f_size):
            if cd[i] > cd[i - 1]:
                f = swap(f, i, i - 1)
                cd = swap(cd, i, i - 1)
                swapped = 1
                # print('swap')
        if swapped == 0:
            break
    # print('f_v2:',f_v)
    # print('f2:',f)
    return f


def swap(d, i, j):
    val = d[i]
    d[i] = d[j]
    d[j] = val
    return d


def selection(p0, rank, Fr, crowding_distance, POPULATION_SIZE):
    p = list(p0)
    r = list(rank)
    cd = list(crowding_distance)
    f = list(Fr)
    parents = [0] * 2
    for i in range(2):
        rand_a = random.randint(0, (POPULATION_SIZE - 1))
        rand_b = random.randint(0, (POPULATION_SIZE - 1))
        while rand_a == rand_b:
            rand_b = random.randint(0, (POPULATION_SIZE - 1))
            # print('while')
        if r[rand_a] < r[rand_b]:
            parents[i] = p[rand_a]

        elif r[rand_a] > r[rand_b]:
            parents[i] = p[rand_b]

        elif r[rand_a] == r[rand_b]:
            front = r[rand_a]
            # print('front:',front)
            idx1 = get_index_from_front(rand_a, f[front])
            # print('idx1:',idx1)
            idx2 = get_index_from_front(rand_b, f[front])
            # print('idx2:',idx2)
            if cd[front][idx1] >= cd[front][idx2]:
                parents[i] = p[rand_a]
            else:
                parents[i] = p[rand_b]
        # print('parent', i, ':', parents[i])
    # print('parents:', parents)
    p1 = parents[0]
    p2 = parents[1]
    return p1, p2


def get_index_from_front(idx, front):
    # print('index:',idx)
    # print('the front:',front)
    for i in range(len(front)):
        if front[i] == idx:
            return i


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
            # print('idx1:', idx1)
            idx2 = l[i + 1] - 1
            # print('idx2:', idx2)
            radLat1 = rad(Lat[idx1])
            # print('Lat1:', Lat[idx1])
            radLat2 = rad(Lat[idx2])
            # print('Lat2:', Lat[idx2])
            a = radLat1 - radLat2
            b = rad(Long[idx1]) - rad(Long[idx2])
            s = 2 * math.asin(math.sqrt(
                math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))
            s = s * EARTH_RADIUS
            s = round(s * 10000) / 10000
            # print('s:', s)
            d += s
        else:
            idx1 = l[i] - 1
            idx2 = l[0] - 1
            radLat1 = rad(Lat[idx1])
            # print('Lat1:', Lat[idx1])
            radLat2 = rad(Lat[idx2])
            # print('Lat2:', Lat[idx2])
            a = radLat1 - radLat2
            b = rad(Long[idx1]) - rad(Long[idx2])
            s = 2 * math.asin(math.sqrt(
                math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))
            s = s * EARTH_RADIUS
            s = round(s * 10000) / 10000
            # print('s1:', s)
            d += s
    d = round(d)
    # print('d:', d)
    return d


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
# x3 = [2, 8, 3, 26, 9, 10]
# x1 = [2, 3, 4, 7, 8, 10, 22, 25,29,31]
# evolutionaryAlg(x3)

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
    mr = 0.25
    iteration = 0
    max_iter = 1500

    # generate initial population
    p0 = [1] * POPULATION_SIZE
    d0 = [0] * POPULATION_SIZE
    m0 = [0] * POPULATION_SIZE
    for i in range(POPULATION_SIZE):
        individual = list(init_list)
        temp = individual[1:]
        random.shuffle(temp)
        individual[1:] = temp
        p0[i] = list(individual)
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
        cd = []
        # last front is empty list
        for i in range(len(Fa) - 1):
            cd_front = crowding_distance(d0, m0, Fa[i])
            cd.append(cd_front)

        no_offspring = 0
        while no_offspring != OFFSPRING_SIZE:
            # selection
            [p1, p2] = selection(p0, rank, Fa, cd, POPULATION_SIZE)
            # breeding
            [c1, c2] = crossover_ox(list(p1), list(p2))
            # mutation
            c1 = mutation_inversion(list(c1), mr)
            # evaluation
            m1 = moneyCost(c1)
            d1 = geoDistance(c1)
            # adding the child into new population
            p0.append(c1)
            m0.append(m1)
            d0.append(d1)
            no_offspring += 1
            if no_offspring == OFFSPRING_SIZE:
                break
            else:
                c2 = mutation_inversion(list(c2), mr)
                m2 = moneyCost(c2)
                d2 = geoDistance(c2)
                p0.append(c2)
                m0.append(m2)
                d0.append(d2)
                no_offspring += 1
        [F1, F2, rank1] = non_domninated_sorting(p0, d0, m0)
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
        remain_len = POPULATION_SIZE - len(p_t)
        if remain_len > 0:
            cd_last_front = crowding_distance(d0, m0, F1[idx])
            last_front_sorted = sort_front_by_crowding_distance(F1[idx], cd_last_front)
            for i in range(remain_len):
                p_t.append(p0[last_front_sorted[i]])
                d_t.append(d0[last_front_sorted[i]])
                m_t.append(m0[last_front_sorted[i]])
        p0 = p_t
        d0 = d_t
        m0 = m_t
        best_solution = p0[0]
        best_moneycost = m0[0]
        best_distance = d0[0]
        # print('best solution is:', best_solution, '--------------distance:', best_distance, '------------cost:', best_moneycost,'---------------')
        # print('p0:', p0)
        # print('d0:', d0)
        # print('m0:', m0)
        if checkEqual(m0) or checkEqual(d0):
            print('early stop.')
            break
        iteration += 1

    return best_solution,best_distance,best_moneycost

# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
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
    # the set dominated by i
    s1 = [[] for _ in range(population_size)]
    s2 = [[] for _ in range(population_size)]
    # number of individual that dominate i
    n = [0] * population_size
    rank = [0] * population_size

    front = 0
    # index of front
    F1 = [[]]
    # chromosome of front
    F2 = [[]]
    # https://blog.csdn.net/joekepler/article/details/80820240
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
                # i dominites j
                if dom_more == 0 and dom_equal != 2:
                    if j not in s1[i]:
                        s1[i].append(j)
                        s2[i].append(p[j])
                # j dominites i
                if dom_less == 0 and dom_equal != 2:
                    n[i] += 1

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

# https://github.com/haris989/NSGA-II/blob/master/NSGA%20II.py
def crowding_distance(distance, moneyCost, F):
    lenth_front = len(F)
    cd = [0] * lenth_front
    d = list(distance)
    m = list(moneyCost)
    f = list(F)
    # if the number of individual in the front less than 3, then set both crowding distance to infinity
    if lenth_front < 3:
        for i in range(lenth_front):
            cd[i] = float('inf')
        return cd

    f_sorted_by_d = sort_front(f, d)
    f_sorted_by_m = sort_front(f, m)
    # infinite large number
    cd[0] = 666666666666666
    cd[lenth_front - 1] = 666666666666666
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

    for j in range(f_size):
        swapped = 0
        for i in range(1, f_size):
            if f_v[i] < f_v[i - 1]:
                f = swap(f, i, i - 1)
                f_v = swap(f_v, i, i - 1)
                swapped = 1
        if swapped == 0:
            break
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
        if swapped == 0:
            break
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
        if r[rand_a] < r[rand_b]:
            parents[i] = p[rand_a]

        elif r[rand_a] > r[rand_b]:
            parents[i] = p[rand_b]

        elif r[rand_a] == r[rand_b]:
            front = r[rand_a]
            idx1 = get_index_from_front(rand_a, f[front])
            idx2 = get_index_from_front(rand_b, f[front])
            if cd[front][idx1] >= cd[front][idx2]:
                parents[i] = p[rand_a]
            else:
                parents[i] = p[rand_b]
    p1 = parents[0]
    p2 = parents[1]
    return p1, p2


def get_index_from_front(idx, front):
    for i in range(len(front)):
        if front[i] == idx:
            return i


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
    # print(num_cities)
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
        # print('c1:', c1)

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
            # print('s:', s)
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
    # departure =  city_code -1 ，destination= city_code
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

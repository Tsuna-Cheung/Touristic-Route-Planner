import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

data = pd.read_csv('chinacity_33.csv')
dt = np.array(data)
Lat = np.array(data.iloc[:, 2]).tolist()
Long = np.array(data.iloc[:, 1]).tolist()


def evolutionaryAlg1(cities):
    num_cities = len(cities)
    init_list = list(cities)
    POPULATION_SIZE = (num_cities - 1) * (num_cities - 2)
    if num_cities > 11:
        POPULATION_SIZE = 100
    OFFSPRING_SIZE = round(POPULATION_SIZE / 2)
    # print('OFFSPRING_SIZE:',OFFSPRING_SIZE)
    TOURNAMENT_SIZE = 2
    mr = 0.25
    iteration = 1
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
        d0[i] = geoDistance(individual)

    # find minimum
    idx_sorted = sorted(range(len(d0)), key=lambda k: d0[k])
    # print('idx_sorted:', idx_sorted)
    # print('d0:', d0)
    best_idx = idx_sorted[0]

    # best route
    best_route = p0[best_idx]
    best_distance = d0[best_idx]

    d_result = []
    d_result.append(best_distance)
    print('iteration', iteration, ':', best_distance, '-----------', best_route)

    while iteration < max_iter:
        iteration += 1
        p_t = p0
        d_t = d0
        no_offspring = 0
        while no_offspring != OFFSPRING_SIZE:
            # print('selection begin')
            # selection
            [p1, p2] = selection(list(p0), list(d0), POPULATION_SIZE, TOURNAMENT_SIZE)
            # print('selection done')
            # variation
            [c1, c2] = crossover_cx(list(p1), list(p2))
            # print('crossover done')
            # print('child:', child)
            c1 = mutation_inversion(list(c1), mr)
            d1 = geoDistance(c1)
            p_t.append(c1)
            d_t.append(d1)
            no_offspring += 1
            # print('no_offspring:',no_offspring)
            # print('size of generation:',len(p_t))

            if no_offspring == OFFSPRING_SIZE:
                break
            else:
                c2 = mutation_swap(list(c2), mr)
                d2 = geoDistance(c2)
                p_t.append(c2)
                d_t.append(d2)
                no_offspring += 1
                # print('no_offspring_:',no_offspring)

                # print('size of generation:',len(p_t))
        [p_t, d_t] = sort_population(p_t, d_t)
        iter_best_route = p_t[0]
        iter_best_distance = d_t[0]
        if iter_best_distance < best_distance:
            best_distance = iter_best_distance
            best_route = iter_best_route
        d_result.append(best_distance)
        print('iteration', iteration, ':', best_distance, '-----------', best_route)
        # reproduction
        p0 = p_t[:POPULATION_SIZE]
        d0 = d_t[:POPULATION_SIZE]
        # print('new_P_T:', p0)
        # print('new_D_T:', d0)
        # print('lenth:', len(d0))
        # if checkEqual(d0):
        #     print('early stop.')
        #     break
    # plot_fig(d_result,iteration)
    return d_result


def evolutionaryAlg2(cities):
    num_cities = len(cities)
    init_list = list(cities)
    POPULATION_SIZE = (num_cities - 1) * (num_cities - 2)
    if num_cities > 11:
        POPULATION_SIZE = 100
    OFFSPRING_SIZE = round(POPULATION_SIZE / 2)
    # print('OFFSPRING_SIZE:',OFFSPRING_SIZE)
    TOURNAMENT_SIZE = 2
    mr = 0.5
    iteration = 1
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
        d0[i] = geoDistance(individual)

    # find minimum
    idx_sorted = sorted(range(len(d0)), key=lambda k: d0[k])
    # print('idx_sorted:', idx_sorted)
    # print('d0:', d0)
    best_idx = idx_sorted[0]

    # best route
    best_route = p0[best_idx]
    best_distance = d0[best_idx]

    d_result = []
    d_result.append(best_distance)
    print('iteration', iteration, ':', best_distance, '-----------', best_route)

    while iteration < max_iter:
        iteration += 1
        p_t = p0
        d_t = d0
        no_offspring = 0
        while no_offspring != OFFSPRING_SIZE:
            # print('selection begin')
            # selection
            [p1, p2] = selection(list(p0), list(d0), POPULATION_SIZE, TOURNAMENT_SIZE)
            # print('selection done')
            # variation
            [c1, c2] = crossover_cx(list(p1), list(p2))
            # print('crossover done')
            # print('child:', child)
            c1 = mutation_inversion(list(c1), mr)
            d1 = geoDistance(c1)
            p_t.append(c1)
            d_t.append(d1)
            no_offspring += 1
            # print('no_offspring:',no_offspring)
            # print('size of generation:',len(p_t))

            if no_offspring == OFFSPRING_SIZE:
                break
            else:
                c2 = mutation_swap(list(c2), mr)
                d2 = geoDistance(c2)
                p_t.append(c2)
                d_t.append(d2)
                no_offspring += 1
                # print('no_offspring_:',no_offspring)

                # print('size of generation:',len(p_t))
        [p_t, d_t] = sort_population(p_t, d_t)
        iter_best_route = p_t[0]
        iter_best_distance = d_t[0]
        if iter_best_distance < best_distance:
            best_distance = iter_best_distance
            best_route = iter_best_route
        d_result.append(best_distance)
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
    # plot_fig(d_result,iteration)
    return d_result


def evolutionaryAlg3(cities):
    num_cities = len(cities)
    init_list = list(cities)
    POPULATION_SIZE = (num_cities - 1) * (num_cities - 2)
    if num_cities > 11:
        POPULATION_SIZE = 100
    OFFSPRING_SIZE = round(POPULATION_SIZE / 2)
    # print('OFFSPRING_SIZE:',OFFSPRING_SIZE)
    TOURNAMENT_SIZE = 2
    mr = 0.75
    iteration = 1
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
        d0[i] = geoDistance(individual)

    # find minimum
    idx_sorted = sorted(range(len(d0)), key=lambda k: d0[k])
    # print('idx_sorted:', idx_sorted)
    # print('d0:', d0)
    best_idx = idx_sorted[0]

    # best route
    best_route = p0[best_idx]
    best_distance = d0[best_idx]

    d_result = []
    d_result.append(best_distance)
    print('iteration', iteration, ':', best_distance, '-----------', best_route)

    while iteration < max_iter:
        iteration += 1
        p_t = p0
        d_t = d0
        no_offspring = 0
        while no_offspring != OFFSPRING_SIZE:
            # print('selection begin')
            # selection
            [p1, p2] = selection(list(p0), list(d0), POPULATION_SIZE, TOURNAMENT_SIZE)
            # print('selection done')
            # variation
            [c1, c2] = crossover_cx(list(p1), list(p2))
            # print('crossover done')
            # print('child:', child)
            c1 = mutation_inversion(list(c1), mr)
            d1 = geoDistance(c1)
            p_t.append(c1)
            d_t.append(d1)
            no_offspring += 1
            # print('no_offspring:',no_offspring)
            # print('size of generation:',len(p_t))

            if no_offspring == OFFSPRING_SIZE:
                break
            else:
                c2 = mutation_swap(list(c2), mr)
                d2 = geoDistance(c2)
                p_t.append(c2)
                d_t.append(d2)
                no_offspring += 1
                # print('no_offspring_:',no_offspring)

                # print('size of generation:',len(p_t))
        [p_t, d_t] = sort_population(p_t, d_t)
        iter_best_route = p_t[0]
        iter_best_distance = d_t[0]
        if iter_best_distance < best_distance:
            best_distance = iter_best_distance
            best_route = iter_best_route
        d_result.append(best_distance)
        print('iteration', iteration, ':', best_distance, '-----------', best_route)
        # reproduction
        p0 = p_t[:POPULATION_SIZE]
        d0 = d_t[:POPULATION_SIZE]
        # print('new_P_T:', p0)
        # print('new_D_T:', d0)
        # print('lenth:', len(d0))
        # if checkEqual(d0):
        #     print('early stop.')
        #     break
    # plot_fig(d_result,iteration)
    return d_result


def plot_fig(result1, result2, result3, iteration, no_ex):
    y1 = list(result1)
    y2 = list(result2)
    y3 = list(result3)
    # print('len of y:',len(y))
    x = [i for i in range(iteration)]
    # print('len of x:',len(x))
    plt.figure(figsize=(16, 8))
    plt.plot(x, y1, "b--", linewidth=1, label='0.25')
    plt.plot(x, y2, "r--", linewidth=1, label='0.5')
    plt.plot(x, y3, "g--", linewidth=1, label='0.75')
    plt.legend()
    plt.xlabel("iteration")
    plt.ylabel("Distance(km)")
    plt.title("mutation rate")
    # plt.show()
    fn = 'mutation_rate' + str(no_ex) + '.jpg'
    plt.savefig(fn)


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


def crossover_pmx(p1, p2):
    num_cities = len(p1)
    c1 = [0] * num_cities
    c2 = [0] * num_cities
    a = random.randint(1, num_cities)
    b = random.randint(1, num_cities)
    while a == b:
        b = random.randint(1, num_cities)
    # print('a: ',a)
    # print('b: ',b)
    if a < b:
        cutpoint_a = a
        cutpoint_b = b
    else:
        cutpoint_a = b
        cutpoint_b = a

    # print('cutpoint_a:',cutpoint_a)
    # print('cutpoint_b:',cutpoint_b)
    c1[0] = p1[0]
    c2[0] = p2[0]
    c1[cutpoint_a:cutpoint_b] = p2[cutpoint_a:cutpoint_b]
    c2[cutpoint_a:cutpoint_b] = p1[cutpoint_a:cutpoint_b]
    # print('c1_:',c1)
    # print('c2_:',c2)
    for i in range(1, num_cities):
        if p1[i] not in c1 and c1[i] == 0:
            c1[i] = p1[i]
            # print('c1:',c1)
        if p2[i] not in c2 and c2[i] == 0:
            c2[i] = p2[i]
            # print('c2:',c2)
    if 0 in c1:
        # print('---------c2----------')
        for i in range(1, num_cities):
            if c1[i] == 0:
                shouldbe_value = p1[i]
                idx = p2.index(shouldbe_value)
                mapping_value = p1[idx]
                # print('mapping value:',mapping_value)
                while mapping_value in c1:
                    shouldbe_value = mapping_value
                    idx = p2.index(shouldbe_value)
                    mapping_value = p1[idx]
                    # print('mapping value:',mapping_value)
                c1[i] = mapping_value
    # print('c1:',c1)
    if 0 in c2:
        # print('---------c2----------')
        for i in range(1, num_cities):
            if c2[i] == 0:
                shouldbe_value = p2[i]
                idx = p1.index(shouldbe_value)
                mapping_value = p2[idx]
                # print('mapping value:',mapping_value)
                while mapping_value in c2:
                    shouldbe_value = mapping_value
                    idx = p1.index(shouldbe_value)
                    mapping_value = p2[idx]
                    # print('mapping value:',mapping_value)
                c2[i] = mapping_value
    # print('c2:',c2)
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
        c1_tempA.append(p1[i])
        c2_tempA.append(p2[i])

    # print('c1_tempA: ', c1_tempA)
    # print('c2_tempA: ', c2_tempA)
    for i in range(endPoint, num_cities):
        c1_tempB.append(p2[i])
        c2_tempB.append(p1[i])
    # print('c1_tempB_1: ', c1_tempB)
    # print('c2_tempB_1: ', c2_tempB)
    for i in range(1, endPoint):
        c1_tempB.append(p2[i])
        c2_tempB.append(p1[i])
    # print('c1_tempB_2: ', c1_tempB)
    # print('c2_tempB_2: ', c2_tempB)
    for item in c1_tempA:
        if item in c1_tempB:
            c1_tempB.remove(item)
    # print('c1_tempB_3: ', c1_tempB)

    for item in c2_tempA:
        if item in c2_tempB:
            c2_tempB.remove(item)
    # print('c2_tempB_3: ', c2_tempB)

    c1[startPoint:endPoint] = c1_tempA[:]
    c2[startPoint:endPoint] = c2_tempA[:]
    # print('c1: ', c1)
    # print('c2: ', c2)
    # print('---------')
    tail = num_cities - endPoint
    c1[endPoint:num_cities] = c1_tempB[0:tail]
    c2[endPoint:num_cities] = c2_tempB[0:tail]
    # print('c1: ', c1)
    # print('c2: ', c2)
    # print('---------')
    c1[1:startPoint] = c1_tempB[tail:]
    c2[1:startPoint] = c2_tempB[tail:]
    # print('c1: ', c1)
    # print('c2: ', c2)
    # print('---------')
    c1[0] = p1[0]
    c2[0] = p2[0]
    return c1, c2
    # print('c1: ', c1)
    # print('c2: ', c2)


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
    # print('c1:', c1)

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
    # print('c2:', c2)

    if 0 in c2:
        for i in range(1, num_cities):
            if c2[i] == 0:
                c2[i] = p1[i]
        # print('c2:', c2)
    return c1, c2


def mutation_inversion(individual, mr):
    num_cities = len(individual)
    c = list(individual)
    # print('c_:',c)
    if mr > random.random():
        # print('---------------')
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
        # print('gen_a:',gen_a)
        # print('gen_b:',gen_b)
        c_temp = c[gen_a:gen_b]
        c_temp = list(reversed(c_temp))
        c[gen_a:gen_b] = c_temp[:]
        # print('c:',c)
    return c


def mutation_scramble(individual, mr):
    num_cities = len(individual)
    c = list(individual)
    # print('c:',c)
    temp = []
    for i in range(1, num_cities):
        if mr > random.random():
            # print('take out',c[i])
            temp.append(c[i])
            c[i] = 0
            # print('temp:',temp)
            # print('c_:',c)
    random.shuffle(temp)
    # print('shuffle temp:',temp)
    if 0 in c:
        for i in range(1, num_cities):
            if c[i] == 0:
                c[i] = temp[0]
                temp.remove(temp[0])
    # print('final c:',c)
    return c


def mutation_swap(individual, mr):
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


def main(city):
    for i in range(10):
        result1 = evolutionaryAlg1(list(city))
        result2 = evolutionaryAlg2(list(city))
        result3 = evolutionaryAlg3(list(city))
        plot_fig(result1, result2, result3, 1500, i)


# x1 = [3, 5, 2, 1, 8, 9]
x2 = [3, 4, 8, 2, 7, 1, 6, 5, 11, 13, 15, 17, 18, 19, 23, 24, 27, 29, 30]
# x3 = [3, 2, 5, 1, 6, 8, 4, 7,9,10]
# x4 = [i for i in range(32)]
main(x2)

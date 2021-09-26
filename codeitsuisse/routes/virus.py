import logging
import json
import copy

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def evaluateProblems():
    data = request.get_json('[...]')
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for case in data:
        temp = {}
        room = case.get("room")
        temp.update({"room": room})
        interested_individual = case.get("interestedIndividuals")
        grid = case.get("grid")
        p1 = part1(grid, interested_individual)
        temp.update({"p1": p1})
        p2 = part2(grid)
        temp.update({"p2": p2})
        p3 = part3(grid)
        temp.update({"p3": p3})
        p4 = part4(grid)
        temp.update({"p4": p4})
        result.append(temp)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def part1(grid, coordinates):
    solution = {}
    for coor in coordinates:
        time = 0
        x = int(coor.split(",")[0])
        y = int(coor.split(",")[1])
        if (grid[x][y] == 0 or grid[x][y] == 2 or grid[x][y] == 3):
            time = -1
            solution.update({coor: time})
        else:
            time = steps(grid, (x, y))
            solution.update({coor: time})
    return solution

def steps(grid, target):
    new_grid = copy.deepcopy(grid)
    old_grid = copy.deepcopy(grid)
    path = 0
    new_infected = 1
    while (new_infected != 0):
        new_infected = 0
        for x in range(len(old_grid)):
            for y in range(len(old_grid[0])):
                if (old_grid[x][y] == 1):
                    if (x - 1 >= 0):
                        if (old_grid[x - 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x + 1 < len(old_grid)):
                        if (old_grid[x + 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y - 1 >= 0):
                        if (old_grid[x][y - 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y + 1 < len(old_grid[0])):
                        if (old_grid[x][y + 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break

        path += 1
        old_grid = copy.deepcopy(new_grid)

        if (new_grid[target[0]][target[1]] == 3):
            return path

    return -1

def part2(grid):
    new_grid = copy.deepcopy(grid)
    old_grid = copy.deepcopy(grid)
    time = 0
    new_infected = 0
    while (True):
        new_infected = 0
        for x in range(len(old_grid)):
            for y in range(len(old_grid[0])):
                if (old_grid[x][y] == 1):
                    if (x - 1 >= 0):
                        if (old_grid[x - 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x + 1 < len(old_grid)):
                        if (old_grid[x + 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y - 1 >= 0):
                        if (old_grid[x][y - 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y + 1 < len(old_grid[0])):
                        if (old_grid[x][y + 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break

        time += 1

        if (new_infected == 0):
            for m in range(len(old_grid)):
                for n in range(len(old_grid[0])):
                    if (new_grid[m][n] == 1):
                        return -1
            return time - 1

        old_grid = copy.deepcopy(new_grid)

def part3(grid):
    """new_grid = copy.deepcopy(grid)
    old_grid = copy.deepcopy(grid)
    time = 0
    new_infected = 0
    while (True):
        new_infected = 0
        for x in range(len(old_grid)):
            for y in range(len(old_grid[0])):
                if (old_grid[x][y] == 1):
                    if (x - 1 >= 0):
                        if (old_grid[x - 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x + 1 < len(old_grid)):
                        if (old_grid[x + 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y - 1 >= 0):
                        if (old_grid[x][y - 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y + 1 < len(old_grid[0])):
                        if (old_grid[x][y + 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x - 1 >= 0 and y - 1 >= 0):
                        if (old_grid[x - 1][y - 1]):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x - 1 >= 0 and y + 1 < len(old_grid[0])):
                        if (old_grid[x - 1][y + 1]):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x + 1 < len(old_grid) and y - 1 >= 0):
                        if (old_grid[x + 1][y - 1]):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x + 1 < len(old_grid) and y + 1 < len(old_grid[0])):
                        if (old_grid[x + 1][y - 1]):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break

        time += 1

        if (new_infected == 0):
            for m in range(len(old_grid)):
                for n in range(len(old_grid[0])):
                    if (new_grid[m][n] == 1):
                        return -1
            return time - 1

        old_grid = copy.deepcopy(new_grid)"""
        return 0

def part4(grid):
    return 0
    """new_g = infected_grid(grid)
    print(new_g)
    infected = []
    healthy = []
    nrg = 0
    min = 100
    temp = 0
    for x in range(len(new_g)):
        for y in range(len(new_g[0])):
            if (new_g[x][y] == 3):
                infected.append([x, y])
            if (new_g[x][y] == 1):
                healthy.append([x, y])
    for i in healthy:
        for j in infected:
            temp = abs(j[0] - i[0]) + abs(j[1] - i[1]) - 1
            if temp < min:
                min = temp
            temp = 0
        nrg += min
        min = 100
    return nrg"""

def infected_grid(grid):
    new_grid = copy.deepcopy(grid)
    old_grid = copy.deepcopy(grid)
    new_infected = 0
    while (True):
        new_infected = 0
        for x in range(len(old_grid)):
            for y in range(len(old_grid[0])):
                if (old_grid[x][y] == 1):
                    if (x - 1 >= 0):
                        if (old_grid[x - 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (x + 1 < len(old_grid)):
                        if (old_grid[x + 1][y] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y - 1 >= 0):
                        if (old_grid[x][y - 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break
                    if (y + 1 < len(old_grid[0])):
                        if (old_grid[x][y + 1] == 3):
                            new_grid[x][y] = 3
                            new_infected += 1
                            break

        if (new_infected == 0):
            return new_grid

        old_grid = copy.deepcopy(new_grid)
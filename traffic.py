from random import randrange


def sort_on_position(sites):
    return sorted(sites, key=lambda site: site[1])


def populate_sites_randomly():
    sites = []
    for i in range(CARS):
        v = randrange(0, VMAX)
        while True:
            position = randrange(SIZE)
            if position_not_occupied(sites, position):
                sites.append((v, position))
                break

    return sort_on_position(sites)


def position_not_occupied(sites, position):
    for site in sites:
        if site[1] == position:
            return False
    return True


def distance_to_next(sites, current_site):
    next_site = sites[(sites.index(current_site) + 1) % len(sites)]
    distance = next_site[1] - current_site[1]
    if (distance < 0):
        distance = SIZE - abs(distance)
    return distance


def rules(car, sites):
    v = car[0]
    i = car[1]

    # 1. Acceleration
    if v < VMAX and position_not_occupied(sites, v + 1):
        v = v + 1

    # 2. Slowing down
    j = distance_to_next(sites, car)
    if j <= v:
        v = j - 1
    
    # 3. Randomization
    if v > 0:
        r = randrange(1, 100)
        if r <= PROBABILITY:
            v = v - 1

    # 4. Car motion
    i = i + v

    if i >= SIZE:
        i = i % SIZE

    return v, i


def display_sites(sites):
    temp = ["."] * SIZE
    for site in sites:
        temp[site[1]] = str(site[0])
    print("".join(temp))


ITERATIONS = 22
SIZE = 100
CARS = 20
PROBABILITY = 20
VMAX = 5

sites = populate_sites_randomly()
display_sites(sites)

for _ in range(ITERATIONS):
    sites = sort_on_position(list(map(lambda car: rules(car, sites), sites)))
    display_sites(sites)

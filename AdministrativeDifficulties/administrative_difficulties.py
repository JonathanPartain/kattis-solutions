import fileinput
# Kattis Administrative Difficulties
# https://open.kattis.com/problems/administrativeproblems


class Spy:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.cost = 0
        self.consistent = True
        self.returned = True


class Car:
    def __init__(self, name, catalog_cost, pickup_cost, km_cost):
        self.name = name
        self.catalog_cost = catalog_cost
        self.pickup_cost = pickup_cost
        self.km_cost = km_cost


file = fileinput.input()  # defaults to sys.stdin

num_tests = int(file.readline().strip())  # read first line of file to determine number of tests

for i in range(num_tests):
    spies = {}
    cars = {}

    types = file.readline().strip().split()  # get number of cars and events
    num_cars = types[0]  # assign number of cars to a variable
    num_events = types[1]  # assign number of events to variable

    # add cars loop
    for car in range(int(num_cars)):
        car_line = file.readline().strip().split()  # split into list
        car_name = car_line[0]
        car_catalog_cost = car_line[1]
        car_pickup_cost = car_line[2]
        car_km_cost = car_line[3]
        car_created = Car(car_name, int(car_catalog_cost), int(car_pickup_cost), int(car_km_cost))
        cars[car_name] = car_created

    # add event loop
    for even in range(int(num_events)):
        # read lines, extract t (time of event), S (name of spy), e (type of event)
        # after e, number depends on val of e
        # if e = 'p' (pickup): string C (name of car picked up)
        # if e = 'r' (return): integer d (distance covered in the car last picked up by spy S, in km)
        # if e = 'a' (accident): integer s (severity of accident in percent, 0 to 100)
        event_data = file.readline().strip().split()  # split into list
        event_time = event_data[0]
        spy_name = event_data[1]
        event_type = event_data[2]
        type_result = event_data[3]
        # check if spy_name exists
        if spy_name not in spies:
            new_spy = Spy(spy_name)
            spies[spy_name] = new_spy

        # get current spy
        current_spy = spies[spy_name]

        # pickup event
        if event_type == "p":
            # type_result = name of car
            if current_spy.car is None:  # A spy can use at most one car at a time
                current_car = cars[type_result]
                current_spy.car = current_car
                current_spy.cost += current_car.pickup_cost
                current_spy.returned = False  # returned is False as a car has been picked up
            else:
                current_spy.consistent = False

        if event_type == "r":
            # type_result = distance traveled
            if current_spy.car is not None:  # a spy will always pick up a car before returning it
                type_result = int(type_result)  # set type_result to int
                current_car = current_spy.car
                cost_to_return = current_car.km_cost * type_result  # cost per km * km traveled
                current_spy.cost += cost_to_return
                current_spy.car = None  # return car
                current_spy.returned = True  # A spy will always return a car they picked up
            else:
                current_spy.consistent = False

        if event_type == "a":
            # type_result = severity in percent
            type_result = int(type_result)  # set type_result to int

            if current_spy.car is not None:  # Accidents can only happen when a spy is using a car
                current_car = current_spy.car  # get current car
                car_cost = current_car.catalog_cost  # get catalog cost
                if type_result != 0:
                    cost_to_pay = car_cost * type_result  # multiply by damage percentage (* 100)
                    modulus = cost_to_pay % 100  # get remainder
                    if modulus > 0:
                        cost_to_pay += 100 - modulus  # add 100 - remainder
                    cost_to_pay = int(cost_to_pay / 100)  # divide by 100 to get the actual percentage to add
                    current_spy.cost += cost_to_pay  # add to cost for spy

            else:
                current_spy.consistent = False

    for key, spy in sorted(spies.items()):
        if spy.consistent and spy.returned:  # if the spy is consistent, and returned his car
            print(key, spy.cost)
        else:  # inconsistent!
            print(key, "INCONSISTENT")



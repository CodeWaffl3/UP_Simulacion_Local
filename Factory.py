import simpy
import random
import numpy

PRODUCT_REJECTION_RATE = 0.05 * 100
ACCIDENT_RATE = 0.01 * 100
AVERAGE_REPAIR_RATE = 3
RESOURCE_REFILL_TIME = 1
MACHINE_BUSY_TIME = 4
WORKSTATIONS_FAILING_RATES = [ 0.20, 0.10, 0.15, 0.05, 0.07, 0.10 ]





class WorkStation:
    def __init__(self, env: simpy.Environment, raw_material, failing_rate: float):
        self.env = env
        self.machine_available = simpy.Resource(env, 1)
        self.raw_material = raw_material
        self.failing_rate = failing_rate * 10
        self.down_time = 0

    def Work(self):
            #Does the Machine Fails?
            #Machine Fails
            if random.randint(0,100) < self.failing_rate:
                repair = random.randint(0,AVERAGE_REPAIR_RATE)
                self.down_time += repair
                yield self.env.timeout(repair)

            #Machine works
            #Chec for raw materials in machine
            if self.raw_material <= 0:
                #Replenish of the raw_materials
                yield self.env.timeout(RESOURCE_REFILL_TIME)
                self.raw_material = 25
            #Work
            self.env.timeout(MACHINE_BUSY_TIME)
            #Take materials used
            self.raw_material =- 1







class Factory(object):
    def __init__(self, env):
        self.env = env
        self.work_stations = list()
        for fail_rate in WORKSTATIONS_FAILING_RATES:
            self.work_stations.append(WorkStation(self.env, raw_material=25, failing_rate=fail_rate))
        self.current_machine = 1
        self.total_products_manufactured = 0

    def GoTroughStations(self):
        for i in range(3):
            # Check if machine availabilty
            with self.work_stations[i].machine_available.request() as req:
                yield req
                self.work_stations[i].Work()
        # yield self.work_station[5].machine_available.req | self.work_station[6].machine_available.req

        #Stations 4,5
        with self.work_stations[3].machine_available.request() as req4, self.work_stations[4].machine_available.request() as req5:
            request = yield req4 | req5

            if req4 in request:
                self.current_machine = 3
                self.work_stations[3].Work()
            elif req5 in request:
                self.current_machine = 4
        if self.current_machine == 3:
            with self.work_stations[4].machine_available.request() as req:
                yield req
                self.work_stations[4].Work()
        if self.current_machine == 4:
            with self.work_stations[3].machine_available.request() as req:
                yield req
                self.work_stations[3].Work()
        #Station 6
        with self.work_stations[5].machine_available.request() as req:
            yield req
            self.work_stations[5].Work()
        if random.randint(0,100) > PRODUCT_REJECTION_RATE:
            self.total_products_manufactured += 1
        if random.randint(0,1) < ACCIDENT_RATE:
            yield self.env.timeout(24)






def main():
    env = simpy.Environment()
    factory = Factory(env)
    env.process(factory.GoTroughStations())

    env.run(until=500)
    print(factory.total_products_manufactured)
main()
import simpy
import random

AVERAGE_REPAIR_RATE = 3
WORKSTATIONS_FAILING_RATES = [ 0.20, 0.10, 0.15, 0.05, 0.07, 0.10 ]


class WorkStation:
    def __init__(self, env: simpy.Environment, raw_material, failing_rate: float):
        self.env = env
        self.machine_available = simpy.Resource(env, 1)
        self.raw_material = raw_material
        self.failing_rate = failing_rate * 10

    def Work(self, busy_time, failing_rate):
        #Check if machine availabilty
        with self.machine_available.request() as req:
            yield req
            #Does the Machine Fails?
            #Machine Fails
            if random.randint(0,100) < failing_rate:
                yield self.env.timeout(AVERAGE_REPAIR_RATE)
            #Machine works
            #Chec for raw materials in machine
            if self.raw_material <= 0:
                #Replenish of the raw_materials
                #yield self.env.timeout()
                self.raw_material = 25
            #Work
            self.env.timeout(busy_time)
            #Take materials used
            self.raw_material =+ 1







class Factory(object):
    def __init__(self, env):
        self.env = env
        self.work_stations = list()
        for fail_rate in WORKSTATIONS_FAILING_RATES:
            self.work_stations.append(WorkStation(self.env, raw_material=25, failing_rate=fail_rate))

    #TODO
    def GoTroughStations(self):
        for i in range(3):
            self.work_stations[i].Work()
        # yield self.work_station[5].machine_available.req | self.work_station[6].machine_available.req








def main():
    factory = Factory()

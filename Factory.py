import simpy
import random

AVERAGE_REPAIR_RATE = 3
WORKSTATIONS_FAILING_RATES = [ 0.20, 0.10, 0.15, 0.05, 0.07, 0.10 ]
product_pass = False


class WorkStation:
    def __init__(self, env: simpy.Environment, raw_material, failing_rate: float):
        self.env = env
        self.machine_available = simpy.Resource(env, 1)
        self.raw_material = raw_material
        self.failing_rate = failing_rate * 10

    def Work(self, busy_time):

            #Does the Machine Fails?
            #Machine Fails
            if random.randint(0,100) < self.failing_rate:
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
            # Check if machine availabilty
            with self.work_stations[i].machine_available.request() as req:
                yield req
                self.work_stations[i].Work(4)
        # yield self.work_station[5].machine_available.req | self.work_station[6].machine_available.req

        #Stations 4,5
        with self.work_stations[3].machine_available.request() as req4, self.work_stations[4].machine_available.request() as req5:
            request = yield req4 | req5

            if req4 in request:
                print("MACHINE 4 IS WORKING")
                product_pass = not product_pass
            if req5 in request:
                print("MACHINE 5 IS WORKING")

        # req1 = t1.request()  # Process requests t1
        # req2 = t2.request()  # Process requests t2







def main():
    env = simpy.Environment()
    factory = Factory(env)
    env.process(factory.GoTroughStations())
    env.run(until=50)

main()
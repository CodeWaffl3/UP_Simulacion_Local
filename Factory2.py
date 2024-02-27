import simpy
import random

AVERAGE_REPAIR_RATE = 3
WORKSTATIONS_FAILING_RATES = [0.20, 0.10, 0.15, 0.05, 0.07, 0.10]
PRODUCT_REJECTION_PROBABILITY = 0.05
ACCIDENT_PROBABILITY = 0.0001

total_production = 0
station_occupancy = [0] * 6
station_downtime = [0] * 6
supplier_occupancy = 0
total_fix_time = 0
total_delay = 0
rejected_products = 0
accident_occurrences = 0


class WorkStation:
    def __init__(self, env, raw_material, failing_rate):
        self.env = env
        self.machine_available = simpy.Resource(env, 1)
        self.raw_material = raw_material
        self.failing_rate = failing_rate * 10

    def Work(self, busy_time):
        if random.randint(0, 100) < self.failing_rate:
            yield self.env.timeout(AVERAGE_REPAIR_RATE)
            total_fix_time += AVERAGE_REPAIR_RATE

        if self.raw_material <= 0:
            yield self.env.timeout(0)
            self.raw_material = 25
            supplier_occupancy += 1

        yield self.env.timeout(busy_time)
        self.raw_material -= 1


class Factory:
    def __init__(self, env):
        self.env = env
        self.work_stations = list()
        for fail_rate in WORKSTATIONS_FAILING_RATES:
            self.work_stations.append(WorkStation(self.env, raw_material=25, failing_rate=fail_rate))

    def GoThroughStations(self, product):
        global total_production, station_occupancy, station_downtime, total_delay
        for i in range(3):
            with self.work_stations[i].machine_available.request() as req:
                yield req
                station_occupancy[i] += self.env.now - req.time_requested
                start_time = self.env.now
                yield self.work_stations[i].Work(4)
                end_time = self.env.now
                station_downtime[i] += end_time - start_time - 4

        with self.work_stations[3].machine_available.request() as req4, self.work_stations[4].machine_available.request() as req5:
            request = yield req4 | req5
            if req4 in request:
                station = 4
            else:
                station = 5
            start_time = self.env.now
            yield self.work_stations[station].Work(4)
            end_time = self.env.now
            station_downtime[station] += end_time - start_time - 4

        with self.work_stations[5].machine_available.request() as req:
            yield req
            station_occupancy[5] += self.env.now - req.time_requested
            start_time = self.env.now
            yield self.work_stations[5].Work(4)
            end_time = self.env.now
            station_downtime[5] += end_time - start_time - 4

        if random.random() < PRODUCT_REJECTION_PROBABILITY:
            rejected_products += 1
        else:
            total_production += 1

        if random.random() < ACCIDENT_PROBABILITY:
            accident_occurrences += 1
            yield self.env.timeout(10)
            total_delay += 10


def main():
    env = simpy.Environment()
    factory = Factory(env)

    for i in range(500):
        product = i
        env.process(factory.GoThroughStations(product))

    env.run()

    print("Total Production:", total_production)
    for i in range(6):
        print("Station Occupancy {}: {:.2f}".format(i + 1, station_occupancy[i] / env.now))
        print("Station Downtime {}: {:.2f}".format(i + 1, station_downtime[i] / env.now))
    print("Supplier Occupancy: {:.2f}".format(supplier_occupancy / env.now))
    print("Average Fix Time: {:.2f}".format(total_fix_time / total_production))
    print("Average Delay: {:.2f}".format(total_delay / total_production))
    print("Rejected Products:", rejected_products)
    print("Accident Occurrences:", accident_occurrences)


if __name__ == "__main__":
    main()

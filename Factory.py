import simpy

class WorkStation:
    def __init__(self, env, num_material):
        self.materials = simpy.Resource(env, num_material)

    def Work(self, time_of_work):

class Factory(object):
    def __init__(self, env, WorkStations = list(WorkStation)):
        self.env = env
        self.workStations = WorkStations

def GoTroughStations():
    for i in range(3):
        yield self.workStations[i].work()






def main():
    factory = Factory()

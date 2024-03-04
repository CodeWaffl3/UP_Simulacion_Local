import numpy as np

class Pattern:
    def __init__(self, name, array):
        self.name = name
        self.array = array

ALL_PATTERNS = list()

block = np.array([  [0,0,0,0],
                    [0,255,255,0],
                    [0,255,255,0],
                    [0,0,0,0]])
ALL_PATTERNS.append(Pattern("Block", block))

beehive = np.array([[0,0,0,0,0,0],
                    [0,0,255,255,0,0],
                    [0,255,0,0,255,0],
                    [0,0,255,255,0,0],
                    [0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Beehive", beehive))
loaf = np.array([   [0,0,0,0,0,0],
                    [0,0,255,255,0,0],
                    [0,255,0,0,255,0],
                    [0,0,255,0,255,0],
                    [0,0,0,255,0,0],
                    [0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Loaf", loaf))
boat = np.array([   [0,0,0,0,0],
                    [0,255,255,0,0],
                    [0,255,0,255,0],
                    [0,0,255,0,0],
                    [0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Boat", boat))
tub = np.array([    [0,0,0,0,0],
                    [0,0,255,0,0],
                    [0,255,0,255,0],
                    [0,0,255,0,0],
                    [0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Tub", tub))
blinker1 = np.array([[0,0,0],
                     [0,255,0],
                     [0,255,0],
                     [0,255,0],
                     [0,0,0]])
ALL_PATTERNS.append(Pattern("Blinker", blinker1))
blinker2 = np.array([[0,0,0,0,0],
                     [0,255,255,255,0],
                     [0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Blinker", blinker2))
toad1 = np.array([   [0,0,0,0,0,0],
                    [0,0,0,255,0,0],
                    [0,255,0,0,255,0],
                    [0,255,0,0,255,0],
                    [0,0,255,0,0,0],
                    [0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Toad", toad1))
toad2 = np.array([  [0,0,0,0,0,0],
                    [0,0,255,255,255,0],
                    [0,255,255,255,0,0],
                    [0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Toad", toad2))
beacon1 = np.array([ [0,0,0,0,0,0],
                    [0,255,255,0,0,0],
                    [0,255,255,0,0,0],
                    [0,0,0,255,255,0],
                    [0,0,0,255,255,0],
                    [0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Beacon", beacon1))
beacon2 = np.array([[0,0,0,0,0,0],
                    [0,255,255,0,0,0],
                    [0,255,0,0,0,0],
                    [0,0,0,0,255,0],
                    [0,0,0,255,255,0],
                    [0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Beacon", beacon2))
glider1 = np.array([[0,0,0,0,0],
                    [0,0,255,0,0],
                    [0,0,0,255,0],
                    [0,255,255,255,0],
                    [0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Glider", glider1))
glider2 = np.array([[0,0,0,0,0],
                    [0,255,0,255,0],
                    [0,0,255,255,0],
                    [0,0,255,0,0],
                    [0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Glider", glider2))
glider3 = np.array([[0,0,0,0,0],
                    [0,0,0,255,0],
                    [0,255,0,255,0],
                    [0,0,255,255,0],
                    [0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Glider", glider3))

glider4 = np.array([[0,0,0,0,0],
                    [0,255,0,0,0],
                    [0,0,255,255,0],
                    [0,255,255,0,0],
                    [0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("Glider", glider4))

lws1 = np.array([   [0,0,0,0,0,0,0],
                    [0,255,0,0,255,0,0],
                    [0,0,0,0,0,255,0],
                    [0,255,0,0,0,255,0],
                    [0,0,255,255,255,255,0],
                    [0,0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("LightWeightShip", lws1))

lws2 = np.array([   [0,0,0,0,0,0,0],
                    [0,0,0,255,255,0,0],
                    [0,255,255,0,255,255,0],
                    [0,255,255,255,255,0,0],
                    [0,0,255,255,0,0,0],
                    [0,0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("LightWeightShip", lws2))
lws3 = np.array([   [0,0,0,0,0,0,0],
                    [0,0,255,255,255,255,0],
                    [0,255,0,0,0,255,0],
                    [0,0,0,0,0,255,0],
                    [0,255,0,0,255,0,0],
                    [0,0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("LightWeightShip", lws3))
lws4 = np.array([   [0,0,0,0,0,0,0],
                    [0,0,255,255,0,0,0],
                    [0,255,255,255,255,0,0],
                    [0,255,255,0,255,255,0],
                    [0,0,0,255,255,0,0],
                    [0,0,0,0,0,0,0]])
ALL_PATTERNS.append(Pattern("LightWeightShip", lws4))
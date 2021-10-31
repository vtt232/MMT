def repeat(times, f, *w):
    for _ in range(times):
        f(*w)
def inquisition(weapon1, weapon2, weapon3):
    print("Our weapons are {}, {} and {}".format(weapon1, weapon2, weapon3))

repeat(10, inquisition, "surprise", "fear", "ruthless efficiency")
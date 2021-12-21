#!/usr/bin/python3

class Map:
  def __init__(self):
    self.pairs = list()

  def set(self, key, value):
    """ Add a new pair
    """
    self.pairs.append((key, value))

  def get(self, key):
    """ Get value associated with key, returns None if not found
    """
    for el in self.pairs:
      if (el[0] == key):
        return el[1]
    return None

if __name__ == "__main__":

    skyblogs = Map()

    skyblogs.set('Viviane', "https://edgyncool.skyrock.com")
    skyblogs.set('Hoppy', None)

    print("Viviane's skyblog address is '{}'".format(skyblogs.get("Viviane")))
    print("Hoppy's skyblog address is '{}'".format(skyblogs.get("Hoppy")))
    print("Chuck's skyblog address is '{}'".format(skyblogs.get("Chuck")))

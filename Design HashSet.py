class MyHashSet(object):

    def __init__(self):
        self.hash_index = [False]*10000000
    def add(self, key):
        self.hash_index[key % pow(10,6)] = True

    def remove(self, key):
        self.hash_index[key % pow(10,6)] = False

    def contains(self, key):
        return self.hash_index[key % pow(10,6)]

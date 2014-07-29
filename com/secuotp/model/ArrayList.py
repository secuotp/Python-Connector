__author__ = 'zenology'

class ArrayList:
    data = None

    def size(self):
        return len(self.data)

    def add(self, value):
        self.data[self.size()] = value

    def remove(self, int(index)):

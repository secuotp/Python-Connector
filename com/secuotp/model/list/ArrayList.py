__author__ = 'zenology'


class ArrayList:
    __data = []

    def size(self):
        return len(self.__data)

    def add(self, value):
        self.__data.append(value)

    def remove(self, index):
        i = index + 1
        while i < self.size() + 1:
            if i != self.size():
                self.__data[i - 1] = self.__data[i]
                i += 1
            else:
                del self.__data[-1]

    def get(self, index):
        return self.__data[index]
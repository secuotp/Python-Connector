from com.secuotp.model import ArrayList

__author__ = 'zenology'

class DoubleArrayList (ArrayList):
    __key = []

    def add(self, key, value):
        super(DoubleArrayList, self).add(value)
        self.__key.append(key)

    def getValue(self, index):
        return super(DoubleArrayList, self).getValue(index)

    def getKey(self, index):
        return self.__keyp[index]

    def remove(self, index):
        i = index + 1
        while i < self.size() + 1:
            if i != self.size():
                super(DoubleArrayList, self).data[i - 1] = super(DoubleArrayList, self).data[i]
                self.__key[i - 1] = self.__key[i]
            else:
                del super(DoubleArrayList, self).data[-1]
                del self.__key[-1]

    def size(self):
        return len(self.__key)


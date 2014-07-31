from com.secuotp.model.list import ArrayList as moduleList

__author__ = 'zenology'


class DoubleArrayList(moduleList.ArrayList):
    __key = []

    def add(self, key, value):
        super(DoubleArrayList, self).add(value)
        self.__key.append(key)

    def get_value(self, index):
        return super(DoubleArrayList, self).get(index)

    def get_key(self, index):
        return self.__key[index]

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


from com.secuotp.model.list import DoubleArrayList as module1

__author__ = 'zenology'


class XMLParameter (module1.DoubleArrayList):
    __pointer = 0

    def pop(self):
        val = self.peek()
        self.__pointer += 1
        return val

    def peek(self):
        if self.__pointer <= super(XMLParameter, self).size():
            val = [super(XMLParameter, self).get_key(self.__pointer), super(XMLParameter, self).get_value(self.__pointer)]
            return val
        return None

    def has_next(self):
        return self.__pointer < super(XMLParameter, self).size()

    def first(self):
        self.__pointer = 0
        
    def last(self):
        self.__pointer = super(XMLParameter, self).size() - 1


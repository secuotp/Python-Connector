from com.secuotp.model import DoubleArrayList as dal

__author__ = 'zenology'

a = dal.DoubleArrayList()

a.add('A', 1)
a.add('B', 2)
a.add('C', 3)
a.add('D', 4)

print(a.getKey(1) + ':' + a.getValue(1))
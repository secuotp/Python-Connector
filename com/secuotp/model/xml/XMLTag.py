from com.secuotp.model.list import ArrayList as module1

__author__ = 'zenology'


class XMLTag:
    def __init__(self, tagname, value):
        if value is None:
            self.__tagname = tagname
            self.__value = None
            self.__childnode = module1.ArrayList()
        else:
            self.__tagname = tagname
            self.__value = value
            self.__childnode = None

    def get_tagname(self):
        return self.__tagname

    @property
    def tagname(self):
        return self.__tagname

    @tagname.setter
    def tagname(self, tagname):
        self.__tagname = tagname

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def chlidnode(self):
        return self.__childnode

    @chlidnode.setter
    def chlidnode(self, childnode):
        self.__childnode = childnode

    def have_childnode(self):
        return self.__childnode is not None

    def get_child_tag(self, index):
        return self.__childnode.get(index)

    def add_child_value(self, tagname, value):
        tag = XMLTag(tagname, value)
        self.chlidnode.add(tag)

    def add_child_tag(self, tagname):
        tag = XMLTag(tagname, None)
        self.chlidnode.add(tag)
        return self.chlidnode.get(-1)

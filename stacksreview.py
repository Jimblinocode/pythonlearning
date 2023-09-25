
class node():
    def __init__(self):
        self.__next: node = None
        self.__value = None

    def get_next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next
    
    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value


class stack:
    """stack interface"""
    def __init__(self):
        """the constructor for the stack interface"""
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

class implementationv1(stack):
    def __init__(self):
        self.__collect = []

    def push(self, obj):
        self.__collect.append(obj)

    def pop(self):
        value = self.__collect[-1]
        self.__collect.pop()
        return value
    
class implementationv2(stack):
    def __init__(self):
        self.__top: node = None

    def push(self, value):
        new_node = node()
        new_node.set_value(value)
        new_node.set_next(self.__top)
        self.__top = new_node


    def pop(self):
        if self.__top != None:
            temp = self.__top
            self.__top = self.__top.get_next()
            return temp.get_value()
        return None
            


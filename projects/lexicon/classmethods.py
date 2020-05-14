import random

class Person(object):

    # instance variables created on initiation
    def __init__(self, name):
        self.name = name
        num_of_hands = 3 #INCORRECT DEFINITION! WONT BE ABLE TO ACCESS IN ANY WAY!

    # class variables can just exist on its own
    num_of_legs = 2

    # ================== STATIC METHODS ==================

    # Good static method - doesn't accss anything inside
    @staticmethod
    def print_random_number():
        print(random.randint(1,1000))

    # Bad static method - tries to access a class variable = ERROR
    @staticmethod
    def print_legs_static():
        print(num_of_legs)

    # Bad static method - tries to access an instance variable = ERROR
    @staticmethod
    def print_name_static():
        print(name)

    # ================== CLASS METHODS ==================

    # Good class method - is able to access class attributes
    @classmethod
    def print_legs_class(cls):
        print(cls.num_of_legs)

    # Bad class method - is trying to reach for what looks like a class variable but is actually an instance variable
    @classmethod
    def print_hands_class(cls):
        print(cls.num_of_hands)

    # Bad class method - is trying to reach for instance variables = ERROR
    @classmethod
    def print_name_class(cls):
        print(cls.name)

    # ================== INSTANCE METHODS ==================

    # Instance methods are the only ones that can access instance params
    def print_name(self):
        print(self.name)

    def print_num_of_hands(self):
        print(self.num_of_hands)




if __name__ == "__main__":

    #test static methods
    Person.print_random_number()
    # Person.print_legs_static() #ERROR!
    # Person.print_name_static() #ERROR!

    #test class methods
    print('-'*10)
    Person.print_legs_class()
    # Person.print_hands_class() #ERROR!
    # Person.print_name_class() #ERROR!

    #test instance methods
    print('-'*10)
    #need an instance first!
    ilja = Person('ilja')
    rob = Person('rob')
    #test their attributes
    print(ilja.name)
    print(rob.name)
    print(ilja.num_of_legs)
    print(rob.num_of_legs)

    # Person.print_name() #ERROR
    Person.print_name(ilja)
    ilja.print_name() #equivalent to above
    # ilja.print_num_of_hands() #ERROR COZ INSTANCE ATTRIBUTE DEFINED WITHOUT SELF

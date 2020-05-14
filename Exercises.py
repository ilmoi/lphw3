# # the f string - notice the difference between th below two
# string = 'lawl'
# print('this script is called {script}')
# print(f'this script is called {script}')

# #6
# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! {}"
# print(joke_evaluation.format(hilarious)) # interesting, so seems that .format inserts whatever comes afer into {}
#
# #7
# print('its fleece was white as {} {}.'.format('snow', 'test'))
# print('.'*10)
# print('test1', end=' ') #very cool so end = ' ' concatenates strings into a single line
# print('test2')

# # 8
# print("\nJan\nFeb")

# #9
# print('This -> \\ should print a single tab')
# print('This should print \n\ttabbb\n\ttabbb\n\ttabbb\n\ttabbb')

# #11
# test = input('telll meeeeee')
# print(f"you are {test}")

# #13
# from sys import argv #argv is an "argument variable" - it holds the arguments you pass to your python program from terminal
# script, first, second, third = argv #unpacks whatever is in argv into these
# print(f'this script is called {script}') #note how you need to pass script name +3 arguments, not 4 arguments

# 15
# from sys import argv
# script, filename = argv
# txt = open(filename) #creates a file object
# print(f"here's your {filename}:")
# print(txt.read())

# #16
# from sys import argv
# script, filename = argv
# txt = open(filename, 'w+')
# for i in range(10):
#     txt.write(f'\nstuff{i}!!!!!')
# txt.close()
# txt = open(filename)
# print(txt.read())
#
# # 17
# #option 1
# from sys import argv; from os.path import exists #notice the semicolon to write two things on one line
# script, from_file, to_file = argv
#
# opened = open(from_file)
# text = opened.read()
#
# print(exists(to_file))
#
# out = open(to_file, 'w')
# out.write(text)
#
# out.close()
# opened.close()
# print('hooray')
#
# #option 2, preferred way
# from sys import argv; from os.path import exists #notice the semicolon to write two things on one line
# script, from_file, to_file = argv
#
# text = open(from_file).read()
#
# print(exists(to_file))
#
# with open(to_file, 'w') as f:
#     f.write(text)
#
# print('hooray')
#
# # a bit more readline practice
# from sys import argv
# script, filename = argv
# with open(filename, 'r') as f:
#     for i in range(5):
#         print(f.readline())
#         # print('hooray')

## 23
# import sys
# script, input_encoding, error = sys.argv
#
# def main(language_file, encoding, errors):
#     line = language_file.readline()
#
#     if line:
#         print_line(line, encoding, errors)
#         return main(language_file, encoding, errors)
#
# def print_line(line, encoding, errors):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding, errors=errors)
#     cooked_string = raw_bytes.decode(encoding, errors = errors)
#
#     print(raw_bytes, "<==>", cooked_string)
#
# languages = open('languages.txt', encoding="utf-8")
#
# main(languages, input_encoding, error)
#
# #mnemonic: DBES = decode bytes, encode string
# #
# def break_words(sentence):
#     words = sentence.split()
#     return sorted(words)

# print('something something %i, %f' % (45.5, 45.5))

# a = ["1","2","3"]
# b = " ".join(a)
# print(b)

# stuff = {"name": "Zed", "city": "SF"}
# a = stuff.get('name')
# print(a)
# b = stuff.get('test')
# print(b)
# if not b:
#     print('sorry does not exist')

# class person(object):
#   def __init__(self, name):
#     self.name = name
#
# class student(person):
#   def __init__(self, name, course):
#     person.__init__(self, name)
#     self.course = course
#   def cookie(self):
#       print('i has cookie')
#
# s = student('ilja', 'biology')
# print(s.name)

# class student(object):
#     def __init__(self, name):
#         self.name = name
#     def __lt__(self, other):
#         if len(self.name) < len(other.name):
#             return True
#         else:
#             return False
#
# s1 = student('looooong')
# s2 = student('short')
#
# print(s1<s2)
# print(s1.__lt__(s2))
# print(student.__lt__(s1,s2))
#
# """
# 1. WB
#     1.1. Assert (check inputs, check outputs)
#     1.2. Except (try > except > else > finally)
# 2. BB
#     2.1. If recursion exists (test depth 0, 1, 2)
#     2.2. If loop exists (test loop exectues once, n times, none times)
# """

# class student(object):
#     counter = 0
#     def __init__(self, name):
#         self.name = name
#         self.counter = student.counter
#         student.counter +=1
#
# s1 = student('ilja')
# s2 = student('ben')
#
# print(s1.counter)
# print(s2.counter)



# class Parent(object):
#     def altered(self):
#         print("parent's version of function")
#
#
# class Child(Parent):
#     def altered(self):
#         print("whatever we want before it = our alterations 1")
#         super(Child, self).altered() #prints "parent's version of function"
#         print("whatever we want after it = our alterations 2")
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# print('-'*10)
# son.altered()

# class person(object):
#   def __init__(self, name):
#     self.name = name
#
# class student(person):
#   def __init__(self, name, course):
#     # person.__init__(self, name)
#     super(student, self).__init__(name)
#     self.course = course
#
# s = student('ilja', 'biology')
# print(s.name)
# print(s.course)

## 44e - here we're looking at composition vs inheritance
# class Parent(object):
#     def implicit(self):
#         print("this is implicit function")
#     def override(self):
#         print("this is overriden function")
#     def alter(self):
#         print("this is old non-altered function")
#
# class Child(Parent):
#     #implicit comes down automatically
#     def override(self):
#         print('kids version')
#     def alter(self):
#         print('kids start')
#         super(Child,self).alter()
#         print('kids end')
#
# class NotChild(object):
#     def __init__(self):
#         self.parent = Parent() #key line
#     def implicit(self):
#         self.parent.implicit()
#     def override(self):
#         print("NEW overriden function")
#     def alter(self):
#         print("whatever I want before")
#         self.parent.alter()
#         print("whatever I want after")
#
# parent = Parent()
# parent.implicit()
# parent.override()
# parent.alter()
#
# print('-'*(10))
#
# child = Child()
# child.implicit()
# child.override()
# child.alter()
#
# print('-'*(10))
#
# notchild = NotChild()
# notchild.implicit()
# notchild.override()
# notchild.alter()

# playing with mangling


# class Human(object):
#
#     def __init__(self, name):
#         self.name = name
#         self.__var_to_be_mangled = 10
#
#     def __to_be_mangled(self, x):
#         return x**3
#
#     def setter(self, new_val):
#         self.__var_to_be_mangled = new_val
#
#     def getter(self):
#         return self.__var_to_be_mangled
#
#
# ilja = Human('ilja')
# # print(ilja.name)
# # print(dir(Human))
# # # print(ilja.__to_be_mangled(3)) #returns an error
# # print(ilja._Human__to_be_mangled(3)) #works great!
#
# print(ilja.getter())
# ilja.setter(20)
# print(ilja.getter())

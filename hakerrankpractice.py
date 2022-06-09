# class hack:
#     print("Hello")
#
#     def __init__(self):
#
#         print("Hello this is constructor")
#
#     @classmethod
#     def hack(cls):
#         pass
#
#
# h1 = hack
# h1.hack()
class Person:
    def __init__(self, initialAge):

        if initialAge < 0:
            self.age = 0
            print("Age is not valid , setting age to 0")
        else:
            self.age = initialAge

    def amIOld(self):

        if self.age < 13:
            print("you are young")
        elif self.age < 18:
            print("you are teenager")
        else:
            print("you are old")

    def yearPasses(self):
        self.age += 1

import time

class project:
    def __init__(self, name):
        self.name = name
        print("A project has been created!")

    def sayhello(self):
        print("hello, my name is {}!".format(self.name))

    def presentTime(self):
        print("Time is {}".format(time.ctime()))

    def haha(self):
        for i in range(100):
            print("HAHAHAHAHAHAAHA")


if __name__ == '__main__':
    p = project("co-Learn")
    p.sayhello()
    p.presentTime()
    p.haha()

import time

class project:
    def __init__(self, name):
        self.name = name
        print("A project has been created!")

    def sayhello(self):
        print("hello, my name is {}!".format(self.name))

    def presentTIme(self):
        print(time.ctime())


if __name__ == '__main__':
    p = project("co-Learn")
    p.sayhello()

import time


class project:
    def __init__(self, name):
        self.name = name
        print("A project has been created!")

    def hello_and_introduce(self):
        print("hello, my name is {}!".format(self.name))

    def hello(self):
        print('hello')

    def present_time(self):
        print("Time is {}".format(time.ctime()))

    @staticmethod
    def haha(self):
        for i in range(100):
            print("HAHAHAHAHAHAAHA")

    @staticmethod
    def success(self):
        print('기쁨의 기립박수')

    def pas(self):
        pass


if __name__ == '__main__':
    p = project("co-Learn")
    p.sayhello()
    p.presentTime()
    p.haha()

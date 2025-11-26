class Mobile:
    def __init__(self):
        pass
    def calling(self):
        print("Invoking calling function")

    def message(self):
        print("Invoking message function")

    def games(self):
        print("Invoking games function")

class Samsung_A_22(Mobile):
    def camera(self):
        print("Invoking camera function")

    def music(self):
        print("Invoking music function")

    def videocall(self):
        print("Invoking videocall function")

samsung=Samsung_A_22()
samsung.music()
samsung.calling()
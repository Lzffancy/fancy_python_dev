class Kls():
    def public(self):
        print('Hello public world!')

    def __private(self):
        print('Hello private world!')

    def call_private(self):
        self.__private()


if __name__ == '__main__':
    ins = Kls()
    ins.call_private()

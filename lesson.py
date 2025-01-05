class Numbers:
    def __init__(self, *args):
        self.my_list = list(args)

    def add_number(self, n):
        self.my_list.append(n)

    def get_positive(self):
        return [i for i in self.my_list if i > 0]

    def get_negative(self):
        return [i for i in self.my_list if i < 0]

    def get_zeroes(self):
        return [i for i in self.my_list if i == 0]



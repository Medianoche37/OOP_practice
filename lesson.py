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


nums = Numbers(7, 8, 9)
nums_2 = Numbers(7, 8, 9)

nums.add_number(10)
nums_2.add_number(11)
nums_2.add_number(12)
print(nums.get_positive())
print(nums_2.get_positive())
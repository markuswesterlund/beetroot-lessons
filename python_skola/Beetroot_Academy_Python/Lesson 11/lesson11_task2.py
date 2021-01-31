class Mathematician:
    def square_nums(self, values):
        return [x*x for x in values]

    def remove_positives(self, values):
        # result = []

        # for value in values:
        #     if value < 0:
        #         result.append(value)
        #
        # return result
        # return [x for x in values if x < 0]
        return list(filter(lambda x: x < 0, values))

    def filter_leaps(self, values):
        return [value for value in values if value % 4 == 0]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


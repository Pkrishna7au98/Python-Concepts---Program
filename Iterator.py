class top20even:
    def __init__(self):
        self.nums = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nums <= 20:
            evals = self.nums
            self.nums += 1
            return evals
        else:
            raise StopIteration

evens = top20even()

for i in evens:
    print(i)




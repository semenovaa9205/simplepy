mylist = [2**i for i in range(1, 10)]  
print(mylist)


class fortmas:
    def __getitem__(self, index):
        if index == 0:
            raise IndexError('lit index out of range!! ')
        elif index < 0:
            return super().__getitem__(index)
        return super().__getitem__(index - 1)

    mas2 = fortmas(mylist)

    print(fortmas())

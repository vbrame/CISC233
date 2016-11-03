
class NestedHash:

    def __init__(self, size):
        self.list = []
        self.size = size
        for i in range(size):
            self.list.append([])

    def addItem(self, item):
        index = item % self.size
        x = self.list[index]
        x.append(item)

    def findItem(self, item):
        index = item % self.size
        found = False
        if len(self.list[index]) == 1:
            found = True
        elif len(self.list[index]) > 1:
            for i in self.list[index]:
                if i == item:
                    found = True
                    break

        if found:
            return "Item found"
        else:
            return "Item not found"

    def __str__(self):
        return str(self.list)

l = [54,26,93,17,77,31,44,55,20]
practice = NestedHash(11)
print practice
for i in l:
    practice.addItem(i)
print practice
print practice.findItem(55)
print practice.findItem(1)
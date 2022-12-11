from math import prod

# set this variable to True to print result for part 1 or false to print part 2 result
part1 = False
class Monkey:
    def __init__(self, id, data, op, test, send_to):
        self.id = id
        self.data = data
        self.op = op
        self.mutual = False
        self.test = test
        self.send_to = list(map(int, send_to))
        self.inspected = 0
        self.next = []

    def __repr__(self):
        return f'Monkey {self.id} has {self.data} items currently.\nIt has inspected {self.inspected} items.'

    def inspect(self):
        self.update()
        #print(self)
        for d in self.data:
            old = d
            self.inspected += 1
            # print(d)
            f = lambdas[self.op[0]]
            try:
                self.op[1] = int(self.op[1])
            except:
                self.mutual = True
                self.op[1] = d
            if self.mutual:
                self.op[1] = d

            d = f(d, self.op[1])

            d = d % n if not part1 else d // 3
            if d % self.test == 0:

                self.send(d, self.send_to[0])
            else:

                self.send(d, self.send_to[1])

        self.data = list()

    def send(self, item, id):
        monkeys[id].next.append(item)

    def update(self):
        self.data.extend(self.next)
        self.next = list()


text = [l.strip() for l in open('input#11.txt').readlines()]
monkeys = []

lambdas = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}
for i in range(0, len(text), 7):
    monkeys.append(
        Monkey(int(text[i][-2]), list(map(int, text[i + 1].replace(',', '').split()[2:])), text[i + 2].split()[4:6],
               int(text[i + 3].split()[-1]), list(map(int, [text[i + 4][-1], text[i + 5][-1]]))))
    # print(monkeys[-1],monkeys[-1].op,monkeys[-1].test,monkeys[-1].send_to)
n = prod(m.test for m in monkeys)
for _ in range(20 if part1 else 10000):  # range(20) for part 1
    #print(f'Round {_}')
    for monkey in monkeys:
        monkey.inspect()

views = list()

for monkey in monkeys:
    views.append(monkey.inspected)
views.sort(reverse=True)
print(f'part 1: {views[0]*views[1]}' if part1 else f'part 2: {views[0]*views[1]}')


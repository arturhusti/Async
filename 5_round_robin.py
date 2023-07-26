def generator_one(l):
    for i in l:
        yield i

# g = generator_one('hello')
# next(g) # management control


def example_gen():
    i = 0
    while True:
        i += 1
        yield i
        i += 1


def generator_two(n):
    for i in range(n):
        yield i


g_one = generator_one('hello')
g_two = generator_two(5)

tasks = [g_one, g_two]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

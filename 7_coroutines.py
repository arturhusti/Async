# def gen():
#     x = 'hello'
#     message = yield x
#     print(message)
#
#
# def total():
#     summ = 0
#
#     while True:
#         try:
#             x = yield summ
#         except StopIteration:
#             print('finish')
#             break
#         else:
#             summ += x
#
#     return summ
#
#
#
#
# def subgen():
#     for i in 'hello':
#         yield i
#
#
# def delgen(subgen):
#     for i in subgen:
#         yield i


# def subgen():
#
#     while True:
#         try:
#             message = yield
#         except:
#             pass
#         else:
#             print(message)
#
#
# def delgen(subgen):
#
#     while True:
#         try:
#             data = yield
#             subgen.send(data)
#         except:
#             pass


# def g():
#     yield from 'hello'

# def subgen():
#
#     while True:
#         try:
#             message = yield
#         except StopIteration:
#             print('finish')
#         else:
#             print(message)
#
#
# def delgen(subgen):
#
#     while True:
#         try:
#             data = yield
#             subgen.send(data)
#         except StopIteration as e:
#             subgen.throw(e)




def subgen():

    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print(message)

   # return 'finish'


def delgen(subgen):
        #
        # while True:
        #     try:
        #         data = yield
        #         subgen.send(data)
        #     except StopIteration as e:
        #         subgen.throw(e)

    yield from subgen

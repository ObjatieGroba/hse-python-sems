a = [1, 2, 3, 4, 5, 1,2, 3, 4, 5, 7]
a = ['a', 'b', 'c', 'd', 'a', 'ab']
a = [None, 1]
a = []
# a = [a]
a = [[1, 2, 3], [1, 2, 3], 3, {1, 2, 3}]


def to_hashable(elem):
    pass


print(len(set((elem
               if not isinstance(elem, set)
               else frozenset(elem))
              if not isinstance(elem, list)
              else tuple(elem)
              for elem in a)))

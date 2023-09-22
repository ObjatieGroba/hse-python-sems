l = list(map(int, input().split()))
max_elem = max(l)
min_elem = min(l)
max_index = l.index(max_elem)
min_index = l.index(min_elem)
second_max_elem = min_elem
second_min_elem = max_elem
for i, elem in enumerate(l):
    if i != max_index:
        second_max_elem = max(second_max_elem, elem)
    if i != min_index:
        second_min_elem = min(second_min_elem, elem)

if min_elem * second_min_elem >= max_elem * second_max_elem:
    elem_f, elem_s = min_elem, second_min_elem
else:
    elem_f, elem_s = max_elem, second_max_elem

print(min(elem_f, elem_s), max(elem_f, elem_s))

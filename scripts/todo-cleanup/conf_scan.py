def show(item_set):
    if type(item_set) is str:
        return '{' + item_set + '}'
    else:
        show_text = '{' + item_set[0]
        for item in item_set[1:]:
            show_text += ', '
            show_text += item
        return show_text + '}'


def disjoint(set_one, set_two):
    for a in set_one:
        for b in set_two:
            if a == b:
                return False
    return True


def union(set_one, set_two):
    items = []

    for a in set_one:
        if a not in items:
            items.append(a)
    for b in set_two:
        if b not in items:
            items.append(b)

    return tuple(sorted(items)) if len(items) > 1 else items[0]


if __name__ == '__main__':
    item_sets = {
        'a': 4,
        'b': 4,
        'c': 3,
        'd': 3,
        'e': 3,
        ('a', 'b'): 4,
        ('a', 'c'): 3,
        ('a', 'd'): 3,
        ('a', 'e'): 3,
        ('b', 'c'): 3,
        ('b', 'd'): 3,
        ('b', 'e'): 3,
        ('c', 'e'): 3,
        ('a', 'b', 'c'): 3,
        ('a', 'b', 'd'): 3,
        ('a', 'b', 'e'): 3,
        ('a', 'c', 'e'): 3,
        ('b', 'c', 'e'): 3,
        ('a', 'b', 'c', 'e'): 3
    }

    count = 0
    for p, pf in item_sets.items():
        for q, qf in item_sets.items():
            union_set = union(p, q)
            joint_sup = item_sets.get(union_set, 0)
            joint_conf = joint_sup / pf

            if joint_conf > 0.9 and disjoint(p, q):
                rule = f'{show(p)} => {show(q)}'
                rule += ' ' * (19 - len(rule))
                print(f'| {rule} | {joint_sup} | {pf} | {joint_conf * 100}% |')
                count += 1
    print(count)

    print('-----')

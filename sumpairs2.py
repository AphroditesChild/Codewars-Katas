def sum_pairs(lst, s):
    done = set()
    for item in lst:
        if s - item in done:
            return [s - item, item]
        done.add(item)

print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

input()

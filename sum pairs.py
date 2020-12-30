from itertools import combinations


def sum_pairs(ints, s):
    indexed_ints = [i for i in enumerate(ints)]
    valid_sums = [list(comb) for comb in combinations(indexed_ints, 2) if sum(c[1] for c in comb)==s]
    if len(valid_sums) > 0 :
        sums_sorted = sorted(valid_sums, key=lambda lst: max(tup[0] for tup in lst))
        pair = [tup[1] for tup in sums_sorted[0]]
        return pair
    else :
        return None
print(sum_pairs([10, 2, 2, 3, 7, 5], 10))
input()

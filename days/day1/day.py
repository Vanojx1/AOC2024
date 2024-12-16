from collections import Counter

def main(day_input):
    list_1, list_2 = [], []
    for row in day_input:
        n1, n2 = map(int, row.split('   '))
        list_1.append(n1)
        list_2.append(n2)
    list_1.sort()
    list_2.sort()

    s_l1 = list_1
    c_l2 = Counter(list_2)

    return sum(abs(n2-n1) for n1, n2 in  zip(list_1, list_2)), sum(n1*c_l2[n1] for n1 in s_l1)
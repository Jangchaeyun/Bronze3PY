len = int(input())
count_e = input().count('e')
print(['2', 'e', 'yee'][(count_e > len - count_e) + ((len - count_e) == count_e) * 2])
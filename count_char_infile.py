import pprint
import collections

"""
with open("sample_file.txt","r") as fr:
    count_data = collections.Counter(fr.read())
    count_value = pprint.pformat(count_data)

print(count_value)
"""
with open("sample_file.txt","r") as fr:
    data = fr.read()

str = data.replace("\n", "")
cnt = {}
count = 0
for each in str:
    for i in range(len(str)):
        if each == str[i]:
            cnt[each] = count+1

print(cnt)

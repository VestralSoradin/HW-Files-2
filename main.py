import os.path

file1_path = '1.txt'
file2_path = '2.txt'
file3_path = '3.txt'

with open(file1_path, 'r', encoding='utf-8') as f1:

    file1 = f1.readlines()
    #print(file1)
    #print(len(file1))
with open(file1_path, 'r', encoding='utf-8') as f1:
    content = f1.read()
    #print(content)

with open(file2_path, 'r', encoding='utf-8') as f2:
    file2 = f2.readlines()
    #print(file2)
    #print(len(file2))

with open(file3_path, 'r', encoding='utf-8') as f3:
    file3 = f3.readlines()
    #print(file3)
    #print(len(file3))
path_list = [file1_path, file2_path, file3_path]
file_list = [file1, file2, file3]
leng_list = [len(file1), len(file2), len(file3)]
#print(path_list)
#print(leng_list)

path_dict = dict(zip(path_list, leng_list))
sorted_paths = dict(sorted(path_dict.items(), key=lambda item: item[1]))
#print(sorted_paths)
#print(sorted_paths.keys())

#m = sorted(range(len(file_list)))
#print(m)
file_list.sort(key=len)
#print(file_list)

for o, i in zip(sorted_paths.keys(), file_list):
    print(o)
    print(len(i))
    print(*i)



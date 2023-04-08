# Not working on empty dir

import re, os

piilist = []
with open("rlist.txt", "r") as piidoc:
    piilist = (piidoc.read().splitlines())
#print(piilist)

filepathlist = []
for dirpath, dirnames, filenames in os.walk("/syblack/Documents/file_path_pii/testfiles"):
    for file in filenames:
        filepathlist.append(os.path.join(dirpath, file))
#print(filepathlist)

for stringpattern in piilist:
    regex = re.compile(stringpattern)
    for f in filepathlist:
        result = re.findall(regex, f)
        if not result == []:
            print(f,",".join(result))


# results = []
# for i in piilist:
#     for j in filepathlist:
#         if i in j:
#             results.append(j)
#         else:
#             continue
# print(results)
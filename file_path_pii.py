import re
import os

piilist = []
with open("find.txt", "r") as piidoc:
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
        # how to not print empty matches??
        result = re.findall(regex, f)
        print(f,",".join(result))


# results = []
# for i in piilist:
#     for j in filepathlist:
#         if i in j:
#             results.append(j)
#         else:
#             continue
# print(results)
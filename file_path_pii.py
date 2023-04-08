import os

# https://www.techbeamers.com/program-python-list-contains-elements/
# https://blog.finxter.com/how-to-check-if-items-in-a-python-list-are-also-in-another/

piilist = []
with open("find.txt", "r") as piidoc:
    for pii in piidoc:
        piilist = piidoc.read().splitlines()
#print(piilist)

filepathlist = []
for dirpath, dirnames, filenames in os.walk("/syblack/Documents/pii_file_path/testfiles"):
    for file in filenames:
        filepathlist.append(os.path.join(dirpath, file))
#print(filepathlist)

results = []
for i in piilist:
    for j in filepathlist:
        if i in j:
            results.append(j)
        else:
            continue
print(results)
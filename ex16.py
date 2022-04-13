from sys import argv
from os.path import exists


script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

in_file = open(from_file).read() #合并代码
#indata = in_file.read()

print(f"the input file is {len(in_file)} bytes long.
\ndoes the output file exist? {exists(to_file)} \n",
input("ready, hit return to continue , ctrl-c to abort.")) #合并代码

#print(f"does the output file exist? {exists(to_file)}")
#print("ready, hit return to continue , ctrl-c to abort.")
#input("ready, hit return to continue , ctrl-c to abort.")

out_file = open(to_file, 'a').write(in_file)

#out_file.write(indata)

print("alright, all done.")

#out_file.close()
#in_file.close()

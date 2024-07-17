import os
import sys


args = sys.argv[1:]

if ( len(sys.argv) != 2 ):
    print("Necesitas colocar el nombre del archivo de entrada.")
    exit(1)

if ( not os.path.isfile(sys.argv[1]) ):
    print("El archivo no es valido.")
    exit(1)

same_path, same_file = os.path.split(sys.argv[1])

f = open(sys.argv[1], "r")
nf = open(same_path + "/new_" + same_file, "w")

for line in f:
    fields = line.split(",", 2)
    nf.write(fields[0] + ";" + fields[1] + ";" + fields[2].replace("\n","").replace("\r", "").replace(",", "").replace(".", ",") + "\n")

exit(0)
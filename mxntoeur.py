import os
import sys




def validate_params(args):
    if ( len(args) != 2 ):
        print("Necesitas colocar el nombre del archivo de entrada.")
        print("Ejemplo: " + args[0] + " archivo.txt")
        exit(1)
    return(0)


def validate_file(args):
    if ( not os.path.isfile(args[1]) ):
        print("El archivo no puede leerse.")
        if ( os.name == "nt" ):
            print("Intenta colocar el nombre entre comillas")
            print("Ejemplo: " + args[0] + " \"C:\archivo.txt\"\n")
            print("o colocar el caracter \ de la siguiente forma \\")
            print("Ejemplo: " + args[0] + " C:\\\\archivo.txt")
        exit(1)


def open_files(args):
    same_path, same_file = os.path.split(args[1])

    if ( os.name == "posix" ):
        new_file = same_path + "/new_" + same_file
    else:
        new_file = same_path + "\\new_" + same_file
    print(f"Se creara el archivo: {new_file}")

    f = open(args[1], "r")
    nf = open(new_file, "w")

    return f, nf


def write_file(f, nf):
    for line in f:
        fields = line.split(",", 2)
        nf.write(fields[0] + ";" + fields[1] + ";" + fields[2].replace("\n","").replace("\r", "").replace(",", "").replace(".", ",") + "\n")
    print("Se ha escrito el archivo correctamente.")


def close_file(f, nf):
    f.close()
    nf.close()
    print("Se han cerrado los archivos.")


def convert_file(args):
    validate_params(args)
    validate_file(args)
    f, nf = open_files(args)
    write_file(f, nf)
    close_file(f, nf)
    print("Ha concluido el proceso de transformación.")


if __name__ == '__main__':
    args = sys.argv[0:]
    convert_file(args)
    exit(0)
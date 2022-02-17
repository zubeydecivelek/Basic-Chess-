import sys

harf_sayi={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,
           "Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26," ":27}

def divlist(list1):
    a,b,c,list= len(key),0,1,[]
    while a*c <= len(list1):
        if len(list1)%len(key)==0:
            list.append(list1[a*b:a*c])
            b,c=b+1,c+1
        else:
            while len(list1)%len(key)!=0:
                list1.append(" ")
    return list

def mulmatrix(a,b):
    result=[[0] for i in range(len(a))]
    for i in range(len(b)):
        for j in range(len(a[0])):
            for k in range(len(a)):
                result[i][j]+=b[i][k]*a[k][j]
    return result

def encoding(list):
    final=[]
    for i in divlist(list):
        a=[[(harf_sayi[j])] for j in i]
        b=(mulmatrix(a,key))
        for i in b:
            for j in i:
                final.append(j)
    return final

def birimmatrix(uzunluk):
    I=[]
    for i in range(uzunluk):
        satir=[]
        for j in range(uzunluk):
            if i==j:
                satir.append(1)
            else:
                satir.append(0)
        I.append(satir)
    return I

def tersmatrix(matrix1):
    n = len(matrix1)
    matrix=[i[:] for i in matrix1]
    Imatrix=birimmatrix(n)
    for sabit in range(n):
        sabitcarpan = 1/matrix[sabit][sabit]
        for x in range(n):
            matrix[sabit][x] *=sabitcarpan
            Imatrix[sabit][x] *=sabitcarpan
        for i in range(n):
            if sabit != i:
                carpan = matrix[i][sabit]
                for j in range(n):
                    matrix[i][j] -= carpan*matrix[sabit][j]
                    Imatrix[i][j] -= carpan*Imatrix[sabit][j]

    for i in range(n):
        for j in range(n):
            Imatrix[i][j]=round(Imatrix[i][j])

    return Imatrix

def divdecodinglist(liste):
    a,b,c,list=len(key),0,1,[]
    while a*c <= len(liste):
        list.append(liste[a*b:a*c])
        b,c=b+1,c+1
    return list

def decoding(list):
    final=[]
    for i in divdecodinglist(list):
        a=[[j] for j in i]
        b=mulmatrix(a,tersmatrix(key))
        for i in b:
            for j in i:
                final.append(int(j))
    return final

def get_key(val):
    key_list = list(harf_sayi.keys())
    val_list = list(harf_sayi.values())
    return (key_list[val_list.index(val)])

try:
    assert len(sys.argv) == 5
    if sys.argv[1] not in ["enc","dec"]:
        raise UnicodeError
    if sys.argv[1]=="enc":
        file="Input"
        a=open(sys.argv[3], "r")
        list1=[i.upper() for i in a.readline()]
        if list1==[]:
            raise SyntaxError
        for i in list1:
            if i not in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwXxYyZz ":
                raise ArithmeticError
    elif sys.argv[1]=="dec":
        file="Input"
        a = open(sys.argv[3],"r")
        decode=list(eval(a.readline()))
    if sys.argv[3][-4:] != ".txt":
        raise ChildProcessError
    file="Key"
    b=open(sys.argv[2],"r")
    if sys.argv[2][-4:]!= ".txt":
        raise BrokenPipeError
    key=[]
    for i in b:
        if "\n" in i:
            key.append(i.strip("\n").split(","))
        else:
            key.append(i.split(","))
    for i in range(len(key)):
        for j in range(len(key[0])):
            key[i][j]=int(key[i][j])
    if key==[]:
        raise EnvironmentError

    output = open(sys.argv[4],"w")

    if sys.argv[1]=="enc":
        print(*encoding(list1),sep=",", file=output)
        a.close(),output.close(),b.close()
    elif sys.argv[1]=="dec":
        zubb=[get_key(i) for i in decoding(decode)]
        print(*zubb,sep="",file=output)
        a.close(),output.close,b.close()

except AssertionError:
    print("Parameter number error")
except UnicodeError:
    print("Undefined parameter error")
except FileNotFoundError:
    print(file,"file not found error")
except ChildProcessError:
    print("The input file could not be read error")
except ArithmeticError:
    print("Invalid character in input file error")
except BrokenPipeError:
    print("Key file could not be read error")
except EnvironmentError:
    print("Key file is empty error")
except ValueError:
    print("Invalid character in key file error")
except NameError:
    print("Invalid character in input file error")
except SyntaxError:
    print("Input file is empty error")

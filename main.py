print("Hello World")
print("Hello \"my name\" World")


print('''Hello mu name is ''')
print("Saya", "makan", sep = '', end='-')
print("hello")

# Variables
a = 12
print(a)

# snake_case
nama_makanan = "Nasi Goreng"

nama = "Budi"
umur = 12

print("Nama = %s, Umur = %d" %(nama,umur))
print(r"Hello \nWorld")
print(f"Nama = {nama}, Umur = {umur}")
print(a)

kalimat = "Saya makan nasi bakar"
print(len(kalimat))

print(kalimat[5:10])

a = "Batu"
b = "Kertas"

temp = a
a = b
b = temp
print(a)
print (b)

# floor
a = 5//2
print(a) # round ke bawah

b = 5/2
print(b)

# pangkat
b = 2**3
print(b)

# input
a = input()
print(a*2) # hasilnya 22

a = 1
if(a==1):
    print("a adalah 1")
elif(a==2):
    print("ini adalah dua")
else:
    print("tidak tahu")

# ternary
temp = "ini satu" if(a==1) else "bukan satu"
print(temp)

a = 3
match a:
    case 1:
        print("ini satu")
    case 2:
        print("ini dua")
    case _:
        print("tidak sesuai")
# looping
print("ini while")
a = 10
while a > 0:
    print(a)
    a -= 1

print("ini for")
for a in range(5,10, 2):
    print (a)
# a di increment

# array list/collection
# list, tuple, set, dictionary

# list
test_list = ["Ayam", "Nasi", "Micin"]
test_list.append("Burger")
test_list.insert(1, "Hello")
test_list.sort()
print(test_list)

#Tuple
test_tuple = (1, 2, 3, 4, 5)
print(test_tuple)

#set
test_set = {1,2,3,4,5,5,7,8, 'ayam'}
test_set.add(10)
print(test_set)
# posisi ga jelas
# print unique value

#dictionary
test_dict = {
    "Nama" : "Valencius Rianto",
    "Semester" : 4,
    "BNCCID" : "BNCC212322"
}
# test_dict.pop("Nama")
test_dict.update({"Nama" : "Ming-Ming"})
print(test_dict)

#function
def printHello():
    print("Hello World")

def tambah(a,b):
    print(a+b)

def kali(a,b):
    return a*b

temp = kali(10,2)
print(temp)

a = int(input())
print(a*2)
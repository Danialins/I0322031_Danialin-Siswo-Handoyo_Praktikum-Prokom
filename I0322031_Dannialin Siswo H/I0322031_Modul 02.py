#input
nama = input("masukkan nama: ")
print("halo, "+ nama,"kun :)" )

#challenge 1
id = int(input("masukkan id= "))
print ("id= " + str(id),)

nama = "Dani"
tahun = "2004"
print (type(nama))
print (type(tahun))
print (type("TI UNS"))

#numerik 
a = 10
b = 5
print(a + b)
print(a - b)

x = 10
user = int(input("Enter a number: "))

while user != x:
    if user > x:
        print("Too high")
    elif user < x:
        print("Too low")
    else:
        print("Number correct")
    user = int(input("Enter a number: "))

#challenge 2
x = 10
y = 3

command = 5(input("Masukkan command: "))
if command == 1:
    print(f"{x} pangkat {3} = {x ** y}") # output seharusnya 1000
else:
    print("Command tidak dikenali")

mie_iblis = 13.5
udang_keju = 13

print("harga total adalah {} ribu rupiah".format((mie_iblis + udang_keju)*1000))

x = 121.5689
# dibulatkan ke atas
print("x ceil = {:.2f}".format(x))

# challenge 3
# modifikasi value x dan y
x = 120,5
y = 120,5
print(f"x + y = {x + y}") # x + y should be 241

# challenge 4
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list2[__:__:__]) # output seharusnya [9, 7, 5, 3, 1]

# challenge 5
ls = ["John", 25, True, 3.14, "apple"]
ls.___(__, ___)
print(ls) # Output: ['John', 25, 'orange', True, 3.14, 'apple']
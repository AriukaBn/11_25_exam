phonebook = {}

while True:
    print("\n1.Нэмэх  2.Хайх  3.Устгах  4.Бүгдийг харах  5.Гарах")
    choice = input("Сонголт: ")

    if choice == "1":
        name = input("Нэр: ")
        phone = input("Утас: ")
        phonebook[name] = phone

    elif choice == "2":
        name = input("Хайх нэр: ")
        print(phonebook.get(name, "Олдсонгүй"))

    elif choice == "3":
        name = input("Устгах нэр: ")
        phonebook.pop(name, None)

    elif choice == "4":
        for name, phone in phonebook.items():
            print(name, ":", phone)

    elif choice == "5":
        break
        
        
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Нэмэх
add = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("Нэмэх:", add)

# Үржүүлэх
mul = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            mul[i][j] += A[i][k] * B[k][j]
print("Үржүүлэх:", mul)

# Транспос
transpose = [[A[j][i] for j in range(2)] for i in range(2)]
print("Транспос:", transpose)



students = []

while True:
    print("\n1.Нэмэх 2.Харах 3.Хайх 4.Гарах")
    ch = input("Сонголт: ")

    if ch == "1":
        name = input("Нэр: ")
        age = input("Нас: ")
        grade = input("Дүн: ")
        students.append({"name": name, "age": age, "grade": grade})

    elif ch == "2":
        for s in students:
            print(s)

    elif ch == "3":
        name = input("Хайх нэр: ")
        for s in students:
            if s["name"] == name:
                print(s)

    elif ch == "4":
        break
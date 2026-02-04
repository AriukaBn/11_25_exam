# a = input()
# b = a.split(' ')
# if int(b[0]) == 12 and int(b[1]) == 1 and int(b[2]) == 2:
#     print('winter')
# elif int(b[0]) == 3 and int(b[1]) == 4 and int(b[2]) == 5:
#     print('spring')
# elif int(b[0]) == 6 and int(b[1]) == 7 and int(b[2]) == 8:
#     print('summer')
# elif int(b[0]) == 9 and int(b[1]) == 10 and int(b[2]) == 11:
#     print('autumn')
# else:
#     print('utga oruul')



# a = int(input())
# if (a - 1) == 0:
#     print(1500)
# elif a > 1 and a < 5:
#     print(((a-1) * 1000) + 1500)
# elif a > 5 and a < 10:
#     print(((a-1) * 800) + 1500)
# else:
#     print(((a-1) * 600) + 1500)




# a = input("weight, height: ").split(' ')
# BMI = int(a[0]) / pow(float(a[1]), 2)
# if BMI >= 30:
#     print("Targalalt")
# elif BMI >= 25:
#     print("Iluudel jintei")
# elif BMI >= 18.5:
#     print("Heviin")
# else:
#     print("Turanhai")



# a = input().split(' ')
# if (a[0] + a[1] > a[2]) and (a[0] + a[2] > a[1]) and (a[1] + a[2] > a[0]):
#     print('Gurwaljin Mun')
#     if a[0] == a[1] == a[2]:
#         stype = 'Adil Talt'
#     elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
#         stype = 'Adil Hajuut'
#     else:
#         stype = 'Eldev Talt'
#     b=int(a[0])
#     c=int(a[1])
#     d=int(a[2])
#     sides = sorted([b,c,d])
#     s1,s2,s3 = sides[0],sides[1],sides[2]
#     if s1**2 + s2**2 == s3**2:
#         atype = 'Tegsh Untsugt'
#     elif s1**2 + s2**2 < s3**2:
#         atype = 'Mohoo Untsugt'
#     else:
#         atype = 'Hurts Untsugt'
        
#     print(f'{stype} {atype}')
# else:
#     print('Gurvaljin Bish')



# import random
# songolt = ["chuluu", "haich", "tsaas"]
# gar = input("chuluu, haich, tsaas: ").lower()
# ranc = random.choice(songolt)
# print(f'Random choice: {ranc}')
# if gar == ranc:
#     print('draw')
# elif (gar == 'haich' and ranc == 'tsaas') or (gar == 'tsaas' and ranc == 'chuluu') or (gar == 'chuluu' and ranc == 'haich'):
#     print('You Won!!!')
# elif gar in songolt:
#     print('Lose')
# else:
#     print('garnaas orson utga buruu!!!')

# l=[1,3,4,5,6,7,8,]
#
#
#
# split = 2
# tafel = []
# vel = []
# for apple in l:
#     if apple == split:
#         tafel.append(vel)
#         vel = []
#     else:
#         vel.append(split)
#         tafel.append(vel)
#
# print(tafel)
#
#
# lijst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# splitwaarde = 6
# hoodfveld = []
# subveld = []
# for item in lijst:
#     if item == splitwaarde:
#         hoodfveld.append(subveld)
#         subveld = []
#     else:
#         subveld.append(splitwaarde)
#         hoodfveld.append(subveld)
#
#         print(hoodfveld)

#variable genoemd count met de waarde 0
count = 0

#als de waarde kleinder dan 5 is-
if count < 5:
    #print dat deze string plus de waarde van count uit
    print("Hoi ik ben een if statment en het getal is nu: ", count)
    #zolang de condition true is begin opnieuw, dus hier zolang count kleiner dan 5 is
    while count < 5:
        #print deze string uit met de waarde van count uit
        print("Ik ben een while statement en het getal is nu: ", count)
        #tel steeds 1 waarde bij count op. hier staat count = count + waarde maar dan afgekort
        count += 1
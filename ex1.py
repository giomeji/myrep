import random
pleures = int(input("give the side of the square"))
places = pleures**2

if places % 2 == 1:#βρίσκω πόσες θέσεις θα γεμισω με 1 και 0 αντίστοιχα
    positions = round(places/2) + 1

else:
    positions =  round(places/2)


sum = 0
for w in range (100):#γεμίζω όλες τις διαθέσιμες θέσεις
    noumera=[0,1]
    l1 = 0
    l0 = 0
    pinakas = []
    for i in range (pleures):
        list=[]
        for j in range (pleures):
            number = random.choice(noumera)
            if number == 1 and l1 < positions:
                list.append(number)
                l1 = l1 + 1
            elif number == 0 and l0 < places - positions:
                list.append(number)
                l0 = l0 + 1
            elif l1 == positions:
                    list.append(0)
            elif l0 == places - positions :
                    list.append(1)
        pinakas.append(list)
    
#αρχικοποιώ τους μετρητές για κάθε είδος τετράδας απο μονάδες (οριζόντια, κάθετα, διαγώνια)
    kathet = 0
    orizo = 0
    diagwn = 0

#καθετα
    for i in  range(pleures):
        ka = 0
        for j in range(pleures):
            if pinakas[j][i] == 1:
                ka = ka + 1
                if ka == 4:
                   kathet = kathet + 1
            else:
                ka = 0

#οριζοντια
    for z in  range(pleures):
        oz = 0
        for q in range(pleures):
            if pinakas[z][q] == 1:
                oz = oz + 1
                if oz == 4:
                   orizo = orizo + 1
            else:
                oz = 0

#διαγωνια
    for i in range(pleures):
        for j in range(pleures):
            if i == pleures -4 and j == pleures - 4:
                if pinakas[i][j] == pinakas[i+1][j+1] and pinakas[i][j] == pinakas[i+2][j+2] and pinakas[i][j] == pinakas[i+3][j+3] and pinakas[i][j]==1:
                     diagwn = diagwn + 1
                if pinakas[i][j] == pinakas[i+1][j-1] and pinakas[i][j] == pinakas[i+2][j-2] and pinakas[i][j] == pinakas[i+3][j-3] and pinakas[i][j]==1:
                    diagwn = diagwn + 1
#αφού έχω βρεί τους μετρητές για κάθε είδος τετράδας απο μονάδες τις προσθέτω όλες στο sum που εχω αρχικοποιήσει εξω απο την επαναληψη που κανει 100 φορες το
#πρόγραμμα για την ιδια διασταση, ετσι ωστε να εχω ενα συνολικο αριθμο απο ολες τις τετραδες που εμφανιστηκαν σε ολες τις 100 φορες
    sum = sum + orizo + kathet + diagwn
#διαιρω το sum με 100 για να βρω τον μεσο ορο των τετραδων
mesosoros = sum /100
print(mesosoros)

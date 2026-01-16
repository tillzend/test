cash = 287

# sotki
sotki = cash // 100
ostatok = cash % 100
print ("v summe sotok: " , sotki)

#paltoss
paltoss = ostatok // 50
ostatok = ostatok % 50
print ("v summe paltossov: " , paltoss)

# dvadsatki
dvadsatki = ostatok // 20
ostatok = ostatok % 20
print ("v summe dvadsatok: " , dvadsatki)

#pyaterochka 
pyaterochka = ostatok // 5
ostatok = ostatok % 5
print ("v summe pyatorok: " , pyaterochka)

#odinichka
odinichka = ostatok // 1
ostatok = ostatok % 1
print ("v summe odinichek: " , odinichka)

total_count = sotki+paltoss+dvadsatki+pyaterochka+odinichka
print ("count of bill:" , total_count)
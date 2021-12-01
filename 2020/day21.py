_list=list(open("day21.txt").read().splitlines())

allallergens=set()
foods=[]
for line in _list:
    ingredients=set(line.split(' (contains ')[0].split(' '))
    allergens=line.split(' (contains ')[1][:-1].split(', ')
    foods.append((ingredients,allergens))
    for allergen in allergens:
        allallergens.add(allergen)

unsafeingredients=[]
allergendict={}
for allergen in allallergens:
    possibles=[]
    for food in foods:
        if allergen in food[1]:
            possibles.append(food[0])
    possible=set.intersection(*possibles)
    allergendict[allergen]=list(possible)
    unsafeingredients.append(possible)
    
unsafeingredients=set.union(*unsafeingredients)
count=0
for food in foods:
    for ingredient in food[0]:
        if ingredient not in unsafeingredients:
            count+=1
print(count)

while sum(len(allergendict[allergen]) for allergen in allallergens) >len(allallergens):
    for allergen in allallergens:
        if len(allergendict[allergen])==1:
            remove=allergendict[allergen][0]
            for allergenb in allallergens:
                if allergenb==allergen:
                    continue
                if remove in allergendict[allergenb]:
                    allergendict[allergenb].remove(remove)

for key in sorted(allergendict):
    print(allergendict[key][0],end=',')
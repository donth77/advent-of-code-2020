from collections import Counter

ingredientSet  = set()
allergenMap = dict()
ingredientLst = []

with open('input.txt') as fp:
  line = fp.readline()
  while line:
    tokens = line.strip()[:-1].split(' (contains ')
    ingredients = tokens[0].split()
    allergens = tokens[1].split(', ') 
    ingredientSet = ingredientSet.union(set(ingredients))
    ingredientLst += ingredients

    for allergen in allergens:
      if allergen in allergenMap:
        allergenMap[allergen] = allergenMap[allergen].intersection(set(ingredients))
      else:
        allergenMap[allergen] = set(ingredients)

    line = fp.readline()

# Part 1
safeIngredients = ingredientSet
for ingreds in allergenMap.values():
  safeIngredients = safeIngredients.difference(ingreds)

print(f'Part 1\n{sum(Counter(ingredientLst)[ing] for ing in safeIngredients)}')

# Part 2
sortedAllergens = sorted(allergenMap.keys(), key=lambda allergenKey: len(allergenMap[allergenKey]))
for aKey1 in sortedAllergens:
    if len(allergenMap[aKey1]) == 1:
        ingred = next(iter(allergenMap[aKey1]))
        for aKey2 in sortedAllergens:
            if aKey2 != aKey1:
                allergenMap[aKey2].discard(ingred)

sortedDangerous = ",".join([next(iter(allergenMap[key])) for key in sorted(allergenMap.keys())])

print(f'\nPart 2\n{sortedDangerous}')
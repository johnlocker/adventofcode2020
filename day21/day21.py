with open('input.txt') as f:
	lines = f.read().splitlines()
import numpy as np

def getDangerousIngredients(lines):
    allerDic = {}
    ingredients = []
    for line in lines:
        lineSp = line.replace("(", "").replace(")", "").split(" contains")
        curIngredients = lineSp[0].split(" ")
        ingredients += curIngredients
        allers = lineSp[1].strip().split(", ")
        for aller in allers:
            if aller not in allerDic:
                allerDic[aller] = set(curIngredients)
            else:
                allerDic[aller] &= set(curIngredients)   

    allerIngredients = []
    keys = sorted(list(allerDic.keys()))
    for key in keys:
        value = allerDic[key]
        for val in value:
            if val not in allerIngredients:
                allerIngredients.append(val)

    noAllerList = list(np.setdiff1d(ingredients, allerIngredients))
    count = 0
    for noAller in noAllerList:
        count += ingredients.count(noAller)
    print("No allergen ingredients:", count)
    uniqueDic = {}
    while any([len(val) > 0 for val in allerDic.values()]):
        for key, val in allerDic.items():
            if len(val) == 1:
                uniqueDic[key] = val.pop()
        for key in allerDic:
            allerDic[key] -= set(uniqueDic.values())

    out = uniqueDic[sorted(uniqueDic.keys())[0]]
    for key in sorted(uniqueDic.keys())[1:]:
        out += "," + uniqueDic[key]
    print("Dangerous ingredients list:", out)

print(getDangerousIngredients(lines))
def cakes(recipe, available):
    if not set(recipe).issubset(available): return 0

    for ing in recipe:
        if recipe[ing] > available[ing]: return 0

    return min([available[ing] // recipe[ing] for ing in recipe])




recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}


print(cakes(recipe, available))

input()

import os

def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    for dish in dishes:
        for ingrid in cook_book.get(dish):
            search_food = list_by_dishes.get(ingrid['ingredient_name'], 0)
            if search_food:
                search_food = int(search_food['quantity'])
            list_by_dishes[ingrid['ingredient_name']] = {'measure':ingrid['measure'], 'quantity': int(ingrid['quantity']) * person_count + search_food}
    print(list_by_dishes)

current = os.getcwd()
file_name = 'recipes.txt'
full_path = os.path.join(current, file_name)
with open(full_path, 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingred = f.readline().strip()
            ingredient_name, quantity, measure = ingred.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        f.readline()
        cook_book[dish] = ingredients
    #print(cook_book)


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

get_shop_list_by_dishes(dishes, person_count)
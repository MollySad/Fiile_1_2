def cook(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            cook_book[line.strip()] = []
            component_quantity = int(file.readline().strip())
            for component in range(component_quantity):
                dish = line.strip()
                ing = file.readline().strip().split(' | ')
                es = {'ingredient_name': ing[0], 'quantity': ing[1], 'measure': ing[2]}
                cook_book[dish].append(es)
            file.readline()
    return cook_book

print(cook('recipes.txt'))


def get_shop_list_by_dishes(dishes, persons):
    cook_book = cook('recipes.txt')
    shop_list = {}

    for dish in dishes:
        for item in cook_book[dish]:
            items_list = [(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})]
            if shop_list.get(item['ingredient_name']):
                items_list = [(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons*2})]
                shop_list.update(items_list)
            else:
                shop_list.update(items_list)
    return shop_list

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

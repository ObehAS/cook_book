def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list

# Запрос
dishes_to_prepare = ['Запеченный картофель', 'Омлет']
person_count = 2
result = get_shop_list_by_dishes(dishes_to_prepare, person_count)

# Результата спском
for ingredient, details in result.items():
    print(f"{ingredient}: {details}")

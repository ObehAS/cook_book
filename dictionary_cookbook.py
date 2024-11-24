def read_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        i = 0
        while i < len(lines):
            dish_name = lines[i]
            num_ingredients = int(lines[i + 1])
            ingredients = []
            for j in range(num_ingredients):
                ingredient_line = lines[i + 2 + j].split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_line,
                    'quantity': int(ingredient_line[1]),
                    'measure': ingredient_line[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            i += 2 + num_ingredients
    return cook_book

file_path = 'cook_book.txt'
cook_book = read_cook_book(file_path)
print(cook_book)
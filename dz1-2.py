
def cook_book_creation():
    with open('reciptes.txt', 'rt', encoding='utf8') as f1:
        cook_book = {}
        for line in f1:
            dish = line.strip()
            cook = []
            number_of_ingredients = f1.readline()
            for i in range(int(number_of_ingredients)):
                ingredients = f1.readline()
                ingredient_name, quantity, measure = ingredients.split(' | ')
                cook1 = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                cook.append(cook1)
                cook_book[dish] = cook
            f1.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_creation()
    shop_list = {}
    product_list=[]
    for dish in dishes:
        c = cook_book.get(dish)
        for a in c:
            product = a.get("ingredient_name")
            product_list.append(product)
            quantity = int(a.get("quantity")) * person_count
            if product == a.get("ingredient_name"):
                quantity += int(a.get("quantity")) * person_count
            measure = a.get("measure")
            cook1 = {'measure': measure.strip(), 'quantity': int(quantity)}
            shop_list[product] = cook1

    for key, value in shop_list.items():
        print(key, value, end='\n')


dishes = ['Омлет', 'Фахитос']
person_count = 2

get_shop_list_by_dishes(dishes, person_count)
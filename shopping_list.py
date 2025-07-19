#shopping list assignment
import requests,json
shopping_list = []

shopping_list = list(requests.get("https://fakestoreapi.com/products?limit=5").json())

#function to add items to list
def add_item(item):
    try:
        shopping_list.append(item)
        return shopping_list
    except Exception as e:
        return "not inserted",e
#function to remove item from list
def remove_item(id):
    if shopping_list:
        k = -1
        for(key,value) in enumerate(shopping_list):
            if value['id'] == id:
                k = key
                break
        if k != -1:
            shopping_list.pop(key)
            return shopping_list
        else:
             return "Items not in list"
    else:
        return "No items in list"
    

while(1):
    data = int(input("What do yo want to do:\n1.Display list.\n2.Add Item.\n3.Delete Item.\n"))
    if data == 1:
        print(shopping_list)
    elif data == 2:
        item = dict(json.loads(input("Enter the item")))
        new_list = add_item(item)
        print(new_list)
    elif data == 3:
        id = int(input("Enter the id of item to be removed"))
        new_list = remove_item(id)
        print(new_list)
    else:
        print("Wrong input")
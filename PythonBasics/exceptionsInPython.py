itemsinCart = 0
#2 items will be added

if itemsinCart != 2:
    # raise Exception("There are no products in the cart")
    pass

assert(itemsinCart == 2)

#try and catch
try:
    with open("filelog.txt", "r") as reader:
        reader.read()
except:
    print("File not readable")

try:
    with open("filelog.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)
#clean the data, final step
finally:
    print("cleaning up resources")

# --------------------
ItemsInCart = 0


def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")
    ItemsInCart = ItemsInCart + items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


try:
    add_to_cart(2)  # Add 2 items
    add_to_cart(-1)  # This should raise an exception
except Exception as e:
    print(e)

# ----------------------
person = ("Rahul", 25, 5.9)

print(f"Age: {person[1]}")

try:
    person[0] = "name"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")
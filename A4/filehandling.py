
## Task 1
import os


def save_sales():
    sales=[1200, 450, 980, 1500, 3000]
    with open("sales_data.txt", "w") as file:
        for sale in sales:
            file.write(f"{sale}\n")

    # optional
    with open("sales_data_csv.txt", "w") as file:
        for sale in sales:
            file.write(f"{sale},")

    with open("sales_data.txt", "r") as file:
        content = file.read()
        print("Content of sales_data.txt:")
        print(content)



## Task 2
def read_sales():
    with open("sales_data.txt", "r") as file:
        content = file.read()
        print("Reading sales data as a single string:")
        print(content)

    with open("sales_data.txt", "r") as file:
        content = file.readline()
        print("Reading first line from sales data:")
        print(content)

    with open("sales_data.txt", "r") as file:
        sales_list = [int(line.strip()) for line in file.readlines()]
        print("Reading sales data into a list of integers:")
        print(sales_list)

## Task 3
def update_sales():
    with open("sales_data.txt", "a") as file:
        new_sales = [5000, 2500, 1700]
        for sale in new_sales:
            file.write(f"{sale}\n")

    with open("sales_data.txt", "r") as file:
        content = file.read()
        number_of_sales = len(content.strip().split("\n"))
        print(f"Total number of sales entries: {number_of_sales}")
        print("Updated sales data:")
        print(content)

    
## task 4
def sales_summary():
    with open("sales_data.txt", "r") as file:
        sales_list = [int(line.strip()) for line in file.readlines()]
        total_sales = sum(sales_list)
        average_sales = total_sales / len(sales_list) if sales_list else 0
        max_sale = max(sales_list) if sales_list else 0
        min_sale = min(sales_list) if sales_list else 0

        print(f"Total Sales: {total_sales}")
        print(f"Average Sales: {average_sales}")
        print(f"Maximum Sale: {max_sale}")
        print(f"Minimum Sale: {min_sale}")


## Task 5
def save_products():
    list_of_products = []
    for i in range(3):
        name=input(f"Enter {i+1} names ")
        price=int(input(f"Enter price for {name}: "))
        product={"name":name,"price":price}
        list_of_products.append(product)

    with open("products.txt", "w") as file:
        for product in list_of_products:
            file.write(f"{product['name']}|{product['price']}\n")

    with open("products.txt", "r") as file:
        for line in file.readlines():
            name, price = line.strip().split("|")
            print(f"Product Name: {name}, Price: {price}")

## Task 6
def load_file():
    name=input("Enter file name to load: ")
    if os.path.exists(name.strip()):
        with open(name, "r") as file:
            content = file.read()
            print(f"Content of {name}:")
            print(content)
    else :
        print(f"File not found: {name}. please check the file name and try again.")

## Task 7
def discounted_sales():
    items = {
        "Mouse": 500,
        "keyboard": 800,
        "monitor": 7000,
        "Pendrive": 400,
        "Camera": 5000
    }

    total_price = sum(items.values())
    average_dicounted_price = 0

    discount_rate = float(input("Enter discount rate (e.g., 0.1 for 10%): "))  # 10% discount
    with open("discounted_sales.txt", "w") as file:
        for item, price in items.items():
            discounted_price = price * (1 - discount_rate)
            average_dicounted_price += discounted_price
            file.write(f"{item}|{price}|{discounted_price:.2f}\n")

    with open("discounted_sales.txt", "r") as file:
        for line in file.readlines():
            item, original_price, discounted_price = line.strip().split("|")
            print(f"Item: {item}, Original Price: {original_price}, Discounted Price: {discounted_price}")
    
    average_dicounted_price /= len(items)
    # optional
    print(f"Total Price before Discount: {total_price}")
    print(f"Average Discounted Price: {average_dicounted_price:.2f}")

#save_sales()
#read_sales()
#update_sales()
#sales_summary()
#save_products()
load_file()
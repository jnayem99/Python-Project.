def add_product():
    product_name = input("Enter Product Name: ").strip()
    if not product_name:
        print("Product name cannot be empty.")
        return

    try:
        total_stock = int(input("Enter Total Stock: ").strip())
        number_of_order = int(input("Enter Number of Orders: ").strip())
        shortage = int(input("Enter Shortage: ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values for stock, orders, and shortage.")
        return

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                record = line.strip().split(", ")
                if record[0] == product_name:
                    print("Product already exists. Cannot add duplicate product name.")
                    return

    with open(FILE_NAME, "a") as file:
        file.write(f"{product_name}, {total_stock}, {number_of_order}, {shortage}\n")
    print("Product added successfully!")
import os

FILE_NAME = "products.txt"

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

def display_products():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No records found.")
        return

    print("\nProduct Records:")
    with open(FILE_NAME, "r") as file:
        for line in file:
            try:
                product_name, total_stock, number_of_order, shortage = line.strip().split(", ")
                print(f"Product: {product_name}, Total Stock: {total_stock}, Orders: {number_of_order}, Shortage: {shortage}")
            except ValueError:
                print(f"Malformed line skipped: {line.strip()}")

def search_product():
    product_name = input("Enter Product Name to search: ").strip()

    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No records found.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            record = line.strip().split(", ")
            if record[0] == product_name:
                print(f"Record Found: Product: {record[0]}, Total Stock: {record[1]}, Orders: {record[2]}, Shortage: {record[3]}")
                return
    print("Record not found.")

def edit_product():
    product_name = input("Enter Product Name to edit: ").strip()
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No records found.")
        return

    updated_records = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            record = line.strip().split(", ")
            if record[0] == product_name:
                found = True
                print("Enter new details (leave blank to keep current value):")
                new_total_stock = input(f"New Total Stock (current: {record[1]}): ").strip() or record[1]
                new_number_of_order = input(f"New Number of Orders (current: {record[2]}): ").strip() or record[2]
                new_shortage = input(f"New Shortage (current: {record[3]}): ").strip() or record[3]
                updated_records.append(f"{product_name}, {new_total_stock}, {new_number_of_order}, {new_shortage}\n")
            else:
                updated_records.append(line)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Product updated successfully!")
    else:
        print("Product not found.")

def delete_product():
    product_name = input("Enter Product Name to delete: ").strip()

    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No records found.")
        return

    updated_records = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            record = line.strip().split(", ")
            if record[0] == product_name:
                found = True
                print(f"Product '{product_name}' deleted.")
            else:
                updated_records.append(line)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
    else:
        print("Product not found.")

def main_menu():
    while True:
        print("\n Inventory Management of Walton Wholesale Store:")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Search Product")
        print("4. Edit Product")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            edit_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

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
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
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
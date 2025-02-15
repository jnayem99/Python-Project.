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
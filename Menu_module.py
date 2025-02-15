def main_menu():
    while True:
        print("\nElectronic Product Inventory Management:")
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
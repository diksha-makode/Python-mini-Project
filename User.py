import datetime
from Product import Product
from Admin import Admin


class User:

    def display_product(self):   
        with open("product.txt","r") as fp:
            
            for p in fp:
                print(p.strip())
                sep_txt= p.strip().split(",")
                if (len(sep_txt)>=5):
                    print("P_Id          :",sep_txt[0])
                    print("P_Name        :",sep_txt[1])
                    print("P_Price       :",sep_txt[2])
                    print("P_Quantity    :",sep_txt[3])
                    print("P_Description :",sep_txt[4])

                    print("---------------------------")
        
                else:
                    pass


    def search_product(self, product_name):
        found = False
        with open("Product.txt", "r") as fp:
            for p in fp:
                sep_txt = p.strip().split(",")
                if len(sep_txt) >= 5:
                    if sep_txt[1] == str(product_name):
                        print("Product Found:", p)
                        found = True
                        break

        if not found:
            print("Product not Found")


   
    import datetime

    def Car_Booking(self, product_name, product_quantity):
        container = []
        found = False

        with open("Product.txt", "r") as fp:
            for p in fp:
                sep_txt = p.split(",")
                if len(sep_txt) >= 5:
                    if sep_txt[1] == str(product_name):
                        found = True
                        product_id = sep_txt[0]
                        product_price = int(sep_txt[2])
                        total_cost = product_price * product_quantity
                        Booking_details = (str(product_id), product_name, str(product_price), sep_txt[3].strip(), sep_txt[4].strip())

                        container.append(",".join(Booking_details) + "\n")
                    else:
                        container.append(p)

        if found:
            with open("Product.txt", "w") as fp:
                fp.writelines(container)

            # Read existing customer IDs from Booking.txt
            existing_customer_ids = set()
            try:
                with open("Booking.txt", "r") as fp:
                    for line in fp:
                        if line.startswith("Customer_ID:"):
                            existing_customer_ids.add(line.strip().split(": ")[1])
            except FileNotFoundError:
                pass  # If the file does not exist, we will create it later

            # Prompt the user to enter a unique customer ID
            while True:
                customer_id = input("Enter Customer ID: ")
                if customer_id in existing_customer_ids:
                    print("Customer ID already exists. Please enter a unique Customer ID.")
                else:
                    break

            customer_name = input("Enter Customer Name: ")
            customer_mobile = input("Enter Customer Mobile Number: ")
            date = datetime.datetime.now()

            with open("Booking.txt", "a") as fp:  # Use 'a' to append to the file
                fp.write(f"Customer_ID: {customer_id}\n")
                fp.write(f"Customer_Name: {customer_name}\n")
                fp.write(f"Customer_Mobile: {customer_mobile}\n")
                fp.write(f"Date: {date}\n")
                fp.write(f"Product: {product_name}\n")
                fp.write(f"Quantity: {product_quantity}\n")
                fp.write(f"Cost: {product_price}\n")
                fp.write(f"Total_Cost: {total_cost}\n")
                fp.write("\n")

            print("Booking Done.....", "\n", "Please pay the Bill using option 4")
            return True
        else:
            print("Product name not found")
        return False

    
    def pay_bill(self):
        customer_id = input("Enter Customer ID: ")
        booking_details = []
        total_cost = 0
        found_customer = False

        # Read booking details from Booking.txt
        with open("Booking.txt", "r") as booking_file:
            lines = booking_file.readlines()
            customer_info = {}
            for i, line in enumerate(lines):
                if "Customer_ID" in line and line.split(":")[1].strip() == customer_id:
                    found_customer = True
                    customer_info["Customer_ID"] = line.split(":")[1].strip()
                    customer_info["Customer_Name"] = lines[i+1].split(":")[1].strip()
                    customer_info["Customer_Mobile"] = lines[i+2].split(":")[1].strip()
                    product_name = lines[i+4].split(":")[1].strip()
                    product_quantity = int(lines[i+5].split(":")[1].strip())
                    product_price = int(lines[i+6].split(":")[1].strip())
                    total_cost = int(lines[i+7].split(":")[1].strip())
                    break

        if not found_customer:
            print("Customer ID not found.")
            return False

        # Read the products from Product.txt and update the quantities
        updated_products = []
        product_found = False
        with open("Product.txt", "r") as product_file:
            for line in product_file:
                sep_txt = line.strip().split(",")
                if len(sep_txt) >= 5:
                    if sep_txt[1] == product_name:
                        current_quantity = int(sep_txt[3])
                        if current_quantity >= product_quantity:
                            remaining_quantity = current_quantity - product_quantity
                            sep_txt[3] = str(remaining_quantity)
                            product_found = True
                        else:
                            print(f"Insufficient stock for product: {product_name}")
                            return False
                updated_products.append(",".join(sep_txt) + "\n")

        if not product_found:
            print("Product not found.")
            return False

        # Write the updated products back to Product.txt
        with open("Product.txt", "w") as product_file:
            product_file.writelines(updated_products)

        # Calculate the total bill and print it
        print("                      ")
        print("****** Your Bill ******")
        for key, value in customer_info.items():
            print(f"{key}: {value}")
        print(f"Product: {product_name}")
        print(f"Quantity: {product_quantity}")
        print(f"Cost: {product_price}")
        print(f"Total Cost: {total_cost}")
        print("                      ")
        print("****  Thank You For Payment  ****")

        return True


    
from Product import Product

class Admin:
    def add_product(self):
        while True:
                try:
                 
                    with open("Product.txt", "r") as fp:
                        product_id = int(input("Enter product id: "))
                        if len(str(product_id))< 3:
                            print("Product ID must be at least 3 Digit long")
                            continue

                        product_name = input("Enter product Name: ") 

                        for line in fp:
                            sep_txt = line.strip().split(",")
                            
                            if str(product_id )== sep_txt[0]: 
                                print("Product ID already exists. Please enter a unique ID.")
                                break    
                        
                            elif (len(sep_txt) >= 5) and product_name == sep_txt[1]:
                                    print("Product Name already exists. Please enter a unique Name.")
                                    break
        
                        else: 
                            product_price = int(input("Enter product price: "))
                            product_quantity = int(input("Enter Quantity: "))
                            product_description = input("Enter product description: ")
                        
                            New_entry = Product(product_id, product_name, product_price, product_quantity, product_description)
                                
                            with open("Product.txt","a") as fp:
                                fp.write(str(New_entry))
                                print("\nNew Product Added Successfully...")
                                break
            
                except FileNotFoundError: 
                    with open("Product.txt", "w") as fp:
                        pass
            
    
    def display_product(self):
        try:
            with open("Product.txt", "r") as fp:
                for p in fp:
                    sep_txt = p.strip().split(",")
                    if (len(sep_txt) >= 5):
                        print("P_Id        :", sep_txt[0])
                        print("P_Name      :", sep_txt[1])
                        print("P_Price     :", sep_txt[2])
                        print("P_Quantity  :", sep_txt[3])
                        print("P_Description:", sep_txt[4])
                        print("                           ")
                        print("This Product Available in Stock")
                    else:
                        pass 
        except FileNotFoundError:
            print("please Add Any Entry First Using Option 1")
        


    def search_product(self,product_id):

        with open("product.txt","r") as fp :
            for p in fp:
                try:
                    p.index(str(product_id),0,4)
                    print("product id found :",p)
                    break

                except ValueError:#(substring not found)
                    pass
            else:
                print("product not Found")



    def update_product(self, product_id):
        while True:
            try:
                with open("product.txt", "r") as fp:
                    lines = fp.readlines()  # Read all lines at once

                found = False
                updated_lines = []

                for line in lines:
                    sep_txt = line.strip().split(",")
                    if sep_txt[0] == str(product_id):
                        found = True
                        n_name = input("Enter new name: ")
                        # Check if the new name already exists
                        names = [item.strip().split(",")[1] for item in lines]
                        if n_name in names:
                            print("Product name already exists. Please choose a different name.")
                            break
                        
                        n_price = int(input("Enter new price: "))
                        n_quantity = int(input("Enter new quantity: "))
                        n_description = input("Enter new description: ")

                        update_product = sep_txt[:1] + [str(n_name), str(n_price), str(n_quantity), n_description]
                        updated_lines.append(",".join(update_product) + "\n")

                    else:
                        updated_lines.append(line)  # Keep un-updated lines

                if found and n_name not in names:
                    with open("product.txt", "w") as fp:
                        fp.writelines(updated_lines)
                        print("Product updated successfully")

                elif not found:
                    print("Product ID not found")
                    break

            except ValueError:
                print("Invalid input. Please enter a valid product ID.")

            if not found:  # If duplicate product ID not found
                continue  # Continue the loop to prompt again

            break


    def delete_product(self,product_id):
        container=[]  
        found = False
        with open("Product.txt","r") as fp:
            for line in fp:
                sep_txt=line.split(",")
                if (sep_txt[0]==str(product_id)):
                     found = True   
                else:
                  container.append(line)
        if (found==True):
            with open("product.txt","w") as fp:
                for line in container:
                    fp.write(line)
            print("product deleted successfully..") 

        else:
            print("Product does not exist ")



from Admin import Admin
from User import User

if(__name__=="__main__"):
    a_obj=Admin()
    u_obj=User()
    
    while True:

        print('''Welcome To Car Showroom Management System''')
        print("""
              1. Admin
              2. User
              3. Exit""")
        
        ch = int(input("Enter your Choice: "))
        
        if ch==1:
            admin_ch=0
            while (ch!=6):
                print('''
                        Admin Menu
                        1. Add Product
                        2. Display Product
                        3. Serch Product
                        4. Update Product
                        5. Delete Product
                        6. Exit
                        ''')
                admin_ch=int(input("Enter choice :"))
  
                if(admin_ch==1):
                    a_obj.add_product()
                    
                elif(admin_ch==2):
                    a_obj.display_product()   

                elif(admin_ch==3):
                    product_id=int(input("Enter product Id  to search:"))   
                    a_obj.search_product(product_id)

                elif(admin_ch==4):

                    product_id=int(input("Enter product Id  to update:"))
                    a_obj.update_product(product_id)

                elif(admin_ch==5):

                    product_id=int(input("Enter product Id  to delete:"))
                    a_obj.delete_product(product_id)

                elif(admin_ch==6):
                    print("Admin Exit")
                    break              


        elif ch==2:
            user_ch=0
            while user_ch !=5:
                print('''
                        User Menu:
                        1. Display Product
                        2. Search Product
                        3. Book Car 
                        4. Pay Bill
                        5.Exit
                      ''')
                
                user_ch=int(input("Enter your Choice :"))

                if (user_ch==1):
                    u_obj.display_product()
                    
       
                elif(user_ch==2):
                    product_name = input("Enter product Name to search :")
                    u_obj.search_product(product_name)
                    

                elif(user_ch==3):
                    product_name=(input("Enter product name to Book :"))
                    booking_quantity=int(input("Enter product quantity :"))
                    u_obj.Car_Booking(product_name,booking_quantity)

                elif(user_ch==4):
                    u_obj.pay_bill()

                elif(user_ch==5):
                    print("User Exit..") 
                            
                elif ch==3:
                    print("Exit...")
                    break

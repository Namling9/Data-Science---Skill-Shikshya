# print("Hello World")


# print(f"Sum of 5 and 5 : {5+5}") # 10

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(10))

# books = [
#     ("The Alchemist", "Fiction", 1988, 250),
#     ("The Da Vinci Code", "Mystery", 2003, 300),
#     ("A Brief History of Time", "Science", 1988, 150),
#     ("The Theory of Everything", "Science", 2002, 100),
#     ("Pride and Prejudice", "Fiction", 1813, 200),
#     ("To Kill a Mockingbird", "Fiction", 1960, 180),
#     ("The Catcher in the Rye", "Fiction", 1951, 220),
#     ("Angels & Demons", "Mystery", 2000, 210),
#     ("The Grand Design", "Science", 2010, 90),
#     ("1984", "Fiction", 1949, 190)
# ]
# # Function to filter books based on genre and year
# def filter_books(genre : str, year : int):
#     filter_list = []
#     for n, g, y,b in books:
#         if g == genre and y >= year:
#             filter_list.append(n)
#     return filter_list

# # Example call to the function
# print(filter_books("Mystery", 2000))

def msg_append(filename):
    
    while True :
        
        print('''
        Press 1 : To add message in the file
        press 2 : Exit''')
        
        try: 
            
            choice = int(input("Choose 1 or 2 : "))
            
            if choice == 1: 
                message = input("Enter the message: ")
                with open(filename, 'a+') as file: 
                    file.write(message)
                    print("Message added successfully ")

                    file.seek(0)
                    content = file.read()
                    print(content)
                    
            elif choice == 2:
                break
                
        except FileNotFoundError: 
            print("The given file doesn't exists yet")
        
        except Exception as e : 
            print(f"Error Occurs : {e}")
                
def read_file():

    filename = input("Enter the file name: ")

    try:
        # Open the file in 'a+' mode, which allows for both reading and appending
        with open(filename, 'a+') as file:
            file.seek(0) # Move pointer to the beginning to read the content
            content = file.read()
            print("\nCurrent file content:\n", content)

            # Uncomment the line below if you want to call msg_append after reading
            #msg_append(filename)
            
    except FileNotFoundError:
        print("The file does not exist. It will be created.")
        
    except Exception as e:
        print(f"Error occurred: {e}")

read_file()
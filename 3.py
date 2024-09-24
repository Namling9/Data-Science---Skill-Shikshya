# python3 -m venv "virtual environment name" <- to create virtual environment
# source "virtual environment name"/bin/activate <- to activate virtual environment
# ctrl + shift + p -> python interpreter -> select workspace (It will automatically activate the virutal environment whenever you open the particular folder/ project)


# git restore "file name" <- ( This command restore deleted file)
# git pull <- (This command download/pull the new file in local environment)

# Create branch
# git branch --help <- (gives documentation about branch)
# git branch --list <- (Listing branch you created)
# git branch "branch name" <- (create new branch)
# git checkout "branch name" <- (switches to the given branch name)
# git checkout -b "branch name" <- (create new branch and switch to it)
# git branch -d "branch name" <- (delete branch)
# git branch -D "branch name" <- (delete branch forcefully)
# git merge "branch name" <- (merge branch with current branch)
# git merge --abort <- (abort merge)
# git merge --continue <- (continue merge)
# git merge --no-commit <- (merge branch without commit)
# git branch -M main <- (rename the branch name to main 
# git push -u origin main <- (intitialising main branch for every push operation)
# git diff branch name <- (to compare commit, branches, files & more)
# git pull origin main <- ( used to fetch and download content from a remote repo and immediately update
# the local repo to match the content).

# git push origin branch_name
# Undoing Changes

'''Case 1 : Staged changes (add .)

git reset <- file name -> <-(reset one file)
git reset <- (reset many files)

'''

''' Case 2: commited changes (for one commit)
  
  git reset HEAD~1
'''

''' Case 3 : commited changes( for many commits)

git reset <- commit hash ->
git reset --hard <- commit hash -> (reset changes even from local repo)
'''

#git restore <filename> <- (restore deleted file)
# git restore <file1> <file2> ...  <- (restore multiple deleted files)

# git log <- (checks all the history of commits)

# Fork

''' A fork is a new repo that shares code nad visibility settings with 
the original "upstream" repository'''

# Fork is a rough copy
# clone is a exact copy



class Product:
    
    def __init__(self,products,prices):
        self.products = products
        self.prices = prices
    
    
    def display_products(self):
        dict_products = {}
        for product, price in zip(self.products,self.prices):
            dict_products[product] = price
        print(dict_products)

product_list = ['Bottle', 'Laptop', 'GPU', 'CPU', 'RAM']
price_list = [200,100000,60000,50000,15000]

p1 = Product(product_list,price_list)

# class Store:
#     def __init__(self, products, prices):
#         self.products = products
#         self.prices = prices

#     def display_products(self):
#         for product, price in zip(self.products, self.prices):
#             print(f"Product: {product}, Price: ${price}")

# # Creating a list of products and their corresponding prices
# product_list = ["Laptop", "Phone", "Tablet"]
# price_list = [1000, 500, 300]

# # Initializing the Store object
# store = Store(product_list, price_list)
# store.display_products()


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"
    
class User:
    def __init__(self, name, is_premium=False, is_admin=False):
        self.name = name
        self.is_premium = is_premium
        self.is_admin = is_admin
        self.cart = ShoppingCart()

    def set_premium(self, user):
        if self.is_admin:
            user.is_premium = True
            print(f"{self} has been set as a premium user.")
        else:
            print("Only admins can set a user as premium.")

    def create_admin(self, user):
        if self.is_admin:
            user.is_admin = True
            print(f"{user.name} has been made an admin.")
        else:
            print(f"{self.name}, Only admins can create other admins.")
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)
        print(f"{product.name} added to cart.")

    def remove_product(self, product):
        if product in self.cart_items:
            self.cart_items.remove(product)
            print(f"{product.name} removed from cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def calculate_total_cost(self, user):
        total_cost = sum(product.price for product in self.cart_items)
        if user.is_premium:
            total_cost *= 0.9  # Apply 10% discount for premium users
        return total_cost

    def generate_invoice(self, user):
        print("\nInvoice:")
        print("--------")
        for product in self.cart_items:
            print(f"Product: {product.name}, Price: ${product.price}")
        total_cost = self.calculate_total_cost(user)
        print(f"Total cost: ${total_cost:.2f}")
        if user.is_premium:
            print("A 10% discount has been applied (Premium user).")


# Create some products
laptop = Product("Laptop", 1000)
phone = Product("Phone", 500)
tablet = Product("Tablet", 300)

# Create users
user1 = User("Alice", is_premium=False, is_admin=True)  # Admin user
user2 = User("Bob")  # Regular user
user3 = User("Krish")
# Admin user adds premium feature to Bob
user1.set_premium(user2)

# Add products to Bob's cart
user2.cart.add_product(laptop)
user2.cart.add_product(phone)

# Remove a product
user2.cart.remove_product(phone)

# Generate the invoice for Bob (with premium discount)
user2.cart.generate_invoice(user2)

# Admin creates another admin
user1.create_admin(user2)

user3.create_admin(user2)
print("Hello World")


print(f"Sum of 5 and 5 : {5+5}") # 10

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))

books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1951, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]
# Function to filter books based on genre and year
def filter_books(genre : str, year : int):
    filter_list = []
    for n, g, y,b in books:
        if g == genre and y >= year:
            filter_list.append(n)
    return filter_list

# Example call to the function
print(filter_books("Mystery", 2000))
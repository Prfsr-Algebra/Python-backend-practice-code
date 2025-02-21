from book_class import book
def main():
    #creating instance of the book
    my_book = book("tajweed", "sheikh", 2020)
    #demonstrating __str__
    print(my_book)
    #demonstrating __repr__
    print(repr(my_book))
    #demonstrating __del__
    del my_book
if __name__ == "__main__":
    main()
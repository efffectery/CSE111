import csv
from datetime import datetime

STORE_NAME = "SUPEREST MARKET"

def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}
    with open(filename, newline='') as products_csv:
        products = csv.reader(products_csv)
        rows = list(products)
        del rows[0]
        for row in rows:
            products_dict[row[0]] = row 
    return products_dict

def main():
    formatted_time = datetime.now()
    day_of_week = formatted_time.strftime("%A")
    formatted_time = formatted_time.strftime("%A %b %d %H:%M:%S %Y")
    print(STORE_NAME)

    try:
        products_dict = read_dictionary("products.csv")
        with open("request.csv", "rt") as request_csv:
            read_request = csv.reader(request_csv)
            rows = list(read_request)
            del rows[0]
            print("Ordered Items:")
            num_items_ordered = 0
            subtotal = 0
            for row in rows:
                try:
                    num_items_ordered += float(row[1])
                    subtotal += float(products_dict[row[0]][2]) * int(row[1])
                    print(f"{products_dict[row[0]][1]}, {row[1]}, {products_dict[row[0]][2]}")
                except KeyError as id:
                    print(f"Error: unknown product ID in the request.csv file {id}")

        Sales_tax = subtotal * 0.06
        if day_of_week == "Tuesday" or day_of_week == "Wednesday":
            print("Since Today Is Tuesday or Wednesday You Get A 10% Discount Off Your Total!")
            total = subtotal + Sales_tax
            total *= 0.90
        else:
            total = subtotal + Sales_tax
        print(f"Total Items Ordered: {num_items_ordered}")
        print(f"SubTotal Before Tax: ${round(subtotal, 2)}")
        print(f"Sales Tax: ${round(Sales_tax, 2)}")
        print(f"Total: ${round(total, 2)}")
        print(f"\nThank You For Shopping At {STORE_NAME}")
        print(formatted_time)
    except FileNotFoundError as file:
        print(f"Error: missing file\n[Errno 2] No such file or directory: {file}")

        

if __name__ == "__main__":
    main()
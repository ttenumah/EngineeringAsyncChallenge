import json

# read in JSON file
with open('./data.json') as f:
    data = json.load(f)

# loop through each record
for record in data:
    # extract data fields from NoSQL database
    uuid = record['UUID']
    name = record['customerName']
    cell_phone = record['cellPhone']
    email = record['email']
    address = record['address']
    coaching_services = record['coachingServiceID']
    book_sets = record['bookSetID']
    order_total = record['orderTotal']
    order_date = record['orderDate']
    discount_code = record['discountCode']

    # format data to match new data model
    customer_values = f"({uuid}, '{name}', '{cell_phone}', '{email}', '{address}')"
    coaching_service_values = ", ".join([f"({uuid}, {cs})" for cs in coaching_services])
    book_set_values = ", ".join([f"({uuid}, {bs})" for bs in book_sets])
    order_values = f"({uuid}, {order_total}, '{order_date}', '{discount_code}')"

    # print SQL statements for inserting data into new database
    print(f"INSERT INTO Customers (customer_id, name, cell_phone, email, address) VALUES {customer_values};")
    print(f"INSERT INTO Coaching_Services (coaching_service_id, name) VALUES {coaching_services};")
    print(f"INSERT INTO Book_Sets (book_set_id, name) VALUES {book_sets};")
    print(f"INSERT INTO Orders (order_id, customer_id, order_total, order_date, discount_code) VALUES {order_values};")
    print(f"INSERT INTO Order_Coaching_Services (order_id, coaching_service_id) VALUES {coaching_service_values};")
    print(f"INSERT INTO Order_Book_Sets (order_id, book_set_id) VALUES {book_set_values};")

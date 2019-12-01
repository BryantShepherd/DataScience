import re, csv
from collections import Counter
# # 'r' means read-only
# file_for_reading = open('reading_file.txt', 'r')

# # 'w' is write -- will destroy the file if it already exists!
# file_for_writing = open("writing_file.txt", 'w')

# # 'a' is append -- for adding to the end of the file
# file_for_appending = open('appending_file.txt', 'a')

# # close files
# file_for_writing.close()

# # use with block to close file after finish
# with open(filename, 'r') as f:
#     data = function_that_gets_data_from(f)
# process(data)

# read whole text file
# starts_with_hash = 0

# with open('input.txt', 'r') as f:
#     for line in file:
#         if re.match("^#", line):
#             starts_with_hash += 1

# # get email domain (the part after @)
# def get_domain(email_address):
#     """split on '@' and return the last piece"""
#     return email_address.lower().split("@")[-1]

# with open('email_addresses.txt', 'r') as f:
#     domain_counts = Counter(get_domain(line.strip())
#                             for line in f
#                             if "@" in line)
# print(domain_counts)

# # read file using csv
# with open('tab_delimited_stock_prices.txt', 'rb') as f: # r - read file, b - in binary
#     reader = csv.reader(f, delimiter='\t')
#     for row in reader:
#         date = row[0]
#         symbol = row[1]
#         closing_price = float(row[2])
#         process(date, symbol, closing_price)
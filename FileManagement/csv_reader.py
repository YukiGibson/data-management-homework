import pprint;
from loaders.csv_loader import CsvLoader
from transaction import (
    Transaction,
    convert_list_of_dict_to_list_of_transactions, 
    Transactions
)

csv_loader = CsvLoader("../files/SalesJan2009.csv")
# print(csv_loader.rows)
sales = Transactions(csv_loader.rows)
print("El total de las ventas es {}".format(sales.total_sales))
pprint.pprint(sales.payment_totals)
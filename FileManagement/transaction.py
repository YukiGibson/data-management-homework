class Transaction(object):

    def __init__(self, state):
        self.__Transaction_date = state["Transaction_date"]
        self.__product = state["Product"]
        self.__price = self.__extract_to_int(state, "Price", float)
        self.__payment_type = state["Payment_Type"]
        self.__name = state["Name"]
        self.__city = state["City"]
        self.__state = state["State"]
        self.__country = state["Country"]
        self.__account_created = state["Account_Created"]
        self.__last_login = state["Last_Login"]
        self.__latitude = state["Latitude"]
        self.__longitude = state["Longitude"]

    @property
    def price(self):
        return self.__price
        
    @property
    def payment_method(self):
        return self.__payment_type

    def __extract_to_int(self, state, key, conv_function):
        if key in state:
            return self.__securely_convert_to_int(state[key], conv_function)
        else:
            return 0

    def __securely_convert_to_int(self, string_value, conv_function):
        try:
            return conv_function(string_value)
        except Exception as e:
            # TODO realizar un manejo granular de las excepciones
            return 0


def convert_list_of_dict_to_list_of_transactions(list_of_dict):
    list_of_transactions = []
    for sale in list_of_dict:
        list_of_transactions.append(Transaction(sale))
    return list_of_transactions


class Transactions(object):

    def __init__(self, list_of_sale_dictionaries):
        self.__sales = convert_list_of_dict_to_list_of_transactions(list_of_sale_dictionaries)
        self.__payment_methods = self.__get_group_payments(self.__get_unique_payments())
    
    @property
    def total_sales(self):
        total_ventas = 0
        for sale in self.__sales:
            total_ventas = total_ventas + sale.price
        return total_ventas

    @property
    def average_price(self):
        return self.total_sales / len(self.__sales)
        
    @property
    def payment_totals(self):
        return self.__payment_methods
        
    def __get_group_payments(self, unique_payments):
        for transaction in self.__sales:
            unique_payments[transaction.payment_method] += transaction.price
        return unique_payments
        
    def __get_unique_payments(self):
        unique_payments = {}
        for sale in self.__sales:
            if sale.payment_method not in unique_payments.keys():
                unique_payments[sale.payment_method] = 0
        return unique_payments
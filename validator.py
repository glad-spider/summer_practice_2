from val_from_csv_to_json import CSV_JSON
from uuid import UUID

global_data = []
CELL_FAULT = "--------------------cell fault -->\tcolname: {} row: {} [{}]"

def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test

def checking_ID():
    ID = 0
    for i in range(1, len(global_data) - 1):
        if is_valid_uuid(global_data[i][ID]):
            pass
        else:
            common_action(["error uuid".upper(),
                           'string is not uuid4 format',
                           global_data[0][ID],
                           i + 1,
                           global_data[i][ID]])


def checking_model():
    MODEL = 1
    for i in range(1, len(global_data) - 1):
        is_ban_model  = 'BMW' in global_data[i][MODEL].upper()
        check_condition(is_ban_model,
                        ["error include BMW".upper(),
                        "error include BMW".upper(),
                        global_data[0][MODEL],
                        i + 1,
                        global_data[i][MODEL]])


def checking_price():
    BOUGHT, SOLD = 2, 4
    for i in range(1, len(global_data) - 1):
        global_data[i][BOUGHT], global_data[i][SOLD] = int(global_data[i][BOUGHT]), int(global_data[i][SOLD])

        is_negative_price = global_data[i][BOUGHT] <= 0 or global_data[i][SOLD] <= 0
        check_condition(is_negative_price,
                        ["error price".upper(),
                        "price to cars must be positive",
                        global_data[0][BOUGHT],
                        i + 1,
                        global_data[i][SOLD]])

        is_profit = global_data[i][BOUGHT] > global_data[i][SOLD]
        check_condition(is_profit,
                        ["error selling".upper(),
                        "sold price less than purchase",
                        global_data[0][BOUGHT],
                        i + 1,
                        global_data[i][SOLD]])


def checking_volume():
    VOLUME = 3
    for i in range(1, len(global_data) - 1):
        global_data[i][VOLUME] = int(global_data[i][VOLUME])

        is_exist_volume = global_data[i][VOLUME] <= 0 or global_data[i][VOLUME] == 1900
        check_condition(is_exist_volume,
                        ["error volume".upper(),
                        "unvailable volume",
                        global_data[0][VOLUME],
                        i + 1,
                        global_data[i][VOLUME]])


def checking_mileage():
    MILEAGE = 5
    for i in range(1, len(global_data) - 1):
        global_data[i][MILEAGE] = int(global_data[i][MILEAGE])

        is_out_range_mileage  = global_data[i][MILEAGE] <= 0 or global_data[i][MILEAGE] >= 250000

        check_condition(is_out_range_mileage,
                        ["error mileage".upper(),
                        "car with mileage more 250000, not sold",
                         global_data[0][MILEAGE], i + 1,
                         global_data[i][MILEAGE]])


def common_action(list_text):
    print(list_text[0])
    print(list_text[1])
    print(CELL_FAULT.format(list_text[2], list_text[3], list_text[4]))
    print()

def check_condition(condition, vars):
    if condition:
        common_action([vars[0], vars[1], vars[2], vars[3], vars[4]])


def run():
    fl = CSV_JSON('cars.csv')
    fl.start()

    global global_data
    global_data = fl.data_global        #return[[],[], ..., []]

    checking_ID()
    checking_model()
    checking_price()
    checking_volume()
    checking_mileage()

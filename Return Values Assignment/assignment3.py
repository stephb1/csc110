import doctest 

# All functions in this assignment were implemented by me

NUM_SECONDS_DAY = 86400 
NUM_SECONDS_HOUR = 3600 
NUM_SECONDS_MIN = 60 

KM_TO_METERS = 1000 

DISCOUNT_10 = 0.10 
DISCOUNT_20 = 0.20 

PST = 0.07 
GST = 0.05 
SHIPPING_CHARGE = 4.50 
NEW_CUSTOMER_DISCOUNT = 0.10 

def get_smallest(num1: int, num2: int, num3: int) -> int: 
    '''
    returns the smallest value of three given integers 
    >>> get_smallest(1, -9, 12)
    -9
    >>> get_smallest(5, 6, 7)
    5
    >>> get_smallest(-1, -2, -3)
    -3
    >>> get_smallest(0, 3, 5)
    0
    >>> get_smallest(0, 0, 0)
    0
    >>> get_smallest(3, 3, 3)
    3
    >>> get_smallest(3, 3, 4)
    3
    >>> get_smallest(3, 4, 3)
    3
    >>> get_smallest(4, 3, 3)
    3
    ''' 
    if num1 < num2 and num1 < num3:
        return num1 
    elif num2 < num1 and num2 < num3:
        return num2 
    elif num1 == num2 and num1 < num3: 
        return num1 
    elif num2 == num3 and num2 < num1:
        return num2 
    elif num1 == num3 and num1 < num2:
        return num1 
    else: 
        return num3 

def get_time_in_seconds(days: int, hours: int, minutes: int, seconds: int) -> int:
    '''
    Given a certain number of days, hours, minutes, and seconds print_time_in_seconds returns the total number of seconds within the time given 
    
    Precondition: the times inserted into the function should be greater than or equal to zero. If a negative integer is given, the function will print invalid time 
    >>> get_time_in_seconds(3, 4, 20, 25) 
    274825
    >>> get_time_in_seconds(5, 50, 100, 1000)
    619000
    >>> get_time_in_seconds(4, 0, 2, 0)
    345720
    >>> get_time_in_seconds(1, 1, 1, 1) 
    90061
    ''' 
    days_seconds = days * NUM_SECONDS_DAY 
    hours_seconds = hours * NUM_SECONDS_HOUR 
    mins_seconds = minutes * NUM_SECONDS_MIN 
    
    total_time_seconds = days_seconds + hours_seconds + mins_seconds + seconds 
    
    return total_time_seconds 

def get_average_speed(distance_km: float, days: int, hours: int, minutes: int, seconds: int) -> float:
    '''
    calculates and returns the average speed of a vehicle in meters per second given the distance the vehicle has traveled in kilometers, and a number of days, hours, minutes, and seconds. 
    
    Precondition: distance traveled (in km) should be greater than zero (distance_km > 0). Additionally, all time values should be whole number integers and at least 1 given time value must be greater than zero. 
    >>> get_average_speed(170863.9, 1, 1, 1, 1)
    1897.2018964923775
    >>> get_average_speed(217.56, 3, 4, 20, 25) 
    0.7916310379332302
    >>> get_average_speed(6000.13, 4, 0, 2, 0) 
    17.355461066759226
    ''' 
    distance_meters = distance_km * KM_TO_METERS 
    total_time = get_time_in_seconds(days, hours, minutes, seconds) 
    average_speed = distance_meters / total_time 
    
    return average_speed 

def get_box_charge(num_box: int, box_price: float) -> float:
    '''
    calculates and returns the amount to be charged for boxes of contact lenses, given the number of boxes to be purchased and the price per box. A discount of 10% is applied when 10 or more boxes are purchased and 20% when 20 or more boxes are purchased. 
    
    Precondition: the number of boxes is not negative and the price per box is greater than 0 
    >>> get_box_charge(0, 12.50) 
    0.0
    >>> get_box_charge(3, 15.17) 
    45.51
    >>> get_box_charge(10, 13.17) 
    118.52999999999999
    >>> get_box_charge(15, 12.50) 
    168.75
    >>> get_box_charge(20, 15.60) 
    249.6
    >>> get_box_charge(25, 12.50) 
    250.0
    ''' 
    total_charge = num_box * box_price 
    total_discount_10 = total_charge * DISCOUNT_10 
    total_discount_20 = total_charge * DISCOUNT_20 
    
    if num_box >= 20: 
        return total_charge - total_discount_20 
    elif num_box >= 10: 
        return total_charge - total_discount_10 
    else:
        return total_charge 

def get_order_charge(new_customer: bool, boxes_pres1: int, price_pres1: float, boxes_pres2: int, price_pres2: float) -> float: 
    '''
    calculates and returns the the amount to be charged on an order of contact lenses that allows for up to 2 different prescriptions to be ordered. A discount of 10% is applied when 10 or more boxes are purchased and 20% when 20 or more boxes are purchased. Additionally, if a customer is new, an additional 10% discount is applied before taxes. PST and GST taxes are added to the total order charge and a shipping charge of $4.50 is added after taxes and discounts when the total charge is greater than $0 but less than $100. No shipping charge for orders above $100. 
    
    Precondition: number of boxes is not negative and price is greater than 0 
    >>> get_order_charge(True, 0, 12.50, 0, 13.50)
    0.0
    >>> get_order_charge(True, 12, 12.50, 3, 13.50) 
    176.904
    >>> get_order_charge(False, 12, 12.50, 3, 13.50) 
    196.56
    >>> get_order_charge(True, 10, 12.50, 23, 13.50) 
    363.7872
    >>> get_order_charge(False, 10, 12.50, 23, 13.50) 
    404.20799999999997
    >>> get_order_charge(True, 2, 12.50, 3, 13.50) 
    70.524
    >>> get_order_charge(False, 2, 12.50, 3, 13.50) 
    77.86
    >>> get_order_charge(False, 1, 12.5, 2, 9.5) 
    39.78
    >>> get_order_charge(True, 11, 12.5, 5, 9.5) 
    172.62
    ''' 
    taxes = PST + GST 
    total_order = get_box_charge(boxes_pres1, price_pres1) + get_box_charge(boxes_pres2, price_pres2) 
    order_tax = total_order * taxes 
    discount = total_order * NEW_CUSTOMER_DISCOUNT 
    new_order_total = total_order - discount 
    order_new_tax = new_order_total * taxes 
    
    if new_customer: 
        final_order = new_order_total + order_new_tax 
        if final_order > 0 and final_order < 100: 
            return final_order + SHIPPING_CHARGE 
        else:
            return final_order 
    else: 
        final_order = total_order + order_tax 
        if final_order > 0 and final_order < 100: 
            return final_order + SHIPPING_CHARGE 
        else: 
            return final_order 

def place_order(account_balance: float, new_customer: bool, boxes_pres1: int, price_pres1: float, boxes_pres2: int, price_pres2: float) -> bool: 
    '''
    determines whether an account has sufficient funds to place a contact lens order and returns a boolean value. 
    
    Precondition: the account balance and the number of boxes is not negative and the price per box is greater than 0 
    >>> place_order(177, True, 0, 12.50, 0, 13.50) 
    True
    >>> place_order(191.35, False, 12, 12.50, 3, 13.50) 
    False
    >>> place_order(77.86, False, 2, 12.50, 3, 13.50) 
    True
    >>> place_order(40.50, False, 1, 12.5, 2, 9.5) 
    True
    >>> place_order(32.75, False, 1, 12.5, 2, 9.5) 
    False
    ''' 
    return get_order_charge(new_customer, boxes_pres1, price_pres1, boxes_pres2, price_pres2) <= account_balance 

def get_middle(string: str) -> str: 
    '''
    returns a string with just the middle characters of the given string. If the string is empty, the function will return an empty string. 
    >>> get_middle('Victoria') 
    'to'
    >>> get_middle('Vancouver') 
    'o'
    >>> get_middle('') 
    ''
    ''' 
    str_len = len(string) 
    str_half = len(string)/2
    
    if string == '': 
        return '' 
    elif str_len % 2 == 0: 
        return string[(str_len-1)//2:(str_len+2)//2]
    else: 
        return string[(str_len-1)//2] 

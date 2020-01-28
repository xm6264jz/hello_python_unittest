""" 
Snow shovel service price estimator 

Regular, one side of sidewalk = $20
Corner, two sides = $30

Add $5 for same day service

"""

from datetime import date


def main():
    sidewalk = input('Enter \'r\' for regular sidewalk, \'c\' for corner lot:\n')
    service_date = get_date_from_user()
    price_estimate = estimate(service_date, sidewalk)
    print(f'Estimated price: ${price_estimate}')



def get_date_from_user():
    while True:
        try:
            date_str = input('Enter date as YYYY-MM-DD e.g. 2020-01-21 for Jan 21, 2020:\n')
            service_date = date.fromisoformat(date_str)
            return service_date
        except ValueError:
            print('Error, invalid date. Please try again.')


def estimate(service_date, sidewalk_type):
    
    if sidewalk_type.lower() == 'r':
        price = 20
    elif sidewalk_type.lower() == 'c':
        price = 30
    else:
        raise ValueError('The only valid types are r for regular or c for corner')
    
    if service_date < date.today():
        raise ValueError('Date can\'t be in the past')

    if service_date == date.today():
        price += 5

    return price 



if __name__ == '__main__':
    main()
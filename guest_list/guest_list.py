import collections # Store a list of names and phone numbers.
# Add, remove, entry; edit phone number for an entry

guests = []


def display_menu():

    print('''
    1 Display all entries
    2 Add guest
    3 Delete guest
    4 Search for guest
    q Quit
    ''')

    print('Please enter your selection: ')
    return(input())


def show_all():

    for guest in guests:
        print(guest)

    print('Total {} guest(s)'.format(len(guests)))


def add_entry():

    name = input('Enter new guest name: ')
    add_guest(name)
    print('Added guest')


def delete_entry():

    name = input('Enter name to delete: ')

    if guest_in_list(name):
        remove_guest(name)
        print('{} removed'.format(name))
    else:
        print('{} was not found in the guest list'.format(name))


def search():
    name = input('enter name to search for: ')

    if guest_in_list(name):
        print('{} is in your list'.format(name))
    else:
        print('{} is not in your list'.format(name))


def guest_in_list(name):
    return name in guests


def remove_guest(name):
    if guest_in_list(name):
        guests.remove(name)


def add_guest(name):
    global guests
    guests.append(name)
    guests.sort()


def main():

    choice = ''

    while choice != 'q' :

        choice = display_menu()

        if choice == '1':
            show_all()

        if choice == '2':
            add_entry()

        if choice == '3':
            delete_entry()

        if choice == '4':
            search()

    print('Bye!')


if __name__ == '__main__':
    main()

def decimal(binary_str):

    ''' Convert binary strings to their decimal equivalents.
    Throw ValueError if binary_str contains any characters other than 0 and 1'''

    remove_0_and_1 = binary_str.replace('0', '').replace('1', '')
    if len(remove_0_and_1) > 0:
        raise ValueError('Input binary string can only contain 0 and 1')


    place = 1; # The 1s place, the 2s place, the 4s place...
    dec = 0   # The decimal value

    for bit in binary_str[::-1]: # Loop from end of string to the start
        if (bit == '1'): # If the digit is a 1, add on the place value. If 0, ignore.
            dec += place
        place *= 2  # Muliply place by 2 for the next place value

    return dec

def roman_to_decimal(roman_numeral):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decimal_num = 0
    prev_value = 0
    
    for i in range(len(roman_numeral)-1, -1, -1):
        current_value = roman_dict[roman_numeral[i]]
        if current_value < prev_value:
            decimal_num -= current_value
        else:
            decimal_num += current_value
        prev_value = current_value
    
    return decimal_num

print(roman_to_decimal("XLIV"))
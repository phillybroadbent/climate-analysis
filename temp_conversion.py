"""
A module for converting temperature from imperial to metric units.
Will throw ValueErrors for temperatures below absolute zero.

Functions:
    convert_fahr_to_celsius: converts fahrenheit to celsius
    convert_fahr_to_kelvin: converts fahrenheit to kelvin
"""

def convert_fahr_to_celsius(temp_fahr):
    """
    Given a temperature in fahrenheit, convert it to celsius.
    
    :param temp_fahr: temperature in fahrenheit
    :raises ValueError: if the temperature is below absolute zero
    :return: temperature in celsius
    """
    temp_celsius = (temp_fahr - 32) * (5 / 9)
    if temp_celsius < -273.15:
        raise ValueError(f"Trying to convert impossible temperature: {fahr}F")
    return temp_celsius

def convert_fahr_to_kelvin(temp_fahr):
    temp_celsius = convert_fahr_to_celsius(temp_fahr)
    temp_kelvin = temp_celsius + 273.15
    return temp_kelvin

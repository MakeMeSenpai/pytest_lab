import pytest
"""test_one.py"""

def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

# def calculate_kinetic_energy(mass, velocity): 
#     """Returns kinetic energy of mass [kg] with velocity [ms]."""
#     return mass * velocity ** 2

"""practice one"""
def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_average():
    li = [-2, -1, 0, 1, 2]
    assert get_average(li) == 0

"""Test for exception"""
def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]

def test_palindrom():
    with pytest.raises(TypeError):
        palindrome(44)

def test_palindrom_isBoolean():
    word = "hannah"
    assert palindrome(word) == True
    word = "Kami"
    assert palindrome(word) == False


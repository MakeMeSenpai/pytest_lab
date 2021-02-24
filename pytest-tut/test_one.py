"""test_one.py"""
import pytest
import math

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

"""practice 2"""
T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
     carbon_14_ratio: the percent (0 < percent < 1) of carbon-14
     in the sample conpared to the amount in living
     tissue (unitless)."""
    if carbon_14_ratio <= 0:
        raise TypeError('Cannot be zero or negative')
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF

def test_carbon_dating():
    carbon_14_ratio = 0.35
    assert get_age_carbon_14_dating(carbon_14_ratio) == 8680.34743633106
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(0)

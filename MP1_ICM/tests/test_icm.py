import pytest
import random
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
from IcecreamExceptions import ExceededRemainingChoicesException, OutOfStockException
from IcecreamExceptions import InvalidCombinationException

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
    
@pytest.fixture
def first_order(machine):
    machine.reset()
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine
    
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("Waffle Cone")
    machine.handle_flavor("strawberry")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

# UCID: ap2823
# Date: 10/23/2022
@pytest.fixture
def third_order(second_order, machine):
    machine.handle_container("Sugar Cone")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

# UCID: ap2823
# Date: 10/23/2022
# Checks if an exception is raised when a flavor/topping is picked before
# a container is picked.
def test_first_selection(machine):
    try:
        machine.handle_flavor("vanilla")
        machine.handle_topping("peanuts")
        assert False
    except InvalidCombinationException:
        assert True

# UCID: ap2823
# Date: 10/23/2022
# Checks if an exception is raised when an out of stock flavor is chosen
def test_flavors_instock(machine):
    try:
        machine.reset()
        tmp = machine.flavors[0].quantity
        machine.flavors[0].quantity=0
        machine.handle_container("cup")
        machine.handle_flavor(machine.flavors[0].name)
        assert False
    except OutOfStockException:
        machine.flavors[0].quantity=tmp
        assert True

# UCID: ap2823
# Date: 10/23/2022
# Checks if an exception is raised when an out of stock topping is chosen
def test_toppings_instock(machine):
    try:
        machine.reset()
        tmp = machine.toppings[0].quantity
        machine.toppings[0].quantity=0
        machine.handle_container("cup")
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        assert False
    except OutOfStockException:
        machine.toppings[0].quantity = tmp
        assert True

# UCID: ap2823
# Date: 10/23/2022
# Checks if an exception is raised when more that 3 scoops are picked
def test_max_flavors(machine):
    try:
        machine.reset()
        machine.handle_container("cup")
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_flavor(machine.flavors[0].name)
        assert False
    except ExceededRemainingChoicesException:
        assert True

# UCID: ap2823
# Date: 10/23/2022
# Checks if an exception is raised when more that 3 toppings are picked
def test_max_toppings(machine):
    try:
        machine.handle_container("cup")
        machine.handle_toppings(machine.toppings[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        assert False
    except ExceededRemainingChoicesException:
        assert True

# UCID: ap2823
# Date: 10/23/2022
# Checks if the cost returned by the calculate_cost method is correct
# This check is tested for 4 different combinations of cup,flavor and topping
def test_cost_calculation(machine):
    for i in range(4):
        expected_cost = 0
        machine.reset()
        random_container = random.choice(machine.containers)
        random_flavor = random.choice(machine.flavors)
        random_topping = random.choice(machine.toppings)
        expected_cost = random_container.cost + random_flavor.cost + random_topping.cost
        machine.handle_container(random_container.name)
        machine.handle_flavor(random_flavor.name)
        machine.handle_toppings(random_topping.name)
        if f"{expected_cost:.2f}" != f"{machine.calculate_cost():.2f}":
            assert False
        machine.handle_pay(machine.calculate_cost(), f"{expected_cost:.2f}")
    machine.reset()
    assert True 

# UCID: ap2823
# Date: 10/23/2022
# Checks if total_sales is calculated properly. This is checked by making use of fixtures
# and simulating three different purchases.
def test_total_sales(third_order):
    first_order_expected_cost = 2
    second_order_expected_cost = 2.5
    third_order_expected_cost = 2.25
    assert third_order.total_sales == first_order_expected_cost + second_order_expected_cost + third_order_expected_cost

# UCID: ap2823
# Date: 10/23/2022
# Checks if total_icecream is incremented properly. This is checked by making use of fixtures
# and simulating three different purchases.
def test_total_icecream(third_order):
    assert third_order.total_icecreams == 3
import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException, NoItemChosenException, InvalidCombinationException

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
    
@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000.00")
    return machine
    
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000.00")
    return machine

def test_first_selection(machine):
    try:
        machine.handle_flavor("vanilla")
        machine.handle_topping("peanuts")
        assert False
    except InvalidCombinationException:
        assert True

def test_flavors_instock(machine):
    try:
        machine.flavors[0].quantity=0
        machine.handle_container("cup")
        machine.handle_flavor(machine.flavors[0].name)
        assert False
    except OutOfStockException:
        assert True

def test_toppings_instock():
    pass

def test_max_flavors():
    pass

def test_max_toppings():
    pass

def test_cost_calculation():
    pass

def test_total_sales():
    pass

def test_total_icecream():
    pass
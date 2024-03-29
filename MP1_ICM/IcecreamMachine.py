from enum import Enum
# make a tests folder under the folder you're putting these files in
# add an empty __init__.py to the tests folder
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException, NoItemChosenException, InvalidCombinationException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0

class Container(Usable):
    pass

class Flavor(Usable):
    pass

class Toppings(Usable):
    pass

class STAGE(Enum):
    Container = 1
    Flavor = 2
    Toppings = 3
    Pay = 4

class IceCreamMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 100
    MAX_SCOOPS = 3
    MAX_TOPPINGS = 3


    containers = [Container(name="Waffle Cone", cost=1.5), Container(name="Sugar Cone", cost=1), Container("Cup", cost=1)]
    flavors = [Flavor(name="Vanilla", quantity=100, cost=1), Flavor(name="Chocolate", quantity=100, cost=1), Flavor(name="Strawberry", quantity=100, cost=1)]
    toppings = [Toppings(name="Sprinkles", quantity=200, cost=.25), Toppings(name="Chocolate Chips", quantity=200, cost=.25), Toppings(name="M&Ms", quantity=200, cost=.25), \
    Toppings(name="Gummy Bears", quantity=200, cost=.25), Toppings(name="Peanuts", quantity=200, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_scoops = MAX_SCOOPS
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_icecreams = 0

    inprogress_icecream = []
    currently_selecting = STAGE.Container

    # rules
    # 1 - container must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - scoops can't exceed max
    # 4 - toppings can't exceed max
    # 5 - a container and at least 1 scoop or toppings must be selected
    # 6 - proper cost must be calculated and shown to the user
    # 7 - cleaning must be done after certain number of uses before any more icecreams can be made
    # 8 - total sales should calculate properly based on cost calculation
    # 9 - total_icecreams should increment properly after a payment
    

    def pick_container(self, choice):
        for c in self.containers:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_icecream.append(c)
                return
        raise InvalidChoiceException

    def pick_flavor(self, choice):
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_scoops <= 0:
            raise ExceededRemainingChoicesException
        for f in self.flavors:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_icecream.append(f)
                self.remaining_scoops -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_toppings(self, choice):
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_icecream.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_scoops = self.MAX_SCOOPS
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_icecream = []
        self.currently_selecting = STAGE.Container

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_container(self, container):
        self.pick_container(container)
        self.currently_selecting = STAGE.Flavor

    def handle_flavor(self, flavor):
        if not self.inprogress_icecream:
            raise InvalidCombinationException
        elif flavor == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_flavor(flavor)

    def handle_toppings(self, toppings):
        if not self.inprogress_icecream:
            raise InvalidCombinationException
        if toppings == "done" and any(item in self.flavors + self.toppings for item in self.inprogress_icecream):
            self.currently_selecting = STAGE.Pay
        elif toppings == "done":
            raise NoItemChosenException
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if total == f"{expected:.2f}":
            print("Thank you! Enjoy your icecream!")
            self.total_icecreams += 1
            self.total_sales += expected # only if successful
            self.reset()
        else:
            raise InvalidPaymentException
            
    # UCID: ap2823
    # Date: 10/23/2022
    # Method to calculate cost of the icecream in progress       
    def calculate_cost(self):
        self.cost = 0
        for item in self.inprogress_icecream:
            self.cost += item.cost
        return round(self.cost, 2)

    def run(self):
        # UCID: ap2823
        # Date: 10/23/2022
        try:
            if self.currently_selecting == STAGE.Container:
                container = input(f"Would you like a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
                self.handle_container(container)
            elif self.currently_selecting == STAGE.Flavor:
                flavor = input(f"Would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
                try:
                    self.handle_flavor(flavor)
                # UCID: ap2823
                # Date: 10/23/2022
                # If maximum number of choices are exceeded for flavors, the stage is automatically changed to toppings
                except ExceededRemainingChoicesException:
                    print("Sorry! You've exceeded the maximum number of flavors that you can select, please choose a topping")
                    self.currently_selecting = STAGE.Toppings
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(f"Would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                try:
                    self.handle_toppings(toppings)
                # UCID: ap2823
                # Date: 10/23/2022
                # If maximum number of choices are exceeded for toppings, the stage is automatically changed to pay
                except ExceededRemainingChoicesException:
                    print("Sorry! You've exceeded the maximum number of toppings; proceeding to the payment portal")
                    self.currently_selecting = STAGE.Pay
                # UCID: ap2823
                # Date: 10/23/2022
                # The stage is changed to Flavor if at all no scoop or topping is chosen.
                except NoItemChosenException:
                    print("Please choose at least one scoop or topping.")
                    self.currently_selecting = STAGE.Flavor
            elif self.currently_selecting == STAGE.Pay:
                # UCID: ap2823
                # Date: 10/23/2022
                expected = self.calculate_cost()
                total = input(f"Your total is ${expected:.2f}, please enter the exact value.\n")
                try:
                    self.handle_pay(expected, total)
                # UCID: ap2823
                # Date: 10/23/2022
                # If the entered amount doesn't match the total, the user is prompted with a message to try again.
                except InvalidPaymentException:
                    print("You've entered a wrong amount. Please try again :)")
                    self.run()
                choice = input("What would you like to do? (icecream or quit)\n")
                if choice == "quit":
                    exit()
        # UCID: ap2823
        # Date: 10/23/2022
        # If any of the item is out of stock, the user is prompted with a message to choose a different item
        except OutOfStockException:
            print("The selected option is out of stock. Please select another option")
        # UCID: ap2823
        # Date: 10/23/2022
        # The user is prompted with a message to clean the machine. If yes, the machine is cleaned and the user can resume
        except NeedsCleaningException:
            choice = input("Sorry, The machine needs cleaning! Please type yes to clean the machine \n")
            if choice.lower() == "yes":
                print("The machine has been cleaned, you can continue")
                self.clean_machine()
        # UCID: ap2823
        # Date: 10/23/2022
        # If the entered choice is an invalid choice, the user is prompted with a message to choose again.
        except InvalidChoiceException:
            print("You've entered an invalid choice. Please choose from the given options")
        self.run()


    def start(self):
        self.run()

    
if __name__ == "__main__":
    icm = IceCreamMachine()
    icm.start()
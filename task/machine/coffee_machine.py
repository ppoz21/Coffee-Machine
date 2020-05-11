class CoffeeMachine:

    def __init__(self):
        self.water_state = 400
        self.milk_state = 540
        self.beans_state = 120
        self.money_state = 550
        self.cups_state = 9
        self.running = True

    def __str__(self):
        return f"""The coffee machine has:
{self.water_state} of water
{self.milk_state} of milk
{self.beans_state} of coffee beans
{self.cups_state} of disposable cups
{self.money_state} of money
"""

    def buy(self, choice):
        if choice == '1':
            if self.water_state >= 250 and self.beans_state >= 16 and self.cups_state >= 1:
                print('I have enough resources, making you a coffee!')
                self.water_state -= 250
                self.beans_state -= 16
                self.cups_state -= 1
                self.money_state += 4
            else:
                if self.water_state < 250:
                    print("Sorry, not enough water")
                if self.beans_state < 16:
                    print("Sorry, not enough beans")
                if self.cups_state < 1:
                    print("Sorry, not enough cups")
        elif choice == '2':
            if self.water_state >= 350 and self.milk_state >= 75 and self.beans_state >= 20 and self.cups_state >= 1:
                print('I have enough resources, making you a coffee!')
                self.water_state -= 350
                self.milk_state -= 75
                self.beans_state -= 20
                self.cups_state -= 1
                self.money_state += 7
            else:
                if self.water_state < 350:
                    print("Sorry, not enough water")
                if self.milk_state < 75:
                    print("Sorry, not enough milk")
                if self.beans_state < 20:
                    print("Sorry, not enough beans")
                if self.cups_state < 1:
                    print("Sorry, not enough cups")
        elif choice == '3':
            if self.water_state >= 200 and self.milk_state >= 100 and self.beans_state >= 12 and self.cups_state >= 1:
                print('I have enough resources, making you a coffee!')
                self.water_state -= 200
                self.milk_state -= 100
                self.beans_state -= 12
                self.cups_state -= 1
                self.money_state += 6
            else:
                if self.water_state < 200:
                    print("Sorry, not enough water")
                if self.milk_state < 100:
                    print("Sorry, not enough milk")
                if self.beans_state < 12:
                    print("Sorry, not enough beans")
                if self.cups_state < 1:
                    print("Sorry, not enough cups")

    def fill(self, water, milk, beans, cups):
        self.water_state += water
        self.milk_state += milk
        self.beans_state += beans
        self.cups_state += cups

    def take(self):
        money = self.money_state
        self.money_state = 0
        return money

    def turn_off(self):
        self.running = False


def choose_action():
    print("Write action (buy, fill, remaining,  take, exit):")
    action = input()
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'remaining':
        print(machine)
    elif action == 'take':
        take()
    elif action == 'exit':
        machine.turn_off()
    else:
        pass


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3- cappuccino, back - back to menu")
    choice = input()
    machine.buy(choice)


def fill():
    print('Write how many ml of water do you want to add:')
    water = int(input())
    print('Write how many ml of milk do you want to add:')
    milk = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    beans = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    cups = int(input())
    machine.fill(water, milk, beans, cups)


def take():
    print(f'I gave you ${machine.take()}')


machine = CoffeeMachine()

while machine.running:
    choose_action()

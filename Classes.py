from goblin import Goblin
from superhero import Hero

# '''

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 7
#     goblin_power = 3

# '''
tigerlily = Hero('Lily', 8, 11)
bean = Goblin('Big Bad Bean', 7, 9)

tigerlily.attack(bean)
bean.attack(tigerlily)



while bean.alive() and tigerlily.alive():
    print('You have %d health and %d power. '% (tigerlily.health, tigerlily.power))
    print('The goblin has %d health and %d power. '% (bean.health, bean.power))
    print()
    print('What do you want to do? ')
    print('1. attack goblin')
    print('2. do nothing')
    print('3. gtfo')
    print('> ',)
    user_input = input()
    if user_input == '1':
        bean.health -= tigerlily.power 
        print("You do %d damage to the goblin." % tigerlily.power)
        if bean.health <= 0:
                print("The goblin is out.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Boy BYE.")
            break
        else:
            print("Invalid input %r" % user_input)

        if bean.alive():
            # Goblin attacks hero
            tigerlily.health -= bean.power
            print("The goblin does %d damage to you." % bean.power)
            if tigerlily.health <= 0:
                print("You're out, boo. ")
# main()

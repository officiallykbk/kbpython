# Coffee:[water,coffee,milk,price]
coffeeSpecs={'espresso':[50,18,0,1.5],'latte':[200,24,150,2.5],'cappuccino':[250,24,100,3]}
resources ={'water':[300,'ml'],'coffee':[100,'ml'],'milk':[200,'g'],'money':[0,'¢']}

change=0

def report():
    for i in resources:
        print(f'{i} : {resources[i][0]}{resources[i][1]}')

def cashWorth():
    print('Insert coins')
    quarters=int(input('How many quarters?: '))*0.25
    dime=int(input('How many dime?: '))*0.1
    nickles=int(input('How many nickles?: '))*0.05
    pennies=int(input('How many pennies?: '))*0.01
    total=quarters+dime+nickles+pennies
    print(f'Total: {total}')
    return total

def cashCheck(name):
    print(f'{name} costs ¢{coffeeSpecs[name][3]}')
    money=cashWorth()
    if money<(coffeeSpecs[name][3]):
        print("Sorry that's not enough money. Money refunded")
    else:
        global change
        change=money-coffeeSpecs[name][3]
        resourceCheck(name)
       

def resourceCheck(name):
    check=0
    for indice,i in enumerate(resources):
        if i=='money':
            break
        elif resources[i][0]<coffeeSpecs[name][indice]:
            print(f'Sorry there is not enough {i}')
            check+=1
    if check==0:
        resources['money'][0]+=coffeeSpecs[name][3]
        for indice,i in enumerate(resources):
            if i=='money':
                break
            resources[i][0] -= coffeeSpecs[name][indice]
        print(f'Enjoy your {name}')
        print(f'Here is your change: ¢{change}')



    


# Start
option=str(input('What would you like? (espresso/latte/cappuccino):')).lower()
while option not in ['espresso','latte','cappuccino','report','off']:
    option=str(input('What would you like? (espresso/latte/cappuccino):')).lower()

while option in ['espresso','latte','cappuccino','report','off']:
    if option=='off':
        print('Come back for another refreshing morning')
        break
    elif option=='report':
        report()
    else:
        cashCheck(option)
    option=str(input('What would you like? (espresso/latte/cappuccino):')).lower()


    
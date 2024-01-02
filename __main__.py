from Bot import AddBot, SearchBot, ExitBot, EditBot, RemoveBot, SaveBot, CongratulateBot, LoadBot, ViewBot


if __name__ == "__main__":
    choise = {
        'add': AddBot(),
        'search': SearchBot(),
        'exit': ExitBot(),
        'edit': EditBot(),
        'remove': RemoveBot(),
        'save': SaveBot(),
        'exit': CongratulateBot(),
        'load': LoadBot(),
        'view': ViewBot()
    }
    while True:
        action = input('Chose an action: ')
        if action in choise:
            choise[action].handle()
        else:
            print('Incorrect Action!')

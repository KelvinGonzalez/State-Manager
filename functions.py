from random import randint

def start(data):
    print("Welcome to Rock Paper Scissors")
    print("Press Enter to start")

def options(data):
    print("Press 1 to select Rock, 2 to select Paper, or 3 to select Scissors")
    print("Press Escape to end")

def results(data):
    def determine_win(player, cpu):
        if player == cpu:
            return -1
        if (player - 1) % 3 == cpu:
            return 0
        return 1

    options = ["Rock", "Paper", "Scissors"]
    print(f"Player chose {options[data['player']]} and CPU chose {options[data['cpu']]}")
    result = determine_win(data["player"], data["cpu"])
    if result == -1:
        print("Player and CPU have tied")
        data["ties"] += 1
    elif result == 0:
        print("Player has scored")
        data["player_wins"] += 1
    else:
        print("CPU has scored")
        data["cpu_wins"] += 1
    print("Press Enter to continue or press Escape to end")

def end(data):
    print(f"Player won {data['player_wins']} times")
    print(f"CPU won {data['cpu_wins']} times")
    print(f"Player and CPU tied {data['ties']} times")

def setup(data):
    data["player_wins"] = 0
    data["cpu_wins"] = 0
    data["ties"] = 0

def options_action(data):
    data["player"] = int(data["key"]) - 1
    data["cpu"] = randint(0, 2)

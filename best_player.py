best_player = ""
best_goals = 0

while True:
    player_name = input()
    if player_name == "END":
        break
    goals = int(input())

    if goals > best_goals:
        best_goals = goals
        best_player = player_name

    if best_goals >= 10:
        break

if best_goals >= 3:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_goals} goals.")

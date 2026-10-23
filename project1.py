#Blake Hayama
#Computer Programming
#Project 1
#October 2, 2026
players = []
for i in range(5):
    name = input("Player " + str(i + 1) + " Name: ")
    ab = int(input("Player " + str(i + 1) + " At-bats: "))
    hits = int(input("Player " + str(i + 1) + " Hits: "))
    avg = hits / ab
    players.append([name, ab, hits, avg])
total_ab = 0
total_hits = 0
for player in players:
    total_ab += player[1]
    total_hits += player[2]
overall_average = total_hits / total_ab
print()
print("NAME\t\tAB\tHITS\tAVG")
for player in players:
    print(player[0], "\t\t", player[1], "\t", player[2], "\t", format(player[3], ".3f"))
print("TOTAL\t\t", total_ab, "\t", total_hits, "\t", format(overall_average, ".3f"))
team_average = 0.253
mlb_average = 0.245
print()
if team_average > overall_average:
    print("Team's overall average is higher than the 5 players' average.")
else:
    print("Team's overall average is lower than the 5 players' average.")
if mlb_average > overall_average:
    print("MLB's overall average is higher than the 5 players' average.")
else:
    print("MLB's overall average is lower than the 5 players' average.")

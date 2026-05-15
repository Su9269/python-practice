names = ["freeman", "kim", "ohtani", "betts"]
avgs = [.398, .250, .411, .302]
for name, battingavg in zip(names, avgs):
    print(f"{name}的打擊率是{battingavg}")

newavgs = list(map(lambda x: x/10, avgs))
print(newavgs)


good_batter = list(filter(lambda x: x[1] >= 0.35, zip(names, avgs)))
for batter in good_batter:
    print(f"{batter[0]} is good at batting")

print(sorted(avgs, reverse=True))
ranked = sorted(zip(names, avgs), key=lambda x: x[1], reverse=True)
for i, (name, avg) in enumerate(ranked):
    print(f"第{i+1}位球員{name}的打擊率為{avg}")

players = {"freeman": .398, "kim": .250, "ohtani": .411,
           "betts": .302, "muncy": .228, "smith": .315}
playername = []
playeravg = []
for name, avg in players.items():
    playername.append(name)
    playeravg.append(avg)
myplayer = zip(playername, playeravg)
player_ranked = sorted(
    filter(lambda x: x[1] > .3, zip(playername, playeravg)), key=lambda x: x[1], reverse=True)
print(player_ranked)

player_ranked2 = sorted(
    filter(lambda x: x[1] > .3, players.items()), key=lambda x: x[1], reverse=True)
print(player_ranked2)

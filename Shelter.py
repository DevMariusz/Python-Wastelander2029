#Start of game -found shelter
for t in range(2):
    if t==0:
        pmove=input("\n\nThere's a shelter near here, Let's move! (Press --w-- and enter to move forward): ").lower()
    else:
        clearscreen()
        mainGameScreen()
        pmove=input("\nNothing Found, Let's keep moving! (--w-- move forward): ").lower()
    while pmove!="w":
        print("Standing still...")
        pmove=input("\n\n\nEnter movement  (--w-- forward):  ").lower()
    print("Exploring new area...\n")
    for n in range(3):
        time.sleep(.4)
        print("...")

    print("\n\tYou found the shelter! You can fast travel(h) here to rest safely or store supplies.")
    print("\tLet's see what we can find inside.")
    search_shelter()

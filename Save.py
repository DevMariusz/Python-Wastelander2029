#Saves game to hidden text file
if startgame=="n":
    os.remove("SaveGame.txt")
    save_file=open("SaveGame.txt","a")
    save_file.write("This file stores save game info, do not delete unless starting over.")
    save_file.close()
    save_file=open("SaveGame.txt:Stats.txt","a")
    save_file.write("New Game\n")
    save_file.close()
else:
    input("\n\n\t\tLoading Game... Press Enter to continue.")
    save_file=open("SaveGame.txt:Stats.txt","r+")
    text_in_file = save_file.readlines()
    save_file.close()

#level up
def levelup(self,xp):
    self.Xp+=xp
    self.Xp=round(self.Xp)
    if self.Xp>self.XpMax:
        self.Xp-=self.XpMax
        self.Level+=1
        self.Maxhealth+=20
        self.XpMax=(100*self.Level)+((self.Maxhealth/4)*(self.Level-1))
        self.Health=self.Maxhealth

        clearscreen()
        input("\n\n\n\tYou leveled up!!! +4 skill points (Open inventory to assign)")
        self.skillpoints+=4

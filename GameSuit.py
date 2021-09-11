#variabel
player = '' #u/ input player
bot = '' #u/ input bot/komputer

#import function randint
from random import randint
#merandom pilihan bot
bot = randint(1,3)

#mengubah random angka bot menjadi G/B/K
if (bot=='1'):
    bot='G'
elif (bot=='2'):
    bot='B'
else:
    bot='K'

print("Komputer Telah Memilih...")
print("Giliran Kamu")
#input user
player = input('Kamu Memilih [G/B/K] : ')

#kondisi menang kalah 
if (bot=='G'):
    if(player=='G'):
        print("Kamu dan Komputer Sama kuat")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
    elif(player=='B'):
        print("Kamu Menang!!!")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
    elif(player=='K'):
        print("Kamu Kalah!")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
elif (bot=='B'):
    if(player=='G'):
        print("Kamu Kalah!")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
    elif(player=='B'):
        print("Kamu dan Komputer Sama kuat")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
    elif(player=='K'):
        print("Kamu Menang!!!")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
elif (bot=='K'):
    if(player=='G'):
        print("Kamu Menang!!!")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
    elif(player=='B'):
        print("Kamu Kalah!")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)
    elif(player=='K'):
        print("Kamu dan Komputer Sama kuat")
        print("Pilihan Komputer adalah",bot,"dan Pilihan Kamu adalah",player)

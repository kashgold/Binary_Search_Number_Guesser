#import time

while True:
  try:
    length = int(input("What number do you want to be the highest, I will then guess your number:\n"))
    break
  except Exception as e:
    print(e)


list_o_num = list(range(1, length + 1))

def O1010(list_o_num):
  guessed_num = False
  lower = 0
  upper = len(list_o_num)
  while guessed_num == False:
    guess = (lower+upper)/2
    answer = input("\nIs your number greater than, less than or equal to " + str(round (guess)) + " (use g, l, or e): \n").lower().strip()
    if answer == 'g':
      lower = guess
    elif answer == 'l':
      upper = guess
    elif answer == 'e':
      return guess
    else:
      print("\nHey! Why would you do that? You know what you did\nand you are going to have to live with it... forever.\nYou did this on purpose to mess with me, didn't you?\nI hope you know that this is going on your permenant record.\nYour NSA agent may not be pleased with what you have done.\nListen here, if you do this again I will personally CTRL+ALT+DEL your computer.\nGood day!")

snatched = O1010(list_o_num)
print("\nI GOT YOUR NUMBER HAHAHA IT WAS " + str(round (snatched)))

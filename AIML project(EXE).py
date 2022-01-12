import getpass
from termcolor import colored
from re import search
import random

   

#to accept a movie from the user and remove consonants from it (player v player)
def movie_edit(movie):
    movie_list=[]
    movie_list[:0]=movie
    for i in range(0,len(movie)):
        if(movie_list[i]!='e'and movie_list[i]!='a'and movie_list[i]!='i' and movie_list[i]!='o' and movie_list[i]!='u' ):
            movie_list[i]='X'
        if(movie[i]==' '):
            movie_list[i]=' '  
    movie_new=""
    for x in movie_list:
        if(x=='X'):
            movie_new+='X'
        else:
            movie_new+=x
    return movie_new  

#to accept a movie from the user and remove consonants from it (player v computer)
def movie_edit1(movie,inp):
    inp_alpha=[]
    inp_alpha=inp
    movie_list=[]
    movie_list[:0]=movie
    for i in range(0,len(movie)):
        if(movie_list[i] not in inp_alpha):
            movie_list[i]='X'
        if(movie[i]==' '):
            movie_list[i]=' '  
    movie_new=""
    for x in movie_list:
        if(x=='X'):
            movie_new+='X'
        else:
            movie_new+=x 
    return movie_new  

#display lives for (player v computer)
def movie_lives(opt,liv):
    if(opt=='H'):
        strin = "HOLLYWOOD"
    else:
        strin = "BOLLYWOOD"
    lives_disp=""
    for i in range(9-liv):
        lives_disp+='-'
    lives_disp+=strin[(9-liv):]
    return lives_disp   

#player v player function
def play_player():
    player1=input("Player 1,enter your name\n")
    player2=input("player 2,enter your name\n")
    p1_score=0
    p2_score=0
    round=int(input("How many rounds do you want to play?\n"))

    for i in range(round):
        life2="BOLLYWOOD"
        mlist2=[]
        llist2=["a","i","e","o","u"]
    
        movie=getpass.getpass(player1+" enter a movie\n ")
        movie_game=movie_edit(movie)
        correct2=0
        n2=0

        while(correct2==0 and n2!=9):
            print("Lives:",movie_lives('j',9-n2))
            print(movie_game)
            print("What do you want to do,",player2,"?\n1.Guess Movie\n2.Guess Letter")
            choice=int(input())
            
            if(choice==1):
                  guess=input("Guess the movie name")
                  if(guess not in mlist2):
                      if(guess==movie):
                          print("Congratulations!!!!" , player2 ,"You are correct. The Movie name is" , guess)
                          p2_score=p2_score+1
                          correct2=1
                      else:

                          print("Hard Luck " + player2 +" , "+ guess + " is not the right answer")
                          mlist2.append(guess)
                          n2=n2+1
                          if(n2==9):
                              print("Hard Luck " + player2 +", You ran out of lives")

                  else:
                      print("Movie",guess,"is already tried and failed try again")

            if(choice==2):
                guess=(input("guess the letter"))
                if(guess not in llist2):
                    llist2.append(guess)
                    if(search(guess,movie)):
                        print("Congratulations!!!!" , player2 ,"You have guessed the correct letter")
                        mg=list(movie_game)
                        m=list(movie)
                        movie_game=""
                        movie=""
                        for i in  range(len(m)):
                            if(m[i]==guess):
                                mg[i]=guess
                        for x in mg:
                            movie_game+=x   
                        for x in m:
                            movie+=x       
                        if(movie_game==movie):
                            print("Congratulations!!!!" , player2 ,"You have guessed the movie correctly:",movie_game)  
                            p2_score=p2_score+1
                            correct2=1

                    else:
                        print("Hard Luck " + player2 +" , the letter "+ guess + " does not exist in the movie")
                        n2=n2+1
                        if(n2==9):
                              print("Hard Luck " + player2 +", You ran out of lives")
                else:
                    print("Letter",guess,"is either a vowel or already tried and failed or guessed")

        life1="BOLLYWOOD"
        mlist1=[]
        llist1=["a","i","e","o","u"]
    
        movie=getpass.getpass(player2+" enter a movie\n ")
        movie_game=movie_edit(movie)
        correct1=0
        n1=0

        while(correct1==0 and n1!=9):
            print("Lives:",movie_lives('j',9-n1))
            print(movie_game)
            print("What do you want to do,",player1,"?\n1.Guess Movie\n2.Guess Letter")
            choice=int(input())
            
            if(choice==1):
                  guess=input("Guess the movie name")
                  if(guess not in mlist1):
                      if(guess==movie):
                          print("Congratulations!!!!" , player1 ,"You are correct. The Movie name is" , guess)
                          p1_score=p1_score+1
                          correct1=1
                      else:

                          print("Hard Luck " + player1 +" , "+ guess + " is not the right answer")
                          mlist1.append(guess)
                          live=[]
                          live=list(life1)
                          live[n1]=colored(live[n1],'red')
                          life1=""
                          for x in live:
                              life1+=x
                          n1=n1+1
                          if(n1==9):
                              print("Hard Luck " + player1 +", You ran out of lives")

                  else:
                      print("Movie",guess,"is already tried and failed try again")

            if(choice==2):
                guess=(input("guess the letter"))
                if(guess not in llist1):
                    llist1.append(guess)
                    if(search(guess,movie)):
                        print("Congratulations!!!!" , player1 ,"You have guessed the correct letter")
                        mg=list(movie_game)
                        m=list(movie)
                        movie_game=""
                        movie=""
                        for i in  range(len(m)):
                            if(m[i]==guess):
                                mg[i]=guess
                        for x in mg:
                            movie_game+=x   
                        for x in m:
                            movie+=x       
                        if(movie_game==movie):
                            print("Congratulations!!!!" , player1 ,"You have guessed the movie correctly:",movie_game)  
                            p1_score=p1_score+1
                            correct1=1

                    else:
                        print("Hard Luck " + player1 +" , the letter "+ guess + " does not exist in the movie")
                        live=[]
                        live=list(life1)
                        live[n1]=colored(live[n1],'red')
                        life1=""
                        for x in live:
                            life1+=x
                        n1=n1+1
                        if(n1==9):
                              print("Hard Luck " + player1 +", You ran out of lives")
                else:
                    print("Letter",guess,"is either a vowel or already tried and failed or guessed")        
        print("\nSCORE:\n",player1,":",p1_score,"\n",player2,":",p2_score)
    if(p1_score>p2_score):
        print("Congratulations!!!!" , player1 ,"You won the game!!!!!") 
    elif(p2_score>p1_score):
        print("Congratulations!!!!" , player2 ,"You won the game!!!!!") 
    else:
        print("No One Won The Game!!!!!, It's A Tie")   

#player vs computer function
def play_computer():
    lives = 9
    h_list=['Avengers','Charlie And The Chocolate Factory','The Lion King','Inception','Harry Potter','Suicide Squad','Bird Box','Annabelle','The Ring','The Amazing Spiderman']
    b_list=['Welcome','Ready','Happy New Year','My Name Is Khan','Highway','Student Of The Year','Dear Zindagi','Kahaani','Talaash','Bhaag Milkha Bhaag']
    input_alpha=["a","i","e","o","u","A","E","I","O","U"]

    corr_chr = 0
    n = random.randint(0,9)
    #print("random number="+str(n))
    op1 = ""
    op2 = ""
    print("GUESS THE MOVIE")
    while(op1 != 'H' and op1!='B'):
        if(op1 != ""):
            print("Enter valid option!")
        op1=input("Choose hollywood (H/h) / Bollywood (B/b):")
        op1=op1.strip().upper()
    

    while (lives > 0):
        if ((op1=='H' and movie_edit1(h_list[n],input_alpha) == h_list[n]) or (op1=='B' and movie_edit1(b_list[n],input_alpha) == b_list[n])):
                if(op1=='H'):
                    print("Correct! You Won! The Movie was " + h_list[n])
                else:
                    print("Correct! You Won! The Movie was " + b_list[n])
                break
        if (op1=='H'):
            print("LIVES: "+movie_lives(op1,lives))
            print("Guess this hollywood movie:"+movie_edit1(h_list[n],input_alpha))
        else:
            print("LIVES: "+movie_lives(op1,lives))
            print("Guess this bollywood movie:"+movie_edit1(b_list[n],input_alpha))
        op2=""
        while(op2 != 'A' and op2 !='M'):
            op2 = input("Guess an alphabet(A/a) / Guess the movie(M/m): ")
            op2=op2.strip().upper()
        if(op2 == 'A'):
            while(corr_chr == 0):
                guess=input("Guess alphabet:")
                guess=guess.strip()
                if((ord(guess) >= 97 and ord(guess) <= 122) or (ord(guess) >= 65 and ord(guess) <= 90)):
                    corr_chr==1
                    if(guess in input_alpha):
                        print("Enter Consonants/ Non-repeated character only!")
                    else:
                        input_alpha.append(guess.lower())
                        input_alpha.append(guess.upper())
                        if (op1=='H'):
                            if(h_list[n].lower().find(guess.lower(),0,len(h_list[n])) == -1):
                                print("Wrong, You lost one life !!")
                                lives-=1
                        else:
                            if(b_list[n].lower().find(guess.lower(),0,len(b_list[n])) == -1):
                                print("Wrong, You lost one life !!")
                                lives-=1
                        break 
                else:
                    print("Invalid character, Enter Consonants only!")
        else:
            guess=input("Guess movie: ")
            guess=guess.strip().title()
        
            if ((op1=='H' and guess == h_list[n]) or (op1=='B' and guess == b_list[n])):
                if(op1=='H'):
                    print("Correct! You Won! The Movie was " + h_list[n])
                else:
                    print("Correct! You Won! The Movie was " + b_list[n])

                break
            else:
                print("Wrong, You lost one life !!")
                lives-=1    

    
        if(lives == 0):
                print("YOU LOST, BETTER LUCK NEXT TIME !!")

    
         


#Driver code
print("Welcome to GUESS THE MOVIE")  
valid=0 
while(valid==0):
    n=int(input("Which game mode do you want to play:\n1. Player vs Player\n2. Player vs Computer"))
    if(n==1):                        
        play_player() 
    elif(n==2):
        play_computer()
    else:
        print("Enter a valid input(1/2)")
        valid=0
    print("do you want to play again?(yes/no)")
    ans=input()
    if(ans=="yes"):
        valid=0
    else:
        valid=1        


  

    

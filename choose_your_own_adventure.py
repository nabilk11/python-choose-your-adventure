# Choose Your Own Adventure
print("******* Welcome to the Choose Your Own Adventure Game *******")

playing = input("Would you like to play? ").lower()

if playing != "yes" and playing != "y": # if true (anything but yes, will quit game
    print("Maybe Next Time!")
    quit()


name = input("What is your name? ").title()
print("Welcome", name, "\nAre you ready for an adventure?!")


answer = input("You are on a dirt road, it has come to an end, would you like to go left or right? ").lower()

if answer == "left":
    answer = input("You have come to a river, do you want to swim or walk around? (swim or walk) ").lower()
    if answer == "swim":
        answer = input("Damn...you encountered a CROC! Will you try to fight or run? ").lower()
        if answer == "fight":
            answer = input("You punched it in the nose, and managed to escape into the forest on the shore\nYou come across a scary old cabin, do you wanna knock or keep walking? ").lower()
            if answer == "knock":
                print("A witch answered and captured you for her eternal life potion, you're not dead yet, but you will be soon! You lose ;(")
            if answer in ["keep walking", "walking", "walk"]:
                answer = input("Good minding your own business, you avoided the witch! ")

        if answer == "run":
            print("You can't outswim a CROC! You were eaten piece by piece :( You Lose!")



elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly do you want to cross? (yes or no) ").lower()
    if answer == "no":
        print("Huh, what else you gonna do? You lose!")
    if answer in ["yes", 'y']:
        answer = input("The bridge started to cave in as you neared the end, but luckily a stranger pulled you back up from a certain death! Will you stay and talk to him or no? (yes or no) ").lower()
        if answer in ["yes", 'y']:
            print("Woohoo! He gave you gold and you win the game!")
        if answer in ["no", 'n']:
            print("The stranger was greatly offended and shot you with a bow and arrow. You lose :(")




else:
    print("Not a valid response...You lose!")

print("Thanks for playing", name + "!")
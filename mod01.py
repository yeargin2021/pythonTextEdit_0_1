file = open("Notes.txt", "a")
def runMe():
    saySomething = input("Say something: ")
    file.write('\n' + saySomething)

    if saySomething != "_____":
        runMe()
    else:
        file.close()

runMe()
filename = input("Enter a file name: ")
filename = filename + '.txt'

file = open(filename, "a+")
def runMe():
    saySomething = input("Say something: ")
    file.write('\n' + saySomething)

    if saySomething != "_____":
        runMe()
    else:
        file.close()

runMe()
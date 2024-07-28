import datetime

filename = input("Enter a file name: ")
filename = filename + '.txt'

file = open(filename, "a+")
# Print current date and time
file.write("\nCurrent date and time: " + str(datetime.datetime.now()))


def runMe():
    saySomething = input("Say something: ")
    file.write('\n' + saySomething)

    if saySomething != "_____":
        runMe()
    else:
        file.close()

runMe()
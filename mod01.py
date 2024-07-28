file = open("Notes.txt", "a")
saySomething = input("Say something: ")
file.write('\n' + saySomething)
file.close()

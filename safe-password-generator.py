# takes the platform the password is created for and swops the beginning and the ending
def swopLetters(platform):
    cutoff = len(platform)//2

    beginning = []
    i = cutoff
    
    while (i < len(platform)):
        beginning.append(platform[i])
        i+= 1

    ending = []
    j = 0

    while (j < cutoff):
        ending.append(platform[j])
        j+= 1

    addLengthAsNumber(beginning, len(platform))
    addSpecialCharacter(ending, len(platform))
    combineToWord(uniqueWord(beginning), ending)
    
# calculates the number of characters in the name of the platform and uses the number in the password
def addLengthAsNumber(beginning, length):
    beginning.append(str(length))

    return beginning

def combineToWord(beginning, ending):
    combined = beginning + ending

    password = ""
    for char in combined:
        password+= char
    
    print("Your safe password is: ", password)
    
# adds a special character to the password depending on the length of the platform
def addSpecialCharacter(ending, length):
    
    specialCharacters = ["!", "#", "$", "%", "&", 
                        "*", "+", "?", "=", ":"]
    
    if (length > 9):
        length = length % 10

    characterToBeAdded = specialCharacters[length]

    ending.insert(0, characterToBeAdded)

    return ending

# adds a unique word (capitalised) to the password, chosen by the user
def uniqueWord(beginning):

    print("Enter an unique word you'd like to use in your password: ")
    userWord = input().capitalize()
  
    wordAsArray = list(userWord)
    password = beginning + wordAsArray

    return password

# asks for the platform and capitalises the first letter       
def askForPlatform():
    print("Enter the platform you're creating a password for: ")

    platform = input().capitalize()

    return platform

def makePassword(platform):
    swopLetters(platform)

def run():
    platform = askForPlatform()
    makePassword(platform)
    
run()

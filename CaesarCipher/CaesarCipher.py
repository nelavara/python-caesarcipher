alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def test_word(wordToTest): #This function validates the text entered
  test4 = False
  counter = 0
  spaceContainer = ""
  for y in wordToTest:
    if y.islower() == False and y.isspace() == False:
      test4 = False
    elif y.isspace() or y.isalpha():
      test4 = True
      counter +=1
      if y.isspace(): #This is used to handle any spaces that are entered
        wordToTest = wordToTest.replace(" ","")
        spaceContainer += str(counter)
        spaceContainer += ","
    if test4 == False: 
      wordToTest = "error" #Here we set the error condition if the text has numbers or symbols in it.
  wordToTest += spaceContainer
  return wordToTest

def put_space_back(encryptedString, spaces): #This function places the spaces back into the text.
	container = ""
	tempList = list (encryptedString) #We convert the encrypted text to a list.
	position = 0
	for c in spaces: # Here we place the spaces back into the text using a for loop.
		if c.isdigit(): 
			container += c
		elif c == ",":
			position = int(container)
			container = container.replace(container, "")
			tempList.insert(position-1, " ")
			position = 0
	encryptedString = "".join(tempList) # Convert the list back to a string and return it to the caller.
	return encryptedString

def encrypt_word (secret, rot): #This function takes the unecncrypted text plus the rotations and uses that to encrypt it.
	enword = ""
	for c in secret:
		position = alphabet.index(c) + rot #We determine the position by adding the index of the letter in the alphabet to the rotation.
		if position > len(alphabet)-1:  # inspiration for this function came from https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
			position-=26 #Here we have to account for the array bounds.
		enword += alphabet[position] #Here we build the encrypted text.
	return enword #Finally we return the encrypted text.

def flip_letters(flips, unEnc): # Here we flip the letters
	flips = flips.lower() #All letters are converted to lower case for processing
	lettersToFlip = ""
	for c in flips:
		if c.isalpha(): #We need to make sure that only letters are flipped.
			lettersToFlip +=c
	z = list(lettersToFlip) #Concert the letters to a list for easier manipulation
	count = 0
	if len(z)%2 == 0: #We need to make sure there is an enven amount of letters or there is no reason to flip.
		while count <= len(z)-1:
			if z[count] in unEnc: #If the letter is in the string
				unEnc = unEnc.replace(z[count], "$") #First we set to a garbage value.
				unEnc = unEnc.replace(z[count+1], z[count]) #Then we set the string to replace letters with the next item in the list.
				unEnc = unEnc.replace("$", z[count+1]) #Then we need to replace the garabage values with our intended letter.
			count+=2 #We must increment the count by two to ensure flips.
	return unEnc

def get_number_rotations(rotations): #If no rotations entered we set the value to 5.
  #set to 5 if no rotations are entered
  if len(rotations) == 0:
    rotations = "5"
  return rotations

def get_entry(userInput, count): #This function performs data validation and divides input into different strings
	unEnc = "" #holder for unecnrypted text
	rotations = "" #holder for the numger of rotations to be performed
	letters = "" #holder for letters that will later be used for flips
	tracker = count #This allows us to count the number of commas entered, which is used for data entry
	for c in userInput: #Interate through the string and separate into three different strings
		if c != ',' and c.isalpha and tracker == count:
			unEnc += c #Building the text to later be encrypted
		elif c == ',':
			tracker-=1 #Detecting a comma
		elif c.isdigit and tracker == count-1 and c != ',':
			rotations+=c #Building the string for the number of rotations
		elif c.isalpha and c.isupper and c!= ',' and c!= '(' and c!= ')':
			letters+=c #Building the letters that will be flipped later
		elif c == " ":
			unEnc += c #Accounting for spaces
	unEnc = unEnc.lower() #Here we convert all text to be encrypted to lower case
	unEnc = test_word(unEnc) #We validate the text entered
	rotations = get_number_rotations(rotations) #This function sets the number of rotations to 5 if none entered.
	rotations = int(rotations) #Now we convert rotations to an integer.
	if unEnc != "error":
		unEnc = flip_letters(letters, unEnc) #Now we are flipping the letters in the unencrypted text.
		spacePosition = "" 
		for y in unEnc:# Here we need to remove the spaces from the phrase if any
			if y.isdigit():
				spacePosition += y
				unEnc = unEnc.replace(y, "")
			elif y == ",": #We also remove any remaining commas
				unEnc = unEnc.replace(y,"")
				spacePosition += ","
		unEnc = encrypt_word(unEnc, rotations) #Next we pass the unecrypted to text to the encryption function.
		unEnc=put_space_back(unEnc,spacePosition) #Lastly we need to place the spaces back into the text.
	return unEnc # Now we return the encrypted text back to the caesar_chiper_encrypt function.

def caesar_chiper_encrypt (*args): # This function accepts the arguments passed to it.
	entry = "" # Creation of empty string to accept all arguments passed
	count = 0
	for count, stringText in enumerate(args):
		entry += str(stringText)  # Here we build a string of all arguments passed
		entry+= "," #We separate each item with a comma to assist with processing later.
		count+=1
	entry=get_entry(entry,count) #We send our input to get_entry for
	return entry

test = caesar_chiper_encrypt("valentino",2,("v","a"),("n","o"))
print (test)


import random
HANGMAN_PICS = ['''
       ___________
      |.---------.|
      ||$        ||
      ||         ||
      ||         ||
      |'---------'|
       `)__ ____('
       [=== -- o ]---.
       '---------'    \\
     _______________   )
    |::::::::::: :::| /T\\
    |::::::::::: :::| \\_/
     ---------------''', '''
       ___________
      |.---------.|
      ||         ||
      ||  HELLO! ||
      ||         ||
      |'---------'|
       `)__ ____('
       [=== -- o ]---.
       '---------'    \\
     _______________   )
    |::::::::::: :::| /T\\
    |::::::::::: :::| \\_/
     ---------------''', '''
       ___________
      |.---------.|             __
      ||$        ||    (0)(0)  /  \\
      ||         ||      \\ \\  / /\\ \\
      ||         ||       \\ \\/ /  \\/
      |'---------'|        \\__/
       `)__ ____('
       [=== -- o ]---.
       '---------'    \\
     _______________   )
    |::::::::::: :::| /T\\
    |::::::::::: :::| \\_/
     ---------------''', '''
       ___________
      |.---------.|    __
      ||   ^  ^  ||   /  \\
      ||  (0)(0) ||  / /\\ \\
      ||         ||\\/ /  \\/
      |'---------'|__/
       `)__ ____('
       [=== -- o ]---.
       '---------'    \\
     _______________   )
    |::::::::::: :::| /T\\
    |::::::::::: :::| \\_/
     ---------------''', '''
       ___________
      |.---------.|
      ||         ||
      ||  £%$!#  ||
      ||         ||
      |'---------'|
       `)__ ____('
       [=== -- o ]---.
       '---------'    \\
     _______________   )
    |::::::::::: :::| /T\\
    |::::::::::: :::| \\_/
     ---------------''', '''
       ___________
      |.---------.|
      ||!£%$!#*&~||
      ||)$@&(&@!)||
      ||*&/£@$!#^||
      |'---------'|
       `)__ ____('
       [=== -- o ]---.
       '---------'    \\
     _______________   )
    |::::::::::: :::| /T\\
    |::::::::::: :::| \\_/
     ---------------''', '''
       ___________
      |.---------.|
      ||  X   X  ||
      ||    .    ||
      ||   ___   ||
      |'---------'|
       `)__ ____('
       [=== -- o ]---.
       '---------'    \\
     _______________   )
    |::::::::::: :::| /T\\
    |::::::::::: :::| \\_/
     ---------------''']

rawwords = {
    "ASCII": "Imagine a special language that computers use to talk to each other. In this language, every letter, number, and symbol has its own secret code. When you type something on a computer, it translates the letters you type into these secret codes so that the computer can understand what you're saying.",
    "Authenticity": "This is like knowing your teddy bear is the real one and not a copy or fake because you remember its special marks, smell, and feel.",
    "Bit": "This is like a tiny light switch in a computer. It can be either turned on or off, represented as 1 or 0. By switching the lights on and off in different ways, you can form things like photos, games, and music.",
    "Bitstream": "Imagine you have a super long train made of toy blocks. Each block can be one of two colours: red or blue. The way these blocks are arranged in a row, one after another, makes a special pattern. This pattern can tell a story or show a picture if you know how to read it.",
    "Bitrot": "This is when your digital toys, like photos, videos, or games, start to break or vanish even if no one touched them. It's like when your toy begins to lose its colour or breaks even though it's carefully stored. Thankfully, the grownups have ways to fix this!",
    "Born Digital": "This is like a picture you drew on a tablet or computer. It never was on paper and you didn’t use pencils and crayons to make it. It was made and stays on the computer.",
    "Byte": "Think about this like building blocks in your toy set. Each is a piece that the computer uses to save or show information. For example, if you type a letter on your keyboard, one block is used to store that letter in the computer's memory.",
    "Catalogue": "This is like a big list or book that helps you remember and find all your cool toys or books, showing where you’ve put everything",
    "Checksums": "This is like a special secret code that computers use to make sure the messages they send each other are not mixed up or wrong. It's like when we count the pieces of a puzzle before we start so we know we are not missing anything.",
    "Dark Archive": "Think of this like a special treasure box in a computer where we put important things and only open when we really really need to, like keeping your special toys safe for a long time.",
    "Dependency": "Just like Batman needs his utility belt with all his cool tools, computer programs and files need other programs and files to do their job correctly. Without this they wouldn’t be able to do what they’re supposed to do.",
    "Digitisation": "This would be like taking a picture of your favourite drawing, and then saving it on a computer, so you can still see it even if the original drawing gets torn or lost.",
    "DROID": "This is like a super smart detective for computers. It can look at different types of files and tell you what kind they are, even if they've been changed, much like you can tell the difference between a car and a truck just by looking at them.",
    "Emulation": "This is like pretending something old is something new. Imagine if you have an old VHS tape but your player doesn’t work anymore, so you use a special machine that pretends the VHS is a DVD.",
    "Encryption": "This is like a secret language that only you and your computer understand. If someone tries to read your message without the secret key, they just see gibberish. It keeps your stuff safe from people who want to steal it or look at it without permission.",
    "File Characterisation": "This is like trying to understand what something is just by looking at it. Imagine you find a mysterious toy in a box, but it has no label or name. To figure out what it is, you have to look at its shape, colour, and other details. In the same way this helps us learn about computer files by examining their special features and properties without opening them.",
    "File Format": "These are like different types of boxes that hold information on a computer. Just like you have different toys that need different boxes, different types of information like pictures, videos, or written words have their own boxes.",
    "Fixity": "Think about a puzzle you put together. Once you finish it, you want the pieces to stay in their places, right? The puzzle doesn't change on its own, and the pieces don't move around. It means that no matter how much time passes, you can always count on it being just as it was.",
    "Hardware": "This refers to the physical things we use to store and save digital stuff, like our pictures and games. It can be like a special box, called a hard drive or memory card.",
    "Hex": "This is like the way we count things, but instead of only having numbers from 0 to 9, we also use letters from A to F. This means we can count up to 15 in one digit. We use it to communicate with computers, because they understand these numbers very well.",
    "Infrastructure": "This is like the backbone that supports everything. It includes all the things we need to store and protect digital information, like computers, servers, and data centres. It’s like a big, powerful machine that keeps everything safe and running smoothly.",
    "Ingest": "This is like taking your toys and putting them safely in a box so you can use them later without them getting lost or broken. It's a way of saving your digital stuff, like videos or photos, in a special space where they won't get damaged or disappear.",
    "Lossless Compression": "This is like a magic trick! Imagine if you have a big doll house that you couldn’t fit into your toy box. Then, a magician comes and uses a magic spell to shrink it down and fit it into the box. The good news is whenever you want, he can undo the magic and your dollhouse would be just as it was before. In the same way this shrinks files so they take less space, but can bring them back to their original size without losing any information.",
    "Lossy Compression": "This is like when you use blocks to build a house, but use fewer blocks to make it smaller. You have the same house, it’s just not as detailed anymore. In computers this makes a file smaller by removing some details permanently, which makes the file lose some of its quality.",
    "Malware": "This is like a flu bug for your computer. It’s made by people who want to make your computer sick or take your stuff, like how some bullies want to take your toys.",
    "Metadata": "This is like a special tag that helps us remember and find things later. It tells us information about something, like when it was made, who made it, and what it's about.",
    "Migration": "Imagine your favourite toy getting old and you can't play with it anymore because it's broken, or your friends who have newer toys can't play with it. But then, you find a way to change your toy into a newer, cooler one so you can keep playing with it and your friends can too.",
    "OAIS": "Imagine you have a special treasure chest where you keep all your favourite toys and things. This is a fancy way of organising and taking care of all the important information in the world, just like you take care of your special toys in your treasure chest.",
    "Obsolescence": "This is like when your favourite toy is no longer being made or sold in stores. It’s still useful and fun, but it’s harder to find parts if it breaks or get help if you don’t know how to use it. Similarly, old versions of programs or software are sometimes not supported or updated anymore, making them out of date.",
    "Open Source": "This is like a big, public sandbox where everyone can build sand castles. Anyone can use the sand and the buckets to make their own castle and change and make better other castles. If they think of a cool new way to build, they can show everyone else how to do it too. That way, everyone can work together to make lots of awesome sand castles.",
    "Proprietary": "This is like owning a magical colouring book. This book belongs only to you and only you know how to make the colours appear on the pages. Others can’t use or colour in this book unless you give them special permission, and they can’t make their own magic colouring book because the secret of how to make it is yours alone.",
    "Redundancy": "Imagine you have a special toy, and you're afraid of losing it or breaking it. So, you decide to get an extra toy that's exactly the same, just in case something happens to the first one. Now, you have two identical toys! This means if one toy gets lost or broken, you still have the other one to play with.",
    "Software": "This is like a special helper or friend with a set of instructions or rules that tell computers what to do. It's like a recipe book for computers, telling them how to play games and do lots of other cool things. Without this computers wouldn't know what to do, just like we need instructions to make a yummy cake.",
    "Crawler": "This is a special program that visits lots of websites and collects information from them. It’s like a little bug that travels around the internet, looking at web pages and bringing back important stuff, so we can have it saved and use it later."
}
words = {key.lower(): value for key, value in rawwords.items()}

def getRandomWord(wordList):
	randword = random.choice(list(words.keys()))
	randword = randword.lower()
	return randword

def displayBoard(missedLetters, correctLettersfn, secretWord):
	global correctLetters
	print(HANGMAN_PICS[len(missedLetters)])
	print()
	# print(secretWord)
	print('Missed letters:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()
	
	blanks = '_' * len(secretWord)
	
	for i in range(len(secretWord)):
		if secretWord[i] in correctLettersfn:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
		elif secretWord[i] == " ":
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			correctLetters = correctLetters + secretWord[i]
	
	for letter in blanks:
		print(letter, end=' ')
	print()

def getGuess(alreadyGuessed, words):
	while True:
		print('Guess a letter or type "hint" for a clue.')
		guess = input()
		guess = guess.lower()
		print()
		if guess == 'hint':
			print(words[secretWord])
		elif len(guess) != 1:
			print('Please enter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER.')
		else:
			return guess

def playAgain():
	print()
	print('Do you want to play again? (yes or no)')
	return input().lower().startswith('y')
	
print('H A N G M A N')
print('Based on the code by Al Sweigart. ASCII art of computer by Joan Stark')
print('Hints taken from DP5YO by Francesca Mackenzie and Nathan Isip with ChatGPT4.0')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(missedLetters, correctLetters, secretWord)
	
	guess = getGuess(missedLetters + correctLetters, words)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('The secret word is "' + secretWord + '"!\n\n' + words[secretWord] + '\n\nYou have won!')
			gameIsDone = True
			
	else:
		missedLetters = missedLetters + guess
		
		if len(missedLetters) == len(HANGMAN_PICS) - 1:
			displayBoard(missedLetters, correctLetters, secretWord)
			print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
			gameIsDone = True
		
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break
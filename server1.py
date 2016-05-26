# Save as server.py 
# Message Receiver
import os
import socket
import numpy as np



host ="192.168.1.97"
port = 9041
buf = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
print "Waiting to receive messages..."

tab3letter = ['cat', 'dog', 'tcp', 'man', 'run']
tab4letter = ['port', 'cake', 'host', 'mail', 'line']
tab5letter = ['drink', 'water', 'woman', 'train', 'table']
tab6letter = ['friend', 'rocket', 'spiral', 'socket', 'powder']
tab7letter = ['gravity', 'quicker', 'subject', 'nucleus', 'neutral']
tab8letter = ['angstrom', 'souvenir', 'poincare', 'hamilton', 'reaction']

sock.listen(1)
conn, addr = sock.accept()
i = 0
#data = []
poziom = 0
letters_of_word = 0
word_for_guess = 'initial'
condition = True
condition1 = True


while ((condition == True)and (condition1 == True)):
	if (i == 0):
		text1 = "Enter number of letters:"
		conn.sendall(text1)
		i += 1
		data = conn.recv(buf)
		letters_of_word = int(data)
		if (letters_of_word == 3):
			word_for_guess = tab3letter[(int)(np.random.random()*(5))]
		if (letters_of_word == 4):
			word_for_guess = tab4letter[(int)(np.random.random()*(5))]
		if (letters_of_word == 5):
			word_for_guess = tab5letter[(int)(np.random.random()*(5))]
		if (letters_of_word == 6):
			word_for_guess = tab6letter[(int)(np.random.random()*(5))]
		if (letters_of_word == 7):
			word_for_guess = tab7letter[(int)(np.random.random()*(5))]
		if (letters_of_word == 8):
			word_for_guess = tab8letter[(int)(np.random.random()*(5))]

		print "slowo: ", word_for_guess
		zaszyfrowany_string = "#"*len(word_for_guess)
		szyfr = list(zaszyfrowany_string)
		print "Recieved message: " + data
	elif (i == 1):
		text1 = "Wybierz poziom: 1, 2, 3"
		conn.sendall(text1)
		i += 1
		data = conn.recv(buf)
		poziom = int(data)
		print "Poziom : " + data 

	else:
		if ((poziom ==  1) and (condition1 == True)) : #poziom 1
			#print ("wchodze do poziom 1 gry!")
			for j in range (10):
				if (j == 9):
					# oznacza koniec gry
					condition = False
					condition1 = False
					text = "No mistake or failure is as bad as to stop and not try again :) " + "\n"
					conn.sendall(text)
					sock.close()
					os._exit(0)
				word_length = len(word_for_guess)
				text = "Word:   " + "".join(szyfr) + "\n"
				conn.sendall(text)
				text = "Guess: letter (L) or word (W)? " + "\n"
				conn.sendall(text)
				choice = conn.recv(buf)
				print "Recieved message: " + data
				if(((choice == 'L') or (choice == 'l') )and (condition1 == True)):
					text = "Guess letter? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Recieved letter: " + choice1
					if ((choice1 in word_for_guess) == True):
						text = "Good guess. Letter is on place:  " + str(word_for_guess.index(choice1)+1) + "\n"
						conn.sendall(text)
						szyfr[word_for_guess.index(choice1)] = 	choice1
						if '#' not in szyfr:
							text = "Good guess. You won the game! " 
							conn.sendall(text)
							condition = False
							condition1 = False
							sock.close()
							os._exit(0)
					
						conn.sendall("".join(szyfr)) #zamienia liste na stringa
						
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)	
					j += 1
					#print ("j= ", j)

				elif(((choice == 'W') or (choice == 'w') )and (condition1 == True)):
					text = "Guess word? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Recieved word: " + choice1
					if ((choice1 == word_for_guess) ):
						text = "Good guess. You won the game! " 
						conn.sendall(text)
						sock.close()
						os._exit(0)
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
				
					j += 1
					#print ("j= ", j)
						
		if ((poziom ==  2) and (condition1 == True)) : #poziom 2
			print ("wchodze do poziom 1 gry!")
			for j in range (8):
				if (j == 7):
					condition = False
					condition1 = False
					text = "No mistake or failure is as bad as to stop and not try again :) " + "\n"
					conn.sendall(text)
					sock.close()
					os._exit(0)

				word_length = len(word_for_guess)
				text = "Word: " + "".join(szyfr) + "\n"
				conn.sendall(text)
				text = "Guess: letter (L) or word (W)? " + "\n"
				conn.sendall(text)
				choice = conn.recv(buf)
				print "Recieved message: " + data
				if(((choice == 'L') or (choice == 'l') )and (condition1 == True)):
					text = "Guess letter? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Recieved letter: " + choice1
					if ((choice1 in word_for_guess) == True):
						text = "Good guess. Letter is on place:  " + str(word_for_guess.index(choice1)+1) + "\n"
						conn.sendall(text)
						szyfr[word_for_guess.index(choice1)] = 	choice1
						if '#' not in szyfr:
							text = "Good guess. You won the game! " 
							conn.sendall(text)
							condition = False
							condition1 = False
							sock.close()
							os._exit(0)
					
						conn.sendall("".join(szyfr)) #zamienia liste na stringa
						
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
						
					j += 1
				#	print ("j= ", j)

				elif(((choice == 'W') or (choice == 'w') )and (condition1 == True)):
					text = "Guess word? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Recieved word: " + choice1
					if ((choice1 == word_for_guess) ):
						text = "Good guess. You won the game! " 
						conn.sendall(text)
						sock.close()
						os._exit(0)
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
				
					j += 1
				#	print ("j= ", j)

		if ((poziom ==  3) and (condition1 == True)) : #poziom 3
			for j in range (6):
				if (j == 5):
					# oznacza koniec gry
					condition = False
					condition1 = False
					text = "No mistake or failure is as bad as to stop and not try again :) " + "\n"
					conn.sendall(text)
					sock.close()
					os._exit(0)

				word_length = len(word_for_guess)
				text = "Word:   " + "".join(szyfr) + "\n"
				conn.sendall(text)
				text = "Guess: letter (L) or word (W)? " + "\n"
				conn.sendall(text)
				choice = conn.recv(buf)
				print "Recieved message: " + data
				if(((choice == 'L') or (choice == 'l') )and (condition1 == True)):
					text = "Guess letter? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Recieved letter: " + choice1
					if ((choice1 in word_for_guess) == True):
						text = "Good guess. Letter is on place:  " + str(word_for_guess.index(choice1)+1) + "\n"
						conn.sendall(text)
						szyfr[word_for_guess.index(choice1)] = 	choice1
						if '#' not in szyfr:
							text = "Good guess. You won the game! " 
							conn.sendall(text)
							condition = False
							condition1 = False
							sock.close()
							os._exit(0)
					
						conn.sendall("".join(szyfr)) #zamienia liste na stringa
						
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
						
					j += 1
				#	print ("j= ", j)

				elif(((choice == 'W') or (choice == 'w') )and (condition1 == True)):
					text = "Guess word? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Recieved word: " + choice1
					if ((choice1 == word_for_guess) ):
						text = "Good guess. You won the game! " 
						conn.sendall(text)
						sock.close()
						os._exit(0)
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
				
					j += 1
				#	print ("j= ", j)

				
	# else:
		
		# data = conn.recv(buf)
		# print "Recieved message: " + data

	if data == "exit":
		break
sock.close()

os._exit(0)
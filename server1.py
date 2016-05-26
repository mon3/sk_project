# Save as server.py 
# Message Receiver
import os
import socket
import numpy as np



host ="192.168.1.97"
port = 9033
buf = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
print "Waiting to receive messages..."

tab3letter = ['cat', 'dog', 'tcp', 'man', 'run']
tab4letter = ['port', 'cake', 'host', 'mail', 'line']
tab5letter = ['drink', 'water', 'woman', 'train', 'table']
tab6letter = ['friend', 'rocket', 'spiral', 'socket', 'powder']
tab7letter = ['passion', 'crosswords', 'wisdoms', 'address', 'florist']
tab8letter = ['backpack', 'backpays', 'backrest', 'backroom', 'backseat']

sock.listen(1)
conn, addr = sock.accept()
i = 0
#data = []
poziom = 0
letters_of_word = 0
word_for_guess = 'initial'
condition = True
condition1 = True

#while (condition == True):
while ((condition == True)and (condition1 == True)):
	print condition, condition1
	print "ciagle dziala while: "
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
		print "Received message: " + data
	elif (i == 1):
		text1 = "Wybierz poziom: 1, 2, 3"
		conn.sendall(text1)
		i += 1
		data = conn.recv(buf)
		poziom = int(data)
		#print "typ poziomu: ", type(poziom)
		print "Poziom : " + data #zamiast "Received data: " w celach debugowania

	else:
		if ((poziom ==  1) and (condition1 == True)) : #poziom 1
			print ("wchodze do poziom 1 gry!")
			for j in range (10):
				#if (condition1 == True):
				if (j == 9):
					# oznacza koniec gry
					print ("wchodze do petli z condition!")
					condition = False
					condition1 = False
					print condition, condition1
					text = "No mistake or failure is as bad as to stop and not try again :) " + "\n"
					conn.sendall(text)
					sock.close()
					os._exit(0)
				word_length = len(word_for_guess)
				text = "Recieved word:   " + "".join(szyfr) + "\n"
				conn.sendall(text)
				text = "Guess: letter (L) or word (W)? " + "\n"
				conn.sendall(text)
				choice = conn.recv(buf)
				print "Received message: " + data
				if(((choice == 'L') or (choice == 'l') )and (condition1 == True)):
					text = "Guess letter? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Received message: " + choice1
					if ((choice1 in word_for_guess) == True):
						print "type(letter): ", type(choice1)
						text = "Good guess. Letter is on place:  " + str(word_for_guess.index(choice1)+1) + "\n"
						conn.sendall(text)
						szyfr[word_for_guess.index(choice1)] = 	choice1					
						conn.sendall("".join(szyfr))
						#i += 1
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
						#i += 1
					j += 1
					print ("j= ", j)
						
		if ((poziom ==  2) and (condition1 == True)) : #poziom 2
			print ("wchodze do poziom 1 gry!")
			for j in range (8):
				#if (condition1 == True):
				if (j == 7):
					# oznacza koniec gry
					print ("wchodze do petli z condition!")
					condition = False
					condition1 = False
					print condition, condition1
					text = "No mistake or failure is as bad as to stop and not try again :) " + "\n"
					conn.sendall(text)
					sock.close()
					os._exit(0)
				word_length = len(word_for_guess)
				text = "Recieved word:   " + "".join(szyfr) + "\n"
				conn.sendall(text)
				text = "Guess: letter (L) or word (W)? " + "\n"
				conn.sendall(text)
				choice = conn.recv(buf)
				print "Received message: " + data
				if(((choice == 'L') or (choice == 'l') )and (condition1 == True)):
					text = "Guess letter? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Received message: " + choice1
					if ((choice1 in word_for_guess) == True):
						print "type(letter): ", type(choice1)
						text = "Good guess. Letter is on place:  " + str(word_for_guess.index(choice1)+1) + "\n"
						conn.sendall(text)
						szyfr[word_for_guess.index(choice1)] = 	choice1					
						conn.sendall("".join(szyfr))
						#i += 1
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
						#i += 1
					j += 1
					print ("j= ", j)
						
		if ((poziom ==  3) and (condition1 == True)) : #poziom 3
			print ("wchodze do poziom 1 gry!")
			for j in range (6):
				#if (condition1 == True):
				if (j == 5):
					# oznacza koniec gry
					print ("wchodze do petli z condition!")
					condition = False
					condition1 = False
					print condition, condition1
					text = "No mistake or failure is as bad as to stop and not try again :) " + "\n"
					conn.sendall(text)
					sock.close()
					os._exit(0)
				word_length = len(word_for_guess)
				text = "Recieved word:   " + "".join(szyfr) + "\n"
				conn.sendall(text)
				text = "Guess: letter (L) or word (W)? " + "\n"
				conn.sendall(text)
				choice = conn.recv(buf)
				print "Received message: " + data
				if(((choice == 'L') or (choice == 'l') )and (condition1 == True)):
					text = "Guess letter? " + "\n"
					conn.sendall(text)
					choice1 = conn.recv(buf)
					print "Received message: " + choice1
					if ((choice1 in word_for_guess) == True):
						print "type(letter): ", type(choice1)
						text = "Good guess. Letter is on place:  " + str(word_for_guess.index(choice1)+1) + "\n"
						conn.sendall(text)
						szyfr[word_for_guess.index(choice1)] = 	choice1					
						conn.sendall("".join(szyfr))
						#i += 1
					else:
						text = "Unfortunately, bad guess " + "\n"
						conn.sendall(text)
						#i += 1
					j += 1
					print ("j= ", j)
						
				
	# else:
		
		# data = conn.recv(buf)
		# print "Received message: " + data

	if data == "exit":
		break
sock.close()

os._exit(0)
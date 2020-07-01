passw={'Gabe':'figyfigy','Gabriel':'fasciolasis'}
user=input('Enter username')
if user in passw:
	password=input('Enter password:  ')
	if password==passw[user]:
		print('You\'re logged in.')
	else:
		print('Invalid password.')
else:
	print('Not a valid user.')
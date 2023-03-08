import requests,os,sys
os.system('clear')
print('''\033[1;32m
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
''')
print('''\033[1;32m
█▀▀ █▀▀█ █▀▀ ── █───█ █▀▀ █▀▀▄ 
▀▀█ █▄▄▀ █── ▀▀ █▄█▄█ █▀▀ █▀▀▄ 
▀▀▀ ▀─▀▀ ▀▀▀ ── ─▀─▀─ ▀▀▀ ▀▀▀─
''')

print('''\033[1;32m
------------------------[~~~~~~~~~~~~~~~]-----------------------

                          [  SECURITY ]

                          [  WELCOME  ]

Telegram : https://t.me/protection17

------------------------[~~~~~~~~~~~~~~~]-----------------------
''')
try:
	web = input('\033[;131nEnter web ○~~> :  ')
	url = requests.get(web)
	cc = (url.text)
	op = open('src.html','w')
	op.write(cc)
	os.system('mv src.html /sdcard')
	os.system('cd')
	print('\033[1;33m-'*30)
	print('\033[1;31m☆save sdcard')
	print('\033[1;33m-'*30)
	print('\033[1;34mDo you run')
	x = input('[ n / y ]》: ')
	if x == 'y':
		os.system('python3 src.py')
	else:
		if x == 'n':
			os.system('clear')
			os.system('cd')
			os.system('cd $HOME')
except Exception as awol:
	print(awol)
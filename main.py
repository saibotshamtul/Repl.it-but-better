import os
import server

key = os.getenv('key')

if not key: # if there's no api key set then show tutorial
	print('How to use Repl.it but better:')
	print('')
	print('1) go to https://devs.turbio.repl.co/ and get an api key')
	print('2) fork the repl')
	print('3) create a file called .env')
	print('4) inside that file put key=YOURAPIKEY (replacing YOURAPIKEY with your api key)')
	exit()


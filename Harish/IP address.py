import ipaddress

def check(ip):
	try:
		ipaddress.ip_address(ip)
		print("Valid IP address")
	except ValueError:
		#
		print("Invalid IP address")

# Driver Code
if __name__ == '__main__':
	ip = "192.168.0.1"
	check(ip)

	ip = "110.234.52.124"
	check(ip)

	ip = "366.1.2.2"
	check(ip)


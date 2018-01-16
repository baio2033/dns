import dns.resolver
import datetime
import time

if __name__ == "__main__":

	#f = open("dns.txt", "w")
	domain = "xer0ma.info"

	while 1:
		resolv = dns.resolver.Resolver()
		ans = resolv.query(domain, "A")

		now = time.localtime()
		now = "%02d-%02d-%02d %02d:%02d:%02d" %(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
		for r in ans:
			print now, ",", domain, ",",r
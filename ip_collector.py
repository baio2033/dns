import dns.resolver
import datetime
import time

if __name__ == "__main__":

	#f = open("dns.txt", "w")
	domain = "xer0ma.info"
	cnt = 0
	f = open("result.csv", "w")
	f.write("idx,time,domain,ip\n")
	while 1:
		line = ""
		resolv = dns.resolver.Resolver()
		ans = resolv.query(domain, "A")

		now = time.localtime()
		now = "%02d-%02d-%02d %02d:%02d:%02d" %(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
		for r in ans:
			print now, ",", domain, ",",r
		line += str(cnt) + "," + now + "," + domain + "," + r + "\n"
		f.write(line)
		time.sleep(3600)

	f.close()
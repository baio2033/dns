import threading, time, csv
import dns.resolver

def getIP(domain):
	resolv = dns.resolver.Resolver()
	ans = resolv.query(domain, "A")

	for r in ans:
		ip = str(r)

	return ip

def getTime():
	now = time.localtime()
	now = "%02d-%02d-%02d %02d:%02d:%02d" %(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
	return now

def record(domain):
	while True:
		f = open('result.csv', 'a')
		with f:
			writer = csv.writer(f)

			ip = getIP(domain)
			date = getTime()

			row = [domain,ip,date]
			writer.writerow(row)
			print(row)

		time.sleep(1)
		f.close()



if __name__ == "__main__":
	domain = "fl0ckfl0ck.info"

	t1 = threading.Thread(target=record, args=(domain,))
	t1.start()
import threading, time, csv
import dns.resolver

def getIP(domain):
	resolv = dns.resolver.Resolver()

	try:
		ans = resolv.query(domain, "A")
	except:
		print("[-] dns change -> 8.8.8.8")
		resolv.nameservers = ['8.8.8.8']
		ans = resolv.query(domain, "A")

	for r in ans:
		ip = str(r)

	return ip, resolv.nameservers[0]

def getTime():
	now = time.localtime()
	now = "%02d-%02d-%02d %02d:%02d:%02d" %(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
	return now

def record(domain):
	idx = 0
	field = ["index","date","domain","IP","DNS"]
	while True:
		f = open('result.csv', 'a')
		with f:
			writer = csv.writer(f)
			if idx == 0:
				writer.writerow(field)
			ip, nameserver = getIP(domain)
			date = getTime()

			row = [idx,date,domain,ip,nameserver]
			writer.writerow(row)			

		time.sleep(3600)	
		f.close()
		idx += 1



if __name__ == "__main__":
	domain = "fl0ckfl0ck.info"

	t1 = threading.Thread(target=record, args=(domain,))
	t1.start()
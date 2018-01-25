import threading, time, csv, sys
import dns.resolver
from datetime import timezone, timedelta, datetime

def getIP(domain,nameserver):
	resolv = dns.resolver.Resolver(configure=False)
	if nameserver:
		resolv.nameservers = nameserver

	try:
		ans = resolv.query(domain, "A")
	except:
		print("[-] dns change -> ",nameserver[1])
		resolv.nameservers[0] = nameserver[1]		
		ans = resolv.query(domain, "A")

	for r in ans:
		ip = str(r)

	return ip, resolv.nameservers[0]

def getTime():
	dt = datetime.now(timezone.utc)
	tz = timezone(timedelta(hours=9))
	now = str(dt.astimezone(tz))
	return now

def record(domain,nameserver):
	idx = 0
	field = ["index","date","domain","IP","DNS"]
	while True:
		f = open('result.csv', 'a')
		with f:
			writer = csv.writer(f)
			if idx == 0:
				writer.writerow(field)
			ip, server = getIP(domain,nameserver)
			date = getTime()

			row = [idx,date,domain,ip,server]
			writer.writerow(row)			

		time.sleep(3600)	
		f.close()
		idx += 1



if __name__ == "__main__":
	domain = "fl0ckfl0ck.info"

	if len(sys.argv) < 2:
		print("[-] Error!\n")
		print("Check your input argument\n")
		sys.exit() 
	else:
		nameserver = []
		nameserver.append(str(sys.argv[1]))
		nameserver.append(str(sys.argv[2]))

	print('''
  ___ ____     ____ _               _                 
 |_ _|  _ \   / ___| |__   ___  ___| | _____ _ __     
  | || |_) | | |   | '_ \ / _ \/ __| |/ / _ \ '__|    
  | ||  __/  | |___| | | |  __/ (__|   <  __/ |     _ 
 |___|_|      \____|_| |_|\___|\___|_|\_\___|_|    (_)
                                                      
''')		

	print("\n[+] DNS List\n")
	for d in nameserver:
		print("[-] ", d)

	print("\n\n[+] Target Domain\n")
	print("[-] ", domain, "\n")
	t1 = threading.Thread(target=record, args=(domain,nameserver))
	t1.start()

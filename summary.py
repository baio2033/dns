import csv

if __name__ == "__main__":
	f = open('result.csv','r')

	domain = "fl0ckfl0ck.info"
	ip = []
	dns = []
	cnt = 0
	while True:
		line = f.readline()	
		if cnt == 0:
			cnt += 1
			continue	
		entry = line.split(",")
		
		if line == "":
			break

		if entry[3] not in ip:
			ip.append(entry[3])
		if entry[4] not in dns:
			dns.append(entry[4])

	f.close()

	summary = open('summary.txt','w')

	print("\nSummary\n")
	summary.write("[+] Domain :"+domain+"\n")
	print("[+] Domain : " , domain)
	print("\n[+] IP List")
	summary.write("\n[+] IP List\n")
	for i in ip:
		print("\t- ",i)
		summary.write("\t- "+i+"\n")

	print("\n[+] DNS List")
	summary.write("\n[+] DNS List\n")
	for i in dns:
		print("\t- ",i)
		summary.write("\t- "+i+"\n")

	summary.close()
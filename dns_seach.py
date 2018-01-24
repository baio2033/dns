import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from time import *
from functools import partial
import dns.resolver
import pygeoip

class MainDialog(QDialog):
	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.setWindowTitle("DNS Search")
		self.createTable()

		self.domain = ""

		self.domainLabel = QLabel("Domain:")
		self.domainValue = QLineEdit(self)
		self.domainBtn = QPushButton("Search")
		self.domainBtn.clicked.connect(self.search)

		topLayout = QGridLayout()
		topLayout.setAlignment(Qt.AlignLeft)
		topLayout.addWidget(self.domainLabel,0,0,Qt.AlignLeft)
		topLayout.addWidget(self.domainValue,0,1,Qt.AlignLeft)
		topLayout.addWidget(self.domainBtn,0,2,Qt.AlignLeft)

		self.web = QWebView()
		self.web.load(QUrl("https://www.google.co.kr/maps/dir/"))

		midLayout = QHBoxLayout()
		midLayout.addWidget(self.dTable)
		midLayout.addWidget(self.web)		

		buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel)
		buttonBox.rejected.connect(self.reject)

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(topLayout)
		mainLayout.addLayout(midLayout)		
		mainLayout.addWidget(buttonBox)

		self.setLayout(mainLayout)
		self.resize(1920,1080)

		self.show()

	def createTable(self):
		"domain, ip, country, city, long, lat"
		self.dTable = QTableWidget()
		self.dTable.setRowCount(6)
		self.dTable.setColumnCount(2)
		self.dTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
		self.dTable.setHorizontalHeaderLabels(["Key","Value"])
		self.dTable.setItem(0,0,QTableWidgetItem("Domain"))
		self.dTable.setItem(1,0,QTableWidgetItem("IP"))
		self.dTable.setItem(2,0,QTableWidgetItem("Country"))
		self.dTable.setItem(3,0,QTableWidgetItem("City"))
		self.dTable.setItem(4,0,QTableWidgetItem("Longitude"))
		self.dTable.setItem(5,0,QTableWidgetItem("Latitude"))

	def search(self):
		self.domain = self.domainValue.text()
		try:
			self.ip = getIP(self.domainValue.text())
			raw = pygeoip.GeoIP('GeoLiteCity.dat')
			data = raw.record_by_name(self.ip)		
			self.country = data['country_name']
			self.city = data['city']
			self.long = data['longitude']
			self.lat = data['latitude']

			tmp_lng = fix(self.long)
			tmp_lat = fix(self.lat)
			
			self.dTable.setItem(0,1,QTableWidgetItem(self.domain))		
			self.dTable.setItem(1,1,QTableWidgetItem(self.ip))		
			self.dTable.setItem(2,1,QTableWidgetItem(self.country))		
			self.dTable.setItem(3,1,QTableWidgetItem(self.city))		
			self.dTable.setItem(4,1,QTableWidgetItem(str(self.long)))
			self.dTable.setItem(5,1,QTableWidgetItem(str(self.lat)))

			self.dTable.resizeColumnsToContents()

			url = "https://www.google.co.kr/maps/dir/" + tmp_lat + "," + tmp_lng					
			self.web.load(QUrl(url))
		except:
			return

def fix(target):
	tmp = str(target)
	tmp = tmp.split(".")
	tmp = tmp[0] + "." + tmp[1][:5]
	return tmp

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


if __name__ == "__main__":
	app = QApplication(sys.argv)
	dialog = MainDialog()
	sys.exit(app.exec_())

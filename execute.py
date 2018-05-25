import urllib2
from bs4 import BeautifulSoup
import csv

csv_file = open("buscojobs.csv","w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow((['Propuesta','Link','Empresa','Fecha']))

#Buscojobs
for i in range(0,20):
	try:
		url = 'https://www.buscojobs.com.uy/ofertas/ts210/trabajo-de-programacion/'+str(i)
		page = urllib2.urlopen(url)

		soup = BeautifulSoup(page , 'html.parser')
		listNames = soup.find_all(class_ ="col-lg-12 col-md-12 link-header")
		listCompanies = soup.find_all(class_ ="col-lg-12 col-md-12 link-footer")

		for (jobs,company) in zip(listNames,listCompanies):
			'''print "\n"
												print jobs.a.text
												print 'https:' + jobs.a.get('href')'''
			if company.a == None:
				csv_writer.writerow([jobs.a.text.encode('utf-8'),'https:' + jobs.a.get('href').encode('utf-8'),"Desconocida",company.find("small",{"class":"pull-right"}).text.encode('utf-8')]) 
			else:
				csv_writer.writerow([jobs.a.text.encode('utf-8'),'https:' + jobs.a.get('href').encode('utf-8'),company.a.text.strip().encode('utf-8'),company.find("small",{"class":"pull-right"}).text.encode('utf-8')])
			#print company.find("small",{"class":"pull-right"}).text
	except urllib2.HTTPError,e:
		break

csv_file.close()
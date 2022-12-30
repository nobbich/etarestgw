import prometheus_client as prom  #import 'prometheus_client', this is important as the python Prometheus library is called that  
import time
import requests
from bs4 import BeautifulSoup

#here we are defining the gauge, it has only one metric, which is, for just to generate a number
GAUGE_VORRAT = prom.Gauge('Pelletvorrat', 'Aktueller Lagerbestand Pellets')

#this is the function reads the pelletvorrat

def vorrat():
    while True:
        response = requests.get('http://192.168.0.50:8080/user/var/40/10201/0/0/12015/')

        soup = BeautifulSoup(response.text, 'xml')
        val=soup.find('value').text
        print(val)
        GAUGE_VORRAT.set(val)
        time.sleep(5) 


if __name__ == '__main__':  #this is the closing function
    prom.start_http_server(8000)  #and here are starting our server with the Prometheus client itself to post our results
    vorrat()
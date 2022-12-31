import prometheus_client as prom  #import 'prometheus_client', this is important as the python Prometheus library is called that  
import time
import requests
import yaml
import sys
from bs4 import BeautifulSoup

def config():
    with open("config.yaml") as fileStream:
        try:
            config = yaml.safe_load(fileStream)
        except yaml.YAMLError as exception:
            print(exception)
            sys.exit(0)
    global url_source
    global port_source
    global prom_port
    
    url_source=config["PU15"]["url"]
    port_source=config["PU15"]["port"]
    prom_port=config["Server"]["port"]

#here we are defining the gauge, it has only one metric, which is, for just to generate a number
GAUGE_VORRAT = prom.Gauge('Pelletvorrat', 'Aktueller Lagerbestand Pellets')

#this is the function reads the pelletvorrat

def vorrat():
    while True:
        response = requests.get(url_source + ":" + port_source + "/user/var/40/10201/0/0/12015/")

        soup = BeautifulSoup(response.text, 'xml')
        val=soup.find('value').text
        print(val)
        GAUGE_VORRAT.set(val)
        time.sleep(5) 


if __name__ == '__main__':  #this is the closing function
    config()
    prom.start_http_server(prom_port)  #and here are starting our server with the Prometheus client itself to post our results
    vorrat()

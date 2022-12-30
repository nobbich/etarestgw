# etarestgw
Gateway between REST-Service ETA PU15 to Prometheus

Das ETAtouch-Gerät bietet einen Webservice an um Zugriff auf das interne CAN-Subsystem zu erhalten. Die Webservices sind als REST-Interfaces implementiert. Du kannst auf die Webdienste des ETAtouch-Geräts zugreifen, indem man Anfragen über das HTTP-Protokoll an Port 8080 sendet. Schema: http://IP_der_ETAtouch:8080/Ressource

Der Webservice muss auf dem Gerät aktiviert sein.

mit http://IP_der_ETAtouch:8080/user/menu/ erhält man eine Auflistung aller Ressourcen.

und mit http://IP_der_ETAtouch:8080/user/var/[object uri] lassen sich die Werte abrufen.

Um mit Prometheus diese Werte abzurufen und zu persistieren benötigt es einen kleinen Service, der hier als Python-Code ausgeführt ist. In diesem Service werden die gewünschten Werte beim Aufruf der metric-Adresse beim ETAtouch über die REST-Schnittstelle abgerufen und für Prometheus im bekannte Format zur Verfügung gestellt.

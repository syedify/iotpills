#include <SPI.h>
#include <WiFi.h>


//char ssid[] = "OpenSkyHotspot";     //  your network SSID (name) 
//char pass[] = "opensky@41";  // your network passwordchar pass[] = "secretPassword";    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

//int status = WL_IDLE_STATUS;
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
//IPAddress server(74,125,232,128);  // numeric IP for Google (no DNS)
char server[] = "gentle-waters-19180.herokuapp.com/";    // name address for Google (using DNS)

// Initialize the Ethernet client library
// with the IP address and port of the server 
// that you want to connect to (port 80 is default for HTTP):
WiFiClient client;

void setup_WiFIWebClient(){
}

bool uploadDataServer(String medicine_info, String manufacturer_info, String patient_info, String phar_doc_info){
  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  if (client.connect(server, 80)) {
    Serial.println("connected to server");
    // Make a HTTP request:
    client.println("POST / HTTP/1.1");
    client.println("Host: gentle-waters-19180.herokuapp.com/");
    client.println(medicine_info);
    client.println(manufacturer_info);
    client.println(patient_info);
    client.println(phar_doc_info);
    client.stop();
    return true;
  }
  else{
    return false;
  }
}


#include <Arduino.h>
#include <ESP8266HTTPClient.h> 
#include <ESP8266WiFi.h>
#include <string>
#include <WiFiClient.h>

// VARIABLES DE ENTORNO
const char* ssid = "Nexxt_751184";
const char* password = "Password28";
const String url = "http://c6a3-181-114-28-135.ngrok.io";
WiFiClient wifiClient;
int ledPin = 16; // GPIO16
int blinkPin = 5; // GPIO5 blink
WiFiServer server(80);

void setup() {
  HTTPClient http;
  Serial.begin(115200);
  delay(10);
 
  pinMode(ledPin, OUTPUT);
  pinMode(blinkPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  digitalWrite(blinkPin, LOW);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    http.begin(wifiClient,(url+"/guardar/"+"TryingToConnectWifi"));
    int httpCode = http.GET();
    http.end();
  }
 
  http.begin(wifiClient,(url+"/guardar/"+"WifiConnected"));
  int httpCode = http.GET();
  http.end();
 
  // Start the server
  server.begin();
}
 
void loop() {
  HTTPClient http;
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
 
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
 
  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
 
  // Match the request
 
  int value = LOW;
  if (request.indexOf("/LED=ON") != -1)  {
        digitalWrite(blinkPin, LOW);

    digitalWrite(ledPin, HIGH);
    value = HIGH;
    http.begin(wifiClient,(url+"/guardar/"+"LedOn"));
    // Obtenemos el status code
    int httpCode = http.GET();
    http.end();
    
  }
  if (request.indexOf("/LED=OFF") != -1)  {
    digitalWrite(blinkPin, LOW);
    digitalWrite(ledPin, LOW);
    value = LOW;
    http.begin(wifiClient,(url+"/guardar/"+"LedOff"));
    // Obtenemos el status code
    int httpCode = http.GET();
    http.end();
  }
  if (request.indexOf("/LED=BLINKON") != -1)  {

    http.begin(wifiClient,(url+"/guardar/"+"Blink"));
    // Obtenemos el status code
    int httpCode = http.GET();
    http.end();
    boolean blink =true;
    int blinked =0;
    while(blink){
      if((request.indexOf("/LED=OFF") != -1) || (request.indexOf("/LED=ON") != -1)){
        blink = false;  
      }
      digitalWrite(blinkPin, HIGH);
      delay(1000);
      digitalWrite(blinkPin, LOW);
      delay(1000);
      blinked++;
    }
    value = LOW;    
  }
 
// Set ledPin according to the request
//digitalWrite(ledPin, value);
 
  // Return the response
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
 
  client.print("Led is: ");
 
  if(value == HIGH) {
    client.print("On");
  } else {
    client.print("Off");
  }
  client.println("<br><br>");
  client.println("<a href=\"/LED=ON\"\"><button>Turn On </button></a>");
  client.println("<a href=\"/LED=OFF\"\"><button>Turn Off </button></a>");
  client.println("<a href=\"/LED=BLINKON\"\"><button>Blink</button></a>");
  client.println("</html>");
 
  delay(1);
  Serial.println("Client disonnected");
  Serial.println("");
 
}
 

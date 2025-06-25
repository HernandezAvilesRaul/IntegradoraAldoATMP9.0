/*
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>


const char* ssid = "Totalplay-E64E";
const char* password = "196AE64E";
const char* serverUrl = "http://192.168.100.41:5000/estado_boton";

const int botonPin = 13;
bool botonPresionado = false;

void setup() {
  pinMode(botonPin, INPUT_PULLUP); 
  Serial.begin(115200);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando al WiFi...");
  }
  Serial.println("Conectado al WiFi.");
}

void enviarCredenciales() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Error: WiFi desconectado");
    return;
  }

  HTTPClient http;
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/json");

 
  JsonDocument doc;
  // Construir el JSON
  doc["credenciales"]["usuario"] = "admin";
  doc["credenciales"]["password"] = "123";
  
  String json;
  serializeJson(doc, json);

  int httpCode = http.POST(json);
  
  if (httpCode == HTTP_CODE_OK) {
    Serial.println("Credenciales enviadas correctamente");
  } else {
    Serial.println("Error al enviar credenciales. Código: " + String(httpCode));
    Serial.println(json);
  }

  http.end();
}

void loop() {
  int botonValue = digitalRead(botonPin);

  if (botonValue == LOW && !botonPresionado) {
    enviarCredenciales();
    botonPresionado = true;
  } else if (botonValue == HIGH) {
    botonPresionado = false; 
  }

  delay(100); // Pequeño delay para evitar rebotes
}
*/
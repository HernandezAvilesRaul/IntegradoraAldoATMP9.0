/*
#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "Totalplay-E64E";
const char *password = "196AE64E";
const char *serverUrl = "http://192.168.100.41:5000/estado_boton";

const int botonPin = 13;
bool estado = false;

void setup()
{
  pinMode(botonPin, INPUT_PULLUP);
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Conectando al WiFi...");
  }
  Serial.println("Conectado al WiFi.");
}

void loop()
{
  estado = !estado;
  String valor = (estado == HIGH) ? "HIGH" : "LOW";

  if (WiFi.status() == WL_CONNECTED)
  {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String json = "{\"estado\":\"" + valor + "\"}";
    int code = http.POST(json);
    Serial.println("Estado del botón enviado: " + valor);
    Serial.println("Código de respuesta: " + String(code));
    Serial.println(json);
    http.end();
  }

  delay(500);
}
*/
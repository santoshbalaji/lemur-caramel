// For WIFI 
#include <ESP8266WiFi.h>

// For OLED
#include <SSD1306Wire.h>

//For MQTT
#include <PubSubClient.h>

//For Json in Arduino
#include <ArduinoJson.h>

const uint8_t WIFI_LOGO_BITS[] PROGMEM = {
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xFF, 0x07, 0x00, 0x00, 0x00,
  0x00, 0x00, 0xE0, 0xFF, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8, 0xFF,
  0x7F, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC, 0xFF, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x00, 0xFE, 0xFF, 0xFF, 0x01, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF,
  0xFF, 0x03, 0x00, 0x00, 0x00, 0xFC, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00,
  0x00, 0xFF, 0xFF, 0xFF, 0x07, 0xC0, 0x83, 0x01, 0x80, 0xFF, 0xFF, 0xFF,
  0x01, 0x00, 0x07, 0x00, 0xC0, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x0C, 0x00,
  0xC0, 0xFF, 0xFF, 0x7C, 0x00, 0x60, 0x0C, 0x00, 0xC0, 0x31, 0x46, 0x7C,
  0xFC, 0x77, 0x08, 0x00, 0xE0, 0x23, 0xC6, 0x3C, 0xFC, 0x67, 0x18, 0x00,
  0xE0, 0x23, 0xE4, 0x3F, 0x1C, 0x00, 0x18, 0x00, 0xE0, 0x23, 0x60, 0x3C,
  0x1C, 0x70, 0x18, 0x00, 0xE0, 0x03, 0x60, 0x3C, 0x1C, 0x70, 0x18, 0x00,
  0xE0, 0x07, 0x60, 0x3C, 0xFC, 0x73, 0x18, 0x00, 0xE0, 0x87, 0x70, 0x3C,
  0xFC, 0x73, 0x18, 0x00, 0xE0, 0x87, 0x70, 0x3C, 0x1C, 0x70, 0x18, 0x00,
  0xE0, 0x87, 0x70, 0x3C, 0x1C, 0x70, 0x18, 0x00, 0xE0, 0x8F, 0x71, 0x3C,
  0x1C, 0x70, 0x18, 0x00, 0xC0, 0xFF, 0xFF, 0x3F, 0x00, 0x00, 0x08, 0x00,
  0xC0, 0xFF, 0xFF, 0x1F, 0x00, 0x00, 0x0C, 0x00, 0x80, 0xFF, 0xFF, 0x1F,
  0x00, 0x00, 0x06, 0x00, 0x80, 0xFF, 0xFF, 0x0F, 0x00, 0x00, 0x07, 0x00,
  0x00, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x01, 0x00, 0x00, 0xF8, 0xFF, 0xFF,
  0xFF, 0x7F, 0x00, 0x00, 0x00, 0x00, 0xFE, 0xFF, 0xFF, 0x01, 0x00, 0x00,
  0x00, 0x00, 0xFC, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8, 0xFF,
  0x7F, 0x00, 0x00, 0x00, 0x00, 0x00, 0xE0, 0xFF, 0x1F, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x80, 0xFF, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  };

//WIFI PROPERTIES & CONNECTIONS
const char* WIFI_SSID = "*********";
const char* WIFI_PASSWORD = "**********";
const int WIFI_LOGO_X = 34;
const int WIFI_LOGO_Y = 15;
const int WIFI_LOGO_WIDTH = 60;
const int WIFI_LOGO_HEIGHT = 36;
WiFiClient esp_client;

//MQTT PROPERTIES & CONNECTIONS
const char* MQTT_SERVER = "192.168.1.222";
const int MQTT_PORT = 1883;
IPAddress server(192, 168, 1, 122);
PubSubClient client(esp_client);
const int MQTT_LOAD_X = 34;
const int MQTT_LOAD_Y = 15;
const char* MQTT_NAME = "MQTT .....";
const char* MQTT_TOPIC_COMMAND = "command";
const char* MQTT_TOPIC_RESULT = "result";

//OLED PROPERTIES
const int OLED_SCL = 5;
const int OLED_SDA = 4;
const int OLED_ADDRESS = 0x3c;
SSD1306Wire display(OLED_ADDRESS, OLED_SDA, OLED_SCL);

//SERIAL
const int SERAIL_BAUD_RATE = 115200;

//INIT MODE
const int INIT_LOAD_X = 25;
const int INIT_LOAD_Y = 20;
const char* INIT_NAME = "WAITING ....";

//OPERATION
const char* KEY_OPERATION_ID = "operation_id";
const char* KEY_USER_ID = "user_id";
const char* KEY_OPERATION = "operation";
const char* KEY_PARAMETERS = "parameters";
const char* KEY_TYPE = "type";
const char* OPERATION_MODE_WASH = "WASH";
const char* OPERATION_MODE_TYPE_QUICK = "QUICK";
const char* OPERATION_MODE_TYPE_NORMAL = "NORMAL";
const char* OPERATION_DESC_MODE = "MODE: ";
const char* OPERATION_DESC_DONE = "COMPLETED";
const int OPERATION_TOP_X = 10;
const int OPERATION_TOP_Y = 2;
const int OPERATION_BOTTOM_X = 34;
const int OPERATION_BOTTOM_Y = 20;
const int OPERATION_QUICK_WASH_TIME = 5000;
const int OPERATION_NORMAL_WASH_TIME = 10000;
const int OPERATION_D3 = 0;
const int OPERATION_D4 = 2;

void setup_serial()
{
  Serial.begin(SERAIL_BAUD_RATE);
}

void setup_display()
{
  display.init();
  display.flipScreenVertically();
}

void setup_wifi()
{
  display.clear();
  display.drawXbm(WIFI_LOGO_X, WIFI_LOGO_Y, WIFI_LOGO_WIDTH, WIFI_LOGO_HEIGHT, WIFI_LOGO_BITS);
  display.display();  
  
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while(WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }
   WiFi.setSleepMode(WIFI_NONE_SLEEP);

  Serial.println("-------- connected to wifi ---------");
}

void setup_mqtt()
{
  display.clear();
  display.setFont(ArialMT_Plain_16);
  display.drawString(MQTT_LOAD_X, MQTT_LOAD_Y, MQTT_NAME);
  display.display();
  
  client.setServer(MQTT_SERVER, 1883);
  client.setCallback(callback);
 
  while (!client.connected()) 
  {
    if (client.connect("esp8266-caramel")) 
    {
      Serial.println("--------- connected to mqtt ----------");  
    } 
    else 
    {
      Serial.print("----------- failed with state --------" + client.state());
      delay(2000);
    }
  }
  client.subscribe(MQTT_TOPIC_COMMAND);
}

void setup_pins()
{
  pinMode(OPERATION_D3, OUTPUT);
  pinMode(OPERATION_D4, OUTPUT);
  Serial.println("------------- setup of pins complete -------------");
}

void init_mode()
{
  display.clear();
  display.setFont(ArialMT_Plain_16);
  display.drawString(INIT_LOAD_X, INIT_LOAD_Y, INIT_NAME);
  display.display();   

  digitalWrite(OPERATION_D4, HIGH);
}

void callback(char* topic, byte* payload, unsigned int length) 
{
  if(strcmp(topic, MQTT_TOPIC_COMMAND) == 0)
  {
    Serial.println("---------- recieved new command ----------");
    char* json_command = (char*) payload;
    DynamicJsonDocument doc(4028);
    deserializeJson(doc, json_command);
    int operation_id = doc[KEY_OPERATION_ID];
    int user_id = doc[KEY_USER_ID];
    String operation = doc[KEY_OPERATION];
    String type = doc[KEY_PARAMETERS][KEY_TYPE];
    char operation_array[operation.length() + 1];
    operation.toCharArray(operation_array, (operation.length() + 1));
    if(strcmp(operation_array, OPERATION_MODE_WASH) == 0)
    {
      Serial.println("-------- starting wash sequence -----------");
      wash(operation_id, user_id, type);
    }
  }
}

void wash(int operation_id, int user_id, String type)
{
  String message = "{\"operation_id\":";
  message.concat(operation_id);
  message.concat(",\"status\":\"executing\"}");
  char message_array[message.length() + 1];
  message.toCharArray(message_array, (message.length() + 1));
  client.publish(MQTT_TOPIC_RESULT, message_array);
  Serial.println("-------- published execution status ----------");

  display.clear();
  display.setFont(ArialMT_Plain_10);
  display.drawString(OPERATION_TOP_X, OPERATION_TOP_Y, OPERATION_DESC_MODE + type);
  display.setFont(ArialMT_Plain_16);
  display.drawString(OPERATION_BOTTOM_X, OPERATION_BOTTOM_Y, String(user_id));
  display.display();

  digitalWrite(OPERATION_D4, LOW);

  char type_array[type.length() + 1];
  type.toCharArray(type_array, (type.length() + 1));

  if(strcmp(type_array, OPERATION_MODE_TYPE_QUICK) == 0)
  {
    digitalWrite(OPERATION_D3, HIGH);
    delay(OPERATION_QUICK_WASH_TIME);    
    digitalWrite(OPERATION_D3, LOW);
  }
  else if(strcmp(type_array, OPERATION_MODE_TYPE_NORMAL) == 0)
  {
    digitalWrite(OPERATION_D3, HIGH);
    delay(OPERATION_NORMAL_WASH_TIME);    
    digitalWrite(OPERATION_D3, LOW);
  }

  display.clear();
  display.setFont(ArialMT_Plain_10);
  display.drawString(OPERATION_TOP_X, OPERATION_TOP_Y, OPERATION_DESC_DONE);
  display.setFont(ArialMT_Plain_16);
  display.drawString(OPERATION_BOTTOM_X, OPERATION_BOTTOM_Y, String(user_id));
  display.display();
  delay(2000);
  
  message = "{\"operation_id\":";
  message.concat(operation_id);
  message.concat(",\"status\":\"completed\"}");
  message_array[message.length() + 1];
  message.toCharArray(message_array, (message.length() + 1));
  client.publish(MQTT_TOPIC_RESULT, message_array);

  Serial.println("-------- published completion status ----------");

  init_mode();
}

void setup() 
{
  setup_serial();
  setup_display();
  setup_wifi();
  setup_mqtt();
  setup_pins();
  init_mode();
}

void loop() 
{
  client.loop();
}

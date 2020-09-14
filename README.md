# caramel - home automation

## Arduino

### Components Required <br>
1) ESP8266 (Any arduino supported microcontroller boards with wifi capabilities) <br>
2) OLED 1306 <br>
3) LED <br>
4) Resistor (< 300 ohms) <br>


### Information:

##### 1) Connection for OLED to ESP8266
<img src="https://github.com/santoshbalaji/lemur-caramel/blob/master/images/oled.png" />

##### 2) Connecting LED to ESP8266 (for the current code connect 2 LED's to pin D3 and D4 respectively)
<img src="https://github.com/santoshbalaji/lemur-caramel/blob/master/images/led.png" />

##### 3) Dependencies for arduino modules <br>
   <a href="https://github.com/knolleary/pubsubclient.git">MQTT Library</a><br>
   <a href="https://github.com/ThingPulse/esp8266-oled-ssd1306.git">SSD1306Wire (For writing to oled display)</a><br>
   <a href="https://arduinojson.org/">ArduinoJSON (For parsing json from API)</a><br>

##### 4) External Dependences
1) MQTT Server


##### 5) Message Format
Command Format 
{
  "operation_id": 123,
  "user_id": 123,
  "operation": "WASH",
  "parameters": {"type": "QUICK"}
}

Result Format
{
  "operation_id": 12,
  "status": "executing"
}


## Flask Rest API (Python based)

### Information:

##### 1) Install dependencies (Use python3)
pip install -r requirements.txt

##### 2) To start server (Use python3)
python main.py 

##### 3) Info on Running server (Multi Thread App Server) 
Host: 127.0.0.1
Port: 3000


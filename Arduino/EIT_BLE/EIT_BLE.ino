#include <ArduinoBLE.h>

BLEService EITService("19b10010-e8f2-537e-4f6c-d104768a1214");
BLEUnsignedCharCharacteristic EITChar1("19b10011-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar2("19b10012-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar3("19b10013-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar4("19b10014-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar5("19b10015-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar6("19b10016-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar7("19b10017-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar8("19b10018-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar9("19b10019-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar10("19b1001a-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar11("19b1001b-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar12("19b1001c-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar13("19b1001d-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar14("19b1001e-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar15("19b1001f-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar16("19b10020-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar17("19b10021-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar18("19b10022-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar19("19b10023-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar20("19b10024-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar21("19b10025-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar22("19b10026-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar23("19b10027-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar24("19b10028-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar25("19b10029-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar26("19b1002a-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar27("19b1002b-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar28("19b1002c-e8f2-537e-4f6c-d104768a1214",BLERead | BLENotify| BLEWrite);
BLEUnsignedCharCharacteristic EITChar[28] = {EITChar1,EITChar2,EITChar3,EITChar4,EITChar5,EITChar6,EITChar7,
                    EITChar8,EITChar9,EITChar10,EITChar11,EITChar12,EITChar13,EITChar14,
                    EITChar15,EITChar16,EITChar17,EITChar18,EITChar19,EITChar20,EITChar21,
                    EITChar22,EITChar23,EITChar24,EITChar25,EITChar26,EITChar27,EITChar28};
int p[28];

void setup() {
  Serial.begin(9600);
  while (!Serial);
  pinMode(LED_BUILTIN, OUTPUT); 
  if (!BLE.begin()) {
    Serial.println("starting BLE failed!");
    while (1);
  }

  BLE.setLocalName("Nano 33 BLE");
  
  BLE.setAdvertisedService(EITService); 
  for (int i=0; i<28; i++)
  {
    EITService.addCharacteristic(EITChar[i]);
  }
  BLE.addService(EITService);
  
  //设置特征的ASCII码初值
  for (int i=0; i<28; i++)
  {
    EITChar[i].writeValue(0);
  }
  
  BLE.setConnectable(true);
  BLE.advertise();
//  Serial.println("Bluetooth device active, waiting for connections...");
}

void loop() {
  delay(100);
  Serial.println("xiao");
  for (int i=0; i<28; i++)//生成28个EIT值
  {
    p[i] = random(255);
  }
  
  //更新特征值
  for (int i=0; i<28; i++)
  {
    EITChar[i].writeValue(p[i]);
  }

  BLEDevice central = BLE.central();

  if (central) {
//    Serial.print("Connected to central: ");
//    Serial.println(central.address());
    digitalWrite(LED_BUILTIN, HIGH);
  
    
//    while (central.connected()) {
//      Serial.println("Connected ");
//      Serial.println(EITChar.value());
//    }
  }
  else{
    digitalWrite(LED_BUILTIN, LOW);
//    Serial.print("Disconnected from central: ");
//    Serial.println(central.address());
  }
}

#include <ArduinoBLE.h>
#include <Wire.h> // IIC control AD5933

//设置UUID
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
int impedence;
char statusnow = 0;
char real =0;
char imag = 0;
char realhigh = 0;
char reallow = 0;
char imaghigh = 0;
char imaglow = 0;

int compute()
{
  int impedence;
//启动频率扫描
  Wire.beginTransmission(13);
  Wire.write(byte(0x80));
  Wire.write(byte(0x20)); 
  Wire.endTransmission();

//检查DFT是否完成
  do
  {
    Wire.beginTransmission(13);//设置状态寄存器地址指针
    Wire.write(byte(0xb0));
    Wire.write(byte(0x8f)); 
    Wire.endTransmission();
    Wire.requestFrom(13, 1, true);
    while(Wire.available())
      statusnow = Wire.read();
  }
  while((statusnow | byte(0xFD)) != byte(0xFF));//检查实值虚值是否有效

//读取实值高字节
  Wire.beginTransmission(13);
  Wire.write(byte(0xb0));
  Wire.write(byte(0x94)); 
  Wire.endTransmission();
  Wire.requestFrom(13, 1, true);
  while(Wire.available())
  {
    realhigh = Wire.read();
  }
//读取实值低字节
  Wire.beginTransmission(13);
  Wire.write(byte(0xb0));
  Wire.write(byte(0x95)); 
  Wire.endTransmission();
  Wire.requestFrom(13, 1, true);
  while(Wire.available())
  {
    reallow = Wire.read();
  }
//读取虚值高字节
  Wire.beginTransmission(13);
  Wire.write(byte(0xb0));
  Wire.write(byte(0x96)); 
  Wire.endTransmission();
  Wire.requestFrom(13, 1, true);
  while(Wire.available())
  {
    imaghigh = Wire.read();
  }
//读取虚值低字节
  Wire.beginTransmission(13);
  Wire.write(byte(0xb0));
  Wire.write(byte(0x97)); 
  Wire.endTransmission();
  Wire.requestFrom(13, 1, true);
  while(Wire.available())
  {
    imaglow = Wire.read();
  }
//获得16位二进制补码的实值虚值
  real = (realhigh << 8) | reallow;
  imag = (imaghigh << 8) | imaglow;
//阻抗计算
//***************************************
//准备发布
  impedence = 1;
//***************************************
  return impedence;
}


void setup() {
//引脚2~7初始化
  pinMode(2, OUTPUT);//emitter的A0
  pinMode(3, OUTPUT);//emitter的A1
  pinMode(4, OUTPUT);//emitter的A2
  pinMode(5, OUTPUT);//receiver的A0
  pinMode(6, OUTPUT);//receiver的A1
  pinMode(7, OUTPUT);//receiver的A2

//串口、I2C、BLE初始化
  pinMode(LED_BUILTIN, OUTPUT); 
  Serial.begin(9600);
  while (!Serial);  
  Wire.begin();
  if (!BLE.begin())
  {
    Serial.println("starting BLE failed!");
    while (1);
  }
  
//BLE设置并发布广告
  BLE.setLocalName("Nano 33 BLE");
  BLE.setAdvertisedService(EITService); 
  EITService.addCharacteristic(EITChar1);
  EITService.addCharacteristic(EITChar2);
  BLE.addService(EITService);
  EITChar1.writeValue(0);//设置阻抗初值的ASCII码
  EITChar2.writeValue(0);
  BLE.setConnectable(true);
  BLE.advertise();
//  Serial.println("Bluetooth device active, waiting for connections...");

//频率扫描初始设置
  Wire.beginTransmission(13);//写入初始频率40kHZ
  Wire.write(byte(0x82));
  Wire.write(byte(0x13));
  Wire.write(byte(0x83));
  Wire.write(byte(0x88));
  Wire.write(byte(0x84));
  Wire.write(byte(0x5c));
  Wire.endTransmission();
  Wire.beginTransmission(13);//进入待机模式
  Wire.write(byte(0x80));
  Wire.write(byte(0xb0)); 
  Wire.endTransmission();
  Wire.beginTransmission(13);//写入建立时间周期数*80
  Wire.write(byte(0x8a));
  Wire.write(byte(0x00)); 
  Wire.write(byte(0x8b));
  Wire.write(byte(0x50)); 
  Wire.endTransmission();
  Wire.beginTransmission(13);//起始频率初始化
  Wire.write(byte(0x80));
  Wire.write(byte(0x10)); 
  Wire.endTransmission();
  delay(500);
}

void loop() 
{
//指示灯以指示中央设备是否连接
  BLEDevice central = BLE.central();
  if (central) 
  {    
    digitalWrite(LED_BUILTIN, HIGH);
//    Serial.print("Connected to central: ");
//    Serial.println(central.address());
  }
  else
  {
    digitalWrite(LED_BUILTIN, LOW);
//    Serial.print("Disconnected from central: ");
//    Serial.println(central.address());
  }

//ADG1608数据选择(考虑switch-case语句)
  for (int n=0;n<28;n++){
  switch(n){
      case 0: EA2=0;EA1=0;EA0=0;RA2=0;RA1=0;RA0=1; break;
      case 1: EA2=0;EA1=0;EA0=0;RA2=0;RA1=1;RA0=0; break;
      case 2: EA2=0;EA1=0;EA0=0;RA2=0;RA1=1;RA0=1; break;
      case 3: EA2=0;EA1=0;EA0=0;RA2=1;RA1=0;RA0=0; break;
      case 4: EA2=0;EA1=0;EA0=0;RA2=1;RA1=0;RA0=1; break;
      case 5: EA2=0;EA1=0;EA0=0;RA2=1;RA1=1;RA0=0; break;
      case 6: EA2=0;EA1=0;EA0=0;RA2=1;RA1=1;RA0=1; break;
      case 7: EA2=0;EA1=0;EA0=1;RA2=0;RA1=1;RA0=0; break;
      case 8: EA2=0;EA1=0;EA0=1;RA2=0;RA1=1;RA0=1; break;
      case 9: EA2=0;EA1=0;EA0=1;RA2=1;RA1=0;RA0=0; break;
      case 10: EA2=0;EA1=0;EA0=1;RA2=1;RA1=0;RA0=1; break;
      case 11: EA2=0;EA1=0;EA0=1;RA2=1;RA1=1;RA0=0; break;
      case 12: EA2=0;EA1=0;EA0=1;RA2=1;RA1=1;RA0=1; break;
      case 13: EA2=0;EA1=1;EA0=0;RA2=0;RA1=1;RA0=1; break;
      case 14: EA2=0;EA1=1;EA0=0;RA2=1;RA1=0;RA0=0; break;
      case 15: EA2=0;EA1=1;EA0=0;RA2=1;RA1=0;RA0=1; break;
      case 16: EA2=0;EA1=1;EA0=0;RA2=1;RA1=1;RA0=0; break;
      case 17: EA2=0;EA1=1;EA0=0;RA2=1;RA1=1;RA0=1; break;
      case 18: EA2=0;EA1=1;EA0=1;RA2=1;RA1=0;RA0=0; break;
      case 19: EA2=0;EA1=1;EA0=1;RA2=1;RA1=0;RA0=1; break;
      case 20: EA2=0;EA1=1;EA0=1;RA2=1;RA1=1;RA0=0; break;
      case 21: EA2=0;EA1=1;EA0=1;RA2=1;RA1=1;RA0=1; break;
      case 22: EA2=1;EA1=0;EA0=0;RA2=1;RA1=0;RA0=1; break;
      case 23: EA2=1;EA1=0;EA0=0;RA2=1;RA1=1;RA0=0; break;
      case 24: EA2=1;EA1=0;EA0=0;RA2=1;RA1=1;RA0=1; break;
      case 25: EA2=1;EA1=0;EA0=1;RA2=1;RA1=1;RA0=0; break;
      case 26: EA2=1;EA1=0;EA0=1;RA2=1;RA1=1;RA0=1; break;
      case 27: EA2=1;EA1=1;EA0=0;RA2=1;RA1=1;RA0=1; break;
    }
    digitalWrite(2, EA0);
    digitalWrite(3, EA1);
    digitalWrite(4, EA2);
    digitalWrite(5, RA0);
    digitalWrite(6, RA1);
    digitalWrite(7, RA2); 
    impedence = compute();
    //更新阻抗值以发布到对应的第n个char特征里
    EITChar[n].writeValue(impedence);
  }
}

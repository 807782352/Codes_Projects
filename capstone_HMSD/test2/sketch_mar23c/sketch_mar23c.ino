//加载SPI库和SD库
#include <SPI.h>
#include <SD.h>
 
//声明文件对象
File myFile;
 
void setup() 
{
    Serial.begin(9600); //设置波特率
    while (!Serial) 
    {
    ; // wait for serial port to connect. Needed for native USB port only
      //等待串行端口连接。 仅适用于本机USB端口
    }
    
    Serial.print("Initializing SD card...");//正在初始化
 
    //如果返回4则初始化失败
    if (!SD.begin(4)) {
      Serial.println("initialization failed!");
      return;
    }
    Serial.println("initialization done.");//初始化结束
 
    myFile = SD.open("LINGSH~1.TXT");//打开指定文件
    if (myFile) {
      Serial.println("LingShunLAB.txt:");//串口输出test。txt
      Serial.println("↓↓↓↓");//串口输出↓↓↓↓
      // read from the file until there's nothing else in it:
      //从文件中读取，直到没有其他内容
      while (myFile.available()) {
        Serial.write(myFile.read());//不断循环读取直到没有其他内容
      }
      // close the file:
      //关闭文件
      myFile.close();
  } else {
    // if the file didn't open, print an error:
    //如果文件没有打开，打印错误：
    Serial.println("error opening test.txt");
  }
}
 
void loop() {
  
 
}

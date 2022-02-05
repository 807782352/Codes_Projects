
#define SIZE 20
int list[SIZE];  // the array
int datafromUser1=0;
//int datafromUser2=0;
byte list_end = 0 ; // the end pointer

void setup() {
  // put your setup code here, to run once;
  pinMode( LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly;
  if(Serial.available() > 0) {
    datafromUser1=int(Serial.read());
  }
  list.append_list(datafromUser1)

  if (list[0] == 3 && list[1] == 2){
    digitalWrite(LED_BUILTIN,HIGH);
  }
  else {
    digitalWrite(LED_BUILTIN,LOW);
  }
}


// A function to append - it may fail if the array is full, but returns a boolean to indicate if it worked.
bool append_list (int element)
{
  if (list_end < SIZE)
  {
    list[list_end++] = element ;
    return true;
  }
  return false;
}

void setup(){
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  setup_WiFi();
  setup_WiFIWebClient();
  setup_NFC_HUB_edison();
}

void loop(){
  static int counter = 0;

  String data = Serial.readString();
  
  String medicine_info = data.substring(0,data.indexOf("|"));
  data = data.substring(data.indexOf("|")+1);
  String manufacturer_info = data.substring(0,data.indexOf("|"));
  data = data.substring(data.indexOf("|")+1);
  String patient_info = data.substring(0, data.indexOf("|"));
  data = data.substring(data.indexOf("|")+1);
  String phar_doc_info = data;
  
  if(medicine_info.equals("")){
    medicine_info = "Hello";
  }
  if(manufacturer_info.equals("")){
    manufacturer_info = "FYDP Solutions";
  }
  if(patient_info.equals("")){
    patient_info = "Sridhar";
  }
  if(phar_doc_info.equals("")){
    phar_doc_info = "Syed, Syed and Udit";
  }

  delay(5000);
  
  NFC_write(medicine_info, manufacturer_info, patient_info, phar_doc_info);
  if(counter > 1){
    counter = 0;
    printCurrentNet();
  }
  counter++;
}


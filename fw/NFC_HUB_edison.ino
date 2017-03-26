// Formats a Mifare Classic tags as an NDEF tag
// This will fail if the tag is already formatted NDEF
// nfc.clean will turn a NDEF formatted Mifare Classic tag back to the Mifare Classic format

#if 0
#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);
#else

#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
#endif

void setup_NFC_HUB_edison(void) {
    Serial.println("NDEF Formatter");
    nfc.begin();
}

void NFC_write(String medicine_info,String manufacture_info, String patient_info, String phar_doc_info){
  Serial.println("\nAttempting write data on the NFC\n");
  
  if(nfc.tagPresent()){
    NdefMessage message = NdefMessage();
    message.addTextRecord(medicine_info);
    message.addTextRecord(manufacture_info);
    message.addTextRecord(patient_info);
    message.addTextRecord(phar_doc_info);
    bool success = nfc.write(message);
    if(success){
      while(!uploadDataServer(medicine_info, manufacture_info, patient_info, phar_doc_info)){
        ;
      }
      Serial.println("Success");
    }
    else{
      Serial.println("Fail");
    }
  }
}

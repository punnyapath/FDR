char floorData;

void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0) {
    floorData = Serial.read();
    Serial.print (floorData);

    if(floorData == '1'){
      Serial.println("Ground Floor");
      digitalWrite(8, 1);
      digitalWrite(7, 0);
      digitalWrite(6, 0);
      digitalWrite(5, 0);
      digitalWrite(4, 0);
      digitalWrite(3, 0);
      digitalWrite(2, 0); 
    }
    else if (floorData == '2'){
      Serial.println(" First Floor");
      digitalWrite(8, 0);
      digitalWrite(7, 1);
      digitalWrite(6, 0);
      digitalWrite(5, 0);
      digitalWrite(4, 0);
      digitalWrite(3, 0);
      digitalWrite(2, 0);
    }
    else if (floorData == '3'){
      Serial.println("Seccond Floor");
      digitalWrite(8, 0);
      digitalWrite(7, 0);
      digitalWrite(6, 1);
      digitalWrite(5, 0);
      digitalWrite(4, 0);
      digitalWrite(3, 0);
      digitalWrite(2, 0); 
    }
    else if (floorData == '4'){
      Serial.println("Third Floor");
      digitalWrite(8, 0);
      digitalWrite(7, 0);
      digitalWrite(6, 0);
      digitalWrite(5, 1);
      digitalWrite(4, 0);
      digitalWrite(3, 0);
      digitalWrite(2, 0);
    }
    else if (floorData == '5'){
     Serial.println("Fourth Floor");
      digitalWrite(8, 0);
      digitalWrite(7, 0);
      digitalWrite(6, 0);
      digitalWrite(5, 0);
      digitalWrite(4, 1);
      digitalWrite(3, 0);
      digitalWrite(2, 0); 
    }
    else if (floorData == '6'){
      Serial.println("Fifth Floor");
      digitalWrite(8, 0);
      digitalWrite(7, 0);
      digitalWrite(6, 0);
      digitalWrite(5, 0);
      digitalWrite(4, 0);
      digitalWrite(3, 1);
      digitalWrite(2, 0);
    }
    else if (floorData == '7'){
      Serial.println("Sixth Floor");
      digitalWrite(8, 0);
      digitalWrite(7, 0);
      digitalWrite(6, 0);
      digitalWrite(5, 0);
      digitalWrite(4, 0);
      digitalWrite(3, 0);
      digitalWrite(2, 1);
    }
  }

}

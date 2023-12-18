void setup() {
  // Set all digital pins 2-53 and analog pins 0-14 to INPUT_PULLUP
  for (int i = 2; i <= 53; i++) {
    pinMode(i, INPUT_PULLUP);
  }
  for (int i = 0; i <= 14; i++) {
    pinMode(A0 + i, INPUT_PULLUP);
  }

  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Check all digital pins 2-53
  for (int i = 2; i <= 53; i++) {
    if (digitalRead(i) == LOW) {
      Serial.print("Digital Pin ");
      Serial.print(i);
      Serial.println(" pressed");
      delay(100); // debounce delay
    }
  }

  // Check all analog pins 0-14
  for (int i = 0; i <= 14; i++) {
    if (digitalRead(A0 + i) == LOW) {
      Serial.print("Analog Pin ");
      Serial.print(i);
      Serial.println(" pressed");
      delay(100); // debounce delay
    }
  }
}

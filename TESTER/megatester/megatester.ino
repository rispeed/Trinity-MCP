const int ledPin = 46;
const int excludedPins[] = {0, 1, 13, 46, 47};
const int totalDigitalPins = 54; // Total number of digital pins on Arduino Mega 2560
const int totalAnalogPins = 16;  // Total number of analog pins on Arduino Mega 2560

bool isExcluded(int pin) {
  for (int i = 0; i < sizeof(excludedPins)/sizeof(excludedPins[0]); i++) {
    if (pin == excludedPins[i]) {
      return true;
    }
  }
  return false;
}

void printPinState(int pin, int state) {
  if (pin < totalDigitalPins) {
    Serial.print("D");
    Serial.print(pin);
  } else {
    Serial.print("A");
    Serial.print(pin - totalDigitalPins);
  }
  Serial.print(": ");
  Serial.println(state == HIGH ? "HIGH" : "LOW");
}

void setup() {
  Serial.begin(9600);

  // Initialize LED pin as output
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  // Initialize digital pins as INPUT_PULLUP
  for (int pin = 2; pin < totalDigitalPins; pin++) {
    if (!isExcluded(pin)) {
      pinMode(pin, INPUT_PULLUP);
    }
  }

  // Initialize analog pins as INPUT_PULLUP
  for (int pin = totalDigitalPins; pin < totalDigitalPins + totalAnalogPins; pin++) {
    pinMode(pin, INPUT_PULLUP);
  }

  // Print initial state of all pins
  Serial.println("Initial pin states:");
  for (int pin = 2; pin < totalDigitalPins + totalAnalogPins; pin++) {
    if (!isExcluded(pin)) {
      printPinState(pin, digitalRead(pin));
    }
  }
}

void loop() {
  static int previousPinState[totalDigitalPins + totalAnalogPins] = {HIGH};

  // Check the state of all pins
  for (int pin = 2; pin < totalDigitalPins + totalAnalogPins; pin++) {
    if (!isExcluded(pin)) {
      int currentState = digitalRead(pin);
      if (currentState != previousPinState[pin]) {
        if (currentState == LOW) {
          analogWrite(ledPin, 255); // Turn LED full blast
          Serial.print("Pin ");
          if (pin < totalDigitalPins) {
            Serial.print("D");
            Serial.print(pin);
          } else {
            Serial.print("A");
            Serial.print(pin - totalDigitalPins);
          }
          Serial.println(" pressed.");
        } else {
          analogWrite(ledPin, 0); // Turn LED off
          Serial.print("Pin ");
          if (pin < totalDigitalPins) {
            Serial.print("D");
            Serial.print(pin);
          } else {
            Serial.print("A");
            Serial.print(pin - totalDigitalPins);
          }
          Serial.println(" released.");
        }
        previousPinState[pin] = currentState;
      }
    }
  }
}


#define top_right 3
#define bottom_right 4
#define bottom_left 5
#define top_left 6
#define mid_right 7
#define mid_left 8
#define mid 9

#define LED 10

void setup() {
  Serial.begin(9600);

  pinMode(top_right, INPUT);
  pinMode(bottom_right, INPUT);
  pinMode(bottom_left, INPUT);
  pinMode(top_left, INPUT);
  pinMode(mid_right, INPUT);
  pinMode(mid_left, INPUT);
  pinMode(mid, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  int signal2 = digitalRead(top_right);
  int signal3 = digitalRead(bottom_right);
  int signal4 = digitalRead(bottom_left);
  int signal5 = digitalRead(top_left);
  int signal6 = digitalRead(mid_right);
  int signal7 = digitalRead(mid_left);
  int signal8 = digitalRead(mid);

  bool pressed = false;

  if (signal2 == LOW) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
    Serial.print("2");
    pressed = true;
  }

  if (signal3 == LOW) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
    Serial.print("3");
    pressed = true;
  }

  if (signal4 == LOW) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
    Serial.print("4");
    pressed = true;
  }

  if (signal5 == LOW) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
    Serial.print("5");
    pressed = true;
  }

  if (signal6 == LOW) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
    Serial.print("6");
    pressed = true;
  }

  if (signal7 == LOW) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
    Serial.print("7");
    pressed = true;
  }

  if (signal8 == LOW) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
    Serial.print("8");
    pressed = true;
  }
  

  if (pressed == true) {
    Serial.println("");
  }

  delay(10);  // avoid spamming
}

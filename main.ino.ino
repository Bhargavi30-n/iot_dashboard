#define TRIG D1
#define ECHO D2
#define WATER_SENSOR A0

long duration;
float distance;
int waterLevel;

float previousWater;
unsigned long previousTime;
float riseRate;

const int totalReadings = 20;
int readingsSent = 0;

float getDistance()
{
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn(ECHO, HIGH);

  if(duration == 0)
  {
    return -1;
  }

  float dist = duration * 0.034 / 2;
  return dist;
}

void setup()
{
  Serial.begin(9600);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  previousWater = analogRead(WATER_SENSOR);
  previousTime = millis();
}

void loop()
{
  if(readingsSent < totalReadings)
  {
    distance = getDistance();

    if(distance == -1)
    {
      return;
    }

    waterLevel = analogRead(WATER_SENSOR);

    unsigned long currentTime = millis();
    float timeDiff = (currentTime - previousTime) / 1000.0;

    if(timeDiff > 0)
    {
      riseRate = (waterLevel - previousWater) / timeDiff;
    }

    previousWater = waterLevel;
    previousTime = currentTime;

    Serial.print(waterLevel);
    Serial.print(",");
    Serial.print(distance);
    Serial.print(",");
    Serial.println(riseRate);

    readingsSent++;
  }
  else
  {
    Serial.println("Completed readings.");
    while(true);
  }

  delay(2000);
}
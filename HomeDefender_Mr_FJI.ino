#include "DHT.h"
#include <Wire.h>
#include "rgb_lcd.h"
#include "Ultrasonic.h"

#define DHTTYPE DHT22
#define DHTPIN 2
DHT dht(DHTPIN, DHTTYPE);

#if defined(ARDUINO_ARCH_AVR)
#define debug Serial
#elif defined(ARDUINO_ARCH_SAMD) || defined(ARDUINO_ARCH_SAM)
#define debug SerialUSB
#else
#define debug Serial
#endif

Ultrasonic ultrasonic(7);

void setup()
{
    Wire.begin();
    Serial.begin(9600);
    dht.begin();
}

void loop()
{
    long RangeInCentimeters;
    RangeInCentimeters = ultrasonic.MeasureInCentimeters();
    Serial.println(RangeInCentimeters);
    delay(1500);
}
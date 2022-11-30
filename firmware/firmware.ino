
#include <Servo.h>

#include "artl/encoder.h"
#include "artl/digital_in.h"
#include "artl/pin_change_int.h"
#include "artl/yield.h"

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

using enc_a_in = artl::digital_in< artl::port::B, 4 >;
using enc_b_in = artl::digital_in< artl::port::B, 5 >;

using enc_a_int = artl::pin::change_int< artl::port::B, 4 >;
using enc_b_int = artl::pin::change_int< artl::port::B, 5 >;

struct encoder_handler : public artl::default_encoder_handler {
    void on_rotate(short, unsigned long);
};

using encoder_type = artl::encoder<encoder_handler, artl::default_encoder_time_traits, 1>;
encoder_type encoder_;

int pos = 90;    // variable to store the servo position

void setup() {
    myservo.attach(6);  // attaches the servo on pin 6 to the servo object

    enc_a_in::setup();
    enc_b_in::setup();

    enc_a_int::enable();
    enc_b_int::enable();
}

inline void
encoder_handler::on_rotate(short dir, unsigned long)
{
    pos += dir;

    if (pos < 0) pos = 0;
    if (pos > 180) pos = 180;

    myservo.write(pos);              // tell servo to go to position in variable 'pos'
}

void loop() {
  encoder_.update(!enc_a_in::read(), !enc_b_in::read(), millis());
/*
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
*/
  artl::yield();
}

#if defined(ISR) && defined(PCINT0_vect)
ISR(PCINT0_vect) {
}
#endif

"""
Copyright (c) 2020, Heung Kit Leslie Chung
All rights reserved.
Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
"""

# Import GPIO and other packages needed for pin control
import RPi.GPIO as GPIO
import time

# We will use pin 12 (GPIO18) to power the LED
pwm_pin = 12

# Set pin reading mode to BOARD
GPIO.setmode(GPIO.BOARD)

# Make pin 12 the output pin (power)
GPIO.setup(pwm_pin, GPIO.OUT)

# Instantiate pulse width modulation on pin 12 and set frequency at 50Hz
pwm = GPIO.PWM(pwm_pin, 50)
pwm.start(100)

# This loop will keep runing indefinitely until keyboard interruption
try:
    while True:
        # Increase duty cycle from 0 to 100 at increments of 20
        for i in range(0, 100, 20):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.2)
        # Decrease duty cycle from 100 to 0 at increments of 20
        for i in range(100, 0, -20):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting program")
    GPIO.cleanup()

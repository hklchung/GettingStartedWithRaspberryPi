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

# We will use pin 8 for power and 10 for button signal
lightpin = 8
buttonpin = 10

# Set pin reading mode to BOARD
GPIO.setmode(GPIO.BOARD)

# Make lighpin the output pin (power) and pull up
GPIO.setup(lightpin, GPIO.OUT)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# This loop will keep runing indefinitely until keyboard interruption
try:
    while True:
        # We have a manual input from the button pin
        input = GPIO.input(buttonpin)
        # If button is not pressed, give power to LED
        if (input==False):
            GPIO.output(lightpin, True)
        # If button is pressed, blink the LED by alternating power output
        else:
            GPIO.output(lightpin, True)
            time.sleep(1)
            GPIO.output(lightpin, False)
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

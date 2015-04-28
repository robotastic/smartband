Smartband Magic!
================

This code combines together the example programs for LibNFC and the Pimoroni Unicorn Hat. When you touch a band to the RFID reader, it will dispaly an animation on the LED Matrix. There is some information on it here: http://lukeberndt.com/2015/magicbands-rpi-leds-fun/ ‎

When you tap an RFID/NFC band or card it will print out the ID number. You will have to update the ID numbers that are hard coded in the program. This happens around line 457 in smartband.c. The array of tokens (~line 78) also has to be set to number of RFID card and magic bands you want train.

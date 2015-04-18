all: lib
	gcc -Wall unicorn.c -o unicorn -Irpi-ws281x/lib -Lrpi-ws281x/lib -lm -lws2811 -lpng -lnfc 

lib:
	make -C rpi-ws281x/lib/ lib

clean:
	-rm unicorn

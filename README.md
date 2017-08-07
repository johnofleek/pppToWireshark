# pppToWireshark
A python script  to convert raw ppp serial port captures into a file to import into wireshark via import hex 

# NOTE # 
use python3

when importing into wireshark and wanting time select timestamp and use format %H:%M:%S.

Uses HDLC decoder yahdlc

I have called the example source file "PPPrawexample.txt" in this git but the code expects "PPP_decode.txt"

The output is currently just pumped to stdout - sorry I was in a hurry

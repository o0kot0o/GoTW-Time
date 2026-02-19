import binascii
import re

with open("WorldData.sav", 'rb') as f:
    hex_data = bytearray(f.read())

pattern = re.compile(b'TotalPlaytime\x00\x0e\x00\x00\x00FloatProperty')
for match in pattern.finditer(hex_data):
    offset = match.end() + 11
    print(f"Offset found at: {offset} (0x{offset:X})")
    print(binascii.hexlify(hex_data[offset:offset+16]).decode('utf-8'))
    hex_data[offset:offset+2] = b'\xFA\xFA'

with open("WorldData_modified.sav", 'wb') as f_out:
    f_out.write(hex_data)



        #print(binascii.hexlify(hex_data[match.end()+11:]).decode('utf-8'))
#print(hex_data)


# to Find b'\x54\x6F\x74\x61\x6C\x65\x00\x0E\x00\x00\x00\x46\x6C\x6F\x72\x74\x79'
import binascii
import re

#TEST

with open("WorldData.sav", 'r+b') as f:
    hex_data = f.read()
    pattern = re.compile(b'TotalPlaytime\x00\x0e\x00\x00\x00FloatProperty')
    for match in pattern.finditer(hex_data):
        print(f"Match: {match.end()+11} (0x{match.end()+11:X})")
        print(binascii.hexlify(hex_data[match.end()+11:]).decode('utf-8'))
        #f.seek(match.end()+11)
        #f.write(b'\x00\x00')

        #print(binascii.hexlify(hex_data[match.end()+11:]).decode('utf-8'))
#print(hex_data)


# to Find b'\x54\x6F\x74\x61\x6C\x65\x00\x0E\x00\x00\x00\x46\x6C\x6F\x72\x74\x79'
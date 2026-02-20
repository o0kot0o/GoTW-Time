import binascii
import re

save_file = "WorldData.sav"
new_save_file = "WorldData_modified.sav"
find_bytes = b'TotalPlaytime\x00\x0e\x00\x00\x00FloatProperty'
replace_bytes = b'\x00\x00\x00\x00'

print(f"Opening file {save_file}.")
with open(save_file, 'rb') as f:
    print(f"Reading from file {save_file}.")
    hex_data = bytearray(f.read())

pattern = re.compile(find_bytes)

print(f"Looking at {len(hex_data)} bytes for the offset.")
for match in pattern.finditer(hex_data):
    offset = match.end() + 11
    print(f"Found {offset}:{offset+4}.")
    print(f" ---> {binascii.hexlify(hex_data[offset:offset+4]).decode('utf-8').upper()}")
    print(f"Replacing bytes {offset}:{offset+4} with {replace_bytes}")
    hex_data[offset:offset+4] = replace_bytes

print(f"Saving file to {new_save_file}")
with open(new_save_file, 'wb') as f_out:
    f_out.write(hex_data)
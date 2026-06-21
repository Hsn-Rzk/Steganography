from PIL import Image

def Text_To_Binary(text):
    listb = []
    for char in text:
        char_num = ord(char)
        char_bin = format(char_num, '08b')
        listb.append(char_bin)
    binary_stream = ''.join(listb)
    return binary_stream

def Binary_To_Text(binary):
    text = ''
    i = 0

    while i < len(binary):
        byte = binary[i:i+8]
        if len(byte) == 8:
            char_num = int(byte, 2)
            char = chr(char_num)
            i += 8
            text += char
    return text


def encode(cover_image_path, secret_text, output_image_path):
    secret_text += "###"
    binary_data = Text_To_Binary(secret_text)
    data_index = 0
    
    img = Image.open(cover_image_path)
    img = img.convert('RGB')
    width, height = img.size
    
    if len(binary_data) > (width * height * 3):
        raise ValueError("Error: The image is too small to hold this message!")

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            if data_index < len(binary_data):
                r = (r & ~1) | int(binary_data[data_index])
                data_index += 1

            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index])
                data_index += 1
                
            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index])
                data_index += 1
                
            img.putpixel((x, y), (r, g, b))
            
            if data_index >= len(binary_data):
                break
        if data_index >= len(binary_data):
            break

    img.save(output_image_path, "PNG")
    print(f"Success! Message hidden in {output_image_path}")

    
def decode(stego_image_path):
    img = Image.open(stego_image_path)
    img = img.convert('RGB')
    width, height = img.size
    binary_data = ""
    
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
            
    decoded_text = Binary_To_Text(binary_data)
    
    if "###" in decoded_text:
        end_index = decoded_text.find("###")
        return decoded_text[:end_index]
    else:
        return "Error: No hidden message found, or the delimiter is missing."

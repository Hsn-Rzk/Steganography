# Steganography Basic Tool!!

A Python-based command-line tool that hides secret messages inside PNG images using LSB (Least Significant Bit) steganography. Perfect for learning about data hiding techniques and image manipulation.

   Features

   Encode Mode: Hide secret text messages inside PNG images

   Decode Mode: Extract hidden messages from steganographic images

   Interactive CLI: User-friendly command-line interface with guided prompts

   Error Handling: Robust validation with clear, user-friendly error messages

   Transparency Support: Automatically handles RGBA images with alpha channels

   Capacity Checking: Validates if the image is large enough before encoding

   Fast Processing: Optimized bitwise operations for quick encoding/decoding



   How It Works

This tool uses LSB (Least Significant Bit) Steganography, a technique that exploits how digital images store color information.

The Science Behind It

Digital images are made up of pixels, and each pixel has three color channels: Red, Green, and Blue (RGB). Each channel is represented by a number from 0 to 255.

In binary, these numbers look like: 10011010


The Least Significant Bit is the very last bit (the rightmost one). Changing it has a minimal effect on the actual color:

10011010 (154) → 10011011 (155)


The color changes by just 1 unit out of 256 — invisible to the human eye!


The Encoding Process

Text → Binary: Your secret message is converted to binary (e.g., "Hi" → 01001000 01101001)

Pixel Scanning: The tool reads each pixel's RGB values one by one

Bit Replacement: Each bit of your message replaces the LSB of a color channel

Save: The modified image is saved as a PNG (lossless format)


Visual Example:

Original Pixel:  (154, 200, 100)

Secret Bit:      1

Modified Pixel:  (155, 200, 100)  ← Only Red changed by 1!


The Decoding Process

Read Pixels: Extract the LSB from each RGB channel

Binary → Text: Reconstruct the binary string and convert back to text

Find Delimiter: Stop when the ### marker is found


   Installation Prerequisites

Python 3.7 or higher

pip (Python package manager)

Git (for cloning the repository)


Step-by-Step Installation

1.Clone the repository:

                                           git clone https://github.com/Hsn-Rzk/steganography-tool.git
                                           
                                           cd steganography-tool



2.Install dependencies:

                                           pip install -r requirements.txt
                                           



3. ENJOY!!





   Usage

Running the tool: 

                                            python main.py

                                      
Encode Mode:

Run the program and select (e) for encode

Provide the path to your cover image (must be PNG format)

Type the secret message you want to hide

Specify the output filename for the steganographic image



Decode Mode:

Run the program and select (d) for decode

Provide the path to the image containing the hidden message

The tool will display the extracted secret message




####################################################################################################





Example 1: 


Encoding a Message: 



-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!- Welcome to Steganography Tool -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-



This Tool Supports only png images...

Do you want to (e)ncode or (d)ecode data? : e

-!-!- ENCODE MODE -!-!-

Enter the path to the cover image (e.g. Desktop/Pictures/cover.png): test.png
Enter the secret message you want to hide: test message
Enter the name for the output image (e.g. hidden.png): output.png
Success! Message hidden in output.png


Your message is now successfully hidden...




####################################################################################################




Example 2:


Decoding a Message:



-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!- Welcome to Steganography Tool -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-



This Tool Supports only png images...

Do you want to (e)ncode or (d)ecode data? : d

--- DECODE MODE ---

Enter the path to the image you want to decode (e.g. Desktop/Pictures/hidden.png): output.png

  
  Message Is Successfully Extracted    

  
  EXTRACTED MESSAGE


========================================

test message

========================================




####################################################################################################




Example 3: 


Error Handling:



-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!- Welcome to Steganography Tool -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-



This Tool Supports only png images...

Do you want to (e)ncode or (d)ecode data? : d

--- DECODE MODE ---
Enter the path to the image you want to decode (e.g. Desktop/Pictures/hidden.png): ppppppp.png

Error: Could not find the file 'ppppppp.png'. Please check the spelling and path.

                                                                                      

####################################################################################################



Key Functions:


Text_To_Binary(text)


Converts a string into a binary representation. Each character is converted to its ASCII value, then to an 8-bit binary string.



Binary_To_Text(binary_string)



Reverses the process: takes a binary string and converts it back to readable text by splitting into 8-bit chunks.



encode(cover_image_path, secret_text, output_image_path)



The main encoding function that:

Validates image capacity

Converts text to binary

Modifies pixel LSBs using bitwise operations

Saves the result as PNG



decode(stego_image_path)



The main decoding function that:

Reads LSBs from all pixels

Reconstructs the binary message

Extracts text until the delimiter is found





   Limitations


Image Format

PNG Only: The tool requires PNG images because JPEG uses lossy compression that destroys hidden data

No JPEG Support: JPEG compression alters pixel values, corrupting the hidden message

Capacity Constraints

Each pixel stores 3 bits (one in R, one in G, one in B)

Formula: Max characters = (width × height × 3) / 8

Example: A 1000×1000 image can hold ~375,000 characters

Security Considerations

No Encryption: Messages are hidden but not encrypted. Anyone who knows the technique can extract them

Statistical Detection: LSB steganography can be detected using statistical analysis tools

Not for High-Security: Suitable for learning and casual use, not for protecting sensitive data

Image Quality

Works best with images that have natural noise and variation

Solid color images may show visible artifacts after encoding




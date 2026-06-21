import Steganography_Methods

def main():
    print("\n\n-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!- Welcome to Steganography Tool -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-\n\n")
    print("\nThis Tool Supports only png images...\n")

    choice = input('Do you want to (e)ncode or (d)ecode data? : ')

    choice = choice.strip().lower()

    if choice == 'e':
        print("\n-!-!- ENCODE MODE -!-!-\n")
        
        cover_img = input("Enter the path to the cover image (e.g. Desktop/Pictures/cover.png): ")
        
        secret_msg = input("Enter the secret message you want to hide: ")
        
        output_img_name = input("Enter the name for the output image (e.g. hidden.png): ")
        
        try:
            Steganography_Methods.encode(cover_img, secret_msg, output_img_name)
            print("\n\nYour message is now successfully hidden...")
            
        except FileNotFoundError:
            print(f"\nError: Could not find the file '{cover_img}'. Please check the spelling and path.")
        except ValueError as e:
            print(f"\nError: {e}")

    elif choice == 'd':
        print("\n--- DECODE MODE ---")
    
        stego_img = input("Enter the path to the image you want to decode (e.g. Desktop/Pictures/hidden.png): ")
        
        try:
            extracted_msg = Steganography_Methods.decode(stego_img)
            
            print("\n\n     Message Is Successfully Extracted    \n")
            print("         EXTRACTED MESSAGE")
            print("\n========================================")
            print(extracted_msg)
            print("========================================\n")
            
        except FileNotFoundError:
            print(f"\nError: Could not find the file '{stego_img}'. Please check the spelling and path.")

    else:
        print("\nInvalid choice. Please run the program again and type 'E' or 'D'.")
if __name__ == "__main__":
    main()

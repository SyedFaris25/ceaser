from PIL import Image
import os

def encrypt_image(input_path, key, output_path):
    try:
        img = Image.open(input_path)
        encrypted_img = Image.new(img.mode, img.size)
        pixels = img.load()
        encrypted_pixels = encrypted_img.load()

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                encrypted_pixels[x, y] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256
                )

        encrypted_img.save(output_path)
        print(f"Image encrypted and saved as: {output_path}")
    except Exception as e:
        print("Error:", e)

def decrypt_image(input_path, key, output_path):
    try:
        img = Image.open(input_path)
        decrypted_img = Image.new(img.mode, img.size)
        pixels = img.load()
        decrypted_pixels = decrypted_img.load()

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                decrypted_pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )

        decrypted_img.save(output_path)
        print(f"Image decrypted and saved as: {output_path}")
    except Exception as e:
        print("Error:", e)

def main():
    print("Simple Image Encryption/Decryption Tool")
    mode = input("Choose mode: (E)ncrypt or (D)ecrypt: ").strip().upper()
    
    if mode not in ['E', 'D']:
        print("Invalid mode selected.")
        return

    input_path = input("Enter path to input image: ").strip()
    if not os.path.exists(input_path):
        print("Image file not found.")
        return

    try:
        key = int(input("Enter a numeric key (1-255): "))
        if not 1 <= key <= 255:
            raise ValueError
    except ValueError:
        print("Invalid key. It must be a number between 1 and 255.")
        return

    output_path = input("Enter path to save output image (e.g., output.png): ").strip()

    if mode == 'E':
        encrypt_image(input_path, key, output_path)
    else:
        decrypt_image(input_path, key, output_path)

if __name__ == "__main__":
    main()


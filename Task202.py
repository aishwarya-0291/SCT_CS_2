import os
from PIL import Image

def load_image(image_path):
    """Loads an image and returns the object along with its dimensions."""
    try:
        img = Image.open(image_path)
        return img.convert("RGB")
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def encrypt_decrypt_xor(image_path, output_path, key):
    """
    Encrypts or decrypts an image by applying a bitwise XOR operation 
    on each pixel's RGB values using a secret key (0-255).
    Running this a second time with the same key decrypts the image.
    """
    img = load_image(image_path)
    if not img:
        return

    # Ensure key is within 8-bit bounds
    key = key % 256
    
    # Load pixel data
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply XOR operation to each channel
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Success! Image saved to {output_path}")

def scramble_pixels(image_path, output_path, block_size=2):
    """
    Scrambles an image by swapping adjacent blocks of pixels.
    Running this a second time will revert the swap (decrypt it).
    """
    img = load_image(image_path)
    if not img:
        return

    pixels = img.load()
    width, height = img.size

    # Loop through the image in steps of block_size * 2
    for x in range(0, width - block_size, block_size * 2):
        for y in range(0, height):
            for i in range(block_size):
                # Ensure we don't go out of bounds
                if x + block_size + i < width:
                    # Swap pixel blocks horizontally
                    p1 = pixels[x + i, y]
                    p2 = pixels[x + block_size + i, y]
                    
                    pixels[x + i, y] = p2
                    pixels[x + block_size + i, y] = p1

    img.save(output_path)
    print(f"Success! Scrambled image saved to {output_path}")

# --- Demonstration ---
if __name__ == "__main__":
    # Replace 'input.jpg' with the path to an actual image on your computer
    input_file = "input.jpg"
    
    # Create a dummy image for testing if you don't have one handy
    if not os.path.exists(input_file):
        print(f"Creating a placeholder '{input_file}' for demonstration...")
        test_img = Image.new("RGB", (300, 300), color="teal")
        test_img.save(input_file)

    secret_key = 123  # Any integer between 1 and 255

    print("\n--- Testing XOR Encryption ---")
    encrypt_decrypt_xor(input_file, "encrypted_xor.png", secret_key)
    encrypt_decrypt_xor("encrypted_xor.png", "decrypted_xor.png", secret_key)

    print("\n--- Testing Pixel Scrambling ---")
    scramble_pixels(input_file, "scrambled.png", block_size=4)
    scramble_pixels("scrambled.png", "unscrambled.png", block_size=4)
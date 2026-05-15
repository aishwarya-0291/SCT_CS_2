# Simple Image Encryption Tool

A lightweight, educational Python tool that demonstrates image cryptography using direct pixel manipulation. The project showcases how to alter image data at the pixel level using symmetric operations, allowing you to easily obscure and later recover visual information.

## Features

* **Mathematical Manipulation (XOR Encryption):** Applies a bitwise XOR operation to every individual pixel's RGB channels using a secret key (an integer between 0 and 255). 
* **Pixel Value Swapping (Scrambling):** Breaks the image into horizontal segments based on a defined `block_size` and swaps adjacent blocks, structurally distorting the layout of the image.
* **Symmetric Decryption:** Because both operations are mathematically reversible, running the same function a second time with the identical parameters completely decrypts the image.
* **Auto-Generated Test Environment:** The script automatically generates a 300x300 teal image placeholder if an `input.jpg` file is not detected, making it ready to run right out of the box.

---

## Prerequisites

This tool requires Python 3.x and the **Pillow** library for loading, manipulating, and saving image pixels.

You can install Pillow via `pip`:

```bash
pip install Pillow

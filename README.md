# QR-Code-Generator
Absolutely, here's a shortened version:  ---  **Custom QR Code Generator:** Python tool for personalized QR codes. Input data, colors, and logos. Simple CLI. Requires Python 3.x, `qrcode`, and `PIL`. MIT License.  ---


Certainly! Here's a description you can use for your GitHub repository:

---

## QR Code Generator with Custom Design

This Python program allows users to generate QR codes with custom designs. Users can specify various parameters such as data to encode, background color, QR code color, and optionally include a logo with customizable size, position, and border.

### Features:

- Generate QR codes with custom designs.
- Specify data to encode.
- Choose background color and QR code color.
- Optionally include a logo with customizable size, position, and border.

### Usage:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the `qr_code_generator.py` script.
4. Follow the prompts to input data, filename, background color, QR code color, and whether to include a logo.
5. If including a logo, provide the logo's path, size, position, and whether to include a border.
6. The program will generate the QR code with the specified parameters and save it to the provided filename.

### Requirements:

- Python 3.x
- `qrcode` library
- `PIL` (Python Imaging Library)

### Example:

```bash
$ python qr_code_generator.py
Enter the data you want to encode in QR code: Hello, world!
Enter the filename to save the QR code (with extension): example.png
Enter background color (default is white): 
Enter QR code color (default is black): 
Do you want to include a logo? (yes/no): yes
Enter logo path (with extension): logo.png
Enter logo size (width height): 50 50
Enter logo position (x y): 100 100
Do you want a border around the logo? (yes/no): no
```

This will generate a QR code with the text "Hello, world!" on a white background, with black QR code color and a logo positioned at (100, 100) with size (50x50) without a border.

### License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the description according to your preferences and additional details you may want to include!

from tkinter import Tk, filedialog
from PIL import Image
import os

# Step 1: Open file dialog to select a PNG file
root = Tk()
root.withdraw()  # Hide the root window
png_path = filedialog.askopenfilename(
    title="Select a PNG file to convert to ICO",
    filetypes=[("PNG files", "*.png")]
)

# Step 2: Proceed if a file was selected
if png_path:
    try:
        # Load the PNG image
        img = Image.open(png_path)

        # Define icon sizes
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256), (512, 512)]

        # Define output path in the same directory
        base_name = os.path.splitext(os.path.basename(png_path))[0]
        output_path = os.path.join(os.path.dirname(png_path), f"{base_name}.ico")

        # Save as ICO with multiple sizes
        img.save(output_path, format="ICO", sizes=sizes)

        print(f"ICO file created successfully at: {output_path}")
    except Exception as e:
        print(f"Error converting PNG to ICO: {e}")
else:
    print("No file selected.")

from rembg import remove
from PIL import Image
import io

  #First it need to install (pip install rembg pillow)


def remove_background(input_image_path, output_image_path):
    try:
        # Open the input image
        with open(input_image_path, "rb") as input_file:
            input_image = input_file.read()

        # Remove the background
        output_image = remove(input_image)

        # Save the output image
        with open(output_image_path, "wb") as output_file:
            output_file.write(output_image)

        print(f"Background removed successfully! Saved to {output_image_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input and output paths
    input_path = input("Enter the path to the input image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()

    remove_background(input_path, output_path)

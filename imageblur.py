from PIL import Image, ImageFilter
import os

# Function to blur a single image
def blur_image(input_path, output_path):
    try:
        # Open an image file
        with Image.open(input_path) as img:
            # Apply a blur filter (using GaussianBlur with a radius of 100 for moderate blur)
            blurred_img = img.filter(ImageFilter.GaussianBlur(radius=100))
            # Save the blurred image to the specified output path
            blurred_img.save(output_path)
            print(f"Blurred image saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred while blurring the image: {e}")

# Function to blur all images in the specified folder
def blur_images_in_folder(folder_path):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return
        
        # Create a folder for blurred images
        blurred_folder = os.path.join(folder_path, "blurred_images")
        if not os.path.exists(blurred_folder):
            os.makedirs(blurred_folder)
        
        # Iterate over all files in the folder
        for filename in os.listdir(folder_path):
            # Check for common image extensions
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(blurred_folder, f"blurred_{filename}")
                # Blur the image and save it in the blurred images folder
                blur_image(input_path, output_path)
        
        print(f"All images in '{folder_path}' have been blurred and saved in '{blurred_folder}'.")
    
    except Exception as e:
        print(f"An error occurred while processing the folder: {e}")

# Example usage:
image_folder = "/Users/rudycazares/Desktop/images"  # Path to the image folder on your desktop
blur_images_in_folder(image_folder)

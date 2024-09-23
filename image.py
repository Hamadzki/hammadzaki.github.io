import os
from PIL import Image
from tqdm import tqdm

# Convert all images to .webp with dynamic quality based on file size
def convert_images_to_webp(folder_path, quality=80):
    output_folder = folder_path
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        # Check for both .jpg and .png files
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            
            img = Image.open(img_path)

            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_path = os.path.join(output_folder, webp_filename)

            # Save the image as WebP
            img.save(webp_path, 'webp', quality=quality)
            print(f'Converted {filename} to {webp_filename} with quality {quality}.')


# Function to optimize and reduce the size of WebP files
def optimize_webp_images(folder_path, quality=70):
    for filename in os.listdir(folder_path):
        # Check for webp files
        if filename.endswith('.webp'):
            img_path = os.path.join(folder_path, filename)
            # file_size_kb = os.path.getsize(img_path) / 1024  # Get file size in KB
            
            img = Image.open(img_path)

            # Set quality based on file size
            
            img.save(img_path, 'webp', quality=quality)
            print(f'Reduced size of {filename} with quality {quality}.')


# Convert specific images based on list and file size condition
def convert_specific_images_to_webp(folder_path, image_names, quality=60):
    output_folder = folder_path
    os.makedirs(output_folder, exist_ok=True)

    for image_name in (image_names):
        img_path_jpg = os.path.join(folder_path, image_name + '.jpg')
        img_path_png = os.path.join(folder_path, image_name + '.webp')

        if os.path.exists(img_path_jpg):
            img_path = img_path_jpg
        elif os.path.exists(img_path_png):
            img_path = img_path_png
        else:
            print(f'Image {image_name} not found as .jpg or .webp in {folder_path}.')
            continue

        img = Image.open(img_path)

        webp_filename = image_name + '.webp'
        webp_path = os.path.join(output_folder, webp_filename)

        img.save(webp_path, 'webp', quality=quality)
        print(f'Converted {image_name} to {webp_filename} with quality {quality}.')


def optimize_specific_webp_images(image_paths, quality=40):
    for img_path in image_paths:
        # Check if the file is a webp file
        if img_path.endswith('.webp'):
            # Get original file size
            original_size_kb = os.path.getsize(img_path) / 1024
            
            img = Image.open(img_path)

            # Save the image with reduced quality
            img.save(img_path, 'webp', quality=quality)

            # Get new file size
            new_size_kb = os.path.getsize(img_path) / 1024
            
            print(f'Reduced size of {os.path.basename(img_path)}:')
            print(f'  Original size: {original_size_kb:.2f} KB')
            print(f'  New size: {new_size_kb:.2f} KB')
            print(f'  Quality set to: {quality}\n')
        else:
            print(f'Skipped {os.path.basename(img_path)}: Not a WebP file.')

# Example usage:
# image_paths = ['path/to/image1.webp', 'path/to/image2.webp']
# optimize_webp_images(image_paths, quality=70)


# Example usage:
# For converting all images
# convert_images_to_webp('assets/img/certificates')
# convert_images_to_webp('assets/img/skills')

# convert_images_to_webp('assets/img')

# optimize_webp_images('assets/img/project')

# For converting specific images
# convert_specific_images_to_webp('assets/img/skills', ['airflow.png'])

# images_path = ['portfolio/assets/img/project/crypto.webp','portfolio/assets/img/project/temperature.webp']
images_path = ['assets/img/project/NLP-With-HuggingFace1.webp'] 
optimize_specific_webp_images(images_path)
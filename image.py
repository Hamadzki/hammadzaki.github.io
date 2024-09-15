import os
from PIL import Image
from tqdm import tqdm

# Convert all images to .webp with dynamic quality based on file size
def convert_images_to_webp(folder_path, quality=90, size_threshold=200):
    output_folder = folder_path
    os.makedirs(output_folder, exist_ok=True)

    for filename in tqdm(os.listdir(folder_path)):
        if filename.endswith('.jpg') or filename.endswith('.webp'):
            img_path = os.path.join(folder_path, filename)
            file_size_kb = os.path.getsize(img_path) / 1024  # Get file size in KB
            
            img = Image.open(img_path)

            # Set quality based on file size
            if file_size_kb < size_threshold:
                save_quality = 98
            else:
                save_quality = quality

            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_path = os.path.join(output_folder, webp_filename)

            img.save(webp_path, 'webp', quality=save_quality)
            print(f'Converted {filename} to {webp_filename} with quality {save_quality}.')


# Convert specific images based on list and file size condition
def convert_specific_images_to_webp(folder_path, image_names, quality=90, size_threshold=200):
    output_folder = folder_path
    os.makedirs(output_folder, exist_ok=True)

    for image_name in tqdm(image_names):
        img_path_jpg = os.path.join(folder_path, image_name + '.jpg')
        img_path_png = os.path.join(folder_path, image_name + '.webp')

        if os.path.exists(img_path_jpg):
            img_path = img_path_jpg
        elif os.path.exists(img_path_png):
            img_path = img_path_png
        else:
            print(f'Image {image_name} not found as .jpg or .webp in {folder_path}.')
            continue

        file_size_kb = os.path.getsize(img_path) / 1024  # Get file size in KB
        img = Image.open(img_path)

        # Set quality based on file size
        if file_size_kb < size_threshold:
            save_quality = 98
        else:
            save_quality = quality

        webp_filename = image_name + '.webp'
        webp_path = os.path.join(output_folder, webp_filename)

        img.save(webp_path, 'webp', quality=save_quality)
        print(f'Converted {image_name} to {webp_filename} with quality {save_quality}.')

# Example usage:
# For converting all images
# convert_images_to_webp('assets/img/certificates')
# convert_images_to_webp('assets/img/certificates')

# For converting specific images
convert_specific_images_to_webp('assets/img', ['my-profile-img.jpg'])

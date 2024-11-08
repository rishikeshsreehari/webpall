from PIL import Image
import os
import argparse
import sys

def convert_images(input_folder='.', delete_originals=False, file_type='all', quality=90, include_subdirs=False):
    # Check if the directory exists
    if not os.path.isdir(input_folder):
        print(f"Error: Directory '{input_folder}' does not exist.")
        sys.exit(1)  # Exit the program with an error code

    # Collect applicable files
    applicable_files = []
    if not include_subdirs:
        # Only process files in the specified folder, excluding subdirectories
        files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
        for file in files:
            if (file_type == 'all' and file.lower().endswith(('jpg', 'jpeg', 'png'))) or \
               (file_type == 'jpg' and file.lower().endswith(('jpg', 'jpeg'))) or \
               (file_type == 'png' and file.lower().endswith('png')):
                applicable_files.append(os.path.join(input_folder, file))
    else:
        # Process files in specified folder and subdirectories
        for root, _, files in os.walk(input_folder):
            for file in files:
                if (file_type == 'all' and file.lower().endswith(('jpg', 'jpeg', 'png'))) or \
                   (file_type == 'jpg' and file.lower().endswith(('jpg', 'jpeg'))) or \
                   (file_type == 'png' and file.lower().endswith('png')):
                    applicable_files.append(os.path.join(root, file))

    # Print summary of found files
    print(f"Found {len(applicable_files)} image files to convert.")

    # Convert each applicable file
    for file_path in applicable_files:
        img = Image.open(file_path).convert('RGB')
        webp_path = f"{os.path.splitext(file_path)[0]}.webp"
        
        # Save the image in WebP format with specified quality
        img.save(webp_path, 'webp', quality=quality, lossless=(quality == 100))
        conversion_message = f"Converted {file_path} to {webp_path}"
        
        # Delete the original file if specified
        if delete_originals:
            os.remove(file_path)
            conversion_message += f" and deleted {file_path}"
        
        print(conversion_message)

def main():
    print("Starting conversion process...")
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Convert images to WebP format.")
    parser.add_argument('--dir', default='.', type=str, help="Path to the folder with images (default: current directory).")
    parser.add_argument('--delete', action='store_true', help="Delete original files after conversion.")
    parser.add_argument('--type', choices=['all', 'jpg', 'png'], default='all', help="File types to process: jpg, png, or all.")
    parser.add_argument('--quality', type=int, default=90, help="Quality of WebP conversion (1-100, default: 90 for high-quality lossless).")
    parser.add_argument('--subdirs', '-s', action='store_true', help="Include subdirectories in the conversion process.")
    args = parser.parse_args()

    # Check if the quality is within the acceptable range (1-100)
    if not (1 <= args.quality <= 100):
        print("Error: Quality must be between 1 and 100.")
        sys.exit(1)

    # Run the conversion with provided arguments
    convert_images(
        input_folder=args.dir, 
        delete_originals=args.delete, 
        file_type=args.type, 
        quality=args.quality, 
        include_subdirs=args.subdirs
    )

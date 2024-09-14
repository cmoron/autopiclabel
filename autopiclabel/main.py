"""
autopiclabel - A module to analyze images, generate descriptive names, and rename image files.

This module uses the Pillow library to open and analyze images, and Ollama to generate descriptions
and filenames based on those descriptions. It allows processing an entire directory of images,
generating new names for each image, and renaming the files accordingly.

Functions:
- generate_name(description): Generates a name based on a description using Ollama.
- rename_file(old_path, new_name): Renames a file with a new name.
- process_directory(directory_path): Processes all image files in a directory, analyzes the images,
generates new names, and renames the files.
- describe_image(image_path): Generates a description of an image using an LLM model.

Execution:
This module can be run from the command line to process a specified directory of images.

Example usage:
    python autopiclabel.py /path/to/directory

Dependencies:
- os
- argparse
- ollama
- re
"""
import os
import argparse
import re
import ollama

def rename_file(old_path, new_name):
    """
    Rename the file to the new name.
    
    Args:
        old_path (str): The current path of the file.
        new_name (str): The new name for the file.
    """
    directory = os.path.dirname(old_path)
    extension = os.path.splitext(old_path)[1]
    new_name = new_name.split(" ")[0]
    new_path = os.path.join(directory, f"{new_name}{extension}")
    os.rename(old_path, new_path)
    print(f"File renamed: {old_path} -> {new_path}")

def process_directory(directory_path):
    """
    Process all image files in the directory, analyze them, generate new names
    and rename the files.
    
    Args:
        directory_path (str): The path to the directory containing the images.
    """
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            full_path = os.path.join(directory_path, filename)
            new_name = generate_name(full_path)
            if new_name:
                rename_file(full_path, new_name)

def generate_name(image_path):
    """
    Generate a name for the image using an LLM model.

    Args:
        image_path (str): The path to the image file.
    
    Returns:
        str: The generated name for the image.
    """
    # handle the case where the model is not available
    try:
        prompt = "Generate filename: \
            Use snake case \
            Max 25 characters \
            English only \
            No file extension \
            No special characters \
            Only key elements of the image \
            One word if possible \
            Noun-verb format \
            Respond only with the filename"
        response = ollama.generate(model="llava", prompt=prompt, images=[image_path])
        filename = response['response'].strip()
        filename = filename.replace(" ", "_")
        filename = filename.replace("-", "_")
        filename = re.sub(r'[^a-zA-Z0-9_]', '', filename) # remove special characters
        filename = filename.lower()
    except ollama.ResponseError as e:
        print(f"Error: {e}")
        return None
    return filename

def main():
    """
    Main function to process a directory of images to generate new names and rename the files.
    """
    parser = argparse.ArgumentParser(
        description="Process a directory of images to generate new names and rename the files.")
    parser.add_argument("directory_path", type=str,
                        help="The path to the directory containing the images.")
    args = parser.parse_args()
    process_directory(args.directory_path)

if __name__ == "__main__":
    main()

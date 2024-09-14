# AutoPicLabel

AutoPicLabel is a Python project that uses a local language model (LLM, run via Ollama) to automatically analyze and rename image files in a wallpaper directory. The model generates file names based on the visual content of each image.

## Objectives

1. **Image Analysis**: Traverse a directory containing image files (wallpapers) and analyze each image to determine its visual content.
2. **Name Generation**: Use a language model (LLM) to generate descriptive and relevant names for each image.
3. **Automatic Renaming**: Rename each image file using the generated names.
4. **Automation**: The process should be fully automated to handle a large number of files.

## Planned Features

- Support for the most common image formats (JPEG, PNG, etc.).
- Batch processing of images in a directory.
- Use of a language model via Ollama to interpret the visual content of images.
- Renaming files with unique and descriptive names.
- Support for command line arguments to specify the directory to process.

## Prerequisites

- **Python 3.8+**: Ensure that Python is installed on your machine.
- **Ollama**: Installation and configuration of Ollama to run the llava language model locally.
- **Python Libraries**:
  - `Ollama` (to interact with the language model)
  - `argparse` (to handle command line arguments)
  - `setuptools` (to handle the package)

  You can install the required libraries with the following command:
  ```bash
  pip install -r requirements.txt
  ```

## Installation

To install AutoPicLabel, run the following command:
```bash
pip install .
```

## Usage

To use AutoPicLabel, run the following command:
```bash
autopiclabel /path/to/directory
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
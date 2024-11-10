
# webpall

`webpall` is a Python-based command-line tool designed to convert images in JPG and PNG formats to WebP format. It offers flexible options for quality settings, including or excluding subdirectories, and managing original files post-conversion. With WebP format, you can achieve smaller file sizes without significant loss in quality, making it an excellent choice for web optimization and storage management.

## Features

- **Selective File Type Conversion**: Choose to convert only JPGs, only PNGs, or both file types.
- **Quality Control**: Adjust the WebP conversion quality from 1-100 (with 100 offering lossless compression).
- **Delete Originals Option**: Optionally delete original images after conversion to WebP format.
- **Recursive Processing**: Include subdirectories in the conversion process to handle large, nested image folders.

## Installation

`webpall` is available on [PyPI](https://pypi.org/project/webpall/) and can be installed using `pip`:

```bash
pip install webpall
```

### Requirements

- Python 3.6 or later.
- **Pillow** library for image processing (automatically installed with `webpall`).

## Usage

After installing, you can use `webpall` from the command line to quickly convert images in a specified folder.

### Default Behavior

If you run `webpall` without any options, it will:

- **Convert all JPG and PNG images** in the **current directory** to WebP format.
- **Keep the original image files intact** (i.e., they will not be deleted).
- **Set the WebP conversion quality to 90%**, providing high-quality compressed images.

To use this default behavior, run:

```bash
webpall
```

### Basic Command Structure

```bash
webpall --dir <directory_path> [options]
```

### Command-Line Options

| Option                 | Description                                                                                             | Default         |
|------------------------|---------------------------------------------------------------------------------------------------------|-----------------|
| `--dir <directory>`    | Path to the folder containing images.                                                                   | Current folder (`.`) |
| `--delete`             | Deletes the original files after conversion.                                                            | Disabled        |
| `--type <all\|jpg\|png>` | Specifies the type of images to convert: `jpg`, `png`, or `all`.                                        | `all`           |
| `--quality <1-100>`    | Sets the quality of the WebP conversion (100 is lossless).                                              | 90              |
| `--subdirs` or `-s`    | Includes subdirectories in the conversion process.                                                      | Disabled        |

### Examples

Here are some common usage examples to help you get started:

#### Example 1: Convert All Images in the Current Directory to WebP

```bash
webpall
```

This converts all JPG and PNG files in the current directory to WebP format, keeping the original files and using the default quality of 90%.

#### Example 2: Convert All Images in a Specific Directory with Custom Quality

```bash
webpall --dir /path/to/images --quality 80
```

This command converts all JPG and PNG images in `/path/to/images` to WebP with a quality setting of 80.

#### Example 3: Convert Only JPG Images and Delete the Original Files

```bash
webpall --dir /path/to/images --type jpg --delete
```

This will convert only JPG files to WebP in `/path/to/images`, deleting the original JPG files after conversion.

#### Example 4: Convert All Images in Subdirectories with Lossless Quality

```bash
webpall --dir /path/to/images --subdirs --quality 100
```

This command will convert all JPG and PNG images within `/path/to/images` and its subdirectories to WebP with lossless quality (100), retaining the original images.

## Example Output

During the conversion process, `webpall` will display status messages for each file:

```plaintext
Starting conversion process...
Found 5 image files to convert.
Converted /path/to/image1.jpg to /path/to/image1.webp
Converted /path/to/image2.png to /path/to/image2.webp and deleted /path/to/image2.png
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Bitmap Service

Bitmap Service is a Python script designed to handle bitmap images. You can use this tool to resize or vectorize bitmap files with ease. It integrates with the Vectorizer API to provide efficient vectorization capabilities. Here's how to set it up and use it.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Support](#support)
- [License](#license)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/bitmapservicerepo.git
    ```

2. Navigate to the directory:

    ```bash
    cd bitmapservicerepo
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before using Bitmap Service, there are a few configuration steps:

1. **Vectorizer API Key**: 

    This script uses the Vectorizer API to convert bitmaps to vectors. Obtain a key from [Vectorizer's website](https://vectorizer.io) and place it in `config.ini`:

    ```ini
    [Vectorizer]
    vectorizer_key = YOUR_VECTORIZE_API_KEY
    ```

2. **Root Directory**: 

    Update the `root_directory` variable on line 6 of `entrypoint.py` with the path to the directory containing your bitmap files. 

    ```python
    root_directory = "/path/to/your/bitmaps"
    ```

    **Note**: We should probably move root_directory to the `config.ini` file in the future for easier access and management.

## Usage

Once you've configured Bitmap Service, you're ready to use it!

1. Run the `entrypoint.py` script:

    ```bash
    python entrypoint.py
    ```

2. Follow the on-screen prompts to resize or vectorize your bitmap files.

## Support

If you encounter any issues or have feature requests, please file an issue on this repository's [issue tracker](https://github.com/yourusername/bitmapservicerepo/issues).

## License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) file for details.

---

Happy Bitmap processing! 🖼️

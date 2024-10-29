# Stable Diffusion Image Generator

## Overview

This project is a web application built with Streamlit that leverages the Stable Diffusion model to generate images from text prompts and an initial uploaded image. 
The application is designed to provide a user-friendly interface for experimenting with image generation using deep learning techniques.

## Features

- `Text-and-Image-to-Image Generation:` Enter a descriptive prompt and upload an initial image to generate an image.
- `Responsive UI:` Intuitive layout with centered buttons and stylish design for ease of use.
- `Real-time Feedback:` Receive updates during the image generation process.

## Requirements

To run this application, you need:

- Python 3.7 or later
- Libraries:
  - `streamlit`
  - `torch` (for PyTorch support)
  - `Pillow` (for image processing)
  - `diffusers` (for loading the Stable Diffusion model)

## Installation

1. Clone the Repository:
     - First clone the repository from GitHub using the command:
       git clone https://github.com/BizuhanAbate/stable-diffusion-image-generator.git,
     - And then navigate into the project directory with: cd stable-diffusion-image-generator
2. Install Required Packages:
    - pip install streamlit torch Pillow diffusers
It's recommended to create a virtual environment to manage dependencies, which you can do with:
 - python -m venv venv on Windows or
 - python3 -m venv venv on macOS/Linux
   
## Usage

1. Run the Application:
 To start the Streamlit server, since the name of the application is app.py, execute the following command in your terminal:
   streamlit run app.py

3. Interact with the App:
   - It directly opens it on the web browser or you can navigate yourself to the address you get from the terminal.
   - Enter a descriptive text prompt in the input field.
   - Upload an initial image using browse files button.
   - Finally click the "Generate Image" button and wait until the spinner finishs and provide you the artwork!

4. View Results:
   The application will display the initial and generated images side by side after processing.
   Finally, deactivate the virtual environment with deactivate when you’re done.

## Code Structure

- `app.py`: Main application script that contains the Streamlit code and model inference logic.

## Customization

You can customize the application by modifying:

- The text prompt: Change the default text prompt in the `st.text_input()` function.
- Image processing parameters: Adjust image resizing or generation parameters in the code.



# VividPal
This project is a comprehensive image processing pipeline designed to colorize, enhance, and repair images. The application leverages state-of-the-art deep learning models and is built on a Flask web framework to provide a user-friendly interface for processing images.

### Project Overview
Objective
The main objective of this project is to take an input image—potentially black and white or low quality—and apply a series of processing steps to produce a high-quality, colorized, and repaired output image. The project uses a combination of deep learning models and traditional image processing techniques to achieve this.

### Processing Steps
Image Colorization: Converts black-and-white images into color images.
Image Enhancement: Enhances the details and color quality of the image.
Image Repair: Repairs any defects or artifacts in the image, such as scratches, noise, or distortions.
Technologies Used
Flask: A micro web framework used to create a web interface for users to upload images and view the processed results.
DeOldify: A deep learning model specifically designed for colorizing black-and-white images.
CycleGAN: A type of Generative Adversarial Network (GAN) that enhances the quality of the image by learning the mapping between unpaired datasets.
OpenCV: An open-source computer vision library used for image processing tasks such as reading, writing, and manipulating images.

### Project Structure:
├── code.ipynb           # Main code
├── app.py               # Main Flask application file
├── templates/           # HTML templates for the Flask app
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation

### Installation
To get started with this project, follow these steps:

# 1. Clone the Repository
'''bash

git clone https://github.com/Mihawk1891/VividPal.git 
cd VividPal
'''
# 2. Install Dependencies
Ensure you have Python installed. Then, install the required Python packages using pip:

'''bash

pip install -r requirements.txt
'''
# 3. Download Pre-trained Models
The project relies on pre-trained models like DeOldify and CycleGAN. You need to download these models and place them in the models/ directory. Instructions for downloading the models are available on their respective GitHub repositories.

# 4. Run the Flask Application
Start the Flask server by running:

'''bash

python app.py '''
This will start the application on http://127.0.0.1:5000.

### How It Works
# 1. Uploading an Image
The user interface allows you to upload an image file. Supported formats include JPEG, PNG, etc.
Once an image is uploaded, the file is saved in the uploads/ directory.

# 2. Image Processing Pipeline
a. Colorization with DeOldify
Purpose: The first step is to colorize the image, especially if it is black and white.
How It Works: DeOldify is a deep learning model based on a Generative Adversarial Network (GAN) architecture. It uses a combination of a generator and a discriminator to colorize images. The generator attempts to colorize the image, while the discriminator tries to differentiate between real and colorized images. Over time, the generator improves, producing more realistic colorized images.
b. Enhancement with CycleGAN
Purpose: After colorization, the image may still require enhancement, especially if it is of low quality or has faded over time.
How It Works: CycleGAN is used to enhance the image. Unlike traditional GANs that require paired datasets (e.g., low-quality and high-quality images of the same scene), CycleGAN learns to map between two unpaired datasets. In this project, CycleGAN improves the colorization quality, sharpness, and overall aesthetics of the image.
c. Image Repair
Purpose: The final step is to repair any defects in the image, such as noise, scratches, or other artifacts.
How It Works: This step might involve traditional image processing techniques provided by OpenCV, such as inpainting, denoising, or smoothing. The repaired image is then saved in the results/ directory.

# 3. Downloading the Processed Image
After the image has been processed, a link to download the final image is provided on the web interface.
Detailed Explanation of Technologies

# Flask
Role: Flask is a lightweight web framework used to create the web interface for this application.
Functionality: It handles HTTP requests, file uploads, and serves the HTML templates that form the user interface. Flask routes are defined in app.py to link the user actions (like uploading an image) to the corresponding backend processing functions.

# DeOldify
Role: DeOldify is a deep learning model used for colorizing black-and-white images.
Functionality: The model uses a GAN architecture to add realistic colors to black-and-white photos. It has been trained on large datasets of color images, allowing it to predict and apply appropriate colors to various objects in the image.

# CycleGAN
Role: CycleGAN is used to enhance the colorized images.
Functionality: CycleGAN is particularly powerful in scenarios where paired datasets are not available. It uses two generators and two discriminators to learn the mapping between two image domains (e.g., low-quality and high-quality images) and applies this knowledge to enhance the image.

# OpenCV
Role: OpenCV is used for additional image processing tasks such as image repair.
Functionality: It provides tools for reading, writing, and manipulating images. In this project, OpenCV might be used to apply filters, inpaint damaged areas, or remove noise from the image.
Future Improvements
Model Fine-tuning: Fine-tune the pre-trained models on a custom dataset to improve the results for specific types of images.
User Interface: Improve the web interface to provide more features such as image cropping, multiple file uploads, or real-time preview of the processing steps.
Deployment: Deploy the application on a cloud platform (e.g., AWS, Heroku) to make it accessible online.

### Open for Collaboration
I am open to collaboration! Feel free to reach out if you're interested in improving this project or have any ideas.

Contact: pranavbansoode2604@gmail.com

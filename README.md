# VividPal

This project is focused on the restoration and colorization of historical images using advanced AI techniques, specifically Generative Adversarial Networks (GANs). The aim is to enhance the visual quality of old and degraded images while maintaining historical accuracy.

## Project Description

In this project, I utilized a variety of cutting-edge technologies and methodologies to restore and colorize historical images. The core techniques included advanced preprocessing pipelines, sophisticated GAN architectures, model training and deployment, image repair and enhancement, and the development of user-friendly interfaces.

### Advanced Preprocessing Pipelines

I developed advanced preprocessing pipelines to prepare historical images for restoration and colorization. This involved:
- Handling various image formats. (.png, .jpg, .img)
- Normalizing data and removing noise and artifacts using libraries like OpenCV and scikit-image (skimage).
- Specific preprocessing steps like resizing images, converting them to grayscale, and enhancing image contrast.

### GAN Architectures

The project utilized sophisticated GAN architectures, including:
- **DeOldify** for colorization.
- **CycleGAN** for style transfer and enhancement.

The models were trained using TensorFlow and PyTorch, with extensive experimentation on hyperparameters, loss functions, and training schedules to achieve the best results.

### Model Training and Deployment

I implemented robust training pipelines using GPU acceleration to handle the computational demands. The training involved:
- Large datasets of historical and modern images.
- Techniques like model quantization and pruning for optimized deployment.

### Image Repair and Enhancement

Beyond colorization, I developed algorithms for:
- **Edge detection and inpainting** to repair and enhance the quality of historical images.
- Techniques like edge detection and inpainting using OpenCV and skimage.

### User-Friendly Tools and Interfaces

To make the technology accessible, I designed and developed user-friendly tools with web-based interfaces that allow users to upload images and see real-time restoration and colorization results.

## Code Overview

The codebase is organized into several key components:

- **Image Preprocessing:** Prepares historical images for restoration.
- **GAN Architectures:** Implements DeOldify and CycleGAN for colorization and enhancement.
- **Model Training:** Trains the GAN models with extensive optimization.
- **Image Repair:** Uses edge detection and inpainting for image enhancement.
- **Flask Application:** Provides a web-based interface for users to upload and restore images.


## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Mihawk1891/VividPal.git
   cd VividPal

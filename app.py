import flask
from flask import Flask, request, render_template, send_file
# Define paths and global variables
UPLOAD_FOLDER = '/content/Upload_folder'
RESULT_FOLDER = '/content/Result_folder'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
# Flask Routes for User Interaction
@app.route('/')
def upload_image():
    return render_template('upload.html')

@app.route('/restore', methods=['POST'])
def restore_image():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Preprocess the image
        preprocessed_image = preprocess_image(file_path)
        
        # Restore and colorize the image
        deoldify = DeOldifyColorizer()
        colorized_image = deoldify.colorize_image(file_path)
        
        # Enhance the image with CycleGAN
        cyclegan = CycleGANEnhancer()
        enhanced_image = cyclegan.enhance_image(colorized_image)

        # Repair the image
        repaired_image = repair_image(enhanced_image)

        # Save the result
        result_path = os.path.join(app.config['RESULT_FOLDER'], filename)
        cv2.imwrite(result_path, repaired_image)

        return send_file(result_path, mimetype='image/jpeg')

    return 'File not allowed'

if __name__ == '__main__':
    app.run(debug=True)
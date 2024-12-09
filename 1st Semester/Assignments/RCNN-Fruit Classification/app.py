# app.py

from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import os

# Define the RCNN model structure (same as in train.py)
class RCNNModel(nn.Module):
    def __init__(self, num_classes):
        super(RCNNModel, self).__init__()
        
        # Define a simple CNN architecture
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(32 * 64 * 64, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.pool(nn.ReLU()(self.conv1(x)))
        x = self.pool(nn.ReLU()(self.conv2(x)))
        x = x.view(-1, 32 * 64 * 64)
        x = nn.ReLU()(self.fc1(x))
        x = self.fc2(x)
        return x

# Initialize the Flask application
app = Flask(__name__)

# Define the 30 fruit class labels based on your dataset
class_labels = [
    'Apple Braeburn', 'Apple Granny', 'Smith', 'Apricot', 'Avocado', 'Banana', 'Blueberry', 
    'Cactus fruit', 'Cantaloupe', 'Grape Blue', 'Kiwi', 'Lemon', 'Limes', 'Mango', 'Onion White', 
    'Orange', 'Papaya', 'Pepper Red', 'Pineapple', 'Plum', 'Pomegranate', 'Potato Red', 
    'Raspberry', 'Strawberry', 'Tomato', 'Cherry', 'Clementine', 'Passion Fruit', 'Peach', 
    'Watermelon'
]

# Set the number of classes
num_classes = len(class_labels)

# Initialize the model and load trained weights
model = RCNNModel(num_classes=num_classes)
model.load_state_dict(torch.load('model/rcnn_model.pth'))  # Load state_dict
model.eval()  # Set the model to evaluation mode

# Define image transformation
transform = transforms.Compose([
    transforms.Resize((256, 256)),  # Resize image
    transforms.ToTensor()            # Convert image to tensor
])

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page

# Route for predicting fruit from an uploaded image
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:  # Check if file part is in request
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']  # Get the uploaded file
    
    if file.filename == '':  # Check if no file is selected
        return jsonify({'error': 'No selected file'})
    
    # Process the image
    try:
        image = Image.open(file.stream)  # Open the uploaded image
        image = transform(image).unsqueeze(0)  # Transform and add batch dimension
    except Exception as e:
        return jsonify({'error': str(e)})  # Return error if image processing fails

    # Get the model's prediction
    with torch.no_grad():  # Disable gradient calculation
        outputs = model(image)  # Get model predictions
        _, predicted = torch.max(outputs.data, 1)  # Get the predicted class index

    predicted_class = class_labels[predicted.item()]  # Map index to class label
    return jsonify({'class': predicted_class})  # Return the predicted class as JSON

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development

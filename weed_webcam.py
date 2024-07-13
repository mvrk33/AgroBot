import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# Load and preprocess the dataset using pandas
data_path = "C://Users//kumar//Downloads//projecttrain.csv"
df = pd.read_csv(data_path)

# Assuming your dataset has columns 'image_path' for image file paths and 'label' for labels
image_paths = df['image_path'].values
labels = df['label'].values

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train_paths, X_test_paths, y_train, y_test = train_test_split(image_paths, labels, test_size=0.2, random_state=42)

# Image data preprocessing using ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
),

test_datagen = ImageDataGenerator(rescale=1./255)

# Define batch size and image dimensions
batch_size = 32
img_height = 224
img_width = 224

# Create data generators for training and testing sets
train_generator = train_datagen.flow_from_dataframe(
    dataframe=df,
    directory=None,  # Assuming image paths are absolute or relative to current directory
    x_col='image_path',
    y_col='label',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

test_generator = test_datagen.flow_from_dataframe(
    dataframe=df,
    directory=None,  # Assuming image paths are absolute or relative to current directory
    x_col='image_path',
    y_col='label',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

# Load pre-trained MobileNetV2 model
base_model = MobileNetV2(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)

# Compile the model
model = Model(inputs=base_model.input, outputs=predictions)
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.n // batch_size,
    epochs=10,
    validation_data=test_generator,
    validation_steps=test_generator.n // batch_size
)

# Save the trained model
model.save('weed_detection_model.h5')

# Inference on new images
def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(img_height, img_width))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch dimension
    return img_array / 255.0  # Normalize pixel values

# Load the trained model
model = tf.keras.models.load_model('weed_detection_model.h5')

# Preprocess the new image
new_image_path = 'C://Users//kumar//OneDrive//Pictures//Saved Pictures//weedplant.jpg'
new_image = preprocess_image(new_image_path)

# Perform inference
prediction = model.predict(new_image)
if prediction > 0.5:
    print('The image contains a weed.')
else:
    print('The image does not contain a weed.')

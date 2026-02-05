import tensorflow as tf
from tensorflow.keras import layers, models
import os

# Define dataset path
dataset_path = "/Users/bhavaniboyapati/Downloads/images"
 # <-- Update this to your dataset path
img_size = (64, 64)
batch_size = 32

# Load and preprocess dataset
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

# Define model
model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(64, 64, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(len(train_ds.class_names), activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(train_ds, validation_data=val_ds, epochs=10)

# Save model
os.makedirs("app/models", exist_ok=True)
model.save("app/models/your_cnn_model.keras")

# Save class names
with open("app/models/class_labels.txt", "w") as f:
    for class_name in train_ds.class_names:
        f.write(f"{class_name}\n")

print("Model trained and saved.")

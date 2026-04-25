import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# 1. Load Data
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize values (0-255 -> 0-1)
train_images = train_images / 255.0
test_images = test_images / 255.0

print("Data Loaded!")

# 2. Build CNN Model
model = models.Sequential()

# Step 1 : Detect features
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))

# Step 2 : Reduce size
model.add(layers.MaxPooling2D((2, 2)))

# Step 3 : Convert to 1D
model.add(layers.Flatten())

# Step 4 : Learn Patterns
model.add(layers.Dense(64, activation='relu'))

# Step 5 : Output (10 Classes)
model.add(layers.Dense(10, activation='softmax'))

print("Model Built!")

# 3. Compile Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Train Model
model.fit(train_images, train_labels, epochs=3)

# 5. Test Model
loss, accuracy = model.evaluate(test_images, test_labels)

print("Test Accuracy:", accuracy)
print("Loss:", loss)
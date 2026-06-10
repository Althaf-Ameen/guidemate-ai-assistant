import os
import cv2

image_folder = "Your_Image_Folder_Path"  # Change to your image folder
label_folder = "Your_Image_Label_Path"  # Change to your label folder

# Check if the image folder exists
if not os.path.exists(image_folder):
    print(f"Image folder '{image_folder}' does not exist.")
    exit()

# Create the label folder if it doesn't exist
os.makedirs(label_folder, exist_ok=True)

# Loop through all images and create annotation files
for image_file in os.listdir(image_folder):
    if image_file.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(image_folder, image_file)
        txt_filename = os.path.splitext(image_file)[0] + ".txt"
        txt_path = os.path.join(label_folder, txt_filename)

        try:
            # Load the image using OpenCV
            image = cv2.imread(image_path)
            height, width, _ = image.shape
            
            # Define bounding box (full image as box)
            x_center = 0.5  # Center X (normalized)
            y_center = 0.5  # Center Y (normalized)
            bbox_width = 1.0  # Full width (normalized)
            bbox_height = 1.0  # Full height (normalized)

            # Prepare annotation content
            annotation = f"0 {x_center} {y_center} {bbox_width} {bbox_height}\n"
            
            # Write annotation to the label file
            with open(txt_path, "w") as f:
                f.write(annotation)
                print(f"Annotated: {txt_path}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

print("Annotation process completed!")

import os

image_folder = "Your_Image_Folder_Path"  # Change to your image folder
label_folder = "Your_Label_Folder_Path"  # Change to your label folder

# Check if the image folder exists
if not os.path.exists(image_folder):
    print(f"Image folder '{image_folder}' does not exist.")
else:
    print(f"Image folder '{image_folder}' found.")

# Create the label folder if it doesn't exist
os.makedirs(label_folder, exist_ok=True)

# Loop through all images and create empty txt files if they don't exist
for image_file in os.listdir(image_folder):
    if image_file.lower().endswith((".jpg", ".jpeg", ".png")):
        txt_filename = os.path.splitext(image_file)[0] + ".txt"
        txt_path = os.path.join(label_folder, txt_filename)

        try:
            # Create an empty txt file if it doesn't exist
            if not os.path.exists(txt_path):
                with open(txt_path, "w") as f:
                    f.write("")  # Create an empty file
                print(f"Created: {txt_path}")
            else:
                print(f"Already exists: {txt_path}")
        except Exception as e:
            print(f"Error creating {txt_path}: {e}")

print("Process completed!")

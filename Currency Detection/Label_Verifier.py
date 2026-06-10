import os

image_folder = "Your_Image_Folder_Path"  # Change to your image folder
label_folder = "Your_Label_Folder_Path"  # Change to your label folder

# Check if the image and label folders exist
if not os.path.exists(image_folder):
    print(f"Image folder '{image_folder}' does not exist.")
    exit()

if not os.path.exists(label_folder):
    print(f"Label folder '{label_folder}' does not exist.")
    exit()

empty_count = 0
total_count = 0

# Loop through all image files
for image_file in os.listdir(image_folder):
    if image_file.lower().endswith((".jpg", ".jpeg", ".png")):
        txt_filename = os.path.splitext(image_file)[0] + ".txt"
        txt_path = os.path.join(label_folder, txt_filename)
        total_count += 1
        
        # Check if the corresponding label file exists and is not empty
        if os.path.exists(txt_path):
            with open(txt_path, "r") as f:
                content = f.read().strip()
                if not content:
                    print(f"❌ Empty label file: {txt_filename}")
                    empty_count += 1
                else:
                    print(f"✅ Non-empty label file: {txt_filename}")
        else:
            print(f"🚫 Label file not found: {txt_filename}")
            empty_count += 1

print(f"\nTotal images checked: {total_count}")
print(f"Empty or missing label files: {empty_count}")

if empty_count > 0:
    print("\n🔴 Some label files are missing or empty! Please re-annotate those images.")
else:
    print("\n🟢 All label files are present and contain data!")

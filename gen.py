import os
import shutil

BASE_DIR = r"C:\Users\USERNAME\Documents\GitHub\flasharchive"
TEMPLATE_DIR = os.path.join(BASE_DIR, "Ruffle template")

for file in os.listdir(BASE_DIR):
    if file.lower().endswith(".swf"):
        game_name = os.path.splitext(file)[0]
        swf_source_path = os.path.join(BASE_DIR, file)

        game_folder = os.path.join(BASE_DIR, game_name)
        os.makedirs(game_folder, exist_ok=True)

        # Copy entire template contents into game folder
        for item in os.listdir(TEMPLATE_DIR):
            src_path = os.path.join(TEMPLATE_DIR, item)
            dst_path = os.path.join(game_folder, item)

            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dst_path)

        # Copy and rename SWF to file.swf
        shutil.copy2(swf_source_path, os.path.join(game_folder, "file.swf"))

        print(f"Built: {game_name}")

print("All folders regenerated.")

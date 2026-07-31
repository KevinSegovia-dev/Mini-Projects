from pathlib import Path
import shutil

def organize_files():
    downloads_path = Path.home() / "Downloads"
    
    documents_path = Path.home() / "Documents"
    

    downloads_list = downloads_path.iterdir()

    for file in downloads_list:
        if file.is_file() and file.suffix:
    	    # 1. We get the extension name (e.g., 'pdf', 'jpg') in lowercase.
    	    name_folder = file.suffix.replace(".", "").lower()

    	    # 2. We define the destination folder path.
    	    folder_path = documents_path / name_folder

    	    # 3. Create the folder if it does not exist.
    	    folder_path.mkdir(exist_ok=True)

    	    # 4. Move the file to the new folder.
    	    shutil.move(str(file), str(folder_path))

organize_files()

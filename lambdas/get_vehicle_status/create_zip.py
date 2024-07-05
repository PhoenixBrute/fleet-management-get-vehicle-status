import zipfile
import os

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, start=path)
            ziph.write(file_path, arcname)

with zipfile.ZipFile('/get_vehicle_status.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('/lambda-package', zipf)

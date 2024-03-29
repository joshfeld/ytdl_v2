import os
import zipfile
import io


def zip_files():
    file_paths = []
    for root, directories, files in os.walk(r"/files/"):
        for filename in files:
            fp = os.path.join(root, filename)
            file_paths.append(fp)

    if len(file_paths) > 1:
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, "w") as zf:
            for file in file_paths:
                zf.write(file, os.path.basename(file))
        memory_file.seek(0)
        name = "downloads.zip"
        mime = "application/zip"
        return memory_file, name, mime
    else:
        file = file_paths[0]
        name = os.path.basename(file_paths[0])
        mime = "audio/mpeg"
        return file, name, mime

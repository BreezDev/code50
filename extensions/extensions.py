def main():
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    file_name = input("File name: ").strip().lower()
    for ext, media_type in media_types.items():
        if file_name.endswith(ext):
            print(media_type)
            return
    print("application/octet-stream")

main()

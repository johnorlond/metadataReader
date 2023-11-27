from PIL import Image, ExifTags

def read_metadata(file_path):
    # Open the image
    with Image.open(file_path) as img:
        # Print EXIF metadata
        print("EXIF Metadata:")
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = ExifTags.TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")

        # Read IPTC metadata (if available)
        iptc_info = img.info.get("iptc")
        if iptc_info:
            print("\nIPTC Metadata:")
            for key, val in iptc_info.items():
                print(f"{key}: {val}")

        # Read XMP metadata (if available)
        xmp_info = img.info.get("xmp")
        if xmp_info:
            print("\nXMP Metadata:")
            for key, val in xmp_info.items():
                print(f"{key}: {val}")

if __name__ == "__main__":
    file_path = r"C:\Users\johno\OneDrive\Desktop\forensic\testImage1.jpg"  # Replace with the actual path to your image
    read_metadata(file_path)

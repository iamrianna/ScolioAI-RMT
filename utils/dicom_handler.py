import pydicom
import numpy as np
from PIL import Image

def load_uploaded_image(uploaded_file):
    """Parses uploaded DICOM or standard image formats into a PIL Image."""
    fname = uploaded_file.name
    if fname.lower().endswith(('.dcm', '.dicom')):
        dicom = pydicom.dcmread(uploaded_file)
        pixel_array = dicom.pixel_array.astype(float)
        pixel_array -= np.min(pixel_array)
        if np.max(pixel_array) != 0:
            pixel_array /= np.max(pixel_array)
        img_uint8 = (pixel_array * 255).astype(np.uint8)
        return Image.fromarray(img_uint8).convert("RGB"), fname
    else:
        return Image.open(uploaded_file).convert("RGB"), fname

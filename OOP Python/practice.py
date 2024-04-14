import cv2
import numpy as np

# Function to extract LUT from edited picture
def extract_lut_from_picture(edited_picture_path):
    # Load edited picture
    edited_img = cv2.imread(edited_picture_path, cv2.IMREAD_UNCHANGED)

    # Check if the image has an embedded LUT
    data = np.fromfile(edited_picture_path, dtype=np.uint8)
    lut_exists = False
    try:
        # Look for the LUT tag in the image data
        lut_tag = b'mlut'
        lut_start = data.tobytes().find(lut_tag)
        if lut_start != -1:
            lut_length = int.from_bytes(data[lut_start + 8:lut_start + 10], byteorder='little')
            lut = data[lut_start + 10:lut_start + 10 + lut_length * 6].reshape((lut_length, 3, 2))
            lut_exists = True
    except Exception as e:
        print(f"Error extracting embedded LUT: {e}")

    if lut_exists:
        # Use the embedded LUT
        return lut
    else:
        # Calculate the LUT based on the image histogram
        lut = np.zeros((256, 1, 3), dtype=np.uint8)

        # Convert the image to RGB color space
        edited_img = cv2.cvtColor(edited_img, cv2.COLOR_BGR2RGB)

        # Calculate the histogram of the edited image
        hist = cv2.calcHist([edited_img], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

        # Normalize the histogram
        hist /= np.sum(hist)

        # Fill the LUT based on the histogram
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    lut[i, 0, 0] = int(i * hist[i, j, k])
                    lut[i, 0, 1] = int(j * hist[i, j, k])
                    lut[i, 0, 2] = int(k * hist[i, j, k])

        return lut

# Function to apply LUT to new picture
def apply_lut_to_picture(new_picture_path, lut):
    # Load new picture
    new_img = cv2.imread(new_picture_path, cv2.IMREAD_UNCHANGED)

    # Convert the image to RGB color space
    new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)

    # Apply LUT
    new_img_graded = cv2.LUT(new_img, lut)

    # Convert the image back to BGR color space
    new_img_graded = cv2.cvtColor(new_img_graded, cv2.COLOR_RGB2BGR)

    return new_img_graded

# Main function
def main():
    # Paths to edited and new pictures
    edited_picture_path = r"D:\OOP Python\profile.png"
    new_picture_path = r"D:\OOP Python\random.png"

    # Extract LUT from edited picture
    lut = extract_lut_from_picture(edited_picture_path)

    if lut is not None:
        # Apply LUT to new picture
        result_img = apply_lut_to_picture(new_picture_path, lut)

        # Display or save the result
        cv2.imshow("Result", result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to extract LUT from the edited picture.")

if __name__ == "__main__":
    main()
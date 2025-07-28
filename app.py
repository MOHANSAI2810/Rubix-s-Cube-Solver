import cv2
import numpy as np

# Define HSV ranges for color classification
def get_color_label(h, s, v):
    if v < 50:
        return 'k'  # black
    if s < 60:
        return 'w'  # white
    if h < 10 or h >= 160:
        return 'r'  # red
    elif 10 <= h < 25:
        return 'o'  # orange
    elif 25 <= h < 35:
        return 'y'  # yellow
    elif 35 <= h < 85:
        return 'g'  # green
    elif 85 <= h < 130:
        return 'b'  # blue
    else:
        return 'u'  # unknown

def extract_cube_face_colors(image_path, grid_size=3):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return []

    # Resize and center the image (optional)
    image = cv2.resize(image, (300, 300))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    height, width = image.shape[:2]
    cell_h = height // grid_size
    cell_w = width // grid_size

    colors = []

    for row in range(grid_size):
        for col in range(grid_size):
            y1 = row * cell_h + cell_h // 4
            x1 = col * cell_w + cell_w // 4
            y2 = y1 + cell_h // 2
            x2 = x1 + cell_w // 2

            cell = hsv[y1:y2, x1:x2]
            avg_hsv = np.mean(cell.reshape(-1, 3), axis=0)
            h, s, v = avg_hsv
            label = get_color_label(h, s, v)
            colors.append(label)

    return colors

# Example usage
image_path = 'image.png'  # change this if using another image
output = extract_cube_face_colors(image_path)
print("Extracted colors:", output)

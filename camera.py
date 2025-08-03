import cv2
import numpy as np

def get_color_label(h, s, v):
    if v < 50:
        return 'k'  # black
    if s < 60:
        return 'w'  # white
    if (h < 8 or h > 170) and s > 80:
        return 'r'
    elif 8 <= h < 20:
        return 'o'
    elif 20 <= h < 35:
        return 'y'
    elif 35 <= h < 85:
        return 'g'
    elif 85 <= h < 130:
        return 'b'
    else:
        return 'u'

def extract_face_from_frame(frame, grid_size=3):
    image = cv2.resize(frame, (300, 300))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h, w = hsv.shape[:2]
    cell_h = h // grid_size
    cell_w = w // grid_size
    colors = []

    for row in range(grid_size):
        for col in range(grid_size):
            y1 = row * cell_h + cell_h // 4
            x1 = col * cell_w + cell_w // 4
            y2 = y1 + cell_h // 2
            x2 = x1 + cell_w // 2

            cell = hsv[y1:y2, x1:x2]
            avg_hsv = np.mean(cell.reshape(-1, 3), axis=0)
            label = get_color_label(*avg_hsv)
            colors.append(label)

    return colors, image

def draw_grid(image):
    grid_size = 3
    height, width = image.shape[:2]
    cell_h = height // grid_size
    cell_w = width // grid_size

    for i in range(1, grid_size):
        cv2.line(image, (0, i * cell_h), (width, i * cell_h), (255, 255, 255), 1)
        cv2.line(image, (i * cell_w, 0), (i * cell_w, height), (255, 255, 255), 1)
    
    return image

# === Main Logic ===

face_order = ['w', 'y', 'r', 'o', 'g', 'b']
face_names = {
    'w': 'White',
    'y': 'Yellow',
    'r': 'Red',
    'o': 'Orange',
    'g': 'Green',
    'b': 'Blue'
}

print("\n📸 Rubik's Cube Scanner")
print("Please show cube faces in the following order:\n")
for i, face in enumerate(face_order, 1):
    print(f"{i}. {face_names[face]}")

cap = cv2.VideoCapture(0)
cube_faces = {}

for face in face_order:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to capture frame.")
            break

        preview = cv2.resize(frame, (300, 300))
        preview = draw_grid(preview)

        cv2.putText(preview, f"Show {face_names[face]} face & press SPACE", (10, 290),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow("Rubik's Cube Scanner", preview)
        key = cv2.waitKey(1)

        if key == 27:  # ESC to exit
            print("Exit requested.")
            cap.release()
            cv2.destroyAllWindows()
            exit()
        elif key == 32:  # SPACE to capture
            print(f"📸 Captured {face_names[face]} face.")
            colors, final_image = extract_face_from_frame(frame)
            cube_faces[face] = colors
            cv2.imshow(f"{face_names[face]} Face", draw_grid(final_image))
            cv2.waitKey(500)
            cv2.destroyWindow(f"{face_names[face]} Face")
            break

cap.release()
cv2.destroyAllWindows()

# ✅ Final Output
print("\n🧩 Final Cube Face Data:")
for face in face_order:
    print(f"{face.upper()}: {cube_faces.get(face, 'Not captured')}")
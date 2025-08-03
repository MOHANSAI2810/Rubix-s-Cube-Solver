import kociemba
from collections import Counter

# Face order instructions
face_order = ['White', 'Red', 'Green', 'Yellow', 'Orange', 'Blue']
face_inputs = []
ALLOWED_COLORS = {'W', 'R', 'G', 'Y', 'O', 'B'}

print("➡️ Enter the 9 stickers for each face (row by row, left to right)")
print("➡️ Order: White (U), Red (R), Green (F), Yellow (D), Orange (L), Blue (B)")
print("➡️ Allowed colors: W (White), R (Red), G (Green), Y (Yellow), O (Orange), B (Blue)")

# Input 6 faces
for face in face_order:
    while True:
        entry = input(f"Enter 9 colors for {face} face: ").strip().upper()
        if len(entry) != 9:
            print("❌ Must be exactly 9 characters.")
            continue
        if any(c not in ALLOWED_COLORS for c in entry):
            print("❌ Invalid colors found. Allowed:", ALLOWED_COLORS)
            continue
        face_inputs.append(entry)
        break

# Detect centers to identify face positions
centers = [face[4] for face in face_inputs]
detected_faces = ['U', 'R', 'F', 'D', 'L', 'B']
color_to_face = dict(zip(centers, detected_faces))

print("\n🧠 Detected center-to-face mapping:")
for color, face in color_to_face.items():
    print(f"  {color} → {face}")

# Combine all input into a single string
color_string = ''.join(face_inputs)

# Validate color counts
counts = Counter(color_string)
if any(counts[c] != 9 for c in ALLOWED_COLORS):
    print("\n❌ Error: Each of the 6 colors must appear exactly 9 times.")
    print("Color counts:", counts)
else:
    print("\n✅ Color counts are valid.")

    try:
        # Create the final facelet string
        facelet_string = ''.join(color_to_face[c] for c in color_string)
        print("🧩 Final facelet string:", facelet_string)

        # Solve the cube
        solution = kociemba.solve(facelet_string)
        print("\n✅ Cube solution:")
        print(solution)
    except Exception as e:
        print("\n❌ Error solving cube:", e)

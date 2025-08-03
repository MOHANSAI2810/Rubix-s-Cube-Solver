# 🧩 Rubik's Cube Solver

A comprehensive Python project that solves Rubik's cubes using multiple approaches: manual input, camera scanning, and both custom algorithms and the Kociemba library.

## 📋 Features

- **Multiple Solving Methods**: Choose between custom layer-by-layer algorithm or Kociemba's optimal solver
- **Camera Integration**: Scan cube faces using your webcam for automatic color detection
- **Manual Input**: Enter cube state manually with validation
- **Jupyter Notebook**: Interactive solving with step-by-step guidance
- **Comprehensive Validation**: Ensures cube state is valid before solving

## 🗂️ Project Structure

```
cube solver/
├── rubik_solver_without_kociemba.py    # Custom layer-by-layer solver
├── rubik_solver_with_kociemba.py       # Kociemba library solver
├── camera.py                           # Webcam cube scanner
├── rubix_cube_solver.ipynb             # Jupyter notebook interface
└── README.md                           # This file
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install opencv-python kociemba numpy
```

### Method 1: Camera Scanner (Recommended)

1. **Run the camera scanner**:
   ```bash
   python camera.py
   ```

2. **Follow the prompts** to scan each face of your cube:
   - Show each face to the camera
   - Press SPACE to capture
   - Follow the order: White, Yellow, Red, Orange, Green, Blue

3. **Use the captured data** with any solver method

### Method 2: Manual Input

1. **Run the Kociemba solver**:
   ```bash
   python rubik_solver_with_kociemba.py
   ```

2. **Enter cube state** following the prompts:
   - Enter 9 colors for each face (row by row, left to right)
   - Use color codes: W, R, G, Y, O, B
   - Order: White (U), Red (R), Green (F), Yellow (D), Orange (L), Blue (B)

### Method 3: Jupyter Notebook

1. **Open the notebook**:
   ```bash
   jupyter notebook rubix_cube_solver.ipynb
   ```

2. **Run cells** to solve interactively

## 🧠 Solver Methods

### 1. Custom Layer-by-Layer Solver (`rubik_solver_without_kociemba.py`)

**Algorithm**: Implements the classic layer-by-layer method:
1. **White Cross**: Solve the white cross on the UP face
2. **White Corners**: Complete the white layer
3. **Middle Layer**: Solve middle layer edges
4. **Yellow Cross**: Form yellow cross on DOWN face
5. **Yellow Corners Position**: Position yellow corners correctly
6. **Yellow Corners Orientation**: Orient yellow corners to complete

**Usage**:
```python
from rubik_solver_without_kociemba import RubiksCubeSolver

# Define cube state
cube_state = {
    'U': list("OBYBWRORB"),
    'R': list("RWORROGBW"),
    'F': list("BYWWGGOWY"),
    'D': list("GBRGYRBGG"),
    'L': list("WOWYOORWY"),
    'B': list("BYGGBORYY")
}

# Solve
solver = RubiksCubeSolver(cube_state)
solution = solver.solve()
print("Solution:", solution)
```

### 2. Kociemba Solver (`rubik_solver_with_kociemba.py`)

**Algorithm**: Uses the Kociemba library for optimal solutions (usually 20 moves or fewer)

**Features**:
- Optimal move sequences
- Fast solving
- Automatic face detection from center colors
- Input validation

**Usage**:
```bash
python rubik_solver_with_kociemba.py
```

### 3. Camera Scanner (`camera.py`)

**Features**:
- Real-time color detection using HSV color space
- Automatic grid overlay for face alignment
- Visual feedback during scanning
- Support for all 6 cube colors

**Color Detection**:
- **White (W)**: Low saturation, high value
- **Yellow (Y)**: Hue 20-35
- **Red (R)**: Hue < 8 or > 170, high saturation
- **Orange (O)**: Hue 8-20
- **Green (G)**: Hue 35-85
- **Blue (B)**: Hue 85-130

## 📊 Input Format

### Cube State Representation

Each face is represented as a 3x3 grid flattened into a 9-character string:

```
Face Layout (row by row, left to right):
[0][1][2]
[3][4][5]  → "012345678"
[6][7][8]
```

### Color Codes

- **W**: White
- **R**: Red  
- **G**: Green
- **Y**: Yellow
- **O**: Orange
- **B**: Blue

### Face Order

Standard cube notation:
- **U**: Up (White)
- **D**: Down (Yellow)
- **F**: Front (Green)
- **B**: Back (Blue)
- **L**: Left (Orange)
- **R**: Right (Red)

## 🔧 Technical Details

### Dependencies

- **opencv-python**: Camera capture and image processing
- **kociemba**: Optimal cube solving algorithm
- **numpy**: Numerical operations for image processing

### Color Detection Algorithm

The camera scanner uses HSV (Hue, Saturation, Value) color space for robust color detection:

```python
def get_color_label(h, s, v):
    if v < 50: return 'k'      # Black (too dark)
    if s < 60: return 'w'      # White (low saturation)
    if (h < 8 or h > 170) and s > 80: return 'r'  # Red
    elif 8 <= h < 20: return 'o'                   # Orange
    elif 20 <= h < 35: return 'y'                  # Yellow
    elif 35 <= h < 85: return 'g'                  # Green
    elif 85 <= h < 130: return 'b'                 # Blue
    else: return 'u'                               # Unknown
```

### Move Notation

Standard Rubik's cube notation:
- **F**: Front face clockwise
- **F'**: Front face counter-clockwise
- **F2**: Front face 180 degrees
- **U, D, L, R, B**: Same pattern for other faces

## 🎯 Example Usage

### Complete Workflow

1. **Scan your cube**:
   ```bash
   python camera.py
   ```

2. **Use the output** with the solver:
   ```python
   # Example output from camera.py
   cube_faces = {
       'w': ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
       'y': ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
       # ... other faces
   }
   ```

3. **Convert to solver format** and solve

## 🐛 Troubleshooting

### Common Issues

1. **Camera not detected**:
   - Ensure webcam is connected and not in use by other applications
   - Try different camera indices (0, 1, 2...)

2. **Color detection errors**:
   - Ensure good lighting conditions
   - Avoid shadows and reflections
   - Hold cube steady during scanning

3. **Invalid cube state**:
   - Each color must appear exactly 9 times
   - Check for typos in manual input
   - Ensure cube is physically possible

4. **Kociemba errors**:
   - Cube state must be solvable
   - Check color counts and face relationships

### Validation

The solvers include comprehensive validation:
- Color count verification (9 of each color)
- Face relationship validation
- Solvability checking

## 🤝 Contributing

Feel free to contribute improvements:
- Enhanced color detection algorithms
- Additional solving methods
- Better user interface
- Performance optimizations


## 🙏 Acknowledgments

- **Kociemba library** for optimal solving algorithms
- **OpenCV** for computer vision capabilities
- **Rubik's cube community** for solving methodologies

---

**Happy solving! 🎉** 
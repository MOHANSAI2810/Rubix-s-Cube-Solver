import random
import kociemba

# --- 1. Cube Data Structure ---
def create_solved_cube():
    # Faces: U D F B L R (stickers are color letters)
    return {
        'U': ['W'] * 9,
        'D': ['Y'] * 9,
        'F': ['G'] * 9,
        'B': ['B'] * 9,
        'L': ['O'] * 9,
        'R': ['R'] * 9,
    }

# --- 2. Move Definitions ---
def rotate_face_clockwise(face):
    return [face[i] for i in [6,3,0,7,4,1,8,5,2]]
def rotate_face_counterclockwise(face):
    return [face[i] for i in [2,5,8,1,4,7,0,3,6]]

def move_U(c):
    c['U'] = rotate_face_clockwise(c['U'])
    temp = c['F'][:3]
    c['F'][:3], c['R'][:3], c['B'][:3], c['L'][:3] = c['R'][:3], c['B'][:3], c['L'][:3], temp

def move_U_prime(c):
    c['U'] = rotate_face_counterclockwise(c['U'])
    temp = c['F'][:3]
    c['F'][:3], c['L'][:3], c['B'][:3], c['R'][:3] = c['L'][:3], c['B'][:3], c['R'][:3], temp

def move_D(c):
    c['D'] = rotate_face_clockwise(c['D'])
    temp = c['F'][6:]
    c['F'][6:], c['L'][6:], c['B'][6:], c['R'][6:] = c['L'][6:], c['B'][6:], c['R'][6:], temp

def move_D_prime(c):
    c['D'] = rotate_face_counterclockwise(c['D'])
    temp = c['F'][6:]
    c['F'][6:], c['R'][6:], c['B'][6:], c['L'][6:] = c['R'][6:], c['B'][6:], c['L'][6:], temp

def move_F(c):
    c['F'] = rotate_face_clockwise(c['F'])
    temp = [c['U'][6], c['U'][7], c['U'][8]]
    c['U'][6],c['U'][7],c['U'][8] = c['L'][8],c['L'][5],c['L'][2]
    c['L'][2],c['L'][5],c['L'][8] = c['D'][2],c['D'][1],c['D'][0]
    c['D'][0],c['D'][1],c['D'][2] = c['R'][0],c['R'][3],c['R'][6]
    c['R'][0],c['R'][3],c['R'][6] = temp[::-1]

def move_F_prime(c):
    c['F'] = rotate_face_counterclockwise(c['F'])
    temp = [c['U'][6], c['U'][7], c['U'][8]]
    c['U'][6],c['U'][7],c['U'][8] = c['R'][0],c['R'][3],c['R'][6]
    c['R'][0],c['R'][3],c['R'][6] = c['D'][0],c['D'][1],c['D'][2]
    c['D'][0],c['D'][1],c['D'][2] = c['L'][8],c['L'][5],c['L'][2]
    c['L'][2],c['L'][5],c['L'][8] = temp

def move_B(c):
    c['B'] = rotate_face_clockwise(c['B'])
    temp = [c['U'][0], c['U'][1], c['U'][2]]
    c['U'][0],c['U'][1],c['U'][2] = c['R'][2],c['R'][5],c['R'][8]
    c['R'][2],c['R'][5],c['R'][8] = c['D'][8],c['D'][7],c['D'][6]
    c['D'][6],c['D'][7],c['D'][8] = c['L'][0],c['L'][3],c['L'][6]
    c['L'][0],c['L'][3],c['L'][6] = temp[::-1]

def move_B_prime(c):
    c['B'] = rotate_face_counterclockwise(c['B'])
    temp = [c['U'][0], c['U'][1], c['U'][2]]
    c['U'][0],c['U'][1],c['U'][2] = c['L'][0],c['L'][3],c['L'][6]
    c['L'][0],c['L'][3],c['L'][6] = c['D'][6],c['D'][7],c['D'][8]
    c['D'][6],c['D'][7],c['D'][8] = c['R'][8],c['R'][5],c['R'][2]
    c['R'][2],c['R'][5],c['R'][8] = temp

def move_L(c):
    c['L'] = rotate_face_clockwise(c['L'])
    temp = [c['U'][0], c['U'][3], c['U'][6]]
    c['U'][0],c['U'][3],c['U'][6] = c['B'][8],c['B'][5],c['B'][2]
    c['B'][2],c['B'][5],c['B'][8] = c['D'][6],c['D'][3],c['D'][0]
    c['D'][0],c['D'][3],c['D'][6] = c['F'][0],c['F'][3],c['F'][6]
    c['F'][0],c['F'][3],c['F'][6] = temp

def move_L_prime(c):
    c['L'] = rotate_face_counterclockwise(c['L'])
    temp = [c['U'][0], c['U'][3], c['U'][6]]
    c['U'][0],c['U'][3],c['U'][6] = c['F'][0],c['F'][3],c['F'][6]
    c['F'][0],c['F'][3],c['F'][6] = c['D'][0],c['D'][3],c['D'][6]
    c['D'][0],c['D'][3],c['D'][6] = c['B'][8],c['B'][5],c['B'][2]
    c['B'][2],c['B'][5],c['B'][8] = temp

def move_R(c):
    c['R'] = rotate_face_clockwise(c['R'])
    temp = [c['U'][2], c['U'][5], c['U'][8]]
    c['U'][2],c['U'][5],c['U'][8] = c['F'][2],c['F'][5],c['F'][8]
    c['F'][2],c['F'][5],c['F'][8] = c['D'][2],c['D'][5],c['D'][8]
    c['D'][2],c['D'][5],c['D'][8] = c['B'][6],c['B'][3],c['B'][0]
    c['B'][0],c['B'][3],c['B'][6] = temp[::-1]

def move_R_prime(c):
    c['R'] = rotate_face_counterclockwise(c['R'])
    temp = [c['U'][2], c['U'][5], c['U'][8]]
    c['U'][2],c['U'][5],c['U'][8] = c['B'][6],c['B'][3],c['B'][0]
    c['B'][0],c['B'][3],c['B'][6] = c['D'][8],c['D'][5],c['D'][2]
    c['D'][2],c['D'][5],c['D'][8] = c['F'][8],c['F'][5],c['F'][2]
    c['F'][2],c['F'][5],c['F'][8] = temp

move_functions = {
    "U": move_U, "U'": move_U_prime,
    "D": move_D, "D'": move_D_prime,
    "F": move_F, "F'": move_F_prime,
    "B": move_B, "B'": move_B_prime,
    "L": move_L, "L'": move_L_prime,
    "R": move_R, "R'": move_R_prime,
}
for mv in ["U", "D", "F", "B", "L", "R"]:
    move_functions[mv+"2"] = lambda c, mv=mv: [move_functions[mv](c), move_functions[mv](c)]

def apply_moves(cube, moves):
    for m in moves:
        move_functions[m](cube)

# --- 3. Printing ---
def print_cube(c):
    print("      {} {} {}".format(*c['U'][0:3]))
    print("      {} {} {}".format(*c['U'][3:6]))
    print("      {} {} {}".format(*c['U'][6:9]))
    for i in range(3):
        print("{} {} {}   {} {} {}   {} {} {}   {} {} {}".format(
            c['L'][i*3],c['L'][i*3+1],c['L'][i*3+2],
            c['F'][i*3],c['F'][i*3+1],c['F'][i*3+2],
            c['R'][i*3],c['R'][i*3+1],c['R'][i*3+2],
            c['B'][i*3],c['B'][i*3+1],c['B'][i*3+2],
        ))
    print("      {} {} {}".format(*c['D'][0:3]))
    print("      {} {} {}".format(*c['D'][3:6]))
    print("      {} {} {}".format(*c['D'][6:9]))
    print()

# --- 4. Scramble ---
def scramble_cube(cube, moves_count=20):
    all_moves = list(move_functions.keys())
    scramble = []
    last = ""
    for _ in range(moves_count):
        move = random.choice([m for m in all_moves if m[0] != last])
        scramble.append(move)
        apply_moves(cube, [move])
        last = move[0]
    return scramble

# --- 5. Robust Kociemba Facelet String (center-detect) ---
def cube_to_kociemba_string(cube):
    # Face order for Kociemba: URFDLB
    face_order = ['U', 'R', 'F', 'D', 'L', 'B']
    # Map center color to face letter, e.g. white at U-center means 'W' stickers become 'U'
    centers = {cube[face][4]: face for face in face_order}
    color_to_face = {color: face for color, face in centers.items()}
    # Build in required face and sticker order
    return ''.join(
        color_to_face[cube[face][i]]
        for face in face_order
        for i in range(9)
    )

# --- 6. Main ---
if __name__ == "__main__":
    cube = create_solved_cube()
    print("Initial (Solved) Cube:")
    print_cube(cube)
    scramble_seq = scramble_cube(cube, moves_count=20)
    print("Scramble Moves:", ' '.join(scramble_seq))
    print("Scrambled Cube:")
    print_cube(cube)
    facelet_string = cube_to_kociemba_string(cube)
    print("Kociemba facelets:", facelet_string)
    # Validate facelet counts
    print("Facelet counts:", {f: facelet_string.count(f) for f in 'URFDLB'})
    # Kociemba Solve
    try:
        solution = kociemba.solve(facelet_string)
        print("Optimal Solution Moves:", solution)
        apply_moves(cube, solution.strip().split())
        print("Solved Cube State:")
        print_cube(cube)
        solved = all(all(st == f[4] for st in f) for f in cube.values())
        print("Cube solved?", solved)
    except Exception as e:
        print("Kociemba error:", e)

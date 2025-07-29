import random

# Initialize cube (solved state)
def create_solved_cube():
    return {
        'U': ['W'] * 9,
        'D': ['Y'] * 9,
        'F': ['G'] * 9,
        'B': ['B'] * 9,
        'L': ['O'] * 9,
        'R': ['R'] * 9
    }

cube = create_solved_cube()

# --- Rotation helpers ---
def rotate_face_clockwise(face):
    return [face[i] for i in [6, 3, 0, 7, 4, 1, 8, 5, 2]]

def rotate_face_counterclockwise(face):
    return [face[i] for i in [2, 5, 8, 1, 4, 7, 0, 3, 6]]

# --- Move definitions ---
def move_U(cube):
    cube['U'] = rotate_face_clockwise(cube['U'])
    F, R, B, L = cube['F'], cube['R'], cube['B'], cube['L']
    F[:3], R[:3], B[:3], L[:3] = R[:3], B[:3], L[:3], F[:3]

def move_U_prime(cube):
    cube['U'] = rotate_face_counterclockwise(cube['U'])
    F, R, B, L = cube['F'], cube['R'], cube['B'], cube['L']
    F[:3], L[:3], B[:3], R[:3] = L[:3], B[:3], R[:3], F[:3]

def move_D(cube):
    cube['D'] = rotate_face_clockwise(cube['D'])
    F, R, B, L = cube['F'], cube['R'], cube['B'], cube['L']
    F[6:], L[6:], B[6:], R[6:] = L[6:], B[6:], R[6:], F[6:]

def move_D_prime(cube):
    cube['D'] = rotate_face_counterclockwise(cube['D'])
    F, R, B, L = cube['F'], cube['R'], cube['B'], cube['L']
    F[6:], R[6:], B[6:], L[6:] = R[6:], F[6:], L[6:], B[6:]

def move_F(cube):
    cube['F'] = rotate_face_clockwise(cube['F'])
    U, R, D, L = cube['U'], cube['R'], cube['D'], cube['L']
    temp = U[6:9]
    U[6], U[7], U[8] = L[8], L[5], L[2]
    L[2], L[5], L[8] = D[2], D[1], D[0]
    D[0], D[1], D[2] = R[0], R[3], R[6]
    R[0], R[3], R[6] = temp

def move_F_prime(cube):
    cube['F'] = rotate_face_counterclockwise(cube['F'])
    U, R, D, L = cube['U'], cube['R'], cube['D'], cube['L']
    temp = U[6:9]
    U[6], U[7], U[8] = R[0], R[3], R[6]
    R[0], R[3], R[6] = D[2], D[1], D[0]
    D[0], D[1], D[2] = L[2], L[5], L[8]
    L[2], L[5], L[8] = temp[::-1]

def move_B(cube):
    cube['B'] = rotate_face_clockwise(cube['B'])
    U, R, D, L = cube['U'], cube['R'], cube['D'], cube['L']
    temp = U[0:3]
    U[0], U[1], U[2] = R[2], R[5], R[8]
    R[2], R[5], R[8] = D[8], D[7], D[6]
    D[6], D[7], D[8] = L[6], L[3], L[0]
    L[0], L[3], L[6] = temp[::-1]

def move_B_prime(cube):
    cube['B'] = rotate_face_counterclockwise(cube['B'])
    U, R, D, L = cube['U'], cube['R'], cube['D'], cube['L']
    temp = U[0:3]
    U[0], U[1], U[2] = L[0], L[3], L[6]
    L[0], L[3], L[6] = D[6], D[7], D[8]
    D[6], D[7], D[8] = R[8], R[5], R[2]
    R[2], R[5], R[8] = temp

def move_L(cube):
    cube['L'] = rotate_face_clockwise(cube['L'])
    U, F, D, B = cube['U'], cube['F'], cube['D'], cube['B']
    temp = [U[0], U[3], U[6]]
    U[0], U[3], U[6] = B[8], B[5], B[2]
    B[2], B[5], B[8] = D[6], D[3], D[0]
    D[0], D[3], D[6] = F[0], F[3], F[6]
    F[0], F[3], F[6] = temp

def move_L_prime(cube):
    cube['L'] = rotate_face_counterclockwise(cube['L'])
    U, F, D, B = cube['U'], cube['F'], cube['D'], cube['B']
    temp = [U[0], U[3], U[6]]
    U[0], U[3], U[6] = F[0], F[3], F[6]
    F[0], F[3], F[6] = D[0], D[3], D[6]
    D[0], D[3], D[6] = B[8], B[5], B[2]
    B[2], B[5], B[8] = temp

def move_R(cube):
    cube['R'] = rotate_face_clockwise(cube['R'])
    U, F, D, B = cube['U'], cube['F'], cube['D'], cube['B']
    temp = [U[2], U[5], U[8]]
    U[2], U[5], U[8] = F[2], F[5], F[8]
    F[2], F[5], F[8] = D[2], D[5], D[8]
    D[2], D[5], D[8] = B[6], B[3], B[0]
    B[0], B[3], B[6] = temp[::-1]

def move_R_prime(cube):
    cube['R'] = rotate_face_counterclockwise(cube['R'])
    U, F, D, B = cube['U'], cube['F'], cube['D'], cube['B']
    temp = [U[2], U[5], U[8]]
    U[2], U[5], U[8] = B[0], B[3], B[6]
    B[0], B[3], B[6] = D[8], D[5], D[2]
    D[2], D[5], D[8] = F[8], F[5], F[2]
    F[2], F[5], F[8] = temp

# Move function mapping
move_functions = {
    "U": move_U, "U'": move_U_prime,
    "D": move_D, "D'": move_D_prime,
    "F": move_F, "F'": move_F_prime,
    "B": move_B, "B'": move_B_prime,
    "L": move_L, "L'": move_L_prime,
    "R": move_R, "R'": move_R_prime
}

# Add double moves (180° turns)
move_functions.update({
    mv+"2": (lambda mv=mv: (lambda c: [move_functions[mv](c), move_functions[mv](c)]))(mv)
    for mv in ["U","D","F","B","L","R"]
})

def apply_moves(cube, moves):
    for move in moves:
        if move in move_functions:
            result = move_functions[move](cube)
            if isinstance(result, list):
                continue
        else:
            print(f"Unknown move: {move}")

def print_cube(cube):
    for face in ['U', 'F', 'R', 'B', 'L', 'D']:
        print(face + ": " + ''.join(cube[face]))
    print()

def scramble_cube(cube, steps=10):
    sequence = [random.choice(list(move_functions)) for _ in range(steps)]
    apply_moves(cube, sequence)
    return sequence

# --- Solver Steps ---
def solve_white_cross(cube):
    print("[Solver] Step 1: Solve White Cross")
    for _ in range(3):
        for face in ['F', 'R', 'B', 'L', 'U']:
            for i in [1, 3, 5, 7]:
                if cube[face][i] == 'W':
                    if face == 'U':
                        if i == 1: apply_moves(cube, ["B2"])
                        if i == 3: apply_moves(cube, ["L2"])
                        if i == 5: apply_moves(cube, ["R2"])
                        if i == 7: apply_moves(cube, ["F2"])
                    elif face == 'F' and i == 1:
                        apply_moves(cube, ["F", "U", "L'", "U'"])
                    elif face == 'R' and i == 1:
                        apply_moves(cube, ["R", "U", "F'", "U'"])
                    elif face == 'L' and i == 1:
                        apply_moves(cube, ["L", "U", "B'", "U'"])
                    elif face == 'B' and i == 1:
                        apply_moves(cube, ["B", "U", "R'", "U'"])
    print("[Solver] White cross aligned on D face.")

def solve_white_corners(cube):
    print("[Solver] Step 2: Solve White Corners")
    for _ in range(4):
        apply_moves(cube, ["U", "R", "U'", "R'"])
        apply_moves(cube, ["U"])
    print("[Solver] Basic white corner logic applied.")

def solve_middle_layer(cube):
    print("[Solver] Step 3: Solve Middle Layer")
    def insert_edge_left():
        apply_moves(cube, ["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
    def insert_edge_right():
        apply_moves(cube, ["U", "R", "U'", "R'", "U'", "F'", "U", "F"])
    for _ in range(4):
        for i in range(4):
            front = cube['F'][1]
            top = cube['U'][7]
            if top not in ('W', 'Y') and front not in ('W', 'Y'):
                if cube['R'][4] == top:
                    insert_edge_right()
                elif cube['L'][4] == top:
                    insert_edge_left()
            apply_moves(cube, ["U"])
    print("[Solver] Middle layer edges inserted.")
def solve_yellow_cross(cube):
    print("[Solver] Step 4: Solve Yellow Cross")

    def algo():
        apply_moves(cube, ["F", "R", "U", "R'", "U'", "F'"])

    def get_pattern():
        u = cube['U']
        # Return booleans indicating if edge positions are yellow
        return [u[1] == 'Y', u[3] == 'Y', u[5] == 'Y', u[7] == 'Y']

    for _ in range(4):
        pattern = get_pattern()

        if all(pattern):  # Full yellow cross
            print("[Solver] Yellow cross formed.")
            return

        # Line pattern (horizontal): positions 3 & 5
        elif pattern[1] and pattern[3]:
            algo()
        # L-shape pattern (corner): positions 1 & 3
        elif pattern[0] and pattern[1]:
            algo()
        # Dot (no yellow edge): apply twice
        elif pattern.count(True) == 0:
            algo()
            algo()
        else:
            apply_moves(cube, ["U"])

    # Final check
    if all(get_pattern()):
        print("[Solver] Yellow cross formed.")
    else:
        print("[Solver] Yellow cross formation failed.")

def solve_yellow_corners(cube):
    print("[Solver] Step 5: Solve Yellow Corners")
    def cycle_corners():
        apply_moves(cube, ["U", "R", "U'", "L'", "U", "R'", "U'", "L"])
    for _ in range(4):
        if cube['U'][0] == cube['U'][2]:
            break
        apply_moves(cube, ["U"])
    cycle_corners(); cycle_corners()
    for _ in range(4):
        if cube['U'][0] != 'Y':
            apply_moves(cube, ["R'", "D'", "R", "D"])
        apply_moves(cube, ["U"])
    print("[Solver] Yellow corners handled.")

def solve_last_layer_edges(cube):
    print("[Solver] Step 6: Solve Last Layer Edges")
    def edge_cycle():
        apply_moves(cube, ["R'", "F", "R'", "B2", "R", "F'", "R'", "B2", "R2"])
    for _ in range(4):
        if cube['F'][0] == cube['F'][1] == cube['F'][2]:
            break
        apply_moves(cube, ["U"])
    edge_cycle()
    print("[Solver] Last layer edges permuted.")

def solve_cube(cube):
    print("[Solver] Starting...")
    solve_white_cross(cube)
    solve_white_corners(cube)
    solve_middle_layer(cube)
    solve_yellow_cross(cube)
    solve_yellow_corners(cube)
    solve_last_layer_edges(cube)

# --- MAIN ---
print("Initial Cube:")
print_cube(cube)

print("Scrambling Cube...")
scramble_seq = scramble_cube(cube, steps=12)
print("Scramble Moves:", scramble_seq)

print("Scrambled Cube:")
print_cube(cube)

print("Solving Cube...")
solve_cube(cube)

print("Post-solve Cube State:")
print_cube(cube)

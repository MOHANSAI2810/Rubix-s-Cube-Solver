from collections import deque

class RubiksCubeSolver:
    def __init__(self, cube_state):
        # Initialize cube state
        self.cube = {
            'U': [list(cube_state['U'][i:i+3]) for i in range(0, 9, 3)],
            'D': [list(cube_state['D'][i:i+3]) for i in range(0, 9, 3)],
            'F': [list(cube_state['F'][i:i+3]) for i in range(0, 9, 3)],
            'B': [list(cube_state['B'][i:i+3]) for i in range(0, 9, 3)],
            'L': [list(cube_state['L'][i:i+3]) for i in range(0, 9, 3)],
            'R': [list(cube_state['R'][i:i+3]) for i in range(0, 9, 3)]
        }
        self.solution = []
        
        # Center colors for reference
        self.center_colors = {
            'U': self.cube['U'][1][1],
            'D': self.cube['D'][1][1],
            'F': self.cube['F'][1][1],
            'B': self.cube['B'][1][1],
            'L': self.cube['L'][1][1],
            'R': self.cube['R'][1][1]
        }

    def rotate_face(self, face, clockwise=True):
        """Rotate a face 90 degrees clockwise/counter-clockwise"""
        f = self.cube[face]
        if clockwise:
            # Transpose and reverse each row
            f[:] = [list(row) for row in zip(*f[::-1])]
        else:
            # Reverse each row and transpose
            f[:] = [list(row) for row in zip(*f)][::-1]

    def move(self, notation):
        """Perform a cube move and track solution"""
        if not notation:
            return
            
        face = notation[0]
        clockwise = not ("'" in notation)
        double = ("2" in notation)
        
        if double:
            self.move(face)
            self.move(face)
            return
            
        self.rotate_face(face, clockwise)
        
        # Handle edge pieces
        if face == 'U':
            self.cube['F'][0], self.cube['L'][0], self.cube['B'][0], self.cube['R'][0] = (
                self.cube['L'][0] if clockwise else self.cube['R'][0],
                self.cube['B'][0] if clockwise else self.cube['F'][0],
                self.cube['R'][0] if clockwise else self.cube['L'][0],
                self.cube['F'][0] if clockwise else self.cube['B'][0]
            )
        elif face == 'D':
            self.cube['F'][2], self.cube['R'][2], self.cube['B'][2], self.cube['L'][2] = (
                self.cube['R'][2] if clockwise else self.cube['L'][2],
                self.cube['B'][2] if clockwise else self.cube['F'][2],
                self.cube['L'][2] if clockwise else self.cube['R'][2],
                self.cube['F'][2] if clockwise else self.cube['B'][2]
            )
        elif face == 'F':
            # Rotate front face and adjacent edges
            temp = [row[2] for row in self.cube['U']]
            if clockwise:
                for i in range(3):
                    self.cube['U'][i][2] = self.cube['L'][2][2-i]
                for i in range(3):
                    self.cube['L'][2][i] = self.cube['D'][i][0]
                for i in range(3):
                    self.cube['D'][i][0] = self.cube['R'][2][2-i]
                for i in range(3):
                    self.cube['R'][2][i] = temp[i]
            else:
                for i in range(3):
                    self.cube['U'][i][2] = self.cube['R'][2][i]
                for i in range(3):
                    self.cube['R'][2][i] = self.cube['D'][2-i][0]
                for i in range(3):
                    self.cube['D'][i][0] = self.cube['L'][2][i]
                for i in range(3):
                    self.cube['L'][2][i] = temp[2-i]
                    
        self.solution.append(notation)

    def find_edge(self, color1, color2):
        """Find position of an edge piece"""
        edges = [
            # Up edges
            (('U', 0, 1), ('B', 0, 1)),
            (('U', 1, 0), ('L', 0, 1)),
            (('U', 1, 2), ('R', 0, 1)),
            (('U', 2, 1), ('F', 0, 1)),
            # Middle edges
            (('F', 1, 0), ('L', 1, 2)),
            (('F', 1, 2), ('R', 1, 0)),
            (('B', 1, 0), ('R', 1, 2)),
            (('B', 1, 2), ('L', 1, 0)),
            # Down edges
            (('D', 0, 1), ('F', 2, 1)),
            (('D', 1, 0), ('L', 2, 1)),
            (('D', 1, 2), ('R', 2, 1)),
            (('D', 2, 1), ('B', 2, 1))
        ]
        
        for edge in edges:
            pos1, pos2 = edge
            c1 = self.cube[pos1[0]][pos1[1]][pos1[2]]
            c2 = self.cube[pos2[0]][pos2[1]][pos2[2]]
            if {c1, c2} == {color1, color2}:
                return edge
        return None

    def solve_white_cross(self):
        """Solve the white cross on top"""
        white = self.center_colors['U']
        
        # Solve each white edge
        edges = [
            (white, self.center_colors['F']),  # Front
            (white, self.center_colors['R']),  # Right
            (white, self.center_colors['B']),  # Back
            (white, self.center_colors['L'])   # Left
        ]
        
        for target in edges:
            edge = self.find_edge(*target)
            if not edge:
                continue
                
            pos1, pos2 = edge
            face1 = pos1[0]
            
            # If already in position
            if face1 == 'U' and self.cube[pos2[0]][pos2[1]][pos2[2]] == target[1]:
                continue
                
            # Bring to bottom layer
            if face1 != 'D':
                if face1 == 'U':
                    # Move to bottom
                    self.move(pos2[0] + "2")
                else:
                    # Middle layer edge
                    self.move(pos1[0] + ("'" if pos1[2] == 2 else ""))
                    self.move("U'")
                    self.move(pos1[0] + ("'" if pos1[2] != 2 else ""))
            
            # Now edge is on bottom
            edge = self.find_edge(*target)
            pos1, pos2 = edge
            face1 = pos1[0]
            
            # Rotate to match center
            while self.cube[pos2[0]][pos2[1]][pos2[2]] != target[1]:
                self.move("D")
                edge = self.find_edge(*target)
                pos1, pos2 = edge
                
            # Move to top
            self.move(pos2[0] + "2")

    def solve(self):
        """Main solve method"""
        self.solution = []
        self.solve_white_cross()
        return self.solution

# Test with your cube
default_cube_input = {
    'U': list("OBYBWRORB"),
    'R': list("RWORROGBW"),
    'F': list("BYWWGGOWY"),
    'D': list("GBRGYRBGG"),
    'L': list("WOWYOORWY"),
    'B': list("BYGGBORYY")
}

solver = RubiksCubeSolver(default_cube_input)
solution = solver.solve()
print(f"Solution: {solution}")
print(f"Total moves: {len(solution)}")
class RubiksCubeSolver:
    def __init__(self, cube_state):
        self.cube = {
            'U': [cube_state['U'][i:i+3] for i in range(0, 9, 3)],
            'D': [cube_state['D'][i:i+3] for i in range(0, 9, 3)],
            'F': [cube_state['F'][i:i+3] for i in range(0, 9, 3)],
            'B': [cube_state['B'][i:i+3] for i in range(0, 9, 3)],
            'L': [cube_state['L'][i:i+3] for i in range(0, 9, 3)],
            'R': [cube_state['R'][i:i+3] for i in range(0, 9, 3)]
        }
        self.solution = []
        self.color_map = {
            'U': self.cube['U'][1][1],  
            'D': self.cube['D'][1][1],   
            'F': self.cube['F'][1][1],   
            'B': self.cube['B'][1][1],   
            'L': self.cube['L'][1][1],   
            'R': self.cube['R'][1][1]    
        }

    def rotate_face(self, face, clockwise=True):
        f = self.cube[face]
        if clockwise:
            f[:] = [list(row) for row in zip(*f[::-1])]
        else:
            f[:] = [list(row) for row in zip(*f)][::-1]

    def move(self, notation):
        if len(notation) == 0:
            return
        face = notation[0]
        clockwise = True
        
        if len(notation) > 1:
            if notation[1] == "'":
                clockwise = False
            elif notation[1] == '2':
                self.move(notation[0])
                self.move(notation[0])
                return
        
        self.rotate_face(face, clockwise)
        if face == 'U':
            self.cube['F'][0], self.cube['R'][0], self.cube['B'][0], self.cube['L'][0] = (
                self.cube['R'][0] if clockwise else self.cube['L'][0],
                self.cube['B'][0] if clockwise else self.cube['F'][0],
                self.cube['L'][0] if clockwise else self.cube['R'][0],
                self.cube['F'][0] if clockwise else self.cube['B'][0]
            )
        elif face == 'D':
            self.cube['F'][2], self.cube['L'][2], self.cube['B'][2], self.cube['R'][2] = (
                self.cube['L'][2] if clockwise else self.cube['R'][2],
                self.cube['B'][2] if clockwise else self.cube['F'][2],
                self.cube['R'][2] if clockwise else self.cube['L'][2],
                self.cube['F'][2] if clockwise else self.cube['B'][2]
            )
        elif face == 'F':
            temp = [self.cube['U'][2][i] for i in range(3)]
            if clockwise:
                for i in range(3):
                    self.cube['U'][2][i] = self.cube['L'][2-i][2]
                for i in range(3):
                    self.cube['L'][i][2] = self.cube['D'][0][i]
                for i in range(3):
                    self.cube['D'][0][i] = self.cube['R'][2-i][0]
                for i in range(3):
                    self.cube['R'][i][0] = temp[i]
            else:
                for i in range(3):
                    self.cube['U'][2][i] = self.cube['R'][i][0]
                for i in range(3):
                    self.cube['R'][i][0] = self.cube['D'][0][2-i]
                for i in range(3):
                    self.cube['D'][0][i] = self.cube['L'][i][2]
                for i in range(3):
                    self.cube['L'][i][2] = temp[2-i]
        elif face == 'B':
            # Similar to F but with different edges
            temp = [self.cube['U'][0][i] for i in range(3)]
            if clockwise:
                for i in range(3):
                    self.cube['U'][0][i] = self.cube['R'][i][2]
                for i in range(3):
                    self.cube['R'][i][2] = self.cube['D'][2][2-i]
                for i in range(3):
                    self.cube['D'][2][i] = self.cube['L'][i][0]
                for i in range(3):
                    self.cube['L'][i][0] = temp[2-i]
            else:
                for i in range(3):
                    self.cube['U'][0][i] = self.cube['L'][2-i][0]
                for i in range(3):
                    self.cube['L'][i][0] = self.cube['D'][2][i]
                for i in range(3):
                    self.cube['D'][2][i] = self.cube['R'][2-i][2]
                for i in range(3):
                    self.cube['R'][i][2] = temp[i]
        elif face == 'L':
            # Left face rotation
            temp = [self.cube['U'][i][0] for i in range(3)]
            if clockwise:
                for i in range(3):
                    self.cube['U'][i][0] = self.cube['B'][2-i][2]
                for i in range(3):
                    self.cube['B'][i][2] = self.cube['D'][2-i][0]
                for i in range(3):
                    self.cube['D'][i][0] = self.cube['F'][i][0]
                for i in range(3):
                    self.cube['F'][i][0] = temp[i]
            else:
                for i in range(3):
                    self.cube['U'][i][0] = self.cube['F'][i][0]
                for i in range(3):
                    self.cube['F'][i][0] = self.cube['D'][i][0]
                for i in range(3):
                    self.cube['D'][i][0] = self.cube['B'][2-i][2]
                for i in range(3):
                    self.cube['B'][i][2] = temp[2-i]
        elif face == 'R':
            # Right face rotation
            temp = [self.cube['U'][i][2] for i in range(3)]
            if clockwise:
                for i in range(3):
                    self.cube['U'][i][2] = self.cube['F'][i][2]
                for i in range(3):
                    self.cube['F'][i][2] = self.cube['D'][i][2]
                for i in range(3):
                    self.cube['D'][i][2] = self.cube['B'][2-i][0]
                for i in range(3):
                    self.cube['B'][i][0] = temp[2-i]
            else:
                for i in range(3):
                    self.cube['U'][i][2] = self.cube['B'][2-i][0]
                for i in range(3):
                    self.cube['B'][i][0] = self.cube['D'][2-i][2]
                for i in range(3):
                    self.cube['D'][i][2] = self.cube['F'][i][2]
                for i in range(3):
                    self.cube['F'][i][2] = temp[i]
        
        self.solution.append(notation)

    def get_edge_position(self, color1, color2):
        """Find the position of an edge piece with given colors"""
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
            if (c1 == color1 and c2 == color2) or (c1 == color2 and c2 == color1):
                return edge
        return None

    def solve_white_cross(self):
        """Solve the white cross on the UP face"""
        white = self.color_map['U']
        
        # Solve each white edge
        edges = [
            (white, self.color_map['F']),  # Front
            (white, self.color_map['R']),   # Right
            (white, self.color_map['B']),   # Back
            (white, self.color_map['L'])    # Left
        ]
        
        for target_color in edges:
            edge_pos = self.get_edge_position(target_color[0], target_color[1])
            if not edge_pos:
                continue
                
            pos1, pos2 = edge_pos
            face1, row1, col1 = pos1
            face2, row2, col2 = pos2
            
            # If already in correct position and oriented
            if face1 == 'U' and face2 in ['F', 'R', 'B', 'L'] and self.cube[face2][row2][col2] == target_color[1]:
                continue
                
            # Bring the edge to the DOWN face
            if face1 == 'U':
                # Move to DOWN face
                if face2 == 'F':
                    self.move("F")
                    self.move("F")
                elif face2 == 'R':
                    self.move("R")
                    self.move("R")
                elif face2 == 'B':
                    self.move("B")
                    self.move("B")
                elif face2 == 'L':
                    self.move("L")
                    self.move("L")
            elif face1 != 'D':
                # Edge is in middle layer
                if face1 == 'F' and row1 == 1 and col1 == 0:  # FL edge
                    self.move("L'")
                    self.move("U'")
                    self.move("L")
                elif face1 == 'F' and row1 == 1 and col1 == 2:  # FR edge
                    self.move("R")
                    self.move("U")
                    self.move("R'")
                elif face1 == 'B' and row1 == 1 and col1 == 0:  # BR edge
                    self.move("R'")
                    self.move("U'")
                    self.move("R")
                elif face1 == 'B' and row1 == 1 and col1 == 2:  # BL edge
                    self.move("L")
                    self.move("U")
                    self.move("L'")
            
            # Now the edge should be on DOWN face
            edge_pos = self.get_edge_position(target_color[0], target_color[1])
            pos1, pos2 = edge_pos
            face1, row1, col1 = pos1
            face2, row2, col2 = pos2
            
            # Position the edge under its target position
            target_face = target_color[1]
            current_face = face2 if face1 == 'D' else face1
            
            while current_face != target_face:
                self.move("D")
                edge_pos = self.get_edge_position(target_color[0], target_color[1])
                pos1, pos2 = edge_pos
                current_face = face2 if face1 == 'D' else face1
            
            # Flip the edge into place
            if target_face == 'F':
                self.move("F")
                self.move("F")
            elif target_face == 'R':
                self.move("R")
                self.move("R")
            elif target_face == 'B':
                self.move("B")
                self.move("B")
            elif target_face == 'L':
                self.move("L")
                self.move("L")

    def solve_white_corners(self):
        """Solve the white corners to complete first layer"""
        white = self.color_map['U']
        
        # Find each white corner and solve it
        corners = [
            (white, self.color_map['F'], self.color_map['R']),  # FRU corner
            (white, self.color_map['R'], self.color_map['B']),  # RBU corner
            (white, self.color_map['B'], self.color_map['L']),  # BLU corner
            (white, self.color_map['L'], self.color_map['F'])   # LFU corner
        ]
        
        for corner in corners:
            # Find the corner position
            corner_pos = None
            # Check all possible corner positions
            possible_positions = [
                (('U', 0, 0), ('B', 0, 2), ('L', 0, 0)),
                (('U', 0, 2), ('B', 0, 0), ('R', 0, 2)),
                (('U', 2, 0), ('F', 0, 0), ('L', 0, 2)),
                (('U', 2, 2), ('F', 0, 2), ('R', 0, 0)),
                (('D', 0, 0), ('F', 2, 0), ('L', 2, 2)),
                (('D', 0, 2), ('F', 2, 2), ('R', 2, 0)),
                (('D', 2, 0), ('B', 2, 2), ('L', 2, 0)),
                (('D', 2, 2), ('B', 2, 0), ('R', 2, 2))
            ]
            
            for pos in possible_positions:
                colors = [self.cube[p[0]][p[1]][p[2]] for p in pos]
                if sorted(colors) == sorted(corner):
                    corner_pos = pos
                    break
            
            if not corner_pos:
                continue
                
            # If corner is already in place
            if corner_pos[0][0] == 'U':
                continue
                
            # Bring corner to DOWN layer
            if corner_pos[0][0] != 'D':
                # Corner is in middle layer - need to move it down
                # Find which face it's on
                if corner_pos[0][0] == 'F':
                    if corner_pos[1][0] == 'L':
                        # FL corner
                        self.move("L'")
                        self.move("D'")
                        self.move("L")
                    else:
                        # FR corner
                        self.move("R")
                        self.move("D")
                        self.move("R'")
                elif corner_pos[0][0] == 'B':
                    if corner_pos[1][0] == 'L':
                        # BL corner
                        self.move("L")
                        self.move("D")
                        self.move("L'")
                    else:
                        # BR corner
                        self.move("R'")
                        self.move("D'")
                        self.move("R")
            
            # Now corner should be on DOWN face
            # Rotate DOWN to position under target
            target_faces = [c for c in corner if c != white]
            target_face1, target_face2 = target_faces
            
            while True:
                # Check current position
                down_pos = None
                for pos in possible_positions:
                    if pos[0][0] == 'D':
                        colors = [self.cube[p[0]][p[1]][p[2]] for p in pos]
                        if sorted(colors) == sorted(corner):
                            down_pos = pos
                            break
                
                if not down_pos:
                    break
                    
                adj_faces = []
                for p in down_pos[1:]:
                    adj_faces.append(self.cube[p[0]][1][1])  # Center color
                
                if target_face1 in adj_faces and target_face2 in adj_faces:
                    break
                
                self.move("D")
            
            # Insert the corner
            # Determine which algorithm to use based on white position
            corner_colors = [self.cube[p[0]][p[1]][p[2]] for p in down_pos]
            white_pos = corner_colors.index(white)
            
            if white_pos == 0:  # White on DOWN
                if target_face1 == self.color_map['F']:
                    self.move("F")
                    self.move("D")
                    self.move("F'")
                    self.move("D'")
                else:
                    self.move("R'")
                    self.move("D'")
                    self.move("R")
                    self.move("D")
            elif white_pos == 1:  # White on one side
                if target_face1 == self.color_map['F']:
                    self.move("F")
                    self.move("D'")
                    self.move("F'")
                else:
                    self.move("R'")
                    self.move("D")
                    self.move("R")
            else:  # white_pos == 2, white on other side
                if target_face1 == self.color_map['F']:
                    self.move("D'")
                    self.move("F")
                    self.move("D")
                    self.move("F'")
                else:
                    self.move("D")
                    self.move("R'")
                    self.move("D'")
                    self.move("R")

    def solve_middle_layer(self):
        """Solve the middle layer edges"""
        # Find edges that belong in middle layer (no yellow/white)
        edges = [
            (self.color_map['F'], self.color_map['R']),
            (self.color_map['R'], self.color_map['B']),
            (self.color_map['B'], self.color_map['L']),
            (self.color_map['L'], self.color_map['F'])
        ]
        
        for edge in edges:
            edge_pos = self.get_edge_position(edge[0], edge[1])
            if not edge_pos:
                continue
                
            pos1, pos2 = edge_pos
            face1, row1, col1 = pos1
            face2, row2, col2 = pos2
            
            # If edge is already in middle layer and correct
            if (face1 in ['F', 'R', 'B', 'L'] and row1 == 1 and 
                face2 in ['F', 'R', 'B', 'L'] and row2 == 1):
                continue
                
            # Bring edge to DOWN face
            if face1 != 'D' and face2 != 'D':
                # Edge is in middle layer but wrong position - remove it
                if face1 == 'F' and row1 == 1 and col1 == 0:  # FL edge
                    self.move("L'")
                    self.move("U'")
                    self.move("L")
                    self.move("U")
                    self.move("F")
                    self.move("U")
                    self.move("F'")
                elif face1 == 'F' and row1 == 1 and col1 == 2:  # FR edge
                    self.move("R")
                    self.move("U")
                    self.move("R'")
                    self.move("U'")
                    self.move("F'")
                    self.move("U'")
                    self.move("F")
                elif face1 == 'B' and row1 == 1 and col1 == 0:  # BR edge
                    self.move("R'")
                    self.move("U'")
                    self.move("R")
                    self.move("U")
                    self.move("B")
                    self.move("U")
                    self.move("B'")
                elif face1 == 'B' and row1 == 1 and col1 == 2:  # BL edge
                    self.move("L")
                    self.move("U")
                    self.move("L'")
                    self.move("U'")
                    self.move("B'")
                    self.move("U'")
                    self.move("B")
            
            # Now edge should be on DOWN face
            edge_pos = self.get_edge_position(edge[0], edge[1])
            pos1, pos2 = edge_pos
            face1, row1, col1 = pos1
            face2, row2, col2 = pos2
            
            # Determine which color is on DOWN face
            if face1 == 'D':
                down_color = self.cube[face1][row1][col1]
                side_color = self.cube[face2][row2][col2]
            else:
                down_color = self.cube[face2][row2][col2]
                side_color = self.cube[face1][row1][col1]
            
            # Rotate DOWN to align with target face
            target_face = side_color
            current_face = face2 if face1 == 'D' else face1
            
            while current_face != target_face:
                self.move("D")
                edge_pos = self.get_edge_position(edge[0], edge[1])
                pos1, pos2 = edge_pos
                current_face = face2 if face1 == 'D' else face1
            
            # Insert the edge
            if down_color == self.color_map['F']:
                if target_face == self.color_map['R']:
                    self.move("D")
                    self.move("R")
                    self.move("D'")
                    self.move("R'")
                    self.move("D'")
                    self.move("F'")
                    self.move("D")
                    self.move("F")
                else:  # target_face == self.color_map['L']
                    self.move("D'")
                    self.move("L'")
                    self.move("D")
                    self.move("L")
                    self.move("D")
                    self.move("F")
                    self.move("D'")
                    self.move("F'")
            else:  # down_color == self.color_map['B']
                if target_face == self.color_map['R']:
                    self.move("D")
                    self.move("R")
                    self.move("D'")
                    self.move("R'")
                    self.move("D'")
                    self.move("B'")
                    self.move("D")
                    self.move("B")
                else:  # target_face == self.color_map['L']
                    self.move("D'")
                    self.move("L'")
                    self.move("D")
                    self.move("L")
                    self.move("D")
                    self.move("B")
                    self.move("D'")
                    self.move("B'")

    def solve_yellow_cross(self):
        """Form a yellow cross on the DOWN face"""
        yellow = self.color_map['D']
        
        # Count how many yellow edges are already on DOWN face
        down_edges = [
            self.cube['D'][0][1],
            self.cube['D'][1][0],
            self.cube['D'][1][2],
            self.cube['D'][2][1]
        ]
        yellow_count = down_edges.count(yellow)
        
        if yellow_count == 4:
            return  # Cross already solved
        
        if yellow_count == 0:
            # No edges - perform algorithm to get line or cross
            self.move("F")
            self.move("R")
            self.move("U")
            self.move("R'")
            self.move("U'")
            self.move("F'")
            # Check again
            down_edges = [
                self.cube['D'][0][1],
                self.cube['D'][1][0],
                self.cube['D'][1][2],
                self.cube['D'][2][1]
            ]
            yellow_count = down_edges.count(yellow)
        
        if yellow_count == 2:
            # Could be line or L shape
            # Check if opposite edges (line)
            if (down_edges[0] == yellow and down_edges[2] == yellow) or \
               (down_edges[1] == yellow and down_edges[3] == yellow):
                # Line - rotate to horizontal
                if down_edges[0] == yellow and down_edges[2] == yellow:
                    self.move("D")
                # Perform algorithm
                self.move("F")
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("F'")
            else:
                # L shape - rotate to bottom-left
                while not (down_edges[1] == yellow and down_edges[2] == yellow):
                    self.move("D")
                # Perform algorithm
                self.move("F")
                self.move("U")
                self.move("R")
                self.move("U'")
                self.move("R'")
                self.move("F'")

    def solve_yellow_corners_position(self):
        """Position the yellow corners (may not be oriented correctly yet)"""
        yellow = self.color_map['D']
        
        # Find which corners are already in correct position
        corners = [
            (('D', 0, 0), ('F', 2, 0), ('L', 2, 2)),
            (('D', 0, 2), ('F', 2, 2), ('R', 2, 0)),
            (('D', 2, 0), ('B', 2, 2), ('L', 2, 0)),
            (('D', 2, 2), ('B', 2, 0), ('R', 2, 2))
        ]
        
        correct_corners = 0
        for corner in corners:
            pos1, pos2, pos3 = corner
            color1 = self.cube[pos1[0]][pos1[1]][pos1[2]]
            color2 = self.cube[pos2[0]][pos2[1]][pos2[2]]
            color3 = self.cube[pos3[0]][pos3[1]][pos3[2]]
            
            adj_colors = [color2, color3]
            if color1 == yellow and self.color_map[pos2[0]] in adj_colors and self.color_map[pos3[0]] in adj_colors:
                correct_corners += 1
        
        if correct_corners == 4:
            return  # All corners correct
        
        # If no corners correct, perform algorithm to get at least one correct
        if correct_corners == 0:
            self.move("R'")
            self.move("F")
            self.move("R'")
            self.move("B")
            self.move("B")
            self.move("R")
            self.move("F'")
            self.move("R'")
            self.move("B")
            self.move("B")
            self.move("R")
            self.move("R")
            # Check again
            correct_corners = 0
            for corner in corners:
                pos1, pos2, pos3 = corner
                color1 = self.cube[pos1[0]][pos1[1]][pos1[2]]
                color2 = self.cube[pos2[0]][pos2[1]][pos2[2]]
                color3 = self.cube[pos3[0]][pos3[1]][pos3[2]]
                
                adj_colors = [color2, color3]
                if color1 == yellow and self.color_map[pos2[0]] in adj_colors and self.color_map[pos3[0]] in adj_colors:
                    correct_corners += 1
        
        # Rotate until correct corner is at DRF position
        while True:
            pos1, pos2, pos3 = corners[1]  # DRF corner
            color1 = self.cube[pos1[0]][pos1[1]][pos1[2]]
            color2 = self.cube[pos2[0]][pos2[1]][pos2[2]]
            color3 = self.cube[pos3[0]][pos3[1]][pos3[2]]
            
            adj_colors = [color2, color3]
            if color1 == yellow and self.color_map[pos2[0]] in adj_colors and self.color_map[pos3[0]] in adj_colors:
                break
            self.move("D")
        
        # Perform algorithm to position remaining corners
        self.move("R'")
        self.move("F")
        self.move("R'")
        self.move("B")
        self.move("B")
        self.move("R")
        self.move("F'")
        self.move("R'")
        self.move("B")
        self.move("B")
        self.move("R")
        self.move("R")

    def orient_yellow_corners(self):
        """Orient the yellow corners to complete the cube"""
        yellow = self.color_map['D']
        
        # Repeat until all corners are oriented
        while True:
            # Find a corner that needs to be rotated
            corner_pos = None
            corners = [
                (('D', 0, 0), ('F', 2, 0), ('L', 2, 2)),
                (('D', 0, 2), ('F', 2, 2), ('R', 2, 0)),
                (('D', 2, 0), ('B', 2, 2), ('L', 2, 0)),
                (('D', 2, 2), ('B', 2, 0), ('R', 2, 2))
            ]
            
            for corner in corners:
                if self.cube[corner[0][0]][corner[0][1]][corner[0][2]] != yellow:
                    corner_pos = corner
                    break
            
            if not corner_pos:
                break  # All corners oriented
            
            # Rotate corner to DRF position
            while corner != corners[1]:
                self.move("D")
                corners = [
                    (('D', 0, 0), ('F', 2, 0), ('L', 2, 2)),
                    (('D', 0, 2), ('F', 2, 2), ('R', 2, 0)),
                    (('D', 2, 0), ('B', 2, 2), ('L', 2, 0)),
                    (('D', 2, 2), ('B', 2, 0), ('R', 2, 2))
                ]
            
            # Perform algorithm to rotate corner
            self.move("R'")
            self.move("D'")
            self.move("R")
            self.move("D")
            # Repeat until this corner is oriented
            while self.cube[corner[0][0]][corner[0][1]][corner[0][2]] != yellow:
                self.move("R'")
                self.move("D'")
                self.move("R")
                self.move("D")

    def is_solved(self):
        """Check if the cube is solved"""
        for face, center in self.color_map.items():
            color = center
            for row in self.cube[face]:
                for cell in row:
                    if cell != color:
                        return False
        return True

    def solve(self):
        """Solve the cube using layer-by-layer method"""
        self.solution = []
        self.solve_white_cross()
        self.solve_white_corners()
        self.solve_middle_layer()
        self.solve_yellow_cross()
        self.solve_yellow_corners_position()
        self.orient_yellow_corners()
        return self.solution

# Example usage with your default cube input
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
print("Solution steps:", solution)
print("Is solved?", solver.is_solved())
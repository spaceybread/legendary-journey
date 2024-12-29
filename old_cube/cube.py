from collections import Counter as ctr

class Cube:
    def __init__(self, state = "AAAA BBBB CCCC DDDD EEEE FFFF"):
        self.clrs = set()
        self.cube = self.get_empty_cube()
        faces = state.split()
        
        for i, face in enumerate(faces):
            for j, square in enumerate(face):
                x, y = self.idx_to_cord(j)
                self.cube[i][x][y] = square

    def idx_to_cord(self, idx): return idx // 2, idx % 2
    
    def get_empty_cube(self):
        out = []
        for i in range(6):
            out.append([])
            out[-1].append([i, i])
            out[-1].append([i, i])
        return out
    
    def is_solved(self):
        for l in self.cube:
            if l[0] != l[1]:
                return False
        return True
    
    def display_cube(self):
        for l in self.cube: print(l)

cube = Cube()
cube.display_cube()
print()
        

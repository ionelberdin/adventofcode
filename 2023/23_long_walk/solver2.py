from queue import LifoQueue
from timeit import default_timer

class Tile(object):

    collection = {}

    def __init__(self, x:int, y:int, tile_type:str):
        self.x = x
        self.y = y
        self.type = tile_type
        self.neighbours = set()
        Tile.add(self)

    @classmethod
    def add(cls, tile):
        cls.collection[(tile.x, tile.y)] = tile

    @classmethod
    def get(cls, x:int, y:int):
        try:
            return cls.collection[(x, y)]
        except:
            return None

    @classmethod
    def find_neighbours(cls, tile=None):
        if (tile is None):
            for tile in cls.collection.values():
                cls.find_neighbours(tile)
            return

        x = tile.x
        y = tile.y
        if (tile.type in '.v'):
            neighbour = cls.get(x + 1, y)
            if neighbour is not None:
                tile.neighbours.add(neighbour)
        if (tile.type in '.^'):
            neighbour = cls.get(x - 1, y)
            if neighbour is not None:
                tile.neighbours.add(neighbour)
        if (tile.type in '.>'):
            neighbour = cls.get(x, y + 1)
            if neighbour is not None:
                tile.neighbours.add(neighbour)
        if (tile.type in '.<'):
            neighbour = cls.get(x, y - 1)
            if neighbour is not None:
                tile.neighbours.add(neighbour)

    @classmethod
    def init(cls):
        cls.collection = {}

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.type)

class Path(object):

    def __init__(self, tiles, last_visited_tile):
        self.tiles = set(tiles)
        self.last_visited_tile = last_visited_tile

    def get_next_tiles(self):
        return self.last_visited_tile.neighbours - self.tiles

    def __len__(self):
        return len(self.tiles) - 1

    def __repr__(self):
        output = ""
        for x, row in enumerate(self.map):
            for y, tile_type in enumerate(row):
                tile_type = 'x' if (tile_type == '.') else tile_type
                tile = Tile.get(x, y)
                output += tile_type if (tile not in self.tiles) else tile.type
            output += '\n'
        return output

    @classmethod
    def store_map(cls, map:str):
        cls.map = map

class Junction(object):
    collection = set()
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connectors = set()

class Solver(object):

    def __init__(self, filepath:str):
        Tile.init()
        self.map = []
        self.path = None
        self.paths = LifoQueue()
        self.result = 0
        with open(filepath, 'r') as f:
            x = 0
            while (input_line := f.readline().strip('\n\s\t')):
                self.map.append(input_line)
                self.process_input_line(input_line, x)
                x += 1
        Path.store_map(self.map)
        self.xmax = x - 1

    def process_input_line(self, input_line:str, x:int):
        for y, tile_type in enumerate(input_line):
            if (tile_type == '#'):
                continue
            Tile(x, y, tile_type)

    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2_alt()

    def solve_part_1(self):
        Tile.find_neighbours()

        start = list(filter(lambda tile: tile.x == 0, Tile.collection.values()))
        self.paths.put(Path(set(start), start[0]))

        while (not self.paths.empty()):
            path = self.paths.get()
            next_tiles = path.get_next_tiles()
            if (len(next_tiles) == 0):
                if (path.last_visited_tile.x == self.xmax):
                    if (len(path) > self.result):
                        self.path = path
                        self.result = len(path)
                continue
            for tile in next_tiles:
                self.paths.put(Path(path.tiles | set([tile]), tile))
        # print(self.path)
        return self.result

    def solve_part_2(self):
        tiles = filter(lambda tile: tile.type != '.', Tile.collection.values())
        for tile in tiles:
            tile.type = '.'

        Tile.find_neighbours()

        start = list(filter(lambda tile: tile.x == 0, Tile.collection.values()))
        self.paths.put(Path(set(start), start[0]))

        while (not self.paths.empty()):
            path = self.paths.get()
            next_tiles = path.get_next_tiles()
            if (len(next_tiles) == 0):
                if (path.last_visited_tile.x == self.xmax):
                    if (len(path) > self.result):
                        self.path = path
                        self.result = len(path)
                        print(self.paths.qsize(), self.result)
                continue
            for tile in next_tiles:
                self.paths.put(Path(path.tiles | set([tile]), tile))
        # print(self.path)
        return self.result

    def solve_part_2_alt(self):
        tiles = filter(lambda tile: tile.type != '.', Tile.collection.values())
        for tile in tiles:
            tile.type = '.'

        Tile.find_neighbours()
    
        tiles = Tile.collection.values()
        boundaries = filter(lambda tile: tile.x in (0, self.xmax) , tiles)
        start = next(filter(lambda tile: tile.x == 0, boundaries), None)
        end = next(filter(lambda tile: tile.x == self.xmax, boundaries), None)

        print("Start:", start)
        print("End:", end)

        multi_neighbour_tiles = set(filter(lambda tile: len(tile.neighbours) > 2, tiles))
        junctions = map(lambda tile: Junction(tile.x, tile.y), multi_neighbour_tiles)
        junctions = set(junctions)
        print("Number of junctions:", len(junctions))  # Only 34 for puzzle input!!!
        self.junctions = junctions

        connectors = int(sum(map(lambda tile: len(tile.neighbours), multi_neighbour_tiles)) / 2)
        print("Number of connectors", connectors)  # Only 59 of them!!!

        dead_ends = filter(lambda tile: len(tile.neighbours) < 2, tiles)
        dead_ends = set(dead_ends)
        print("Number of dead ends:", len(dead_ends))  # Surprisingly only Start and End...
        
        self.connect_junctions()

    def connect_junctions(self):
        pass


def solve(filepath:str, part:int):
    print("Solving part {} with:".format(part), filepath)
    start = default_timer()
    solver = Solver(filepath)
    result = solver.solve(part=part)
    duration = default_timer() - start
    print("Solved in {}s".format(duration))
    print("Result:", result)
    return result


if __name__ == '__main__':
    # assert(solve('test_01.txt', part=1) == 94)
    # assert(solve('puzzle_input.txt', part=1) == 2178)  # takes more than 5s
    # assert(solve('test_01.txt', part=2) == 154)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('puzzle_input.txt', part=2))

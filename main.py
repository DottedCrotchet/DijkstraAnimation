from manim import *
import numpy as np

# class Node:
# def __init__(self, coor):
# self.coor = coor

# class Edge:
# def __init__(self, n1, n2):
# self.coor = coor

DEFAULT_EDGE_COLOR = YELLOW_D
VISITED_EDGE_COLOR = RED

DEFAULT_NODE_COLOR = WHITE
VISITED_NODE_COLOR = BLUE_C


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.dots = []
        self.lines = []
        self.edge_distances = []

    def add_node(self, coor):
        self.nodes.append(coor)

    def add_edge(self, n1, n2):

        self.edges.append((n1, n2))
        self.edge_distances.append(
            np.sqrt(
                (self.nodes[n1][0] - self.nodes[n2][0]) ** 2
                + (self.nodes[n1][1] - self.nodes[n2][1]) ** 2
            )
        )

    def create_dots(self):
        for idx, node in enumerate(self.nodes):
            self.dots.append(
                LabeledDot("%d"%(idx+1))
            )
            self.dots[-1].move_to((node[0], node[1], 0))
            self.dots[-1].set_z_index(1000+idx)

    def animate_dots(self):
        result = []
        for dot in self.dots:
            result.append(Create(dot))

        return result

    def create_lines(self):
        for edge in self.edges:
            self.lines.append(
                Line(
                    (self.nodes[edge[0]][0], self.nodes[edge[0]][1], 0),
                    (self.nodes[edge[1]][0], self.nodes[edge[1]][1], 0),
                    color=DEFAULT_EDGE_COLOR
                )
            )

    def animate_lines(self):
        result = []
        for line in self.lines:
            result.append(Create(line))

        return result


g1 = Graph()
g1.add_node((0.0, 1.0))
g1.add_node((1.0, 0.0))
g1.add_node((1.6, 1.6))

g1.add_node((-1.0, -1.0))
g1.add_node((-1.0, -3.0))
g1.add_node((-3.0, -3.0))
g1.add_node((-3.0, -1.0))


g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(0, 2)

g1.add_edge(3, 4)
g1.add_edge(4, 5)
g1.add_edge(5, 6)
g1.add_edge(6, 3)

# print(new_object)



class Dijkstra1(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)

        g1.create_lines()
        g1.create_dots()
        dot_animations = g1.animate_dots()
        line_animations = g1.animate_lines()

        self.play(*dot_animations)
        self.play(*line_animations)

        for i in range(10):
            for line in g1.lines:
                line.set_color(VISITED_EDGE_COLOR)
                line.set_stroke_width(12)
                self.wait(0.1)
                line.set_color(DEFAULT_EDGE_COLOR)
                line.set_stroke_width(4)

        self.wait(3)
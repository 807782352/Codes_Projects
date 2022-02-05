#!/usr/bin/env python
"""
    Author: Ziyi Xu - 20705396 - University of Waterloo
    Notes:
        1. Because there were some bugs in Asg1, I rewrote the codes and fixed those bugs in this Assignment
        2. I combined other modules into this main file
"""

import math
import sys
import re
import copy


def regexFlag(line):
    # street_pattern = r"\"[a-zA-Z\s]+\"\s*"    # Accept white spaces
    street_pattern = r"\"([a-zA-Z]+(\s?[a-zA-Z]+)*)\""
    # coordinate_pattern = r"(\s+\(\s*[\+|\-]?\s*\d+\s*\,\s*[\+|\-]?\s*\d+\s*\)\s*)+"  #Accept + and - with white space
    number_pattern = r"(\-?[1-9]\d*|0)"
    # coordinate_pattern = r"(\s+\(\-?\d+\,\-?\d+\)){2,}"
    coordinate_pattern = r"(\s+\(" + number_pattern + r"\," + number_pattern + r"\)){2,}"
    pattern_add = r'^add\s+' + street_pattern + coordinate_pattern + r'\s*'
    pattern_mod = r'^mod\s+' + street_pattern + coordinate_pattern + r'\s*'
    pattern_rm = r'^rm\s+' + street_pattern + r'\s*'
    pattern_gg = r'^gg\s*'

    # print(coordinate_pattern)
    if re.fullmatch(pattern_add, line) is not None:
        isFind = True
    elif re.fullmatch(pattern_mod, line) is not None:
        isFind = True
    elif re.fullmatch(pattern_rm, line) is not None:
        isFind = True
    elif re.fullmatch(pattern_gg, line) is not None:
        isFind = True
    else:
        isFind = False
    return isFind


def parser(cmd):
    # print(cmd)

    # Split the line into different segments:
    # operator [street_name] [coordinates]
    segments = cmd.split('"')

    # get the operator (i.e. add, mod, rm, gg)
    operator = segments[0].split()[0]

    if operator == "add":
        street_name = get_street(segments)
        street_name = street_name.lower()
        coordinates = get_coordinates(segments)
        coordinates = coord_parse(coordinates)

    elif operator == "mod":
        street_name = get_street(segments)
        street_name = street_name.lower()
        coordinates = get_coordinates(segments)
        coordinates = coord_parse(coordinates)

    elif operator == "rm":
        street_name = get_street(segments)
        street_name = street_name.lower()
        coordinates = get_coordinates(segments)
        coordinates = coord_parse(coordinates)

    elif operator == 'gg':
        street_name = None
        coordinates = None

    else:
        print("Error")
        operator = None
        street_name = None
        coordinates = None
    return operator, street_name, coordinates


def coord_parse(coordinates):
    coord_temp = []  # temporary set for storing coordinate, preventing duplication
    # format the coordinates into a list, two entries represent a pair of coordinates
    for coordinate in coordinates:
        coordinate = coordinate.replace("(", " ")
        coordinate = coordinate.replace(")", " ")
        coordinate = coordinate.replace(",", " ")
        temp = coordinate.split()

        pt_x, pt_y = int(temp[0]), int(temp[1])
        pt = Point(pt_x, pt_y)
        coord_temp.append(pt)

    # print(coord_temp)
    if is_Coordinate_Same(coord_temp):
        print("Error Coordinates", coord_temp)
        print("Error: Cannot loop itself")
        return None
    return coord_temp


def get_street(segments):
    """
        get the street name
    :param segments: line segments
    :return: street name -> String
    """
    street_name = segments[1]
    return street_name


def get_coordinates(segments):
    """
        get the coordinates
    :param segments: line segments
    :return: coordinates -> list of String
    """
    coordinates = segments[2]
    coor_pattern = r'\(\s*[\+|\-]?\s*\d+\s*\,\s*[\+|\-]?\s*\d+\s*\)'
    coordinates = re.findall(coor_pattern, coordinates, re.S)
    return coordinates


def is_Coordinate_Same(coordinates):
    """
        Prevent Coordinate duplication
    """
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates), 1):
            # print(coordinates)
            # print(coordinates[j][0])
            if coordinates[i].x == coordinates[j].x:
                if coordinates[i].y == coordinates[j].y:
                    return True
    return False


def pp(x):
    """Returns a pretty-print string representation of a number.
       A float number is represented by an integer, if it is whole,
       and up to two decimal places if it isn't
    """
    if isinstance(x, float):
        if x.is_integer():
            return str(int(x))
        else:
            return "{0:.2f}".format(x)
    return str(x)


class Point(object):
    """A point in a two dimensional space"""

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '(' + pp(self.x) + ', ' + pp(self.y) + ')'

    def isEqual(self, pt):
        return pt.x == self.x and pt.y == self.y

    def isInList(self, pt_list):
        if pt_list is None:
            return False
        for pt in pt_list:
            if self.isEqual(pt):
                return True
        return False

    def indexOf(self, pt_list):
        if pt_list is None:
            return None
        for i in range(len(pt_list)):
            if self.isEqual(pt_list[i]):
                return i
        return None


class Line(object):
    """A line between two points"""

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def distance(self):
        dist = math.sqrt((self.src.x - self.dst.x) ** 2 + (self.src.y - self.dst.y) ** 2)
        return float(pp(dist))

    def is_vertical(self):
        if self.src.x == self.dst.x:
            return True
        return False

    def gradient(self):
        if not self.is_vertical():
            slope = (self.dst.y - self.src.y) / (self.dst.x - self.src.x)
            return slope
        else:
            return None

    def b(self, slope):
        if slope is not None:
            b = self.dst.y - slope * self.dst.x
            return b
        else:
            return None

    def __repr__(self):
        return '<' + str(self.src) + '-->' + str(self.dst) + '>'

    def isEqual(self, line):
        if (line.src.isEqual(self.src) and line.dst.isEqual(self.dst)) or \
                (line.src.isEqual(self.dst) and line.dst.isEqual(self.src)):
            return True
        else:
            return False

    def isInList(self, line_list):
        if line_list is None:
            return False
        for i in range(len(line_list)):
            if self.isEqual(line_list[i]):
                return True
        return False


def parallel(line1, line2):
    if line1.gradient != line2.gradient:
        return False
    return True


def intersect(line1, line2):
    """ Returns a point at which two lines intersect"""
    """ 
        I use cross product to check whether the points in one line 
        is in the different sides of the other line
    """

    x1, y1 = line1.src.x, line1.src.y
    x2, y2 = line1.dst.x, line1.dst.y

    x3, y3 = line2.src.x, line2.src.y
    x4, y4 = line2.dst.x, line2.dst.y

    if x1 == x3 and y1 == y3:
        return Point(x1, y1)
    if x1 == x4 and y1 == y4:
        return Point(x1, y1)
    if x2 == x3 and y2 == y3:
        return Point(x2, y2)
    if x2 == x4 and y2 == y4:
        return Point(x2, y2)

    if not parallel(line1, line2):
        # Check whether two line segments have intersections
        # Double triangle area enclosed by l1 and l2.src
        area1 = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)

        # Double triangle area enclosed by l1 and l2.dst
        area2 = (x4 - x1) * (y2 - y1) - (x2 - x1) * (y4 - y1)
        # if the signs of two area are the same, which means they are in the same side,
        # meaning no intersection

        if area1 * area2 >= 0:
            return None

        # Double triangle area enclosed by l1.src and l2
        area3 = (x2 - x3) * (y4 - y3) - (x4 - x3) * (y2 - y3)
        # Double triangle area enclosed by l1.dst and l2
        area4 = (x1 - x3) * (y4 - y3) - (x4 - x3) * (y1 - y3)

        if area3 * area4 >= 0:
            return None

        # Calculate the intersection coordinate
        xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
        xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        xcoor = xnum / xden

        ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        ycoor = ynum / yden

        return Point(xcoor, ycoor)
    else:
        return None


def sort_pts(pts_list):
    for i in range(len(pts_list) - 1):
        # Last i elements are already in place
        for j in range(0, len(pts_list) - i - 1):
            if pts_list[j].x > pts_list[j + 1].x:
                temp = pts_list[j]
                pts_list[j] = pts_list[j + 1]
                pts_list[j + 1] = temp
            elif pts_list[j].x == pts_list[j + 1].x:
                if pts_list[j].y > pts_list[j + 1].y:
                    temp = pts_list[j]
                    pts_list[j] = pts_list[j + 1]
                    pts_list[j + 1] = temp
            else:
                pass
    return pts_list


class Graph:
    def __init__(self, streets):
        self.final_edges = []
        self.final_pts = []
        self.lines_intersections = {}
        self.vertices = []
        self.pts_intersections = []
        self.streets_dict = streets
        self.streets_name = list(streets.keys())
        self.streets_num = len(self.streets_name)
        self.lines = [[] for i in range(self.streets_num)]

    def get_vertices(self):

        self.set_lines()
        for i in range(len(self.lines) - 1):
            for j in range(i + 1, len(self.lines), 1):
                for line1 in self.lines[i]:
                    for line2 in self.lines[j]:
                        intersect_pt = intersect(line1, line2)
                        # print(line1, line2, intersect_pt)
                        if intersect_pt is not None:
                            if not line1.isInList(list(self.lines_intersections.keys())):
                                self.lines_intersections.update({line1: [intersect_pt]})
                                # print(self.lines_intersections)
                            else:
                                if not intersect_pt.isInList(self.lines_intersections[line1]):
                                    self.lines_intersections[line1].append(intersect_pt)

                            if not line2.isInList(list(self.lines_intersections.keys())):
                                self.lines_intersections.update({line2: [intersect_pt]})
                            else:
                                if not intersect_pt.isInList(self.lines_intersections[line2]):
                                    self.lines_intersections[line2].append(intersect_pt)

                            if not intersect_pt.isInList(self.pts_intersections):
                                self.pts_intersections.append(intersect_pt)

        # print("pts_intersections", self.pts_intersections)
        # print("lines_intersect", self.lines_intersections)
        self.get_final_edges()
        self.get_final_pts()
        self.print()
        # print("lines_intersect2", self.lines_intersections)

    def print(self):
        index = 0
        for pt in self.final_pts:
            index += 1
        print("V ", index)

        edge_str = "E {"
        for i in range(len(self.final_edges)):
            former_coord = self.final_edges[i].src.indexOf(self.final_pts) + 1
            latter_coord = self.final_edges[i].dst.indexOf(self.final_pts) + 1
            if former_coord == latter_coord:
                continue
            if i != len(self.final_edges) - 1:
                edge_str += ("<{0},{1}>,".format(former_coord, latter_coord))
            else:
                edge_str += ("<{0},{1}>".format(former_coord, latter_coord))
        edge_str += "}"
        print(edge_str)

    def get_final_pts(self):
        for edge in self.final_edges:
            pt1 = edge.src
            pt2 = edge.dst
            if not pt1.isInList(self.final_pts):
                self.final_pts.append(pt1)
            if not pt2.isInList(self.final_pts):
                self.final_pts.append(pt2)
        return self.final_pts

    def get_final_edges(self):

        edges_temp = copy.deepcopy(self.lines_intersections)
        for key, value in edges_temp.items():
            pt1 = key.src
            pt2 = key.dst
            value.append(pt1)
            value.append(pt2)
            value = sort_pts(value)
            for i in range(len(value) - 1):
                line = Line(value[i], value[i + 1])
                if not line.isInList(self.final_edges):
                    self.final_edges.append(line)
        return self.final_edges

    def set_lines(self):
        for key, value in self.streets_dict.items():
            self.vertices.append(value)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices[i]) - 1):
                self.lines[i].append(Line(self.vertices[i][j], self.vertices[i][j + 1]))



def main():
    streets = {}

    while True:
        ''' Notes: Can use Ctrl^D to terminate the program'''
        line = input()  # DONT USE READLINE BECAUSE READLINE ONLY READS FROM .TXT!!
        if line == "":
            break
        if line == "\n":
            break
        if regexFlag(line):
            operator, street_name, coordinates = parser(line)
            if operator == 'add':
                if street_name in streets:
                    print("Error: street currently exists.")
                    continue
                streets[street_name] = coordinates

            elif operator == 'mod':
                if street_name not in streets:
                    print("Error:'mod' or 'rm' specified for a street that does not exist")
                    continue
                streets[street_name] = coordinates

            elif operator == 'rm':
                if street_name not in streets:
                    print("Error:'mod' or 'rm' specified for a street that does not exist")
                    continue
                del streets[street_name]

            elif operator == 'gg':
                if len(streets) == 0:
                    print("Error: No streets")
                    continue
                g = Graph(streets)
                g.get_vertices()
            else:
                print("Error: Incorrect Input Format")
        else:
            print("Error: Incorrect input format")
    sys.exit(0)

if __name__ == '__main__':
    main()
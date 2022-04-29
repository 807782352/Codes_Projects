"""
    Database for the street name and its coordinates
"""

import re
from intersect import Point, Line, intersect, is_in_segment
# from intersect import graph_show


class Map(object):
    def __init__(self):
        self.map_dict = {}  # Store basic data directly from the stdin
        self.line_dict = {}  # Store street name with lines
        self.line_list = []
        self.edges_set = set()
        self.vertices_list = []
        self.vertices_dict = {}  # Store the vertices into the dictionary

    def map_show(self):
        self.vertices_dict_show()
        self.edges_set_show()
        # graph_show(self.line_list, self.vertices_list)
        # print("map_dict", self.map_dict)
        # print("line_dict", self.line_dict)
        # print("vertices_list", self.vertices_list)
        # print("vertices_dict", self.vertices_dict)

    def map_setup(self):
        self.vertices_update()
        self.vertices_dict_setup()
        self.edges_set_setup()

    def edges_set_show(self):
        edges_list = list(self.edges_set)
        str_E = "E = {\n"
        # Change the format of Edge-printing with comma
        for e in range(len(edges_list)):
            if e != (len(edges_list) - 1):
                str_E += "\t"
                str_E += edges_list[e]
                str_E += ",\n"
            else:
                str_E += "\t"
                str_E += edges_list[e]
                str_E += "\n"
        str_E += "}\n"
        print(str_E)

    def edges_set_setup(self):
        """
            To find possible valid edges with intersections
        :return:
        """
        self.edges_set = set()  # Store a list of valid edges
        for pt1_idx in range(len(self.vertices_list) - 1):
            for pt2_idx in range(pt1_idx + 1, len(self.vertices_list), 1):
                pt1 = self.vertices_list[pt1_idx]
                pt2 = self.vertices_list[pt2_idx]
                line1 = Line(pt1, pt2)
                for line_2 in self.line_list:
                    if is_in_segment(line1, line_2):
                        edge = "<" + str(pt1_idx) + "," + str(pt2_idx) + ">"
                        self.edges_set.add(edge)
                        break
        # print("edges_set", self.edges_set)

    def vertices_dict_show(self):
        str_V = "V = {\n"
        for key, value in self.vertices_dict.items():
            str_V += "\t"
            str_V += str(key)
            str_V += " : "
            str_V += str(value)
            str_V += "\n"
        str_V += "}\n"
        print(str_V)

    def vertices_dict_setup(self):
        # vertices_idx = []
        # for i in range(len(self.vertices_list)):
        # vertices_idx.append(i)
        # self.vertices_dict = dict(zip(vertices_idx, self.vertices_list))  # The list is not ordered store
        self.vertices_dict = {}
        for i in range(len(self.vertices_list)):
            self.vertices_dict[i] = self.vertices_list[i]


    def street_store(self, cmd):
        """
            Store the basic information (i.e. Street name, points) from the given command in map_dict
            Store the line segments (i.e. edges) in line_dict
            Calculate and store the intersections in intersect_list
        :param cmd: cmd from stdin <String>
        """
        # print(cmd)

        # Split the line into different segments:
        # operator [street_name] [coordinates]
        segments = cmd.split('"')

        # get the operator (i.e. add, mod, rm, gg)
        operator = segments[0].split()[0]

        if operator == "add":

            street_name = get_street(segments)
            street_name = street_name.lower()
            if street_is_same(street_name, self.map_dict):
                print("Error: street currently exists.")
            else:
                self.map_update(segments, street_name)
                self.vertices_update()
                self.map_setup()
                # print(self.map_dict)

        elif operator == "mod":
            street_name = get_street(segments)
            street_name = street_name.lower()
            if street_is_same(street_name, self.map_dict):
                self.map_update(segments, street_name)
                self.vertices_update()
                self.map_setup()
            else:
                print("Error: 'mod' or 'rm' specified for a street that does not exist.")

        elif operator == "rm":
            street_name = get_street(segments)
            street_name = street_name.lower()
            if street_is_same(street_name, self.map_dict):
                self.map_dict.pop(street_name)
                self.line_dict.pop(street_name)
                # print("map_dict", self.map_dict)
                self.line_list_setup()
                self.vertices_update()
                self.map_setup()
            else:
                print("Error: 'mod' or 'rm' specified for a street that does not exist.")

        elif operator == 'gg':
            self.map_show()

        else:
            print("Error")

    def line_list_setup(self):
        """
            Flatten Values from dictionary to list
        :return: a list of all lines in the map
        """
        self.line_list = []
        values = self.line_dict.values()
        line_list_temp = list(values)
        for lines in line_list_temp:
            for l in lines:
                self.line_list.append(l)

    def vertices_update(self):
        self.vertices_list = []
        for i in range(len(self.line_list) - 1):
            for j in range(i + 1, len(self.line_list), 1):
                line1 = self.line_list[i]
                line2 = self.line_list[j]
                intersect_pt = intersect(line1, line2)
                if intersect_pt is not None:
                    # Prevent duplication coordinates
                    if not is_Coordinate_Same(self.vertices_list, intersect_pt.x, intersect_pt.y):
                        self.vertices_list.append(intersect_pt)
                    if not is_Coordinate_Same(self.vertices_list, line1.src.x, line1.src.y):
                        self.vertices_list.append(line1.src)
                    if not is_Coordinate_Same(self.vertices_list, line1.dst.x, line1.dst.y):
                        self.vertices_list.append(line1.dst)
                    if not is_Coordinate_Same(self.vertices_list, line2.src.x, line2.src.y):
                        self.vertices_list.append(line2.src)
                    if not is_Coordinate_Same(self.vertices_list, line2.dst.x, line2.dst.y):
                        self.vertices_list.append(line2.dst)

    def map_update(self, segments, street_name):
        """
            Process data and update them into the map_dict, line_dict with corresponding street name
        :param segments:
        :param street_name:
        :return:
        """
        coordinates = get_coordinates(segments)
        coord_temp = []  # temporary set for storing coordinate, preventing duplication
        lines_temp = []  # temporary list for storing lines

        # format the coordinates into a list, two entries represent a pair of coordinates
        for coordinate in coordinates:
            temp = parse_coordinate(coordinate)
            pt_x, pt_y = int(temp[0]), int(temp[1])

            if len(coord_temp) == 0:
                pt = Point(pt_x, pt_y)
                coord_temp.append(pt)
                continue

            if not is_Coordinate_Same(coord_temp, pt_x, pt_y):
                pt = Point(pt_x, pt_y)
                coord_temp.append(pt)

        for pt in range(len(coord_temp) - 1):
            l = Line(coord_temp[pt], coord_temp[pt + 1])
            lines_temp.append(l)

        # This step will update(overwrite) new coordinate in coord_dict and line_dict

        self.map_dict[street_name] = coord_temp
        self.line_dict[street_name] = lines_temp
        self.line_list_setup()


def is_Coordinate_Same(coordinate_list, ptx, pty):
    """
        Prevent Coordinate duplication
    """
    for c in coordinate_list:
        if c.x == ptx and c.y == pty:
            return True
    return False


def street_is_same(street_name, map_dict):
    """
        Judgement whether street name has already been existed in the database
    :param street_name:
    :param map_dict:
    :return:
    """
    if street_name in map_dict:
        return True
    else:
        return False


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


def parse_coordinate(coordinate):
    """
        Standardize the coordinate, and separate coordinate into x-component and y-component,
        Format: ['x', 'y']
    :param coordinate: a coordinate with informal format (x, y) <list>
    :return: a coordinate with format ['x', 'y'] <list>
    """
    coordinate = coordinate.replace("(", " ")
    coordinate = coordinate.replace(")", " ")
    coordinate = coordinate.replace(",", " ")
    coordinate = coordinate.split()
    return coordinate


if __name__ == "__main__":
    line = 'add "watERLoo street" (-55,99) (88,53) (99,77) '
    map1 = Map()
    map1.street_store(line)
    # map1.show_map()
    line2 = 'add "waterloo street" (22,33) (7,-8)'
    map1.street_store(line2)
    map1.map_show()
    line3 = 'mod "watERLoo street" (2,5) (5,8)'
    map1.street_store(line3)
    map1.map_show()
    line4 = 'add "main street" (5,6) (3,8) (0,0) (0,0)'
    map1.street_store(line4)
    line5 = 'rm "main street"'
    map1.street_store(line5)
    map1.map_show()
    map1.map_setup()
    map1.map_show()

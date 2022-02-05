"""
    Credit from https://git.uwaterloo.ca/ece650-f2021/python-examples/-/blob/master/py/intersect.py
"""

import math
# import matplotlib.pyplot as plt


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


class Line(object):
    """A line between two points"""

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def distance(self):
        dist = math.sqrt((self.src.x - self.dst.x) ** 2 + (self.src.y - self.dst.y) ** 2)
        return float(pp(dist))

    # def is_vertical(self):
    #     if self.src.x == self.dst.x:
    #         return True
    #     return False
    #
    # def slope(self):
    #     if not self.is_vertical():
    #         slope = (self.dst.y - self.src.y) / (self.dst.x - self.src.x)
    #         return slope
    #     else:
    #         return None
    #
    # def b(self, slope):
    #     if slope is not None:
    #         b = self.dst.y - slope * self.dst.x
    #         return b
    #     else:
    #         return None

    def __repr__(self):
        return '<' + str(self.src) + '-->' + str(self.dst) + '>'


def intersect(line1, line2):
    """Returns a point at which two lines intersect"""
    """ 
        I use cross product to check whether the points in one line 
        is in the different sides of the other line
    """

    x1, y1 = line1.src.x, line1.src.y
    x2, y2 = line1.dst.x, line1.dst.y

    x3, y3 = line2.src.x, line2.src.y
    x4, y4 = line2.dst.x, line2.dst.y

    # Check whether two line segments have intersections
    # Double triangle area enclosed by l1 and l2.src
    area1 = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)
    if area1 == 0:
        return Point(x3, y3)
    # Double triangle area enclosed by l1 and l2.dst
    area2 = (x4 - x1) * (y2 - y1) - (x2 - x1) * (y4 - y1)
    if area2 == 0:
        return Point(x4, y4)

    # if the signs of two area are the same, which means they are in the same side,
    # meaning no intersection

    if area1 * area2 > 0:
        return None

    # Double triangle area enclosed by l1.src and l2
    area3 = (x2 - x3) * (y4 - y3) - (x4 - x3) * (y2 - y3)
    if area3 == 0:
        return Point(x1, y1)
    # Double triangle area enclosed by l1.dst and l2
    area4 = (x1 - x3) * (y4 - y3) - (x4 - x3) * (y1 - y3)
    if area4 == 0:
        return Point(x2, y2)

    if area3 * area4 > 0:
        return None

    # Calculate the intersection coordinate
    xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
    xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    xcoor = xnum / xden

    ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    ycoor = ynum / yden

    return Point(xcoor, ycoor)


def is_in_segment(line1, line2):
    """
    if line1 is in the segment of line2, then return True
    :param line1: shorter segment
    :param line2: longer segment
    :return: True or false
    """
    a = line1.src
    b = line1.dst
    c = line2.src
    d = line2.dst
    l1_dist = line1.distance()
    l2_dist = line2.distance()
    if l1_dist >= l2_dist:
        return False

    # Use Triangle Inequality to determine whether point a and b are in the line2
    line_ac = Line(a, c)
    line_ad = Line(a, d)
    line_bc = Line(b, c)
    line_bd = Line(b, d)
    ac_dist = line_ac.distance()
    ad_dist = line_ad.distance()
    bc_dist = line_bc.distance()
    bd_dist = line_bd.distance()

    if ac_dist + ad_dist - l2_dist <= 0.01 \
            and bc_dist + bd_dist - l2_dist <= 0.01:  # give 0.01 bias acception
        return True
    return False
    # print(multi2)

#
# def graph_show(l_list, vertices_list=None):
#     for l in range(len(l_list)):
#         x_lists = [l_list[l].src.x, l_list[l].dst.x]
#         y_lists = [l_list[l].src.y, l_list[l].dst.y]
#         plt.plot(x_lists, y_lists)
#     if vertices_list is not None:
#         for v in range(len(vertices_list)):
#             v_str = str(v) + ": (" + pp(vertices_list[v].x) + "," + pp(vertices_list[v].y) + ")"
#             plt.annotate(v_str, (vertices_list[v].x, vertices_list[v].y), ha='left')
#     plt.savefig("img.jpg")
#     plt.show()


if __name__ == '__main__':
    l1 = Line(Point(3, 8), Point(5, 6))
    l2 = Line(Point(5, 6), Point(4, 7))
    l3 = Line(Point(2, 5), Point(5, 8))

    # print('Intersection of', l1, 'with', l2, 'is', intersect(l1, l2))
    # print('Intersection of', l2, 'with', l3, 'is', intersect(l2, l3))
    print(l1.distance())
    print(is_in_segment(l2, l1))

    line_list = [l1, l2, l3]
    # graph_show(line_list)

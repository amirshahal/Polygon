# Jether Energy Python Exercise - Amir Shahal - Oct 20th, 2020, file 2 out of 5 files.
import math
import Common as Cmn


class Point:
    """
    A class used to represent a Point (Vertex) which is a part of a 2D Polygon.

    Attributes
    ----------
    x : float
        The x coordination of the Point.
    y : float
        The y coordination of the Point.
    next : Point
        the next Point in the Polygon this point is connected to.
    prev : Point
        the previous Point in the Polygon this point is connected to.
    distance_to_next : float
        the Euclidean Distance to the next ('next' attribute) Point in the Polygon.
    angle : float
        the angle (degrees) between the two edges connected to this Point.
    """

    def __init__(self, new_pt):
        """ C-tor. Create stand alone Point, i.e. not connected."""
        self.x = float(new_pt[0])
        self.y = float(new_pt[1])
        self.next = None
        self.prev = None
        self.distance_to_next = 0
        self.angle = None

    def set_neighbors_related_values(self):
        """Set all variables which are related to the Point's neighbors, including:
        - Distance to next Point.
        - Distance from previous Point to this one.
        - Angles of this Point and the two adjacent one.

        This function MUST be called in any case of a typology change.
        """
        self.distance_to_next = self.euclidean_distance(self.next)
        self.prev.distance_to_next = self.prev.euclidean_distance(self)
        self.set_angel()
        self.prev.set_angel()
        self.next.set_angel()

    def set_angel(self):
        """Set the angle between the two edges connected to this Point.
        Assumes each Point is connected to two (usually other) Points.
        i.e. next and prev are referring to Points.
        """
        self.angle = math.degrees(math.atan2(self.next.y - self.y, self.next.x - self.x)
                                  - math.atan2(self.prev.y - self.y, self.prev.x - self.x))

        if self.angle < 0:
            self.angle += 360

    def __eq__(self, other):
        """Equality Operator.

        Parameters: other (Point) or other(tuple)

        Return: for Point parameter: P1.__eq__(P2) <==> ((P1.x == P2.x) && (P1.y == P2.y))
                 for Tuple parameter: P.__eq__(T) <==> ((P.x == T[0]) && (P.y == T[1]))

        """
        if isinstance(other, tuple):
            return math.fabs(self.x - other[0]) < Cmn.EPSILON and math.fabs(self.y - other[1]) < Cmn.EPSILON

        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

        raise Exception('Do NOT know how to compare Point to {}'.format(type(other)))

    def euclidean_distance(self, other_point):
        """Return the Euclidean Distance from this Point to the other one given as an argument.

        Parameters: other_point (Point) a 2-Dim Point which has x and y attributes.

        Return: the distance between the two Points.
        """

        return math.sqrt(math.pow(other_point.x - self.x, 2) + math.pow(other_point.y - self.y, 2))

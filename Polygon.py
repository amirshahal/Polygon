# Jether Energy Python Exercise - Amir Shahal - Oct 20th, 2020, file 4 out of 5 files.
import math
import inspect
import Common as Cmn
from Point import Point
from CircularDoublyLinkedList import CircularDoublyLinkedList


class Polygon:
    """A class used to represent a Polygon.
    Supports the following operations:
    - insert: adding a point to the Polygon using an index.
    - remove: removing a point from the Polygon using an index.
    - read (evaluate) a point using an index. e.g. point = polygon[ind]
    - alter a point (assign) using an index. e.g. polygon[ind] = (x, y)
    - iterating over the points using the polygon object itself. e.g. for point in polygon: {do something with point}
    - getting the length of the polygon (number of points) using len(polygon).
    - getting the area of the polygon which is None for non-regular polygons and the polygon area for regular polygons.

    Data structure:
        The Polygon consists of two parallel data structures.
        - list. Allows quick approaching by index.
        - Circular Doubly linked list. Allows quick approaching from a point to its neighbors.
        Each Point is kept in both data structures.


        Attributes
        ----------
        _vertices_list : list
            List of Points consisting the Polygon.

        _verticesCDL: CircularDoublyLinkedList
            The same Points stored in a circular doubly linked list.
    """

    def __init__(self):
        """C-tor: builds an empty polygon."""
        self._verticesCDL = CircularDoublyLinkedList()
        self._vertices_list = []

    def __getitem__(self, index):
        """Evaluation of polygon[index]

        Parameters:
            index : int - the index of the item required.

        Returns:
            Point at index location.
        """

        self._validate_index(inspect.currentframe().f_code.co_name, index)

        return self._vertices_list[index]

    def __setitem__(self, index, new_pt):
        """Assignment to polygon[index]. Replace the current value stored in this index.

        Parameters:
            index : int - the index of the item required.
            new_pt: tuple (x, y) with the new coordinates assigned.
        """
        self._validate_index(inspect.currentframe().f_code.co_name, index)
        self._validate_point(inspect.currentframe().f_code.co_name, new_pt)

        # Replace the current value
        self._vertices_list[index].x = new_pt[0]
        self._vertices_list[index].y = new_pt[1]

        # Set neighbors related values (distance from and to the current node, angles of this node and the two
        # adjacent ones).
        self._vertices_list[index].set_neighbors_related_values()

    def __len__(self):
        """Return number of Points in the Polygon.

        Returns: number of Points in the Polygon.
        """
        return len(self._vertices_list)

    def __iter__(self):
        """Make Polygon class iterable

        Returns:
            The Polygon with iteration index reset.
        """
        self.iter_index = -1
        return self

    def __next__(self):
        """Return the next Point after the point currently referred by the iterator
            or the first Point on first invocation.
        """
        self.iter_index += 1
        if self.iter_index < len(self):
            return self[self.iter_index]
        raise StopIteration

    def insert(self, new_pt, index):
        """Insert a point at index
        Parameters:
            new_pt: tuple (x, y) with the new coordinates assigned.
            index : int - the index of the item required.
        """
        self._validate_index(inspect.currentframe().f_code.co_name, index)
        self._validate_point(inspect.currentframe().f_code.co_name, new_pt)

        p = Point(new_pt)
        if len(self) == 0 and index == 0:
            self._verticesCDL.insert_at_beg(p)
        elif len(self) == index:
            prev_node = self[index - 1]
            self._verticesCDL.insert_after(prev_node, p)
        elif index < len(self):
            if index == 0:
                self._verticesCDL.insert_at_beg(p)
            else:
                prev_node = self[index - 1]
                self._verticesCDL.insert_after(prev_node, p)
        else:
            raise Exception('{}(): Trying to add to and index beyond length'.format(
                inspect.currentframe().f_code.co_name))

        self._vertices_list.insert(index, p)

    def remove(self, index):
        """Remove Point by index

        Parameters:
            index : int - the index of the item to remove.
        """
        self._validate_index(inspect.currentframe().f_code.co_name, index)
        point = self._vertices_list[index]
        self._verticesCDL.remove(point)
        del self._vertices_list[index]

    def get_area(self):
        """Return the Polygon's area in case it is regular, None otherwise."""
        is_regular = True
        if len(self):
            point = self._verticesCDL.first
            common_edge_length = point.distance_to_next
            common_angle = point.angle
            while id(point.next) != id(self._verticesCDL.first):
                point = point.next

                # Check common length
                if abs(point.distance_to_next - common_edge_length) > Cmn.EPSILON:
                    # Non regular
                    is_regular = False
                    break

                # Check common angle
                if abs(point.angle - common_angle) > Cmn.EPSILON:
                    # Non regular
                    is_regular = False
                    break

        if is_regular:
            return self._calculate_area()
        else:
            return None

    def _validate_index(self, function_name, index):
        """Validate that index is an integer within less or equal to the current Polygon length.
        Raises an Exception for invalid index.

        Parameters:
            function_name: str - the calling function.
            index : int - the index of the item to remove.
        """
        if not isinstance(index, int):
            raise Exception('{}(): index MUST be an integer. Got {} instead.'.format(function_name, type(index)))

        if index > len(self):
            raise Exception('{}(): Can NOT access item {}. List length is {}.'.format(function_name, index, len(self)))

    @staticmethod
    def _validate_point(function_name, new_pt):
        """Validate that a new point is tuple consists of two numbers (each one is an integer or a float).
                Raises an Exception for invalid point.

                Parameters:
                    function_name: str - the calling function.
                    new_pt: two numbers tuple.
                """
        if not isinstance(new_pt, tuple):
            raise Exception('{}(): Point MUST be a tuple. Got {} instead.'.format(function_name, type(new_pt)))

        if len(new_pt) != 2:
            raise Exception('{}(): Point length MUST be 2. Got {} instead'.format(function_name, len(new_pt)))

        if not isinstance(new_pt[0], int) and not isinstance(new_pt[0], float):
            raise Exception('{}(): X coordinate of a point MUST be an int or a float. Got {} instead'.
                            format(function_name, type(new_pt[0])))

        if not isinstance(new_pt[1], int) and not isinstance(new_pt[1], float):
            raise Exception('{}(): y coordinate of a point MUST be an int or a float. Got {} instead'.
                            format(function_name, type(new_pt[1])))

    def _calculate_area(self):
        """Calculate the Polygon's area.

        Returns:
            The Polygon's area for regular Polygon, None otherwise.
        """
        n_sides = len(self)
        if n_sides:
            s_length = self._vertices_list[0].distance_to_next
            area = n_sides * (s_length ** 2) / (4 * math.tan(math.pi / n_sides))
        else:
            area = 0

        return area

# Polygon
The solution includes 4 source files:
Common.py: includes constants which are shared by more than one file (currently only one constant...).
Point.py: includes a Point class implementation.
CircularDoubleLinkedList.py: includes a Circular Double Linked List class implementation .
Polygon.py: includes a Polygon class implementation. 

The solution also includes one source file used for unit tests:
test_polygon.py
Running this script can be used in order to test the solution.

Below are the project's instructions.

----
The exercise requires to implement a planar, closed and simple polygon, defined by a sequence of 2D points. It is required to provide the following interface:
1. insert(new_pt, ind)
2. remove(ind)
3. read polygon[ind]
4. write (with replace functionality): polygon[ind] = ...
5. For the special case of a regular polygon (edges and angles all equal) - compute the area.
6. Enable len(polygon) to return the number of points and enable iterations over the points via the polygon object itself. 

We assume the user does not send input that makes the polygon self intersecting ever, no need to check that.
The insert and remove operations are used a lot and efficiency is to be accounted for. There are also more and less efficient ways to manage the area and regularity of the polygon, to think about. The focus is on good coding practices, standards, code organization, being pythonic and efficient where relevant. The geometric challenges are only here to facilitate a technical discussion, they are NOT the main importance.

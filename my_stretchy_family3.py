#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: [REDACTED]
#    Student name: Ayden Hull
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#

#-----Assignment Description-----------------------------------------#
#
#  MY STRETCHY FAMILY
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_portrait".
#  You are required to complete this function so that when the
#  program is run it produces a portrait of a stick figure family in
#  the style of the car window stickers that have become popular in
#  recent years, using data stored in a list to determine the
#  locations and heights of the figures.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  only your final solution, whether or not you complete both
#  parts.
#
#--------------------------------------------------------------------#  

#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the background.  You should not change any
# of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

window_height = 550 # pixels
window_width = 900 # pixels
grass_height = 200 # pixels
grass_offset = -100 # pixels
location_width = 150 # pixels
num_locations = 5

#
#--------------------------------------------------------------------#

#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background and the locations where the individuals in the
# portrait are required to stand.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up.
#

# Draw the grass as a big green rectangle
def draw_grass():
    
    penup()
    goto(-window_width / 2, grass_offset) # start at the bottom-left
    setheading(90) # face north
    fillcolor('pale green')
    begin_fill()
    forward(grass_height)
    right(90) # face east
    forward(window_width)
    right(90) # face south
    forward(grass_height)
    right(90) # face west
    forward(window_width)
    end_fill()

# Draw the locations where the individuals must stand
def draw_locations(locations_on = True):

    # Only draw the locations if the argument is True
    if locations_on:

        # Define a small gap at each end of each location
        gap_size = 5 # pixels
        location_width_less_gaps = location_width - (gap_size * 2) # pixels

        # Start at the far left, facing east
        penup()
        goto(-num_locations * location_width / 2, 0)
        setheading(0) 
  
        # Draw each location as a thick line with a gap at each end
        color('dark khaki')
        for location in range(num_locations):
            penup()
            forward(gap_size)
            pendown()
            width(5) # draw a thick line
            forward(location_width_less_gaps)
            width(1)
            penup()
            forward(gap_size)

# Draw the numeric labels on the locations
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:
    
        font_size = 16 # size of characters for the labels

        # Start in the middle of the left-hand location, facing east
        penup()
        goto(-((num_locations - 1) * location_width) / 2,
             -font_size * 2)
        setheading(0) 

        # Walk to the right, print the labels as we go
        color('dark khaki')
        for label in range(num_locations):
            write(label, font = ('Arial', font_size, 'bold'))
            forward(location_width)

# As a debugging aid, mark certain absolute coordinates on the canvas
def mark_coords(marks_on = True):

    # Only mark the coordinates if the argument is True
    if marks_on:

        # Mark the "home" coordinate
        home()
        width(1)
        color('black')
        dot(3)
        write('0, 0', font = ('Arial', 10, 'normal'))

        # Mark the centre point of each individual's location
        max_x = (num_locations - 1) * location_width / 2
        penup()
        for x_coord in range(-max_x, max_x + location_width, location_width):
            for y_coord in [0, 400]:
                goto(x_coord, y_coord)
                dot(3)
                write(str(x_coord) + ', ' + str(y_coord),
                      font = ('Arial', 10, 'normal'))
                
#
#--------------------------------------------------------------------#

#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the positions for
# the people in the portrait:
#
# 1. The name of the individual, from 'Person A' to 'Person D' or 'Pet'
# 2. The place where that person/pet must stand, from location 0 to 4
# 3. How much to stretch the person/pet vertically, from 0.5 to 1.5
#    times their normal height
# 4. A mystery value, either '*' or '-', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily include all people and sometimes
# they require the same person to be drawn more than once.  You
# can assume, however, that they never put more than one person in
# the same location.
#
# You may add additional data sets but you may not change any of the
# given data sets below.
#

# The following data set doesn't require drawing any people at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_portrait" function.

portrait_00 = []

# The following data sets each draw just one of the individuals
# at their default height.

portrait_01 = [['Person A', 2, 1.0, '-']]

portrait_02 = [['Person B', 3, 1.0, '-']]

portrait_03 = [['Person C', 1, 1.0, '-']]

portrait_04 = [['Person D', 0, 1.0, '-']]

portrait_05 = [['Pet', 4, 1.0, '-']]

# The following data sets each draw just one of the individuals
# but multiple times and at different sizes.

portrait_06 = [['Person A', 3, 1.0, '-'],
               ['Person A', 1, 0.75, '-'],
               ['Person A', 2, 0.5, '-'],
               ['Person A', 4, 1.4, '-']]

portrait_07 = [['Person B', 0, 0.5, '-'],
               ['Person B', 2, 1.0, '-'],
               ['Person B', 3, 1.5, '-']]

portrait_08 = [['Person C', 0, 0.5, '-'],
               ['Person C', 1, 0.75, '-'],
               ['Person C', 2, 1.0, '-'],
               ['Person C', 3, 1.25, '-'],
               ['Person C', 4, 1.5, '-']]

portrait_09 = [['Person D', 3, 1.25, '-'],
               ['Person D', 1, 0.8, '-'],
               ['Person D', 0, 1.0, '-']]

portrait_10 = [['Pet', 1, 1.3, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Pet', 3, 0.7, '-']]

# The following data sets each draw a family portrait with all
# individuals at their default sizes.  These data sets create
# "natural" looking portraits.  Notably, the first two both
# show the full family.

portrait_11 = [['Person A', 0, 1.0, '-'],
               ['Person B', 1, 1.0, '-'],
               ['Person C', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Pet', 4, 1.0, '-']]

portrait_12 = [['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*'],
               ['Person C', 1, 1.0, '-'],
               ['Person D', 4, 1.0, '-'],
               ['Pet', 0, 1.0, '-']]

portrait_13 = [['Person B', 1, 1.0, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Person C', 3, 1.0, '*']]

portrait_14 = [['Person C', 0, 1.0, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Person B', 4, 1.0, '-']]

portrait_15 = [['Person D', 4, 1.0, '*'],
               ['Person A', 3, 1.0, '-'],
               ['Person B', 2, 1.0, '-']]

portrait_16 = [['Person D', 1, 1.0, '-'],
               ['Person C', 0, 1.0, '-'],
               ['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*']]

# The following data sets draw all five individuals at their
# minimum and maximum heights.

portrait_17 = [['Person A', 0, 0.5, '-'],
               ['Person B', 1, 0.5, '-'],
               ['Person C', 2, 0.5, '*'],
               ['Person D', 3, 0.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_18 = [['Person A', 4, 1.5, '-'],
               ['Person B', 3, 1.5, '*'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 1, 1.5, '-'],
               ['Pet', 0, 1.5, '-']]

# The following data sets each draw a family portrait with
# various individuals at varying sizes.

portrait_19 = [['Person A', 0, 0.5, '*'],
               ['Person B', 1, 0.8, '-'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_20 = [['Person B', 1, 0.8, '*'],
               ['Pet', 2, 1.4, '-'],
               ['Person C', 3, 0.7, '-']]

portrait_21 = [['Person C', 0, 1.5, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '*'],
               ['Person B', 4, 1.5, '-']]

portrait_22 = [['Person D', 4, 1.2, '-'],
               ['Person A', 3, 1.0, '*'],
               ['Person B', 2, 0.8, '-']]

portrait_23 = [['Person D', 1, 1.1, '-'],
               ['Person C', 2, 0.9, '-'],
               ['Person A', 0, 1.1, '*'],
               ['Person B', 3, 0.9, '-']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#

#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_portrait" function.
#

# Code to convert SVG image into code for the below classes/functions
"""
URL.createObjectURL(new Blob(["g = PathGroup()\n\n    #region drawing\n" + [].map.call(document.querySelectorAll("path"), function (path) {
    var segs = path.pathSegList;
    var fnc = [];
    
    if (path.id) {
        fnc[fnc.length] = "# " + path.id;
    }
    
    fnc[fnc.length] = "p = Path()";
    fnc[fnc.length] = "";
    fnc[fnc.length] = "g.add(p)";

    if (path.getAttribute("fill") !== "none") {
        fnc[fnc.length] = "p.fill(\"" + (path.getAttribute("fill") || "#000000") + "\")";
    }

    if (path.getAttribute("stroke")) {
        fnc[fnc.length] = "p.stroke_color(\"" + path.getAttribute("stroke") + "\")";
    }

    if (path.getAttribute("stroke-width")) {
        fnc[fnc.length] = "p.stroke_width(" + path.getAttribute("stroke-width") + ")";
    }

    fnc[fnc.length] = "";

    function fn(x) {
        return x.toFixed(3);
    }

    for (var i = 0; i < segs.numberOfItems; i++) {
        var seg = segs.getItem(i);

        switch (seg.pathSegType) {
            case 10:
                fnc[fnc.length] = "p.arc_abs(" + [seg.x, seg.y, seg.r1, seg.r2, seg.angle, seg.largeArcFlag, seg.sweepFlag].map(fn).join(", ") + ")";
                break;
            case 11:
                fnc[fnc.length] = "p.arc_rel(" + [seg.x, seg.y, seg.r1, seg.r2, seg.angle, seg.largeArcFlag, seg.sweepFlag].map(fn).join(", ") + ")";
                break;
            case 1:
                fnc[fnc.length] = "p.close_path()";
                break;
            case 6:
                fnc[fnc.length] = "p.curve_to_cubic_abs(" + [seg.x, seg.y, seg.x1, seg.y1, seg.x2, seg.y2].map(fn).join(", ") + ")";
                break;
            case 7:
                fnc[fnc.length] = "p.curve_to_cubic_rel(" + [seg.x, seg.y, seg.x1, seg.y1, seg.x2, seg.y2].map(fn).join(", ") + ")";
                break;
            case 16:
                fnc[fnc.length] = "p.curve_to_cubic_smooth_abs(" + [seg.x, seg.y, seg.x2, seg.y2].map(fn).join(", ") + ")";
                break;
            case 17:
                fnc[fnc.length] = "p.curve_to_cubic_smooth_rel(" + [seg.x, seg.y, seg.x2, seg.y2].map(fn).join(", ") + ")";
                break;
            case 8:
                fnc[fnc.length] = "p.curve_to_quadratic_abs(" + [seg.x, seg.y, seg.x1, seg.y1].map(fn).join(", ") + ")";
                break;
            case 9:
                fnc[fnc.length] = "p.curve_to_quadratic_rel(" + [seg.x, seg.y, seg.x1, seg.y1].map(fn).join(", ") + ")";
                break;
            case 18:
                fnc[fnc.length] = "p.curve_to_quadratic_smooth_abs(" + [seg.x, seg.y].map(fn).join(", ") + ")";
                break;
            case 19:
                fnc[fnc.length] = "p.curve_to_quadratic_smooth_rel(" + [seg.x, seg.y].map(fn).join(", ") + ")";
                break;
            case 4:
                fnc[fnc.length] = "p.line_to_abs(" + [seg.x, seg.y].map(fn).join(", ") + ")";
                break;
            case 12:
                fnc[fnc.length] = "p.line_to_horizontal_abs(" + [seg.x].map(fn).join(", ") + ")";
                break;
            case 13:
                fnc[fnc.length] = "p.line_to_horizontal_rel(" + [seg.x].map(fn).join(", ") + ")";
                break;
            case 5:
                fnc[fnc.length] = "p.line_to_rel(" + [seg.x, seg.y].map(fn).join(", ") + ")";
                break;
            case 14:
                fnc[fnc.length] = "p.line_to_vertical_abs(" + [seg.y].map(fn).join(", ") + ")";
                break;
            case 15:
                fnc[fnc.length] = "p.line_to_vertical_rel(" + [seg.y].map(fn).join(", ") + ")";
                break;
            case 2:
                fnc[fnc.length] = "p.move_to_abs(" + [seg.x, seg.y].map(fn).join(", ") + ")";
                break;
            case 3:
                fnc[fnc.length] = "p.move_to_rel(" + [seg.x, seg.y].map(fn).join(", ") + ")";
                break;
            default:
                console.log(seg);
        }
    }

    fnc[fnc.length] = "";
    fnc[fnc.length] = "p.end()"
    
    return fnc.join("\n");
}).join("\n\n").split("\n").map(function (x) { return "    " + x; }).join("\n") + "\n    #endregion drawing"], { "type": "text/plain" }));
"""

# Transformable class used as a common interface/implementation for shapes
class Transformable(object):
    def __init__(self):
        self._transform = [1, 0, 0, 1, 0, 0]
        self._inv_transform = [1, 0, 0, 1, 0, 0]

    def _multiply_matrix(self, a, b):
        # Calculate new transformation matrices

        return [
            a[0] * b[0] + a[2] * b[1],
            a[1] * b[0] + a[3] * b[1],
            a[0] * b[2] + a[2] * b[3],
            a[1] * b[2] + a[3] * b[3],
            a[0] * b[4] + a[2] * b[5] + a[4],
            a[1] * b[4] + a[3] * b[5] + a[5]
        ]

    def _add_matrix(self, a, b, c, d, e, f):
        # Forwrad transformation
        self._transform = self._multiply_matrix(self._transform, [a, b, c, d, e, f])
        
        # Calculate the inverse matrix
        inv_cmn = a * d - b * c
        inv_a = d / inv_cmn
        inv_b = -(b / inv_cmn)
        inv_c = -(c / inv_cmn)
        inv_d = a / inv_cmn
        inv_e = (c * f - e * d) / inv_cmn
        inv_f = (e * b - a * f) / inv_cmn

        # Reverse transformation
        self._inv_transform = self._multiply_matrix(self._inv_transform, [inv_a, inv_b, inv_c, inv_d, inv_e, inv_f])

    # Add a user-defined matrix
    def matrix(self, a, b, c, d, e, f):
        self._add_matrix(a, b, c, d, e, f)

        return self

    # Translation
    def translate(self, x, y = 0):
        self._add_matrix(1, 0, 0, 1, x, y)

        return self

    # Scaling
    def scale(self, x, y = None):
        if y is None:
            y = x

        self._add_matrix(x, 0, 0, y, 0, 0)

        return self

    # Rotation
    # - x and y must either be both defined or both undefined
    # - If x and y are defined, translate first, rotate, then translate back
    def rotate(self, a, x = None, y = None):
        if x is None or y is None:
            if (not x is None) or (not y is None):
                raise Exception("X and Y must both either be defined or undefined")

            self._add_matrix(cos(radians(a)), sin(radians(a)), -sin(radians(a)), cos(radians(a)), 0, 0)
        else:
            self.translate(x, y)
            self._add_matrix(cos(radians(a)), sin(radians(a)), -sin(radians(a)), cos(radians(a)), 0, 0)
            self.translate(-x, -y)

        return self

    # Skew horizontally
    def skew_x(self, a):
        self._add_matrix(1, 0, tan(radians(a)), 1, 0, 0)

        return self

    # Skew vertically
    def skew_y(self, a):
        self._add_matrix(1, tan(radians(a)), 0, 1, 0, 0)

        return self

    # Apply the transformation matrix to x and y
    def get_transformed_vec2d(self, x, y):
        x = float(x)
        y = float(y)

        transform = self._transform

        x = transform[0] * x + transform[2] * y + transform[4]
        y = transform[1] * x + transform[3] * y + transform[5]

        return (x, y)

    # Apply the inverse transformation matrix to x and y
    def get_inverse_transformed_vec2d(self, x, y):
        x = float(x)
        y = float(y)

        transform = self._inv_transform

        x = transform[0] * x + transform[2] * y + transform[4]
        y = transform[1] * x + transform[3] * y + transform[5]

        return (x, y)

# Custom path, based on SVG paths
class Path(Transformable):
    # Initialize the path
    def __init__(self):
        # State variables
        self._pen = False
        self._fill = False
        self._home = None

        # Required for "smototh" versions of bezier curves
        self._last_command = None
        self._last_control_point = None

        # Make the path transformable
        super(Path, self).__init__()

    # Used to end the drawing
    def end(self):
        if self._pen:
            penup()
            self._pen = False

        if self._fill:
            end_fill()
            self._fill = False

    # Get the inverse transformed x-coordinate of the pen's location
    def _xcor(self):
        return self.get_inverse_transformed_vec2d(xcor(), 0)[0]

    # Get the inverse transformed y-coordinate of the pen's location
    def _ycor(self):
        return self.get_inverse_transformed_vec2d(0, ycor())[1]

    # Draw to the transformed coordinates
    def _goto(self, x, y):
        goto(*self.get_transformed_vec2d(x, y))

    # Set-up the shape to fill
    def fill(self, c):
        if not self._fill:
            self._fill = True
            begin_fill()

        fillcolor(c)

    # Set the pen width
    def stroke_width(self, w):
        # Set-up the pen if required
        if not self._pen:
            pendown()
            self._pen = True

        width(w)

    # Set the pen color
    def stroke_color(self, c):
        # Set-up the pen if required
        if not self._pen:
            pendown()
            self._pen = True

        pencolor(c)

    # Close the current sub-path
    def close_path(self):
        self._last_command = "close_path"

        if not self._home is None:
            self._goto(*self._home)

        if self._pen:
            penup()
            self._pen = False

        if self._fill:
            end_fill()
            self._fill = False

    # Move to an absolute position and set-up a new sub-path if required
    def move_to_abs(self, x, y):
        self._last_command = "move_to"

        self._home = (x, y)

        if self._pen:
            penup()

        if self._fill:
            end_fill()

        self._goto(x, y)

        if self._fill:
            begin_fill()

        if self._pen:
            pendown()

    # Move to a relative position (or absolute if a new path), and set-up a new sub-path if required
    def move_to_rel(self, x, y):
        if self._home is None:
            self.move_to_abs(x, y)
            return

        self.move_to_abs(self._xcor() + x, self._ycor() + y)

    # Functions below are pretty self explanatory
    # - based on SVG Path Segment functions

    def line_to_abs(self, x, y):
        self._last_command = "line_to"

        self._goto(x, y)
    
    def line_to_rel(self, x, y):
        self.line_to_abs(self._xcor() + x, self._ycor() + y)

    def curve_to_cubic_abs(self, x, y, x1, y1, x2, y2):
        self._last_command = "curve_to_cubic"
        self._last_control_point = (x2, y2)

        # Cubic beziers have 4 points, but the 0th point is the current position
        x0 = self._xcor()
        y0 = self._ycor()

        # Calculate the x and y for a given t, according to the generalized cubic bezier curve function
        def B(t):
            Btx = (((1.0 - t) ** 3.0) * x0) + (3.0 * ((1.0 - t) ** 2.0) * t * x1) + (3.0 * (1.0 - t) * (t ** 2.0) * x2) + ((t ** 3.0) * x)
            Bty = (((1.0 - t) ** 3.0) * y0) + (3.0 * ((1.0 - t) ** 2.0) * t * y1) + (3.0 * (1.0 - t) * (t ** 2.0) * y2) + ((t ** 3.0) * y)

            return (Btx, Bty)
        
        # Get an approximate step counts (highest pixel count delta along x and y axis)
        steps = abs(float(max(max(max([x0, x1, x2, x]) - min([x0, x1, x2, x]), max([y0, y1, y2, y]) - min([y0, y1, y2, y])), 1)))

        last_point = B(0)

        self._goto(*last_point)

        for i in xrange(1, int(steps) + 1):
            point = B(i / steps)

            # Drop steps where there is no (visible) change in distance
            if (abs(point[0] - last_point[0]) >= 1) or (abs(point[1] - last_point[1]) >= 1):
                last_point = point

                self._goto(*point)

    def curve_to_cubic_rel(self, x, y, x1, y1, x2, y2):
        self.curve_to_cubic_abs(self._xcor() + x, self._ycor() + y, self._xcor() + x1, self._ycor() + y1, self._xcor() + x2, self._ycor() + y2)

    def curve_to_quadratic_abs(self, x, y, x1, y1):
        self._last_command = "curve_to_quadratic"
        self._last_control_point = (x1, y1)

        # Quadratic beziers have 3 points, but the 0th point is the current position
        x0 = self._xcor()
        y0 = self._ycor()

        # Get an approximate step counts (highest pixel count delta along x and y axis)
        steps = abs(float(max(max(max([x0, x1, x]) - min([x0, x1, x]), max([y0, y1, y]) - min([y0, y1, y])), 1)))

        last_x = None
        last_y = None

        for i in xrange(1, int(steps) + 1):
            t = i / steps

            Btx = (((1.0 - t) ** 2.0) * x0) + ((2.0 * (1.0 - t) * t) * x1) + ((t ** 2.0) * x)
            Bty = (((1.0 - t) ** 2.0) * y0) + ((2.0 * (1.0 - t) * t) * y1) + ((t ** 2.0) * y)

            # Drop steps where there is no (visible) change in distance
            if (last_x is None) or abs((Btx - last_x) >= 1) or abs((Bty - last_y) >= 1):
                last_x = Btx
                last_y = Bty

                self._goto(Btx, Bty)

    def curve_to_quadratic_rel(self, x, y, x1, y1):
        self.curve_to_quadratic_abs(self._xcor() + x, self._ycor() + y, self._xcor() + x1, self._ycor() + y1)

    def arc_abs(self, x, y, r1, r2, angle, large_arc_flag, sweep_flag):
        self._last_command = "arc"

        print "Attempted arc to: ", x, y

        self._goto(x, y)

    def arc_rel(self, x, y, r1, r2, angle, large_arc_flag, sweep_flag):
        self.arc_abs(self._xcor() + x, self._ycor() + y, r1, r2, angle, large_arc_flag, sweep_flag)

    def line_to_horizontal_abs(self, x):
        self._last_command = "line_to_horizontal"

        self._goto(x, self._ycor())

    def line_to_horizontal_rel(self, x):
        self.line_to_horizontal_abs(self._xcor() + x)

    def line_to_vertical_abs(self, y):
        self._last_command = "line_to_vertical"

        self._goto(self._xcor(), y)

    def line_to_vertical_rel(self, y):
        self.line_to_vertical_abs(self._ycor() + y)

    def curve_to_cubic_smooth_abs(self, x, y, x2, y2):
        # The first control point is assumed to be the reflection of the second control point on the previous command relative to the current point.
        # If there is no previous command or if the previous command was not an C, c, S or s, assume the first control point is coincident with the current point.

        if self._last_command != "curve_to_cubic":
            x1, y1 = x2, y2
        else:
            # The first control point of the given cubic Bezier segment is calculated by reflecting the previous path segments second control point relative to the current point.
            x1 = 2.0 * self._xcor() - self._last_control_point[0]
            y1 = 2.0 * self._ycor() - self._last_control_point[1]

        self.curve_to_cubic_abs(x, y, x1, y1, x2, y2)

    def curve_to_cubic_smooth_rel(self, x, y, x2, y2):
        self.curve_to_cubic_smooth_abs(self._xcor() + x, self._ycor() + y, self._xcor() + x2, self._ycor() + y2)

    def curve_to_quadratic_smooth_abs(self, x, y):
        # The control point is assumed to be the reflection of the control point on the previous command relative to the current point.
        # If there is no previous command or if the previous command was not a curve_to_quadratic, assume the control point is coincident with the current point.

        if self._last_command != "curve_to_quadratic":
            x1, y1 = self._xcor(), self._ycor()
        else:
            x1 = 2.0 * self._xcor() - self._last_control_point[0]
            y1 = 2.0 * self._ycor() - self._last_control_point[1]

        self.curve_to_quadratic_abs(x, y, x1, y1)

    def curve_to_quadratic_smooth_rel(self, x, y):
        self.curve_to_quadratic_smooth_abs(self._xcor() + x, self._ycor() + y)

def ellipse(path, cx, cy, rx, ry):
    # http://stackoverflow.com/questions/5737975/circle-drawing-with-svgs-arc-path/10477334#10477334
    path.move_to_abs(cx - rx, cy)
    path.arc_rel(+2.0 * rx, 0, rx, ry, 0, 1, 0)
    path.arc_rel(-2.0 * rx, 0, rx, ry, 0, 1, 0)
    path.close_path()

def circle(path, cx, cy, r):
    ellipse(path, cx, cy, r, r)

def line(path, x1, y1, x2, y2):
    path.move_to_abs(x1, y1)
    path.line_to_abs(x2, y2)
    path.close_path()

def rect(path, x, y, width, height, rx = None, ry = None):
    arc = True

    if rx is None or ry is None:
        rx = 0
        ry = 0
        arc = False

    path.move_to_abs(x + rx, y)

    # Top
    path.line_to_abs(x + width - rx, y)

    if arc:
        path.arc_abs(x + width, y + ry, rx, ry, 90, 0, 0)

    # Right
    path.line_to_abs(x + width, y + height - ry)

    if arc:
        path.arc_abs(x + width - rx, y + height, rx, ry, 90, 0, 0)

    # Bottom
    path.line_to_abs(x + rx, y + height)

    if arc:
        path.arc_abs(x, y + height - ry, rx, ry, 90, 0, 0)

    # Left
    path.line_to_abs(x, y + ry)

    if arc:
        path.arc_abs(x + rx, y, rx, ry, 90, 0, 0)

    path.close_path()

def polyline(path, points):
    path.move_to_abs(*points[0])

    for i in xrange(1, len(points)):
        path.line_to_abs(*points[i])

def polygon(path, points):
    polyline(path, points)

    path.close_path()

# Apply a common transformation to "children" of a group
class PathGroup(Transformable):
    def add(self, path):
        path.matrix(*self._transform)

# person_a, person_b, person_c, person_d and the pet were all generated via the output of the js code above
# Spongebob Squarepants
def person_a(x, y, scale_x, scale_y, crown):
    g = PathGroup()

    width = 150.000 * scale_x
    height = 167.160 * scale_y

    g.translate(-width / 2.0, -height)
    g.scale(scale_x, scale_y)
    g.translate(x, y)

    if crown:
        #region crown
        # path4672_2_
        p = Path()
    
        g.add(p)
        p.fill("#870303")
    
        p.move_to_abs(67.132, 0.000)
        p.line_to_abs(66.540, 1.015)
        p.line_to_rel(-6.845, 11.690)
        p.line_to_rel(-11.468, -7.230)
        p.line_to_rel(-0.993, -0.630)
        p.line_to_rel(-0.296, 1.142)
        p.line_to_rel(-3.445, 13.104)
        p.line_to_rel(-12.986, -3.867)
        p.line_to_rel(-1.126, -0.334)
        p.line_to_rel(0.015, 1.170)
        p.line_to_rel(0.222, 13.550)
        p.line_to_rel(-13.549, -0.222)
        p.line_to_rel(-1.178, -0.015)
        p.line_to_rel(0.341, 1.125)
        p.line_to_rel(3.867, 12.987)
        p.line_to_abs(5.986, 46.931)
        p.line_to_rel(-1.134, 0.296)
        p.line_to_rel(0.630, 0.994)
        p.line_to_rel(7.230, 11.460)
        p.line_to_abs(1.015, 66.533)
        p.line_to_abs(0.000, 67.132)
        p.line_to_rel(0.874, 0.786)
        p.line_to_rel(10.053, 9.089)
        p.line_to_rel(-9.408, 9.750)
        p.line_to_rel(-0.814, 0.845)
        p.line_to_rel(1.052, 0.525)
        p.line_to_rel(12.134, 6.039)
        p.line_to_rel(-6.430, 11.926)
        p.line_to_rel(-0.563, 1.039)
        p.line_to_rel(1.156, 0.221)
        p.line_to_rel(13.313, 2.535)
        p.line_to_rel(-2.970, 13.222)
        p.line_to_rel(-0.260, 1.148)
        p.line_to_rel(1.171, -0.096)
        p.line_to_rel(13.498, -1.148)
        p.line_to_rel(0.711, 13.535)
        p.line_to_rel(0.059, 1.169)
        p.line_to_rel(1.104, -0.406)
        p.line_to_rel(12.690, -4.750)
        p.line_to_rel(4.326, 12.848)
        p.line_to_rel(0.378, 1.111)
        p.line_to_rel(0.948, -0.697)
        p.line_to_rel(10.942, -7.993)
        p.line_to_rel(7.638, 11.202)
        p.line_to_abs(72.259, 150.000)
        p.line_to_rel(0.726, -0.926)
        p.line_to_rel(8.378, -10.645)
        p.line_to_rel(10.372, 8.719)
        p.line_to_rel(0.903, 0.756)
        p.line_to_rel(0.453, -1.088)
        p.line_to_rel(5.192, -12.514)
        p.line_to_rel(12.342, 5.602)
        p.line_to_rel(1.067, 0.480)
        p.line_to_rel(0.141, -1.164)
        p.line_to_rel(1.629, -13.452)
        p.line_to_rel(13.395, 2.067)
        p.line_to_rel(1.155, 0.178)
        p.line_to_rel(-0.178, -1.164)
        p.line_to_rel(-2.066, -13.394)
        p.line_to_rel(13.460, -1.630)
        p.line_to_rel(1.163, -0.141)
        p.line_to_rel(-0.481, -1.066)
        p.line_to_rel(-5.601, -12.342)
        p.line_to_rel(12.513, -5.193)
        p.line_to_rel(1.089, -0.451)
        p.line_to_rel(-0.764, -0.897)
        p.line_to_rel(-8.719, -10.372)
        p.line_to_rel(10.652, -8.386)
        p.line_to_abs(150.000, 72.251)
        p.line_to_rel(-0.971, -0.659)
        p.line_to_rel(-11.193, -7.630)
        p.line_to_rel(7.993, -10.949)
        p.line_to_rel(0.696, -0.948)
        p.line_to_rel(-1.118, -0.371)
        p.line_to_rel(-12.839, -4.334)
        p.line_to_rel(4.741, -12.690)
        p.line_to_rel(0.416, -1.104)
        p.line_to_rel(-1.171, -0.060)
        p.line_to_rel(-13.542, -0.703)
        p.line_to_rel(1.147, -13.506)
        p.line_to_rel(0.104, -1.169)
        p.line_to_rel(-1.149, 0.258)
        p.line_to_abs(109.900, 21.365)
        p.line_to_rel(-2.549, -13.320)
        p.line_to_rel(-0.223, -1.148)
        p.line_to_rel(-1.029, 0.555)
        p.line_to_rel(-11.927, 6.431)
        p.line_to_abs(88.134, 1.749)
        p.line_to_rel(-0.525, -1.052)
        p.line_to_rel(-0.846, 0.815)
        p.line_to_rel(-9.756, 9.416)
        p.line_to_abs(67.925, 0.867)
        p.line_to_abs(67.132, 0.000)
        p.line_to_abs(67.132, 0.000)
        p.close_path()
        p.move_to_abs(67.437, 2.896)
        p.line_to_rel(8.889, 9.846)
        p.line_to_rel(0.600, 0.659)
        p.line_to_rel(0.639, -0.623)
        p.line_to_rel(9.549, -9.208)
        p.line_to_rel(5.910, 11.875)
        p.line_to_rel(0.394, 0.799)
        p.line_to_rel(0.786, -0.422)
        p.line_to_rel(11.682, -6.297)
        p.line_to_rel(2.482, 13.031)
        p.line_to_rel(0.170, 0.874)
        p.line_to_rel(0.867, -0.193)
        p.line_to_rel(12.949, -2.912)
        p.line_to_rel(-1.127, 13.217)
        p.line_to_rel(-0.073, 0.888)
        p.line_to_rel(0.889, 0.045)
        p.line_to_rel(13.246, 0.688)
        p.line_to_rel(-4.646, 12.423)
        p.line_to_rel(-0.312, 0.838)
        p.line_to_rel(0.845, 0.281)
        p.line_to_rel(12.564, 4.238)
        p.line_to_rel(-7.823, 10.712)
        p.line_to_rel(-0.525, 0.718)
        p.line_to_rel(0.740, 0.504)
        p.line_to_rel(10.957, 7.475)
        p.line_to_rel(-10.424, 8.201)
        p.line_to_rel(-0.703, 0.548)
        p.line_to_rel(0.578, 0.682)
        p.line_to_rel(8.541, 10.157)
        p.line_to_rel(-12.261, 5.082)
        p.line_to_rel(-0.814, 0.348)
        p.line_to_rel(0.362, 0.809)
        p.line_to_rel(5.490, 12.082)
        p.line_to_rel(-13.179, 1.586)
        p.line_to_rel(-0.882, 0.109)
        p.line_to_rel(0.133, 0.882)
        p.line_to_rel(2.022, 13.112)
        p.line_to_rel(-13.111, -2.021)
        p.line_to_rel(-0.875, -0.142)
        p.line_to_rel(-0.111, 0.890)
        p.line_to_rel(-1.592, 13.164)
        p.line_to_rel(-12.076, -5.482)
        p.line_to_rel(-0.814, -0.363)
        p.line_to_rel(-0.341, 0.823)
        p.line_to_rel(-5.082, 12.253)
        p.line_to_rel(-10.156, -8.541)
        p.line_to_rel(-0.683, -0.570)
        p.line_to_rel(-0.547, 0.695)
        p.line_to_rel(-8.209, 10.424)
        p.line_to_rel(-7.467, -10.956)
        p.line_to_rel(-0.503, -0.735)
        p.line_to_rel(-0.719, 0.520)
        p.line_to_rel(-10.712, 7.831)
        p.line_to_rel(-4.238, -12.573)
        p.line_to_rel(-0.282, -0.844)
        p.line_to_rel(-0.837, 0.312)
        p.line_to_rel(-12.423, 4.645)
        p.line_to_rel(-0.689, -13.245)
        p.line_to_rel(-0.052, -0.889)
        p.line_to_rel(-0.881, 0.072)
        p.line_to_rel(-13.225, 1.127)
        p.line_to_rel(2.912, -12.949)
        p.line_to_rel(0.200, -0.867)
        p.line_to_rel(-0.875, -0.162)
        p.line_to_rel(-13.030, -2.489)
        p.line_to_rel(6.289, -11.683)
        p.line_to_rel(0.423, -0.778)
        p.line_to_rel(-0.792, -0.400)
        p.line_to_abs(3.571, 87.113)
        p.line_to_rel(9.216, -9.549)
        p.line_to_rel(0.615, -0.645)
        p.line_to_rel(-0.660, -0.593)
        p.line_to_rel(-9.845, -8.898)
        p.line_to_rel(11.453, -6.711)
        p.line_to_rel(0.763, -0.445)
        p.line_to_rel(-0.474, -0.755)
        p.line_to_abs(7.564, 48.301)
        p.line_to_rel(12.831, -3.378)
        p.line_to_rel(0.859, -0.222)
        p.line_to_rel(-0.252, -0.852)
        p.line_to_rel(-3.793, -12.712)
        p.line_to_rel(13.268, 0.215)
        p.line_to_rel(0.890, 0.015)
        p.line_to_rel(-0.015, -0.889)
        p.line_to_rel(-0.208, -13.269)
        p.line_to_rel(12.712, 3.786)
        p.line_to_rel(0.852, 0.260)
        p.line_to_rel(0.223, -0.868)
        p.line_to_rel(3.370, -12.831)
        p.line_to_rel(11.224, 7.083)
        p.line_to_rel(0.748, 0.474)
        p.line_to_rel(0.452, -0.770)
        p.line_to_abs(67.437, 2.896)
        p.line_to_abs(67.437, 2.896)
        p.close_path()
    
        p.end()
    
        # path4662_3_
        p = Path()
    
        g.add(p)
        p.fill("#E60000")
    
        p.move_to_abs(126.985, 126.980)
        p.line_to_rel(-14.272, -2.199)
        p.line_to_rel(-1.733, 14.338)
        p.line_to_rel(-13.151, -5.970)
        p.line_to_rel(-5.535, 13.339)
        p.line_to_rel(-11.053, -9.297)
        p.line_to_rel(-8.931, 11.352)
        p.line_to_rel(-8.135, -11.935)
        p.line_to_rel(-11.661, 8.521)
        p.line_to_rel(-4.614, -13.686)
        p.line_to_abs(34.372, 136.500)
        p.line_to_rel(-0.750, -14.423)
        p.line_to_rel(-14.390, 1.223)
        p.line_to_rel(3.168, -14.091)
        p.line_to_rel(-14.186, -2.708)
        p.line_to_rel(6.853, -12.712)
        p.line_to_rel(-12.930, -6.435)
        p.line_to_rel(10.028, -10.392)
        p.line_to_abs(1.452, 67.280)
        p.line_to_rel(12.460, -7.302)
        p.line_to_abs(6.208, 47.763)
        p.line_to_rel(13.968, -3.669)
        p.line_to_rel(-4.123, -13.841)
        p.line_to_rel(14.440, 0.236)
        p.line_to_rel(-0.235, -14.440)
        p.line_to_rel(13.841, 4.123)
        p.line_to_rel(3.669, -13.968)
        p.line_to_rel(12.215, 7.704)
        p.line_to_rel(7.302, -12.460)
        p.line_to_rel(9.684, 10.714)
        p.line_to_abs(87.361, 2.133)
        p.line_to_rel(6.434, 12.929)
        p.line_to_rel(12.713, -6.852)
        p.line_to_rel(2.707, 14.186)
        p.line_to_rel(14.090, -3.169)
        p.line_to_rel(-1.221, 14.390)
        p.line_to_rel(14.422, 0.750)
        p.line_to_rel(-5.058, 13.528)
        p.line_to_rel(13.686, 4.614)
        p.line_to_rel(-8.520, 11.661)
        p.line_to_rel(11.933, 8.135)
        p.line_to_rel(-11.351, 8.930)
        p.line_to_rel(9.296, 11.053)
        p.line_to_rel(-13.338, 5.536)
        p.line_to_rel(5.969, 13.151)
        p.line_to_rel(-14.337, 1.732)
        p.line_to_abs(126.985, 126.980)
        p.close_path()
    
        p.end()
    
        # path4664_2_
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
        p.stroke_color("#4F3A02")
        p.stroke_width(2.3438)
    
        p.move_to_abs(122.198, 122.193)
        p.line_to_rel(-12.964, -1.998)
        p.line_to_rel(-1.573, 13.021)
        p.line_to_rel(-11.943, -5.421)
        p.line_to_rel(-5.028, 12.113)
        p.line_to_rel(-10.039, -8.442)
        p.line_to_rel(-8.110, 10.309)
        p.line_to_rel(-7.388, -10.838)
        p.line_to_rel(-10.591, 7.738)
        p.line_to_rel(-4.189, -12.430)
        p.line_to_rel(-12.286, 4.594)
        p.line_to_rel(-0.682, -13.099)
        p.line_to_rel(-13.069, 1.108)
        p.line_to_rel(2.878, -12.797)
        p.line_to_rel(-12.884, -2.459)
        p.line_to_rel(6.224, -11.545)
        p.line_to_abs(8.810, 86.205)
        p.line_to_rel(9.108, -9.438)
        p.line_to_rel(-9.731, -8.795)
        p.line_to_rel(11.317, -6.631)
        p.line_to_rel(-6.997, -11.094)
        p.line_to_rel(12.686, -3.333)
        p.line_to_rel(-3.745, -12.570)
        p.line_to_rel(13.114, 0.214)
        p.line_to_rel(-0.214, -13.114)
        p.line_to_rel(12.571, 3.744)
        p.line_to_rel(3.332, -12.686)
        p.line_to_rel(11.094, 6.997)
        p.line_to_rel(6.631, -11.317)
        p.line_to_rel(8.794, 9.731)
        p.line_to_rel(9.439, -9.107)
        p.line_to_rel(5.844, 11.742)
        p.line_to_rel(11.545, -6.223)
        p.line_to_rel(2.459, 12.884)
        p.line_to_rel(12.797, -2.878)
        p.line_to_rel(-1.109, 13.069)
        p.line_to_rel(13.099, 0.681)
        p.line_to_rel(-4.594, 12.286)
        p.line_to_rel(12.430, 4.190)
        p.line_to_rel(-7.738, 10.591)
        p.line_to_rel(10.838, 7.387)
        p.line_to_rel(-10.309, 8.111)
        p.line_to_rel(8.443, 10.038)
        p.line_to_abs(127.800, 95.712)
        p.line_to_rel(5.421, 11.943)
        p.line_to_rel(-13.021, 1.574)
        p.line_to_abs(122.198, 122.193)
        p.close_path()
    
        p.end()
    
        # path4666_2_
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
        p.stroke_color("#4F3A02")
        p.stroke_width(2.3438)
    
        p.move_to_abs(127.975, 115.604)
        p.line_to_rel(-13.112, -0.288)
        p.line_to_rel(0.139, 13.115)
        p.line_to_rel(-12.549, -3.814)
        p.line_to_rel(-3.404, 12.664)
        p.line_to_rel(-11.055, -7.059)
        p.line_to_rel(-6.695, 11.279)
        p.line_to_rel(-8.739, -9.781)
        p.line_to_rel(-9.490, 9.054)
        p.line_to_rel(-5.776, -11.775)
        p.line_to_rel(-11.581, 6.157)
        p.line_to_rel(-2.385, -12.898)
        p.line_to_rel(-12.813, 2.807)
        p.line_to_rel(1.183, -13.063)
        p.line_to_rel(-13.095, -0.757)
        p.line_to_rel(4.664, -12.260)
        p.line_to_rel(-12.405, -4.261)
        p.line_to_rel(7.797, -10.545)
        p.line_to_abs(7.863, 76.728)
        p.line_to_rel(10.354, -8.051)
        p.line_to_abs(9.832, 58.591)
        p.line_to_rel(12.142, -4.960)
        p.line_to_rel(-5.353, -11.975)
        p.line_to_rel(13.030, -1.499)
        p.line_to_rel(-1.924, -12.974)
        p.line_to_rel(12.952, 2.071)
        p.line_to_rel(1.647, -13.013)
        p.line_to_rel(11.913, 5.489)
        p.line_to_rel(5.097, -12.085)
        p.line_to_rel(9.990, 8.500)
        p.line_to_rel(8.169, -10.262)
        p.line_to_rel(7.326, 10.880)
        p.line_to_rel(10.635, -7.678)
        p.line_to_rel(4.119, 12.453)
        p.line_to_rel(12.312, -4.523)
        p.line_to_rel(0.606, 13.102)
        p.line_to_rel(13.076, -1.034)
        p.line_to_rel(-2.951, 12.780)
        p.line_to_rel(12.870, 2.532)
        p.line_to_rel(-6.289, 11.510)
        p.line_to_rel(11.709, 5.911)
        p.line_to_rel(-9.162, 9.386)
        p.line_to_rel(9.681, 8.851)
        p.line_to_rel(-11.354, 6.567)
        p.line_to_rel(6.934, 11.133)
        p.line_to_rel(-12.705, 3.261)
        p.line_to_abs(127.975, 115.604)
        p.close_path()
    
        p.end()
    
        # path4658_2_
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
    
        p.move_to_abs(122.198, 122.193)
        p.line_to_rel(-12.964, -1.998)
        p.line_to_rel(-1.573, 13.021)
        p.line_to_rel(-11.943, -5.421)
        p.line_to_rel(-5.028, 12.113)
        p.line_to_rel(-10.039, -8.442)
        p.line_to_rel(-8.110, 10.309)
        p.line_to_rel(-7.388, -10.838)
        p.line_to_rel(-10.591, 7.738)
        p.line_to_rel(-4.189, -12.430)
        p.line_to_rel(-12.286, 4.594)
        p.line_to_rel(-0.682, -13.099)
        p.line_to_rel(-13.069, 1.108)
        p.line_to_rel(2.878, -12.797)
        p.line_to_rel(-12.884, -2.459)
        p.line_to_rel(6.224, -11.545)
        p.line_to_abs(8.810, 86.205)
        p.line_to_rel(9.108, -9.438)
        p.line_to_rel(-9.731, -8.795)
        p.line_to_rel(11.317, -6.631)
        p.line_to_rel(-6.997, -11.094)
        p.line_to_rel(12.686, -3.333)
        p.line_to_rel(-3.745, -12.570)
        p.line_to_rel(13.114, 0.214)
        p.line_to_rel(-0.214, -13.114)
        p.line_to_rel(12.571, 3.744)
        p.line_to_rel(3.332, -12.686)
        p.line_to_rel(11.094, 6.997)
        p.line_to_rel(6.631, -11.317)
        p.line_to_rel(8.794, 9.731)
        p.line_to_rel(9.439, -9.107)
        p.line_to_rel(5.844, 11.742)
        p.line_to_rel(11.545, -6.223)
        p.line_to_rel(2.459, 12.884)
        p.line_to_rel(12.797, -2.878)
        p.line_to_rel(-1.109, 13.069)
        p.line_to_rel(13.099, 0.681)
        p.line_to_rel(-4.594, 12.286)
        p.line_to_rel(12.430, 4.190)
        p.line_to_rel(-7.738, 10.591)
        p.line_to_rel(10.838, 7.387)
        p.line_to_rel(-10.309, 8.111)
        p.line_to_rel(8.443, 10.038)
        p.line_to_abs(127.800, 95.712)
        p.line_to_rel(5.421, 11.943)
        p.line_to_rel(-13.021, 1.574)
        p.line_to_abs(122.198, 122.193)
        p.close_path()
    
        p.end()
    
        # path4660_2_
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
    
        p.move_to_abs(127.975, 115.604)
        p.line_to_rel(-13.112, -0.288)
        p.line_to_rel(0.139, 13.115)
        p.line_to_rel(-12.549, -3.814)
        p.line_to_rel(-3.404, 12.666)
        p.line_to_rel(-11.055, -7.061)
        p.line_to_rel(-6.695, 11.279)
        p.line_to_rel(-8.739, -9.781)
        p.line_to_rel(-9.490, 9.054)
        p.line_to_rel(-5.776, -11.775)
        p.line_to_rel(-11.581, 6.157)
        p.line_to_rel(-2.385, -12.898)
        p.line_to_rel(-12.813, 2.807)
        p.line_to_rel(1.183, -13.063)
        p.line_to_rel(-13.095, -0.757)
        p.line_to_rel(4.664, -12.260)
        p.line_to_rel(-12.405, -4.261)
        p.line_to_rel(7.797, -10.545)
        p.line_to_rel(-10.795, -7.450)
        p.line_to_rel(10.354, -8.052)
        p.line_to_abs(9.832, 58.591)
        p.line_to_rel(12.142, -4.960)
        p.line_to_rel(-5.353, -11.974)
        p.line_to_rel(13.030, -1.500)
        p.line_to_rel(-1.924, -12.974)
        p.line_to_rel(12.952, 2.071)
        p.line_to_rel(1.647, -13.013)
        p.line_to_rel(11.913, 5.489)
        p.line_to_rel(5.097, -12.084)
        p.line_to_rel(9.990, 8.499)
        p.line_to_rel(8.169, -10.262)
        p.line_to_rel(7.326, 10.880)
        p.line_to_rel(10.635, -7.678)
        p.line_to_rel(4.119, 12.453)
        p.line_to_rel(12.312, -4.523)
        p.line_to_rel(0.606, 13.102)
        p.line_to_rel(13.076, -1.034)
        p.line_to_rel(-2.951, 12.780)
        p.line_to_rel(12.870, 2.533)
        p.line_to_abs(129.200, 57.905)
        p.line_to_rel(11.709, 5.911)
        p.line_to_rel(-9.162, 9.386)
        p.line_to_rel(9.681, 8.851)
        p.line_to_rel(-11.354, 6.567)
        p.line_to_rel(6.934, 11.133)
        p.line_to_rel(-12.705, 3.261)
        p.line_to_abs(127.975, 115.604)
        p.close_path()
    
        p.end()
    
        # path4676_2_
        p = Path()
    
        g.add(p)
    
        p.move_to_abs(28.957, 74.800)
        p.curve_to_cubic_rel(46.244, -44.243, 0.553, -24.986, 21.256, -44.794)
        p.curve_to_cubic_rel(44.244, 46.240, 24.986, 0.551, 44.795, 21.253)
        p.curve_to_cubic_rel(-46.237, 44.248, -0.550, 24.988, -21.250, 44.798)
        p.curve_to_cubic_rel(-44.250, -46.236, -24.987, -0.549, -44.798, -21.248)
    
        p.end()
    
        # path4695_2_
        p = Path()
    
        g.add(p)
        p.fill("#E6B52D")
        p.stroke_color("#E6B52D")
        p.stroke_width(1.695)
    
        p.move_to_abs(59.792, 125.185)
        p.curve_to_cubic_rel(-34.974, -63.792, -27.273, -7.959, -42.931, -36.520)
        p.curve_to_cubic_rel(63.789, -34.978, 7.957, -27.273, 36.515, -42.933)
        p.curve_to_cubic_rel(34.980, 63.789, 27.273, 7.955, 42.934, 36.514)
        p.curve_to_cubic_rel(-63.786, 34.982, -7.955, 27.273, -36.512, 42.936)
    
        p.end()
    
        # path4693_2_
        p = Path()
    
        g.add(p)
        p.fill("#FFFBCC")
    
        p.move_to_abs(59.792, 125.185)
        p.curve_to_cubic_rel(-34.974, -63.792, -27.273, -7.959, -42.931, -36.520)
        p.curve_to_cubic_rel(63.789, -34.978, 7.957, -27.273, 36.515, -42.933)
        p.curve_to_cubic_rel(34.980, 63.789, 27.273, 7.955, 42.934, 36.514)
        p.curve_to_cubic_rel(-63.786, 34.982, -7.955, 27.273, -36.512, 42.936)
    
        p.end()
        #endregion crown

    #region drawing
    # path4209
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(57.584, 157.119)
    p.curve_to_cubic_rel(4.736, -2.650, 0.000, 0.000, 0.782, -2.650)
    p.curve_to_cubic_rel(5.344, 2.824, 3.954, 0.000, 5.213, 1.348)
    p.curve_to_cubic_rel(-0.565, 3.779, 0.130, 1.479, -0.565, 3.779)
    p.line_to_rel(1.173, 2.521)
    p.line_to_rel(-5.865, 2.563)
    p.line_to_rel(-2.955, -2.000)
    p.curve_to_cubic_rel(-4.952, 2.564, 0.000, 0.000, -2.911, 2.783)
    p.curve_to_cubic_rel(-6.518, -6.908, -2.042, -0.217, -6.387, -1.912)
    p.curve_to_cubic_smooth_rel(4.518, -4.996, 4.518, -4.996)
    p.curve_to_cubic_smooth_abs(57.584, 157.119, 54.370, 154.556)
    p.close_path()
    
    p.end()
    
    # path4213
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(55.195, 160.162)
    p.curve_to_cubic_rel(-1.325, 1.041, 0.000, 0.574, -0.594, 1.041)
    p.curve_to_cubic_rel(-1.326, -1.041, -0.733, 0.000, -1.326, -0.467)
    p.curve_to_cubic_rel(1.326, -1.043, 0.000, -0.576, 0.593, -1.043)
    p.curve_to_cubic_abs(55.195, 160.162, 54.601, 159.119, 55.195, 159.585)
    p.close_path()
    
    p.end()
    
    # path4215
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(60.582, 163.462)
    p.line_to_rel(1.042, 0.043)
    p.line_to_rel(0.304, 1.045)
    p.line_to_abs(60.582, 163.462)
    p.close_path()
    
    p.end()
    
    # path4209-5
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(85.978, 157.548)
    p.curve_to_cubic_rel(4.735, -2.650, 0.000, 0.000, 0.781, -2.650)
    p.curve_to_cubic_smooth_rel(5.345, 2.824, 5.214, 1.346)
    p.curve_to_cubic_rel(-0.564, 3.779, 0.129, 1.477, -0.564, 3.779)
    p.line_to_rel(1.172, 2.520)
    p.line_to_rel(-5.865, 2.563)
    p.line_to_rel(-2.954, -1.998)
    p.curve_to_cubic_rel(-4.952, 2.563, 0.000, 0.000, -2.911, 2.781)
    p.curve_to_cubic_rel(-6.518, -6.906, -2.043, -0.217, -6.387, -1.912)
    p.curve_to_cubic_rel(4.519, -4.996, -0.130, -4.996, 4.519, -4.996)
    p.curve_to_cubic_smooth_abs(85.978, 157.548, 82.763, 154.984)
    p.close_path()
    
    p.end()
    
    # path4213-4
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(83.588, 160.589)
    p.curve_to_cubic_rel(-1.325, 1.043, 0.000, 0.576, -0.593, 1.043)
    p.curve_to_cubic_smooth_rel(-1.325, -1.043, -1.325, -0.467)
    p.curve_to_cubic_smooth_rel(1.325, -1.043, 0.593, -1.043)
    p.curve_to_cubic_smooth_abs(83.588, 160.589, 83.588, 160.013)
    p.close_path()
    
    p.end()
    
    # path4215-3
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(88.976, 163.890)
    p.line_to_rel(1.042, 0.043)
    p.line_to_rel(0.305, 1.045)
    p.line_to_abs(88.976, 163.890)
    p.close_path()
    
    p.end()
    
    # path4096
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(58.975, 136.351)
    p.curve_to_cubic_rel(1.738, 6.952, 0.000, 0.000, 1.607, 3.910)
    p.curve_to_cubic_rel(0.087, 13.382, 0.130, 3.041, 0.087, 13.382)
    p.curve_to_cubic_smooth_rel(1.434, 0.391, -0.130, 0.348)
    p.curve_to_cubic_smooth_rel(2.041, -0.609, 2.041, -0.609)
    p.line_to_rel(-0.172, -11.772)
    p.curve_to_cubic_rel(-0.391, -2.693, 0.000, 0.000, -0.196, -2.063)
    p.curve_to_cubic_rel(-1.738, -5.909, -0.526, -1.696, -1.738, -5.909)
    p.line_to_rel(-1.694, -0.869)
    p.line_to_abs(58.975, 136.351)
    p.line_to_abs(58.975, 136.351)
    p.close_path()
    
    p.end()
    
    # path4096-7
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(58.975, 136.372)
    p.curve_to_cubic_rel(1.434, 4.683, 0.000, 0.000, 1.375, 4.021)
    p.curve_to_cubic_rel(0.358, 1.803, 0.041, 0.455, 0.358, 1.803)
    p.curve_to_cubic_smooth_rel(0.988, 0.294, 0.217, 0.305)
    p.curve_to_cubic_rel(2.042, -0.608, 1.565, -0.022, 2.042, -0.608)
    p.curve_to_cubic_rel(-0.087, -0.521, -0.217, -1.258, 0.059, 0.746)
    p.curve_to_cubic_rel(-1.738, -5.908, -0.185, -1.766, -1.738, -5.908)
    p.line_to_rel(-1.694, -0.869)
    p.line_to_abs(58.975, 136.372)
    p.line_to_abs(58.975, 136.372)
    p.close_path()
    
    p.end()
    
    # path4131
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(61.252, 145.539)
    p.line_to_rel(2.336, -0.061)
    
    p.end()
    
    # path4131-6
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(61.314, 147.660)
    p.line_to_rel(2.336, -0.063)
    
    p.end()
    
    # path4096-8
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(87.257, 136.851)
    p.curve_to_cubic_rel(1.738, 6.949, 0.000, 0.000, 1.608, 3.910)
    p.curve_to_cubic_rel(0.087, 13.383, 0.131, 3.043, 0.087, 13.383)
    p.curve_to_cubic_smooth_rel(1.435, 0.391, -0.130, 0.348)
    p.curve_to_cubic_rel(2.041, -0.607, 1.563, 0.045, 2.041, -0.607)
    p.line_to_rel(-0.173, -11.773)
    p.curve_to_cubic_rel(-0.392, -2.695, 0.000, 0.000, -0.196, -2.064)
    p.curve_to_cubic_rel(-1.738, -5.908, -0.525, -1.693, -1.738, -5.908)
    p.line_to_rel(-1.693, -0.869)
    p.line_to_abs(87.257, 136.851)
    p.line_to_abs(87.257, 136.851)
    p.close_path()
    
    p.end()
    
    # path4096-7-9
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(87.257, 136.871)
    p.curve_to_cubic_rel(1.434, 4.682, 0.000, 0.000, 1.375, 4.021)
    p.curve_to_cubic_rel(0.359, 1.803, 0.042, 0.455, 0.359, 1.803)
    p.curve_to_cubic_smooth_rel(0.988, 0.293, 0.217, 0.305)
    p.curve_to_cubic_rel(2.043, -0.607, 1.564, -0.021, 2.043, -0.607)
    p.curve_to_cubic_rel(-0.088, -0.521, -0.219, -1.257, 0.058, 0.746)
    p.curve_to_cubic_rel(-1.738, -5.908, -0.184, -1.764, -1.738, -5.908)
    p.line_to_rel(-1.693, -0.870)
    p.line_to_abs(87.257, 136.871)
    p.line_to_abs(87.257, 136.871)
    p.close_path()
    
    p.end()
    
    # path4131-2
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(89.537, 146.037)
    p.line_to_rel(2.336, -0.061)
    
    p.end()
    
    # path4131-6-7
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(89.599, 148.158)
    p.line_to_rel(2.334, -0.063)
    
    p.end()
    
    # path4273
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(40.510, 92.992)
    p.curve_to_cubic_rel(-2.520, 4.563, 0.000, 0.000, -2.433, 3.129)
    p.curve_to_cubic_rel(0.260, 5.215, -0.087, 1.434, -0.652, 4.519)
    p.curve_to_cubic_rel(3.737, 1.042, 0.912, 0.695, 3.737, 1.042)
    p.line_to_abs(40.510, 92.992)
    p.close_path()
    
    p.end()
    
    # path4275
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(40.553, 111.240)
    p.line_to_rel(0.218, 14.511)
    p.curve_to_cubic_rel(-1.044, 4.214, 0.000, 0.000, -1.260, 1.999)
    p.curve_to_cubic_rel(0.783, 5.561, 0.217, 2.217, -0.695, 4.215)
    p.curve_to_cubic_rel(3.605, 2.260, 1.477, 1.348, 2.998, 2.348)
    p.curve_to_cubic_rel(1.087, -0.174, 0.609, -0.086, 1.087, -0.174)
    p.curve_to_cubic_smooth_rel(1.303, 0.912, 0.260, 0.957)
    p.curve_to_cubic_rel(2.085, -1.736, 1.042, -0.043, 2.259, -0.824)
    p.curve_to_cubic_rel(-1.868, -3.521, -0.173, -0.912, -1.781, -2.607)
    p.curve_to_cubic_rel(-0.175, -0.858, -0.024, -0.255, -0.168, -0.652)
    p.curve_to_cubic_rel(0.088, -0.703, -0.032, -1.015, 0.088, -0.703)
    p.line_to_rel(0.412, 0.947)
    p.line_to_rel(0.761, 0.963)
    p.curve_to_cubic_rel(1.521, 0.479, 0.000, 0.000, 1.130, 0.826)
    p.curve_to_cubic_rel(0.565, -1.607, 0.391, -0.350, 0.870, -0.653)
    p.curve_to_cubic_rel(-1.521, -2.695, -0.305, -0.957, -1.478, -2.130)
    p.curve_to_cubic_rel(-0.348, -2.606, -0.044, -0.563, -0.348, -2.606)
    p.line_to_rel(-1.650, -16.205)
    p.line_to_abs(40.553, 111.240)
    p.line_to_abs(40.553, 111.240)
    p.close_path()
    
    p.end()
    
    # path4279
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(43.966, 132.648)
    p.curve_to_cubic_rel(0.365, 2.951, 0.000, 0.000, 0.081, 2.425)
    p.curve_to_cubic_rel(0.807, 1.816, 0.282, 0.525, 0.807, 1.816)
    
    p.end()
    
    # path4281
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(41.421, 132.206)
    p.curve_to_cubic_rel(0.161, 2.827, 0.000, 0.000, -0.081, 2.141)
    p.curve_to_cubic_rel(0.727, 1.858, 0.242, 0.687, 0.727, 1.858)
    
    p.end()
    
    # path4094
    p = Path()
    
    g.add(p)
    p.fill("#C76A27")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(54.978, 125.707)
    p.line_to_rel(-3.259, 8.299)
    p.curve_to_cubic_rel(8.385, 2.260, 0.000, 0.000, 4.041, 2.303)
    p.curve_to_cubic_rel(8.560, -2.086, 4.345, -0.043, 8.560, -2.086)
    p.line_to_rel(-0.521, -5.431)
    p.line_to_rel(15.641, 1.955)
    p.line_to_rel(-2.607, 5.214)
    p.curve_to_cubic_rel(8.776, 2.172, 0.000, 0.000, 5.463, 2.260)
    p.curve_to_cubic_rel(8.212, -3.865, 5.772, -0.150, 8.212, -3.865)
    p.line_to_rel(-2.781, -5.692)
    p.line_to_abs(54.978, 125.707)
    p.close_path()
    
    p.end()
    
    # path3997
    p = Path()
    
    g.add(p)
    p.fill("#C76A27")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(43.332, 117.089)
    p.line_to_rel(-0.082, 10.695)
    p.line_to_rel(50.312, 4.942)
    p.line_to_rel(12.492, -4.463)
    p.line_to_rel(-0.076, -11.181)
    p.line_to_rel(-3.180, -0.643)
    p.line_to_rel(-11.667, 2.105)
    p.line_to_rel(-2.999, 0.893)
    p.line_to_rel(-9.722, -0.973)
    p.line_to_rel(-12.722, -1.945)
    p.line_to_rel(-8.588, 0.406)
    p.line_to_rel(-11.588, -0.081)
    p.line_to_abs(43.332, 117.089)
    p.close_path()
    
    p.end()
    
    # path3997-2
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(43.365, 110.078)
    p.line_to_rel(-0.081, 8.264)
    p.line_to_rel(50.400, 3.813)
    p.line_to_rel(12.229, -4.377)
    p.line_to_rel(0.187, -6.314)
    p.line_to_rel(-3.179, -0.121)
    p.line_to_rel(-11.668, 1.585)
    p.line_to_rel(-2.998, 0.631)
    p.line_to_rel(-9.723, -1.233)
    p.line_to_rel(-12.721, 0.142)
    p.line_to_rel(-8.589, -1.247)
    p.line_to_rel(-11.587, -0.688)
    p.line_to_abs(43.365, 110.078)
    p.line_to_abs(43.365, 110.078)
    p.close_path()
    
    p.end()
    
    # path4277
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(93.333, 116.167)
    p.line_to_rel(-0.079, 16.481)
    
    p.end()
    
    # path4022
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(45.288, 120.277)
    p.line_to_rel(8.604, 0.608)
    p.line_to_vertical_rel(3.433)
    p.line_to_rel(-8.646, -0.697)
    p.line_to_abs(45.288, 120.277)
    p.line_to_abs(45.288, 120.277)
    p.close_path()
    
    p.end()
    
    # path4022-3
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(56.867, 121.210)
    p.line_to_rel(17.988, 1.260)
    p.line_to_rel(0.043, 3.303)
    p.line_to_rel(-18.074, -1.129)
    p.line_to_abs(56.867, 121.210)
    p.line_to_abs(56.867, 121.210)
    p.close_path()
    
    p.end()
    
    # path4022-6
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(78.764, 122.818)
    p.line_to_rel(11.165, 0.607)
    p.line_to_rel(0.044, 3.434)
    p.line_to_rel(-11.253, -0.695)
    p.line_to_abs(78.764, 122.818)
    p.line_to_abs(78.764, 122.818)
    p.close_path()
    
    p.end()
    
    # path4022-5
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(103.138, 119.691)
    p.line_to_rel(-7.473, 3.039)
    p.line_to_rel(0.087, 3.738)
    p.line_to_rel(7.473, -3.172)
    p.line_to_abs(103.138, 119.691)
    p.line_to_abs(103.138, 119.691)
    p.close_path()
    
    p.end()
    
    # path4087
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(56.107, 110.979)
    p.line_to_rel(-0.044, 2.478)
    p.curve_to_cubic_rel(2.086, 3.692, 0.000, 0.000, 1.000, 3.736)
    p.curve_to_cubic_rel(4.388, -4.866, 1.086, -0.043, 4.388, -4.866)
    p.line_to_rel(6.691, 0.043)
    p.curve_to_cubic_rel(3.433, 5.605, 0.000, 0.000, 2.129, 5.648)
    p.curve_to_cubic_rel(5.388, -3.780, 1.302, -0.044, 5.430, -1.695)
    p.curve_to_cubic_rel(-1.564, -2.606, -0.045, -2.086, -1.564, -2.606)
    p.line_to_rel(-11.297, -1.130)
    p.line_to_rel(-4.909, 0.042)
    p.line_to_abs(56.107, 110.979)
    p.close_path()
    
    p.end()
    
    # path4089
    p = Path()
    
    g.add(p)
    p.fill("#FF4128")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(62.712, 112.847)
    p.curve_to_cubic_rel(-0.247, 2.337, 0.000, 0.010, -0.405, 1.220)
    p.curve_to_cubic_rel(1.203, 2.313, 0.156, 1.106, 0.873, 2.122)
    p.curve_to_cubic_rel(-2.652, 6.907, 0.202, 0.116, -2.652, 6.907)
    p.line_to_rel(3.042, 3.779)
    p.line_to_rel(5.127, -3.172)
    p.line_to_rel(-2.693, -7.298)
    p.curve_to_cubic_rel(3.519, -3.737, 0.000, 0.000, 3.475, -2.782)
    p.curve_to_cubic_smooth_rel(-0.782, -1.173, -0.782, -1.173)
    p.line_to_rel(-4.431, 0.043)
    p.line_to_abs(62.712, 112.847)
    p.line_to_abs(62.712, 112.847)
    p.close_path()
    
    p.end()
    
    # path4091
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(63.928, 117.800)
    p.line_to_rel(2.477, -0.043)
    
    p.end()
    
    # path3606
    p = Path()
    
    g.add(p)
    p.fill("#EEE67B")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(100.897, 45.523)
    p.line_to_rel(3.602, -0.492)
    p.curve_to_cubic_rel(2.046, 2.538, 0.000, 0.000, 1.515, 0.368)
    p.curve_to_cubic_rel(1.719, 4.460, 0.532, 2.169, 0.696, 2.782)
    p.curve_to_cubic_rel(4.624, 3.806, 1.023, 1.678, 3.969, 2.251)
    p.curve_to_cubic_rel(0.860, 3.806, 0.655, 1.556, 0.368, 2.947)
    p.curve_to_cubic_rel(3.479, 3.929, 0.491, 0.859, 3.233, 1.637)
    p.curve_to_cubic_rel(-3.520, 9.536, 0.246, 2.292, -3.643, 6.834)
    p.curve_to_cubic_smooth_rel(0.941, 4.747, 1.188, 2.537)
    p.curve_to_cubic_smooth_rel(-2.660, 4.993, -2.456, 3.274)
    p.curve_to_cubic_rel(-0.123, 5.238, -0.205, 1.720, 0.654, 3.274)
    p.curve_to_cubic_smooth_rel(-2.170, 3.970, -1.924, 2.455)
    p.curve_to_cubic_rel(-0.245, 4.297, -0.245, 1.514, -0.245, 4.297)
    p.line_to_rel(-0.286, 12.073)
    p.curve_to_cubic_rel(-0.164, 3.028, 0.000, 0.000, 0.655, 1.964)
    p.curve_to_cubic_smooth_rel(-3.029, 1.801, -3.029, 1.801)
    p.curve_to_cubic_smooth_rel(-3.314, -0.204, -1.881, -0.572)
    p.curve_to_cubic_rel(-3.682, 2.414, -1.432, 0.368, -2.332, 1.924)
    p.curve_to_cubic_rel(-3.480, 1.064, -1.352, 0.492, -2.907, 1.392)
    p.curve_to_cubic_rel(-2.496, -1.228, -0.572, -0.327, -2.496, -1.228)
    p.line_to_abs(100.897, 45.523)
    p.line_to_abs(100.897, 45.523)
    p.close_path()
    
    p.end()
    
    # path3603
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(42.333, 44.991)
    p.curve_to_cubic_rel(3.031, 0.573, 0.000, 0.000, 0.657, 0.573)
    p.curve_to_cubic_rel(5.583, -1.521, 2.375, 0.000, 2.064, -1.521)
    p.curve_to_cubic_rel(6.037, 1.604, 3.521, 0.000, 2.107, 1.521)
    p.curve_to_cubic_rel(6.006, -1.801, 3.929, 0.082, 1.013, -1.719)
    p.curve_to_cubic_rel(7.008, 1.719, 4.993, -0.082, 2.425, 1.719)
    p.curve_to_cubic_rel(6.302, -1.473, 4.584, 0.000, 3.028, -1.473)
    p.curve_to_cubic_rel(5.566, 1.473, 3.275, 0.000, 1.965, 1.637)
    p.curve_to_cubic_rel(6.303, -1.882, 3.602, -0.164, 3.109, -1.882)
    p.curve_to_cubic_rel(6.221, 1.228, 3.191, 0.000, 4.010, 1.228)
    p.curve_to_cubic_smooth_rel(6.549, -1.310, 4.174, -1.473)
    p.curve_to_cubic_rel(4.092, 2.128, 2.373, 0.163, 4.092, 1.146)
    p.curve_to_cubic_smooth_rel(-1.064, 6.629, 0.082, 4.583)
    p.curve_to_cubic_rel(-2.343, 4.748, -1.146, 2.046, -2.343, 3.274)
    p.curve_to_cubic_rel(1.034, 7.448, 0.000, 1.473, 1.034, 5.238)
    p.curve_to_cubic_smooth_rel(-3.357, 6.384, -3.275, 4.666)
    p.curve_to_cubic_rel(0.900, 6.794, -0.081, 1.719, 0.983, 4.911)
    p.curve_to_cubic_rel(-2.782, 7.040, -0.081, 1.882, -2.782, 4.501)
    p.curve_to_cubic_rel(1.146, 5.729, 0.000, 2.536, 1.228, 3.683)
    p.curve_to_cubic_rel(-2.291, 7.203, -0.081, 2.045, -2.374, 4.011)
    p.curve_to_cubic_rel(1.309, 5.564, 0.081, 3.191, 1.555, 3.191)
    p.curve_to_cubic_rel(-2.291, 5.157, -0.244, 2.375, -2.209, 2.783)
    p.curve_to_cubic_smooth_rel(1.064, 4.911, 1.228, 3.192)
    p.curve_to_cubic_rel(-2.128, 3.355, -0.164, 1.719, -0.818, 3.273)
    p.curve_to_cubic_smooth_rel(-7.204, -1.473, -5.321, -1.718)
    p.curve_to_cubic_rel(-6.711, 0.737, -1.882, 0.245, -3.520, 0.982)
    p.curve_to_cubic_rel(-7.040, -1.965, -3.191, -0.246, -4.256, -1.965)
    p.curve_to_cubic_rel(-7.366, 0.655, -2.783, 0.000, -3.928, 0.737)
    p.curve_to_cubic_rel(-6.302, -2.211, -3.438, -0.083, -3.602, -2.047)
    p.curve_to_cubic_rel(-5.648, 2.047, -2.702, -0.163, -1.965, 2.538)
    p.curve_to_cubic_rel(-5.504, -2.291, -3.682, -0.492, -2.966, -2.210)
    p.curve_to_cubic_rel(-5.463, 1.145, -2.537, -0.082, -2.354, 1.800)
    p.curve_to_cubic_rel(-3.765, -4.338, -3.110, -0.654, -4.256, -1.964)
    p.curve_to_cubic_rel(1.309, -6.630, 0.490, -2.374, 2.046, -4.011)
    p.curve_to_cubic_rel(-2.046, -4.829, -0.736, -2.620, -2.209, -3.192)
    p.curve_to_cubic_rel(1.310, -5.074, 0.164, -1.638, 1.227, -1.803)
    p.curve_to_cubic_rel(-1.965, -6.631, 0.082, -3.274, -2.374, -3.193)
    p.curve_to_cubic_rel(1.965, -5.647, 0.409, -3.438, 2.292, -3.192)
    p.curve_to_cubic_rel(-2.046, -6.630, -0.327, -2.456, -2.210, -3.520)
    p.curve_to_cubic_rel(1.801, -6.793, 0.164, -3.111, 1.719, -4.583)
    p.curve_to_cubic_rel(-1.883, -5.565, 0.082, -2.209, -1.883, -2.455)
    p.curve_to_cubic_rel(1.964, -5.812, 0.000, -3.111, 1.801, -3.274)
    p.curve_to_cubic_rel(-1.146, -6.875, 0.165, -2.537, -0.982, -4.338)
    p.curve_to_cubic_rel(1.833, -3.215, -0.098, -1.516, 0.715, -2.693)
    p.curve_to_cubic_abs(42.333, 44.991, 41.074, 44.944, 41.007, 44.860)
    p.line_to_abs(42.333, 44.991)
    p.close_path()
    
    p.end()
    
    # path3841
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(48.264, 72.702)
    p.curve_to_cubic_rel(-5.547, -1.514, 0.000, 0.000, -3.766, -2.123)
    p.curve_to_cubic_rel(-2.881, 3.798, -1.781, 0.609, -2.738, 0.917)
    p.curve_to_cubic_rel(4.898, 3.784, -0.232, 4.693, 4.898, 3.784)
    
    p.end()
    
    # path3863
    p = Path()
    
    g.add(p)
    p.fill("#E39A33")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(46.525, 73.638)
    p.curve_to_cubic_rel(-0.526, 0.507, 0.000, 0.280, -0.236, 0.507)
    p.curve_to_cubic_rel(-0.527, -0.507, -0.291, 0.000, -0.527, -0.227)
    p.curve_to_cubic_rel(0.527, -0.506, 0.000, -0.279, 0.236, -0.506)
    p.curve_to_cubic_abs(46.525, 73.638, 46.291, 73.131, 46.525, 73.358)
    p.close_path()
    
    p.end()
    
    # path3865
    p = Path()
    
    g.add(p)
    p.fill("#E39A33")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(43.547, 75.653)
    p.curve_to_cubic_rel(-0.536, 0.537, 0.000, 0.296, -0.240, 0.537)
    p.curve_to_cubic_rel(-0.537, -0.537, -0.297, 0.000, -0.537, -0.240)
    p.curve_to_cubic_rel(0.537, -0.537, 0.000, -0.297, 0.241, -0.537)
    p.curve_to_cubic_abs(43.547, 75.653, 43.308, 75.117, 43.547, 75.356)
    p.close_path()
    
    p.end()
    
    # path3867
    p = Path()
    
    g.add(p)
    p.fill("#E39A33")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(46.146, 76.692)
    p.curve_to_cubic_rel(-0.528, 0.526, 0.000, 0.291, -0.237, 0.526)
    p.curve_to_cubic_smooth_rel(-0.527, -0.526, -0.527, -0.236)
    p.curve_to_cubic_rel(0.527, -0.527, 0.000, -0.291, 0.236, -0.527)
    p.curve_to_cubic_abs(46.146, 76.692, 45.911, 76.166, 46.146, 76.401)
    p.close_path()
    
    p.end()
    
    # path3611
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(109.177, 64.189)
    p.curve_to_cubic_rel(-2.084, 5.556, 0.000, 3.068, -0.934, 5.556)
    p.curve_to_cubic_smooth_rel(-2.084, -5.556, -2.084, -2.488)
    p.curve_to_cubic_rel(2.084, -5.557, 0.000, -3.069, 0.934, -5.557)
    p.curve_to_cubic_smooth_abs(109.177, 64.189, 109.177, 61.121)
    p.close_path()
    
    p.end()
    
    # path3613
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(108.946, 78.891)
    p.curve_to_cubic_rel(-1.272, 2.488, 0.000, 1.374, -0.570, 2.488)
    p.curve_to_cubic_rel(-1.273, -2.488, -0.704, 0.000, -1.273, -1.115)
    p.curve_to_cubic_rel(1.273, -2.489, 0.000, -1.375, 0.569, -2.489)
    p.curve_to_cubic_abs(108.946, 78.891, 108.375, 76.401, 108.946, 77.516)
    p.close_path()
    
    p.end()
    
    # path3615
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(105.126, 89.250)
    p.curve_to_cubic_rel(-2.432, 4.167, 0.000, 2.302, -1.089, 4.167)
    p.curve_to_cubic_rel(-2.431, -4.167, -1.342, 0.000, -2.431, -1.865)
    p.curve_to_cubic_rel(2.431, -4.167, 0.000, -2.301, 1.089, -4.167)
    p.curve_to_cubic_abs(105.126, 89.250, 104.038, 85.083, 105.126, 86.949)
    p.close_path()
    
    p.end()
    
    # path3615-1
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(91.224, 96.427)
    p.curve_to_cubic_rel(-1.471, 1.787, 0.000, 0.986, -0.658, 1.787)
    p.curve_to_cubic_smooth_rel(-1.469, -1.787, -1.469, -0.801)
    p.curve_to_cubic_rel(1.469, -1.789, 0.000, -0.988, 0.657, -1.789)
    p.curve_to_cubic_abs(91.224, 96.427, 90.566, 94.638, 91.224, 95.439)
    p.close_path()
    
    p.end()
    
    # path3615-4
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(87.170, 105.542)
    p.curve_to_cubic_rel(-3.210, 4.096, 0.000, 2.262, -1.438, 4.096)
    p.curve_to_cubic_rel(-3.210, -4.096, -1.773, 0.000, -3.210, -1.834)
    p.curve_to_cubic_smooth_rel(3.210, -4.095, 1.437, -4.095)
    p.curve_to_cubic_abs(87.170, 105.542, 85.732, 101.448, 87.170, 103.281)
    p.close_path()
    
    p.end()
    
    # path3615-9
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(49.932, 104.542)
    p.curve_to_cubic_rel(-0.685, 2.307, 0.306, 1.080, 0.000, 2.112)
    p.curve_to_cubic_rel(-1.793, -1.604, -0.685, 0.193, -1.487, -0.523)
    p.curve_to_cubic_rel(0.686, -2.307, -0.307, -1.080, 0.000, -2.112)
    p.curve_to_cubic_abs(49.932, 104.542, 48.823, 102.746, 49.625, 103.463)
    p.close_path()
    
    p.end()
    
    # path3615-8
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(48.737, 94.027)
    p.curve_to_cubic_rel(-1.555, 4.415, 0.459, 2.157, -0.236, 4.134)
    p.curve_to_cubic_rel(-3.219, -3.398, -1.319, 0.280, -2.760, -1.241)
    p.curve_to_cubic_rel(1.556, -4.415, -0.459, -2.158, 0.236, -4.135)
    p.curve_to_cubic_abs(48.737, 94.027, 46.836, 90.347, 48.277, 91.869)
    p.close_path()
    
    p.end()
    
    # path3615-2
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(46.008, 52.631)
    p.curve_to_cubic_rel(-1.489, 2.394, 0.000, 1.322, -0.667, 2.394)
    p.curve_to_cubic_rel(-1.487, -2.394, -0.821, 0.000, -1.487, -1.071)
    p.curve_to_cubic_rel(1.487, -2.393, 0.000, -1.321, 0.667, -2.393)
    p.curve_to_cubic_abs(46.008, 52.631, 45.341, 50.238, 46.008, 51.310)
    p.close_path()
    
    p.end()
    
    # path3615-5
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(96.083, 54.029)
    p.curve_to_cubic_rel(-2.642, 3.710, 0.000, 2.049, -1.183, 3.710)
    p.curve_to_cubic_smooth_rel(-2.643, -3.710, -2.643, -1.661)
    p.curve_to_cubic_smooth_rel(2.643, -3.709, 1.184, -3.709)
    p.curve_to_cubic_smooth_abs(96.083, 54.029, 96.083, 51.980)
    p.close_path()
    
    p.end()
    
    # path3615-7
    p = Path()
    
    g.add(p)
    p.fill("#B2B548")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(95.373, 65.170)
    p.curve_to_cubic_rel(-1.304, 1.784, 0.000, 0.984, -0.584, 1.784)
    p.curve_to_cubic_smooth_rel(-1.304, -1.784, -1.304, -0.798)
    p.curve_to_cubic_rel(1.304, -1.784, 0.000, -0.985, 0.584, -1.784)
    p.curve_to_cubic_smooth_abs(95.373, 65.170, 95.373, 64.186)
    p.close_path()
    
    p.end()
    
    # path3884
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(45.640, 79.908)
    p.line_to_rel(3.094, -1.661)
    
    p.end()
    
    # path3886
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(56.354, 84.894)
    p.line_to_rel(0.114, 7.047)
    p.curve_to_cubic_rel(3.208, 0.516, 0.000, 0.000, 0.974, 0.457)
    p.curve_to_cubic_rel(4.069, -0.630, 2.234, 0.057, 4.069, -0.630)
    p.line_to_vertical_rel(-5.730)
    
    p.end()
    
    # path3888
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(65.521, 85.982)
    p.line_to_rel(0.114, 6.588)
    p.curve_to_cubic_rel(3.953, 0.573, 0.000, 0.000, 1.891, 0.688)
    p.curve_to_cubic_rel(3.954, -0.401, 2.063, -0.114, 3.954, -0.401)
    p.line_to_rel(-0.115, -7.734)
    
    p.end()
    
    # path3882
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(85.489, 79.621)
    p.curve_to_cubic_rel(-20.168, 6.187, 0.000, 0.000, -7.333, 6.302)
    p.curve_to_cubic_rel(-17.590, -6.531, -12.834, -0.113, -17.590, -6.531)
    
    p.end()
    
    # path3912
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(54.223, 95.374)
    p.curve_to_cubic_rel(4.213, 2.472, 0.000, 0.000, 1.661, 2.472)
    p.curve_to_cubic_smooth_rel(5.550, -1.418, 3.322, -1.378)
    p.curve_to_cubic_rel(6.807, 2.756, 2.229, -0.041, 4.376, 2.715)
    p.curve_to_cubic_rel(5.875, -3.445, 2.431, 0.040, 5.875, -3.445)
    
    p.end()
    
    # path3702
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(67.019, 64.421)
    p.curve_to_cubic_rel(-10.648, 10.405, 0.000, 5.747, -4.767, 10.405)
    p.curve_to_cubic_rel(-10.647, -10.405, -5.881, 0.000, -10.647, -4.658)
    p.curve_to_cubic_smooth_rel(10.647, -10.405, 4.766, -10.405)
    p.curve_to_cubic_smooth_abs(67.019, 64.421, 67.019, 58.675)
    p.close_path()
    
    p.end()
    
    # path3702-1
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(88.498, 65.312)
    p.curve_to_cubic_rel(-12.032, 11.790, 0.000, 6.511, -5.387, 11.790)
    p.curve_to_cubic_smooth_rel(-12.032, -11.790, -12.032, -5.278)
    p.curve_to_cubic_rel(12.032, -11.789, 0.000, -6.511, 5.386, -11.789)
    p.curve_to_cubic_smooth_abs(88.498, 65.312, 88.498, 58.801)
    p.close_path()
    
    p.end()
    
    # path3729
    p = Path()
    
    g.add(p)
    p.fill("#74CBDE")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(62.482, 64.410)
    p.curve_to_cubic_rel(-4.375, 4.213, 0.000, 2.327, -1.959, 4.213)
    p.curve_to_cubic_rel(-4.376, -4.213, -2.417, 0.000, -4.376, -1.887)
    p.curve_to_cubic_rel(4.376, -4.214, 0.000, -2.327, 1.958, -4.214)
    p.curve_to_cubic_abs(62.482, 64.410, 60.523, 60.196, 62.482, 62.083)
    p.close_path()
    
    p.end()
    
    # path3754
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(60.006, 64.399)
    p.curve_to_cubic_rel(-1.985, 1.863, 0.000, 1.029, -0.889, 1.863)
    p.curve_to_cubic_smooth_rel(-1.985, -1.863, -1.985, -0.834)
    p.curve_to_cubic_smooth_rel(1.985, -1.864, 0.888, -1.864)
    p.curve_to_cubic_smooth_abs(60.006, 64.399, 60.006, 63.370)
    p.close_path()
    
    p.end()
    
    # path3729-1
    p = Path()
    
    g.add(p)
    p.fill("#74CBDE")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(76.574, 65.180)
    p.curve_to_cubic_rel(-4.570, 4.487, 0.000, 2.479, -2.046, 4.487)
    p.curve_to_cubic_rel(-4.570, -4.487, -2.524, 0.000, -4.570, -2.009)
    p.curve_to_cubic_rel(4.570, -4.488, 0.000, -2.479, 2.045, -4.488)
    p.curve_to_cubic_abs(76.574, 65.180, 74.527, 60.691, 76.574, 62.701)
    p.close_path()
    
    p.end()
    
    # path3756
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(74.024, 65.168)
    p.curve_to_cubic_rel(-2.188, 2.147, 0.000, 1.186, -0.980, 2.147)
    p.curve_to_cubic_rel(-2.188, -2.147, -1.208, 0.000, -2.188, -0.961)
    p.curve_to_cubic_rel(2.188, -2.147, 0.000, -1.186, 0.979, -2.147)
    p.curve_to_cubic_abs(74.024, 65.168, 73.044, 63.022, 74.024, 63.983)
    p.close_path()
    
    p.end()
    
    # path3914
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(50.900, 52.146)
    p.line_to_rel(1.540, 2.835)
    
    p.end()
    
    # path3914-5
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(63.705, 52.349)
    p.line_to_rel(-2.516, 2.995)
    
    p.end()
    
    # path3914-5-2
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(57.143, 50.040)
    p.line_to_rel(0.036, 4.170)
    
    p.end()
    
    # path3914-6
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(70.508, 51.436)
    p.line_to_rel(1.540, 2.836)
    
    p.end()
    
    # path3914-5-1
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(83.314, 51.640)
    p.line_to_rel(-2.518, 2.996)
    
    p.end()
    
    # path3914-5-2-4
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(76.750, 49.331)
    p.line_to_rel(0.036, 4.170)
    
    p.end()
    
    # path3833
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(92.751, 73.618)
    p.curve_to_cubic_rel(-8.953, -0.891, 0.000, 0.000, -6.386, -2.888)
    p.curve_to_cubic_rel(-1.453, 1.743, -0.762, 0.592, -1.115, 1.111)
    p.curve_to_cubic_rel(-0.047, 4.740, -0.715, 1.342, -0.762, 2.886)
    p.curve_to_cubic_rel(4.134, 2.957, 0.564, 1.459, 2.027, 2.390)
    p.curve_to_cubic_smooth_rel(4.335, -0.081, 4.335, -0.081)
    
    p.end()
    
    # path3835
    p = Path()
    
    g.add(p)
    p.fill("#E39A33")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(87.486, 75.177)
    p.curve_to_cubic_rel(-0.648, 0.668, 0.000, 0.369, -0.291, 0.668)
    p.curve_to_cubic_rel(-0.648, -0.668, -0.358, 0.000, -0.648, -0.299)
    p.curve_to_cubic_rel(0.648, -0.668, 0.000, -0.369, 0.290, -0.668)
    p.curve_to_cubic_abs(87.486, 75.177, 87.195, 74.509, 87.486, 74.809)
    p.close_path()
    
    p.end()
    
    # path3837
    p = Path()
    
    g.add(p)
    p.fill("#E39A33")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(92.589, 76.251)
    p.curve_to_cubic_rel(-0.648, 0.648, 0.000, 0.358, -0.290, 0.648)
    p.curve_to_cubic_rel(-0.648, -0.648, -0.357, 0.000, -0.648, -0.290)
    p.curve_to_cubic_smooth_rel(0.648, -0.648, 0.291, -0.648)
    p.curve_to_cubic_abs(92.589, 76.251, 92.299, 75.603, 92.589, 75.893)
    p.close_path()
    
    p.end()
    
    # path3839
    p = Path()
    
    g.add(p)
    p.fill("#E39A33")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(88.984, 78.844)
    p.curve_to_cubic_rel(-0.668, 0.688, 0.000, 0.380, -0.299, 0.688)
    p.curve_to_cubic_smooth_rel(-0.669, -0.688, -0.669, -0.309)
    p.curve_to_cubic_rel(0.669, -0.689, 0.000, -0.381, 0.300, -0.689)
    p.curve_to_cubic_abs(88.984, 78.844, 88.685, 78.155, 88.984, 78.463)
    p.line_to_abs(88.984, 78.844)
    p.close_path()
    
    p.end()
    
    # path3859
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(65.406, 75.153)
    p.curve_to_cubic_rel(-6.989, -0.745, 0.000, 0.000, -3.010, 0.271)
    p.curve_to_cubic_rel(-5.844, -2.865, -2.061, -0.526, -3.418, -2.381)
    p.curve_to_cubic_rel(-3.667, 0.344, -2.162, -0.431, -2.616, -0.396)
    p.curve_to_cubic_rel(-0.803, 4.125, -0.469, 0.330, -2.444, 1.919)
    p.curve_to_cubic_rel(5.558, 3.380, 1.834, 2.463, 4.066, 3.104)
    p.curve_to_cubic_rel(5.042, 0.344, 1.077, 0.199, 3.553, 0.401)
    p.curve_to_cubic_rel(4.469, -0.344, 1.490, -0.057, 3.495, -0.172)
    p.curve_to_cubic_rel(1.891, -0.458, 0.974, -0.171, 1.891, -0.458)
    
    p.end()
    
    # path4254
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(104.419, 107.503)
    p.line_to_rel(0.219, 20.898)
    p.curve_to_cubic_rel(-1.609, 3.604, 0.000, 0.000, -1.521, 1.260)
    p.curve_to_cubic_rel(0.045, 7.169, -0.086, 2.347, 0.045, 7.169)
    p.curve_to_cubic_smooth_rel(1.434, 3.173, -0.045, 1.652)
    p.curve_to_cubic_rel(2.605, 0.739, 1.477, 1.521, 2.605, 0.739)
    p.curve_to_cubic_smooth_rel(1.607, 0.435, 0.695, 0.695)
    p.curve_to_cubic_rel(1.479, -1.391, 0.912, -0.262, 1.479, -1.391)
    p.curve_to_cubic_smooth_rel(2.085, 0.043, 0.693, 0.607)
    p.curve_to_cubic_rel(1.130, -2.085, 1.390, -0.564, 1.477, -1.781)
    p.curve_to_cubic_rel(-3.215, -3.432, -0.348, -0.305, -3.215, -3.432)
    p.curve_to_cubic_rel(-2.869, -8.777, 0.377, -3.797, -0.988, -5.703)
    p.line_to_rel(0.174, -20.377)
    p.line_to_horizontal_abs(104.419)
    p.line_to_abs(104.419, 107.503)
    p.close_path()
    
    p.end()
    
    # path4258
    p = Path()
    
    g.add(p)
    p.fill("#FDF66A")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(102.856, 137.089)
    p.curve_to_cubic_rel(-1.694, 1.781, 0.000, 0.000, -1.660, 0.350)
    p.curve_to_cubic_rel(1.912, 1.521, -0.045, 1.781, 1.912, 1.521)
    
    p.end()
    
    # path4260
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(105.115, 137.003)
    p.curve_to_cubic_rel(0.521, 3.432, 0.000, 0.000, -0.435, 1.955)
    p.curve_to_cubic_rel(1.911, 2.868, 0.955, 1.477, 1.911, 2.868)
    
    p.end()
    
    # path4262
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(107.375, 136.308)
    p.curve_to_cubic_rel(0.955, 3.041, 0.000, 0.000, -0.088, 1.650)
    p.curve_to_cubic_rel(2.043, 2.868, 1.043, 1.392, 2.043, 2.868)
    
    p.end()
    
    # path4270
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.4943)
    
    p.move_to_abs(106.332, 92.905)
    p.curve_to_cubic_rel(2.953, 2.304, 0.000, 0.000, 2.259, 0.132)
    p.curve_to_cubic_rel(0.914, 3.867, 0.695, 2.172, 0.564, 3.215)
    p.curve_to_cubic_rel(1.520, 5.256, 0.348, 0.650, 1.779, 3.344)
    p.curve_to_cubic_smooth_rel(-4.822, 4.084, -1.434, 4.127)
    p.curve_to_cubic_smooth_rel(-5.736, -2.477, -5.604, -0.869)
    p.curve_to_cubic_rel(1.260, -9.168, -0.129, -1.607, 0.928, -8.375)
    p.curve_to_cubic_rel(1.349, -2.563, 0.350, -0.824, 0.392, -1.520)
    p.curve_to_cubic_abs(106.332, 92.905, 104.724, 93.166, 105.028, 92.905)
    p.close_path()
    
    p.end()
    #endregion drawing

# Patrick Star
def person_b(x, y, scale_x, scale_y, crown):
    g = PathGroup()

    width = 150.000 * scale_x
    height = 167.160 * scale_y

    g.translate(-width / 2.0, -height)
    g.scale(scale_x, scale_y)
    g.translate(x, y)

    if crown:
        #region crown
        # path4672
        p = Path()
    
        g.add(p)
        p.fill("#870303")
    
        p.move_to_abs(68.390, 0.000)
        p.line_to_rel(-0.498, 0.853)
        p.line_to_rel(-5.751, 9.822)
        p.line_to_abs(52.504, 4.600)
        p.line_to_abs(51.671, 4.070)
        p.line_to_rel(-0.250, 0.958)
        p.line_to_abs(48.527, 16.040)
        p.line_to_rel(-10.912, -3.249)
        p.line_to_rel(-0.946, -0.281)
        p.line_to_rel(0.013, 0.984)
        p.line_to_rel(0.187, 11.384)
        p.line_to_rel(-11.385, -0.187)
        p.line_to_rel(-0.990, -0.012)
        p.line_to_rel(0.287, 0.946)
        p.line_to_rel(3.249, 10.912)
        p.line_to_rel(-11.017, 2.894)
        p.line_to_rel(-0.953, 0.250)
        p.line_to_rel(0.529, 0.834)
        p.line_to_rel(6.075, 9.629)
        p.line_to_rel(-9.829, 5.758)
        p.line_to_rel(-0.853, 0.504)
        p.line_to_rel(0.734, 0.660)
        p.line_to_rel(8.447, 7.637)
        p.line_to_rel(-7.905, 8.192)
        p.line_to_rel(-0.685, 0.709)
        p.line_to_rel(0.884, 0.442)
        p.line_to_rel(10.196, 5.073)
        p.line_to_rel(-5.403, 10.022)
        p.line_to_rel(-0.473, 0.871)
        p.line_to_rel(0.971, 0.187)
        p.line_to_rel(11.186, 2.129)
        p.line_to_rel(-2.497, 11.110)
        p.line_to_rel(-0.217, 0.965)
        p.line_to_rel(0.983, -0.080)
        p.line_to_rel(11.341, -0.965)
        p.line_to_rel(0.598, 11.372)
        p.line_to_rel(0.049, 0.983)
        p.line_to_rel(0.928, -0.343)
        p.line_to_rel(10.663, -3.989)
        p.line_to_rel(3.635, 10.794)
        p.line_to_rel(0.317, 0.934)
        p.line_to_rel(0.797, -0.587)
        p.line_to_rel(9.193, -6.715)
        p.line_to_rel(6.418, 9.411)
        p.line_to_rel(0.554, 0.815)
        p.line_to_rel(0.610, -0.779)
        p.line_to_rel(7.041, -8.943)
        p.line_to_rel(8.714, 7.325)
        p.line_to_rel(0.759, 0.637)
        p.line_to_rel(0.381, -0.916)
        p.line_to_rel(4.363, -10.513)
        p.line_to_rel(10.369, 4.705)
        p.line_to_rel(0.896, 0.404)
        p.line_to_rel(0.119, -0.977)
        p.line_to_rel(1.369, -11.305)
        p.line_to_rel(11.254, 1.737)
        p.line_to_rel(0.971, 0.149)
        p.line_to_rel(-0.149, -0.978)
        p.line_to_rel(-1.736, -11.254)
        p.line_to_rel(11.310, -1.369)
        p.line_to_rel(0.978, -0.118)
        p.line_to_rel(-0.405, -0.896)
        p.line_to_rel(-4.705, -10.370)
        p.line_to_rel(10.514, -4.363)
        p.line_to_rel(0.914, -0.380)
        p.line_to_rel(-0.641, -0.753)
        p.line_to_rel(-7.326, -8.714)
        p.line_to_rel(8.951, -7.045)
        p.line_to_rel(0.771, -0.611)
        p.line_to_rel(-0.815, -0.554)
        p.line_to_rel(-9.405, -6.411)
        p.line_to_rel(6.717, -9.200)
        p.line_to_rel(0.585, -0.796)
        p.line_to_rel(-0.940, -0.311)
        p.line_to_rel(-10.787, -3.642)
        p.line_to_rel(3.984, -10.662)
        p.line_to_rel(0.348, -0.927)
        p.line_to_rel(-0.982, -0.050)
        p.line_to_rel(-11.379, -0.591)
        p.line_to_rel(0.965, -11.348)
        p.line_to_rel(0.087, -0.983)
        p.line_to_rel(-0.965, 0.218)
        p.line_to_rel(-11.104, 2.502)
        p.line_to_abs(102.184, 6.760)
        p.line_to_rel(-0.188, -0.964)
        p.line_to_rel(-0.865, 0.467)
        p.line_to_rel(-10.021, 5.402)
        p.line_to_abs(86.036, 1.469)
        p.line_to_rel(-0.442, -0.884)
        p.line_to_abs(84.885, 1.270)
        p.line_to_rel(-8.197, 7.911)
        p.line_to_rel(-7.632, -8.452)
        p.line_to_abs(68.390, 0.000)
        p.line_to_abs(68.390, 0.000)
        p.close_path()
        p.move_to_abs(68.645, 2.434)
        p.line_to_rel(7.469, 8.273)
        p.line_to_rel(0.505, 0.553)
        p.line_to_rel(0.535, -0.522)
        p.line_to_abs(85.178, 3.000)
        p.line_to_rel(4.967, 9.978)
        p.line_to_rel(0.330, 0.673)
        p.line_to_rel(0.660, -0.355)
        p.line_to_rel(9.815, -5.291)
        p.line_to_rel(2.085, 10.949)
        p.line_to_rel(0.144, 0.734)
        p.line_to_rel(0.729, -0.162)
        p.line_to_rel(10.880, -2.446)
        p.line_to_rel(-0.945, 11.104)
        p.line_to_rel(-0.063, 0.748)
        p.line_to_rel(0.747, 0.038)
        p.line_to_rel(11.130, 0.579)
        p.line_to_rel(-3.903, 10.438)
        p.line_to_rel(-0.262, 0.704)
        p.line_to_rel(0.710, 0.236)
        p.line_to_rel(10.557, 3.561)
        p.line_to_rel(-6.573, 9.000)
        p.line_to_rel(-0.442, 0.604)
        p.line_to_rel(0.623, 0.423)
        p.line_to_rel(9.206, 6.280)
        p.line_to_rel(-8.758, 6.891)
        p.line_to_rel(-0.591, 0.460)
        p.line_to_rel(0.484, 0.573)
        p.line_to_rel(7.178, 8.535)
        p.line_to_rel(-10.302, 4.270)
        p.line_to_rel(-0.685, 0.292)
        p.line_to_rel(0.305, 0.678)
        p.line_to_rel(4.612, 10.152)
        p.line_to_rel(-11.073, 1.332)
        p.line_to_rel(-0.741, 0.094)
        p.line_to_rel(0.112, 0.740)
        p.line_to_rel(1.699, 11.018)
        p.line_to_rel(-11.018, -1.699)
        p.line_to_rel(-0.734, -0.117)
        p.line_to_rel(-0.094, 0.746)
        p.line_to_rel(-1.338, 11.061)
        p.line_to_rel(-10.146, -4.605)
        p.line_to_rel(-0.684, -0.306)
        p.line_to_rel(-0.287, 0.691)
        p.line_to_rel(-4.270, 10.295)
        p.line_to_rel(-8.534, -7.176)
        p.line_to_rel(-0.572, -0.479)
        p.line_to_rel(-0.461, 0.584)
        p.line_to_rel(-6.897, 8.758)
        p.line_to_rel(-6.274, -9.205)
        p.line_to_rel(-0.423, -0.617)
        p.line_to_rel(-0.604, 0.437)
        p.line_to_rel(-9.000, 6.579)
        p.line_to_rel(-3.561, -10.564)
        p.line_to_rel(-0.236, -0.709)
        p.line_to_rel(-0.704, 0.262)
        p.line_to_rel(-10.438, 3.903)
        p.line_to_rel(-0.579, -11.130)
        p.line_to_rel(-0.043, -0.746)
        p.line_to_rel(-0.741, 0.062)
        p.line_to_rel(-11.111, 0.946)
        p.line_to_rel(2.446, -10.881)
        p.line_to_rel(0.168, -0.728)
        p.line_to_rel(-0.734, -0.138)
        p.line_to_rel(-10.949, -2.091)
        p.line_to_rel(5.284, -9.816)
        p.line_to_rel(0.355, -0.654)
        p.line_to_rel(-0.666, -0.336)
        p.line_to_rel(-9.984, -4.960)
        p.line_to_rel(7.743, -8.024)
        p.line_to_rel(0.517, -0.542)
        p.line_to_rel(-0.554, -0.498)
        p.line_to_rel(-8.272, -7.476)
        p.line_to_rel(9.623, -5.640)
        p.line_to_rel(0.642, -0.374)
        p.line_to_rel(-0.398, -0.635)
        p.line_to_rel(-5.945, -9.424)
        p.line_to_rel(10.781, -2.838)
        p.line_to_rel(0.722, -0.187)
        p.line_to_rel(-0.212, -0.716)
        p.line_to_rel(-3.187, -10.681)
        p.line_to_rel(11.148, 0.181)
        p.line_to_rel(0.747, 0.013)
        p.line_to_rel(-0.012, -0.748)
        p.line_to_rel(-0.174, -11.148)
        p.line_to_rel(10.681, 3.181)
        p.line_to_rel(0.716, 0.218)
        p.line_to_rel(0.187, -0.729)
        p.line_to_rel(2.832, -10.781)
        p.line_to_rel(9.430, 5.951)
        p.line_to_rel(0.629, 0.398)
        p.line_to_rel(0.379, -0.647)
        p.line_to_abs(68.645, 2.434)
        p.line_to_abs(68.645, 2.434)
        p.close_path()
    
        p.end()
    
        # path4662_1_
        p = Path()
    
        g.add(p)
        p.fill("#E60000")
    
        p.move_to_abs(118.680, 106.693)
        p.line_to_rel(-11.992, -1.849)
        p.line_to_rel(-1.457, 12.046)
        p.line_to_rel(-11.049, -5.015)
        p.line_to_rel(-4.652, 11.207)
        p.line_to_rel(-9.287, -7.810)
        p.line_to_rel(-7.503, 9.536)
        p.line_to_rel(-6.835, -10.026)
        p.line_to_rel(-9.798, 7.158)
        p.line_to_rel(-3.876, -11.498)
        p.line_to_rel(-11.367, 4.249)
        p.line_to_rel(-0.630, -12.118)
        p.line_to_abs(28.142, 103.600)
        p.line_to_rel(2.663, -11.839)
        p.line_to_rel(-11.919, -2.274)
        p.line_to_rel(5.758, -10.682)
        p.line_to_rel(-10.864, -5.407)
        p.line_to_rel(8.426, -8.732)
        p.line_to_rel(-9.002, -8.137)
        p.line_to_rel(10.469, -6.134)
        p.line_to_rel(-6.473, -10.264)
        p.line_to_rel(11.736, -3.083)
        p.line_to_rel(-3.464, -11.630)
        p.line_to_rel(12.133, 0.198)
        p.line_to_rel(-0.198, -12.133)
        p.line_to_rel(11.630, 3.464)
        p.line_to_rel(3.083, -11.736)
        p.line_to_rel(10.264, 6.473)
        p.line_to_rel(6.135, -10.470)
        p.line_to_rel(8.137, 9.002)
        p.line_to_rel(8.731, -8.425)
        p.line_to_rel(5.406, 10.863)
        p.line_to_rel(10.682, -5.758)
        p.line_to_rel(2.274, 11.920)
        p.line_to_rel(11.840, -2.662)
        p.line_to_rel(-1.026, 12.091)
        p.line_to_rel(12.118, 0.630)
        p.line_to_rel(-4.250, 11.367)
        p.line_to_rel(11.499, 3.876)
        p.line_to_rel(-7.159, 9.798)
        p.line_to_rel(10.027, 6.835)
        p.line_to_rel(-9.537, 7.503)
        p.line_to_rel(7.811, 9.287)
        p.line_to_rel(-11.207, 4.652)
        p.line_to_rel(5.016, 11.050)
        p.line_to_abs(116.832, 94.700)
        p.line_to_abs(118.680, 106.693)
        p.close_path()
    
        p.end()
    
        # path4664
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
        p.stroke_color("#4F3A02")
        p.stroke_width(1.9693)
    
        p.move_to_abs(114.657, 102.669)
        p.line_to_rel(-10.892, -1.678)
        p.line_to_rel(-1.322, 10.941)
        p.line_to_rel(-10.035, -4.556)
        p.line_to_rel(-4.226, 10.179)
        p.line_to_rel(-8.435, -7.094)
        p.line_to_rel(-6.814, 8.661)
        p.line_to_rel(-6.208, -9.106)
        p.line_to_rel(-8.899, 6.502)
        p.line_to_rel(-3.521, -10.443)
        p.line_to_rel(-10.323, 3.859)
        p.line_to_rel(-0.573, -11.006)
        p.line_to_abs(32.430, 99.861)
        p.line_to_rel(2.418, -10.752)
        p.line_to_rel(-10.825, -2.065)
        p.line_to_rel(5.229, -9.702)
        p.line_to_rel(-9.867, -4.910)
        p.line_to_rel(7.653, -7.931)
        p.line_to_rel(-8.176, -7.390)
        p.line_to_rel(9.509, -5.571)
        p.line_to_rel(-5.879, -9.321)
        p.line_to_rel(10.659, -2.800)
        p.line_to_rel(-3.146, -10.562)
        p.line_to_rel(11.019, 0.180)
        p.line_to_rel(-0.180, -11.020)
        p.line_to_rel(10.562, 3.146)
        p.line_to_rel(2.800, -10.659)
        p.line_to_rel(9.322, 5.879)
        p.line_to_rel(5.572, -9.508)
        p.line_to_rel(7.389, 8.176)
        p.line_to_rel(7.932, -7.653)
        p.line_to_rel(4.909, 9.866)
        p.line_to_rel(9.701, -5.229)
        p.line_to_rel(2.065, 10.825)
        p.line_to_rel(10.752, -2.418)
        p.line_to_rel(-0.932, 10.981)
        p.line_to_rel(11.007, 0.572)
        p.line_to_rel(-3.860, 10.323)
        p.line_to_rel(10.443, 3.520)
        p.line_to_rel(-6.501, 8.899)
        p.line_to_rel(9.106, 6.207)
        p.line_to_rel(-8.662, 6.815)
        p.line_to_rel(7.094, 8.435)
        p.line_to_rel(-10.178, 4.225)
        p.line_to_rel(4.555, 10.037)
        p.line_to_rel(-10.941, 1.321)
        p.line_to_abs(114.657, 102.669)
        p.close_path()
    
        p.end()
    
        # path4666
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
        p.stroke_color("#4F3A02")
        p.stroke_width(1.9693)
    
        p.move_to_abs(119.512, 97.134)
        p.line_to_rel(-11.018, -0.243)
        p.line_to_rel(0.117, 11.021)
        p.line_to_rel(-10.545, -3.205)
        p.line_to_rel(-2.859, 10.641)
        p.line_to_rel(-9.289, -5.931)
        p.line_to_rel(-5.625, 9.477)
        p.line_to_rel(-7.343, -8.218)
        p.line_to_rel(-7.974, 7.607)
        p.line_to_rel(-4.854, -9.895)
        p.line_to_rel(-9.730, 5.174)
        p.line_to_rel(-2.004, -10.836)
        p.line_to_rel(-10.766, 2.355)
        p.line_to_rel(0.994, -10.975)
        p.line_to_abs(27.613, 93.470)
        p.line_to_rel(3.918, -10.300)
        p.line_to_rel(-10.423, -3.580)
        p.line_to_rel(6.552, -8.862)
        p.line_to_rel(-9.071, -6.260)
        p.line_to_rel(8.700, -6.765)
        p.line_to_rel(-7.045, -8.475)
        p.line_to_rel(10.202, -4.167)
        p.line_to_rel(-4.498, -10.062)
        p.line_to_rel(10.948, -1.259)
        p.line_to_abs(35.281, 22.840)
        p.line_to_rel(10.882, 1.741)
        p.line_to_rel(1.384, -10.933)
        p.line_to_rel(10.009, 4.612)
        p.line_to_abs(61.840, 8.105)
        p.line_to_rel(8.394, 7.141)
        p.line_to_rel(6.864, -8.623)
        p.line_to_rel(6.155, 9.142)
        p.line_to_rel(8.936, -6.451)
        p.line_to_rel(3.461, 10.463)
        p.line_to_rel(10.345, -3.801)
        p.line_to_rel(0.510, 11.009)
        p.line_to_rel(10.986, -0.869)
        p.line_to_rel(-2.479, 10.739)
        p.line_to_rel(10.813, 2.127)
        p.line_to_rel(-5.283, 9.671)
        p.line_to_rel(9.838, 4.966)
        p.line_to_rel(-7.697, 7.887)
        p.line_to_rel(8.133, 7.436)
        p.line_to_rel(-9.539, 5.518)
        p.line_to_rel(5.826, 9.354)
        p.line_to_rel(-10.676, 2.739)
        p.line_to_abs(119.512, 97.134)
        p.close_path()
    
        p.end()
    
        # path4658
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
    
        p.move_to_abs(114.657, 102.669)
        p.line_to_rel(-10.892, -1.678)
        p.line_to_rel(-1.322, 10.941)
        p.line_to_rel(-10.035, -4.556)
        p.line_to_rel(-4.226, 10.179)
        p.line_to_rel(-8.435, -7.094)
        p.line_to_rel(-6.814, 8.661)
        p.line_to_rel(-6.208, -9.106)
        p.line_to_rel(-8.899, 6.502)
        p.line_to_rel(-3.521, -10.443)
        p.line_to_rel(-10.323, 3.859)
        p.line_to_rel(-0.573, -11.006)
        p.line_to_abs(32.430, 99.861)
        p.line_to_rel(2.418, -10.752)
        p.line_to_rel(-10.825, -2.065)
        p.line_to_rel(5.229, -9.702)
        p.line_to_rel(-9.867, -4.910)
        p.line_to_rel(7.653, -7.931)
        p.line_to_rel(-8.176, -7.390)
        p.line_to_rel(9.509, -5.571)
        p.line_to_rel(-5.879, -9.321)
        p.line_to_rel(10.659, -2.800)
        p.line_to_rel(-3.146, -10.562)
        p.line_to_rel(11.019, 0.180)
        p.line_to_rel(-0.180, -11.020)
        p.line_to_rel(10.562, 3.146)
        p.line_to_rel(2.800, -10.659)
        p.line_to_rel(9.322, 5.879)
        p.line_to_rel(5.572, -9.508)
        p.line_to_rel(7.389, 8.176)
        p.line_to_rel(7.932, -7.653)
        p.line_to_rel(4.909, 9.866)
        p.line_to_rel(9.701, -5.229)
        p.line_to_rel(2.065, 10.825)
        p.line_to_rel(10.752, -2.418)
        p.line_to_rel(-0.932, 10.981)
        p.line_to_rel(11.007, 0.572)
        p.line_to_rel(-3.860, 10.323)
        p.line_to_rel(10.443, 3.520)
        p.line_to_rel(-6.501, 8.899)
        p.line_to_rel(9.106, 6.207)
        p.line_to_rel(-8.662, 6.815)
        p.line_to_rel(7.094, 8.435)
        p.line_to_rel(-10.178, 4.225)
        p.line_to_rel(4.555, 10.037)
        p.line_to_rel(-10.941, 1.321)
        p.line_to_abs(114.657, 102.669)
        p.close_path()
    
        p.end()
    
        # path4660
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
    
        p.move_to_abs(119.512, 97.134)
        p.line_to_rel(-11.018, -0.243)
        p.line_to_rel(0.117, 11.021)
        p.line_to_rel(-10.545, -3.205)
        p.line_to_rel(-2.859, 10.643)
        p.line_to_rel(-9.289, -5.933)
        p.line_to_rel(-5.625, 9.477)
        p.line_to_rel(-7.343, -8.218)
        p.line_to_rel(-7.974, 7.607)
        p.line_to_rel(-4.854, -9.895)
        p.line_to_rel(-9.730, 5.174)
        p.line_to_rel(-2.004, -10.836)
        p.line_to_rel(-10.766, 2.355)
        p.line_to_rel(0.994, -10.975)
        p.line_to_abs(27.613, 93.470)
        p.line_to_rel(3.918, -10.300)
        p.line_to_rel(-10.423, -3.580)
        p.line_to_rel(6.552, -8.862)
        p.line_to_rel(-9.071, -6.260)
        p.line_to_rel(8.700, -6.765)
        p.line_to_rel(-7.045, -8.475)
        p.line_to_rel(10.202, -4.167)
        p.line_to_rel(-4.498, -10.062)
        p.line_to_rel(10.948, -1.259)
        p.line_to_abs(35.281, 22.840)
        p.line_to_rel(10.882, 1.741)
        p.line_to_rel(1.384, -10.933)
        p.line_to_rel(10.009, 4.612)
        p.line_to_abs(61.840, 8.105)
        p.line_to_rel(8.394, 7.141)
        p.line_to_rel(6.864, -8.623)
        p.line_to_rel(6.155, 9.142)
        p.line_to_rel(8.935, -6.451)
        p.line_to_rel(3.462, 10.463)
        p.line_to_rel(10.345, -3.801)
        p.line_to_rel(0.510, 11.009)
        p.line_to_rel(10.986, -0.869)
        p.line_to_rel(-2.479, 10.739)
        p.line_to_rel(10.813, 2.127)
        p.line_to_rel(-5.283, 9.671)
        p.line_to_rel(9.838, 4.966)
        p.line_to_rel(-7.697, 7.887)
        p.line_to_rel(8.133, 7.436)
        p.line_to_rel(-9.539, 5.518)
        p.line_to_rel(5.826, 9.354)
        p.line_to_rel(-10.676, 2.739)
        p.line_to_abs(119.512, 97.134)
        p.close_path()
    
        p.end()
    
        # path4676
        p = Path()
    
        g.add(p)
    
        p.move_to_abs(36.314, 62.849)
        p.curve_to_cubic_rel(38.854, -37.175, 0.464, -20.995, 17.860, -37.638)
        p.curve_to_cubic_rel(37.177, 38.853, 20.994, 0.463, 37.639, 17.858)
        p.curve_to_cubic_rel(-38.851, 37.178, -0.462, 20.995, -17.856, 37.638)
        p.curve_to_cubic_rel(-37.180, -38.849, -20.995, -0.461, -37.641, -17.855)
    
        p.end()
    
        # path4695
        p = Path()
    
        g.add(p)
        p.fill("#E6B52D")
        p.stroke_color("#E6B52D")
        p.stroke_width(1.4242)
    
        p.move_to_abs(62.222, 105.183)
        p.curve_to_cubic_abs(32.835, 51.584, 39.306, 98.498, 26.150, 74.500)
        p.curve_to_cubic_rel(53.598, -29.390, 6.685, -22.916, 30.681, -36.074)
        p.curve_to_cubic_rel(29.391, 53.597, 22.916, 6.685, 36.074, 30.681)
        p.curve_to_cubic_smooth_rel(-53.594, 29.394, -30.678, 36.076)
    
        p.end()
    
        # path4693
        p = Path()
    
        g.add(p)
        p.fill("#FFFBCC")
    
        p.move_to_abs(62.222, 105.183)
        p.curve_to_cubic_abs(32.835, 51.584, 39.306, 98.498, 26.150, 74.500)
        p.curve_to_cubic_rel(53.598, -29.390, 6.685, -22.916, 30.681, -36.074)
        p.curve_to_cubic_rel(29.391, 53.597, 22.916, 6.685, 36.074, 30.681)
        p.curve_to_cubic_smooth_rel(-53.594, 29.394, -30.678, 36.076)
    
        p.end()
        #endregion crown

    #region drawing
    # path3710
    p = Path()
    
    g.add(p)
    p.fill("#F13301")
    
    p.move_to_abs(113.378, 80.589)
    p.curve_to_cubic_rel(-1.353, 0.478, -0.470, 0.516, -1.075, 0.729)
    p.curve_to_cubic_rel(0.354, -1.391, -0.274, -0.252, -0.117, -0.874)
    p.curve_to_cubic_rel(1.351, -0.478, 0.471, -0.515, 1.076, -0.729)
    p.curve_to_cubic_abs(113.378, 80.589, 114.008, 79.451, 113.850, 80.073)
    p.close_path()
    
    p.end()
    
    # path3712-8
    p = Path()
    
    g.add(p)
    p.fill("#F13301")
    
    p.move_to_abs(37.450, 66.832)
    p.curve_to_cubic_rel(0.751, 1.112, 0.577, 0.333, 0.914, 0.831)
    p.curve_to_cubic_rel(-1.338, -0.093, -0.163, 0.281, -0.762, 0.240)
    p.curve_to_cubic_rel(-0.750, -1.112, -0.577, -0.334, -0.913, -0.832)
    p.curve_to_cubic_abs(37.450, 66.832, 36.275, 66.458, 36.874, 66.498)
    p.close_path()
    
    p.end()
    
    # path3610
    p = Path()
    
    g.add(p)
    p.fill("#FC886F")
    p.stroke_color("#F13301")
    p.stroke_width(0.6242)
    
    p.move_to_abs(55.912, 73.168)
    p.curve_to_cubic_rel(-17.633, -11.811, 0.000, 0.000, -12.144, -6.655)
    p.curve_to_cubic_rel(-17.966, -11.644, -5.489, -5.156, -14.752, -14.026)
    p.curve_to_cubic_rel(1.498, 15.803, -3.402, 2.521, -2.495, 7.819)
    p.curve_to_cubic_rel(10.813, 20.127, 3.992, 7.985, 4.657, 11.645)
    p.curve_to_cubic_rel(11.810, 13.475, 6.304, 8.689, 11.810, 13.475)
    
    p.end()
    
    # path3603_1_
    p = Path()
    
    g.add(p)
    p.fill("#FC886F")
    p.stroke_color("#F13301")
    p.stroke_width(0.6242)
    
    p.move_to_abs(45.765, 86.642)
    p.curve_to_cubic_rel(8.151, -13.807, 0.000, 0.000, 6.155, -9.814)
    p.curve_to_cubic_rel(14.307, -33.269, 1.996, -3.993, 14.307, -33.269)
    p.curve_to_cubic_smooth_rel(6.819, -13.309, 3.493, -9.149)
    p.curve_to_cubic_rel(17.134, -15.138, 3.327, -4.159, 12.810, -14.972)
    p.curve_to_cubic_rel(5.323, 6.156, 4.324, -0.166, 5.323, 0.833)
    p.curve_to_cubic_rel(-4.325, 9.814, 0.000, 5.822, -3.493, 6.487)
    p.curve_to_cubic_rel(0.665, 39.757, -1.266, 5.067, -1.663, 32.771)
    p.curve_to_cubic_rel(6.655, 24.120, 2.329, 6.987, 6.655, 24.120)
    p.curve_to_cubic_smooth_rel(7.633, 13.601, 6.455, 9.238)
    p.curve_to_cubic_rel(1.350, 11.852, 1.578, 5.840, 1.350, 11.852)
    p.line_to_rel(-15.471, 22.955)
    p.line_to_rel(2.163, 9.482)
    p.curve_to_cubic_rel(-1.498, 12.975, 0.000, 0.000, 0.167, 10.812)
    p.curve_to_cubic_rel(-6.653, 5.323, -1.663, 2.163, -1.995, 5.489)
    p.curve_to_cubic_smooth_rel(-7.652, -6.654, -6.155, -3.992)
    p.curve_to_cubic_rel(-3.826, -11.644, -1.498, -2.661, -3.826, -11.644)
    p.line_to_rel(-2.329, -11.313)
    p.line_to_rel(-21.625, -1.330)
    p.line_to_rel(4.159, 12.143)
    p.line_to_rel(0.998, 3.160)
    p.curve_to_cubic_rel(-2.662, 7.652, 0.000, 0.000, -0.499, 5.156)
    p.curve_to_cubic_rel(-7.055, 3.131, -2.163, 2.494, -3.772, 4.724)
    p.curve_to_cubic_rel(-6.419, -12.280, -4.661, -2.261, -6.419, -7.290)
    p.curve_to_cubic_rel(1.497, -21.459, 0.000, -4.991, 1.497, -21.459)
    p.line_to_rel(-8.316, -15.802)
    p.curve_to_cubic_rel(-0.167, -7.652, 0.000, 0.000, -0.999, -3.827)
    p.curve_to_cubic_abs(45.765, 86.642, 35.451, 101.281, 46.098, 86.477)
    p.line_to_abs(45.765, 86.642)
    p.close_path()
    
    p.end()
    
    # path3605
    p = Path()
    
    g.add(p)
    p.fill("#FC886F")
    p.stroke_color("#F13301")
    p.stroke_width(0.6242)
    
    p.move_to_abs(90.846, 79.822)
    p.curve_to_cubic_rel(20.129, -16.801, 0.000, 0.000, 15.138, -13.807)
    p.curve_to_cubic_rel(21.458, -9.980, 4.991, -2.993, 18.631, -13.473)
    p.curve_to_cubic_rel(-6.154, 19.962, 2.829, 3.493, 0.999, 10.480)
    p.curve_to_cubic_smooth_rel(-23.122, 30.274, -23.122, 30.274)
    
    p.end()
    
    # path3708
    p = Path()
    
    g.add(p)
    p.fill("#F13301")
    
    p.move_to_abs(87.732, 24.720)
    p.curve_to_cubic_rel(-1.167, 0.920, -0.305, 0.664, -0.828, 1.076)
    p.curve_to_cubic_rel(-0.062, -1.485, -0.339, -0.157, -0.367, -0.821)
    p.curve_to_cubic_rel(1.169, -0.919, 0.305, -0.664, 0.828, -1.075)
    p.curve_to_cubic_abs(87.732, 24.720, 88.010, 23.392, 88.039, 24.056)
    p.close_path()
    
    p.end()
    
    # path3712
    p = Path()
    
    g.add(p)
    p.fill("#F13301")
    
    p.move_to_abs(69.970, 111.097)
    p.curve_to_cubic_rel(-1.066, 0.814, -0.299, 0.594, -0.776, 0.959)
    p.curve_to_cubic_rel(0.016, -1.342, -0.290, -0.146, -0.284, -0.748)
    p.curve_to_cubic_rel(1.066, -0.813, 0.298, -0.596, 0.775, -0.960)
    p.curve_to_cubic_abs(69.970, 111.097, 70.276, 109.901, 70.270, 110.501)
    p.close_path()
    
    p.end()
    
    # path3712-0
    p = Path()
    
    g.add(p)
    p.fill("#F13301")
    
    p.move_to_abs(56.202, 93.060)
    p.curve_to_cubic_rel(-1.283, 0.395, -0.486, 0.455, -1.060, 0.631)
    p.curve_to_cubic_rel(0.479, -1.254, -0.222, -0.238, -0.007, -0.799)
    p.curve_to_cubic_rel(1.282, -0.395, 0.486, -0.455, 1.060, -0.631)
    p.curve_to_cubic_abs(56.202, 93.060, 56.903, 92.044, 56.688, 92.606)
    p.close_path()
    
    p.end()
    
    # path3712-4
    p = Path()
    
    g.add(p)
    p.fill("#F13301")
    
    p.move_to_abs(43.161, 104.100)
    p.curve_to_cubic_rel(-1.024, 0.727, -0.287, 0.530, -0.746, 0.856)
    p.curve_to_cubic_rel(0.015, -1.199, -0.279, -0.130, -0.273, -0.667)
    p.curve_to_cubic_smooth_rel(1.025, -0.728, 0.746, -0.858)
    p.curve_to_cubic_abs(43.161, 104.100, 43.454, 103.031, 43.448, 103.568)
    p.close_path()
    
    p.end()
    
    # path3712-45
    p = Path()
    
    g.add(p)
    p.fill("#F13301")
    
    p.move_to_abs(47.715, 155.673)
    p.curve_to_cubic_rel(-0.193, 1.329, 0.204, 0.635, 0.116, 1.231)
    p.curve_to_cubic_rel(-0.928, -0.969, -0.309, 0.100, -0.724, -0.335)
    p.curve_to_cubic_rel(0.193, -1.329, -0.203, -0.635, -0.115, -1.229)
    p.curve_to_cubic_abs(47.715, 155.673, 47.098, 154.607, 47.513, 155.042)
    p.close_path()
    
    p.end()
    
    # path3814
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(52.096, 115.508)
    p.curve_to_cubic_rel(0.882, 3.882, 0.000, 0.000, -1.118, 2.529)
    p.curve_to_cubic_rel(4.881, 1.118, 2.000, 1.354, 3.882, 1.705)
    p.curve_to_cubic_rel(2.882, -1.765, 1.000, -0.589, 2.882, -1.765)
    
    p.end()
    
    # path3816
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(55.271, 114.451)
    p.curve_to_cubic_rel(-1.294, 2.058, 0.000, 0.000, -1.883, 1.058)
    p.curve_to_cubic_rel(2.117, 1.117, 0.579, 0.985, 1.588, 1.059)
    p.curve_to_cubic_rel(1.353, -0.059, 0.530, 0.060, 1.353, -0.059)
    
    p.end()
    
    # path3613_1_
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(71.130, 56.729)
    p.curve_to_cubic_rel(-9.194, 8.354, -1.244, 5.573, -5.360, 9.313)
    p.curve_to_cubic_rel(-4.690, -11.822, -3.834, -0.957, -5.934, -6.251)
    p.curve_to_cubic_rel(9.194, -8.356, 1.243, -5.572, 5.360, -9.313)
    p.curve_to_cubic_abs(71.130, 56.729, 70.274, 45.864, 72.374, 51.157)
    p.line_to_abs(71.130, 56.729)
    p.close_path()
    
    p.end()
    
    # path3613-1
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(82.816, 57.520)
    p.curve_to_cubic_rel(-9.194, 8.354, -1.242, 5.571, -5.361, 9.313)
    p.curve_to_cubic_rel(-4.690, -11.824, -3.834, -0.957, -5.934, -6.251)
    p.curve_to_cubic_rel(9.195, -8.354, 1.244, -5.571, 5.360, -9.312)
    p.curve_to_cubic_abs(82.816, 57.520, 81.960, 46.654, 84.061, 51.947)
    p.line_to_abs(82.816, 57.520)
    p.close_path()
    
    p.end()
    
    # path3637
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    
    p.move_to_abs(67.083, 55.499)
    p.curve_to_cubic_rel(-2.470, 2.117, -0.362, 1.425, -1.469, 2.373)
    p.curve_to_cubic_smooth_rel(-1.157, -3.042, -1.520, -1.617)
    p.curve_to_cubic_smooth_rel(2.470, -2.117, 1.469, -2.372)
    p.curve_to_cubic_abs(67.083, 55.499, 66.927, 52.712, 67.445, 54.074)
    p.close_path()
    
    p.end()
    
    # path3637-7
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    
    p.move_to_abs(76.932, 56.394)
    p.curve_to_cubic_rel(-2.631, 2.218, -0.387, 1.492, -1.564, 2.485)
    p.curve_to_cubic_rel(-1.231, -3.186, -1.066, -0.268, -1.618, -1.693)
    p.curve_to_cubic_rel(2.630, -2.218, 0.386, -1.492, 1.563, -2.486)
    p.curve_to_cubic_abs(76.932, 56.394, 76.766, 53.474, 77.317, 54.901)
    p.close_path()
    
    p.end()
    
    # path3703
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    
    p.move_to_abs(78.974, 38.935)
    p.curve_to_cubic_rel(-0.530, -1.647, 0.000, 0.000, -1.058, -1.235)
    p.curve_to_cubic_rel(3.469, 1.471, 0.530, -0.412, 2.527, 0.706)
    p.curve_to_cubic_rel(1.648, 2.117, 0.943, 0.765, 2.412, 1.706)
    p.curve_to_cubic_rel(-1.823, -0.235, -0.765, 0.412, -1.823, -0.235)
    p.curve_to_cubic_smooth_rel(0.765, 1.765, 1.647, 1.412)
    p.curve_to_cubic_smooth_rel(-3.706, -1.881, -2.766, -0.940)
    p.curve_to_cubic_rel(-1.530, -1.941, -0.940, -0.941, -2.823, -2.117)
    p.curve_to_cubic_abs(78.974, 38.935, 78.562, 38.758, 78.915, 38.817)
    p.line_to_abs(78.974, 38.935)
    p.close_path()
    
    p.end()
    
    # path3705
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    
    p.move_to_abs(68.445, 37.641)
    p.curve_to_cubic_rel(-2.059, 0.412, 0.000, 0.000, -2.000, 0.823)
    p.curve_to_cubic_smooth_rel(0.589, -0.999, -0.470, -0.588)
    p.curve_to_cubic_rel(4.822, -1.354, 1.058, -0.412, 4.469, -1.823)
    p.curve_to_cubic_rel(-2.058, 1.941, 0.353, 0.471, -2.647, 1.647)
    p.curve_to_cubic_rel(2.234, -0.588, 0.587, 0.294, 2.117, -1.294)
    p.curve_to_cubic_rel(-1.823, 2.058, 0.118, 0.706, -0.412, 1.765)
    p.curve_to_cubic_rel(-3.529, 0.647, -1.411, 0.294, -3.353, 1.176)
    p.curve_to_cubic_abs(68.445, 37.641, 66.445, 39.229, 68.504, 37.758)
    p.line_to_abs(68.445, 37.641)
    p.close_path()
    
    p.end()
    
    # path3662
    p = Path()
    
    g.add(p)
    p.fill("#7D0B01")
    
    p.move_to_abs(85.357, 67.513)
    p.curve_to_cubic_rel(-7.321, 15.637, 0.000, 0.000, -1.000, 10.813)
    p.curve_to_cubic_rel(-16.219, 4.824, -6.321, 4.824, -10.812, 5.988)
    p.curve_to_cubic_rel(-6.487, -2.993, -5.406, -1.164, -6.487, -2.993)
    p.curve_to_cubic_smooth_rel(4.907, -6.655, 4.658, -4.492)
    p.curve_to_cubic_rel(0.666, -6.156, 0.317, -2.748, 0.666, -6.156)
    p.curve_to_cubic_smooth_rel(7.902, 0.666, 4.658, 1.082)
    p.curve_to_cubic_rel(11.063, -2.746, 3.244, -0.416, 8.650, -1.747)
    p.curve_to_cubic_abs(85.357, 67.513, 82.279, 69.092, 85.439, 67.429)
    p.close_path()
    
    p.end()
    
    # path3664
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(55.372, 85.062)
    p.line_to_rel(-1.996, -1.955)
    
    p.end()
    
    # path3664-4
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(60.994, 72.282)
    p.line_to_rel(-2.513, -1.221)
    
    p.end()
    
    # path3688
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(82.943, 66.099)
    p.curve_to_cubic_rel(2.996, 1.373, 0.000, 0.000, 2.162, 0.791)
    p.curve_to_cubic_rel(1.619, 1.496, 0.831, 0.582, 1.619, 1.496)
    
    p.end()
    
    # path3701
    p = Path()
    
    g.add(p)
    p.fill("#F88F96")
    p.stroke_color("#A91827")
    p.stroke_width(0.6242)
    
    p.move_to_abs(79.974, 80.986)
    p.curve_to_cubic_rel(-4.059, -0.656, 0.000, 0.000, -1.991, -0.646)
    p.curve_to_cubic_rel(-4.411, 1.126, -1.906, -0.011, -3.875, 0.590)
    p.curve_to_cubic_rel(-2.353, 2.059, -1.117, 1.118, -2.353, 2.059)
    p.line_to_rel(1.765, -2.059)
    p.curve_to_cubic_rel(-5.410, 0.294, 0.000, 0.000, -3.449, -0.206)
    p.curve_to_cubic_rel(-1.436, 0.471, -0.375, 0.095, -0.908, 0.272)
    p.curve_to_cubic_rel(-3.152, 2.352, -0.996, 0.375, -2.390, 1.226)
    p.curve_to_cubic_rel(-0.537, 2.948, -0.715, 1.058, -0.958, 2.539)
    p.curve_to_cubic_rel(3.389, 0.821, 0.270, 0.262, 2.965, 0.776)
    p.curve_to_cubic_rel(2.907, 0.061, 1.401, 0.148, 1.562, 0.161)
    p.curve_to_cubic_rel(3.409, -0.811, 1.330, -0.101, 2.782, -0.788)
    p.curve_to_cubic_rel(2.789, -1.095, 0.636, -0.023, 1.794, -0.563)
    p.curve_to_cubic_rel(5.687, -3.571, 0.982, -0.525, 5.687, -3.571)
    
    p.end()
    
    # path3692
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(85.357, 67.513)
    p.curve_to_cubic_rel(-7.321, 15.637, 0.000, 0.000, -1.000, 10.813)
    p.curve_to_cubic_rel(-16.219, 4.824, -6.321, 4.824, -10.812, 5.988)
    p.curve_to_cubic_rel(-6.487, -2.993, -5.406, -1.164, -6.487, -2.993)
    p.curve_to_cubic_smooth_rel(4.907, -6.655, 4.658, -4.492)
    p.curve_to_cubic_rel(0.666, -6.156, 0.317, -2.748, 0.666, -6.156)
    p.curve_to_cubic_smooth_rel(7.902, 0.666, 4.658, 1.082)
    p.curve_to_cubic_rel(11.063, -2.746, 3.244, -0.416, 8.650, -1.747)
    p.curve_to_cubic_abs(85.357, 67.513, 82.279, 69.092, 85.439, 67.429)
    p.close_path()
    
    p.end()
    
    # path3694
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(55.372, 85.062)
    p.line_to_rel(-1.996, -1.955)
    
    p.end()
    
    # path3696
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(60.994, 72.282)
    p.line_to_rel(-2.513, -1.221)
    
    p.end()
    
    # path3698
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(82.943, 66.099)
    p.curve_to_cubic_rel(2.996, 1.373, 0.000, 0.000, 2.162, 0.791)
    p.curve_to_cubic_rel(1.619, 1.496, 0.831, 0.582, 1.619, 1.496)
    
    p.end()
    
    # path3768
    p = Path()
    
    g.add(p)
    p.fill("#B2DB1F")
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(39.568, 134.917)
    p.curve_to_cubic_rel(-0.353, 4.353, 0.000, 0.000, 0.588, 1.529)
    p.curve_to_cubic_rel(-1.765, 5.176, -0.942, 2.823, -2.353, 4.116)
    p.curve_to_cubic_rel(7.293, 5.529, 0.589, 1.058, 3.882, 4.470)
    p.curve_to_cubic_rel(12.233, 1.764, 3.411, 1.058, 9.763, 2.352)
    p.curve_to_cubic_smooth_rel(3.646, -2.117, 3.646, -2.117)
    p.line_to_rel(-0.706, -5.410)
    p.line_to_rel(-13.174, -14.469)
    p.line_to_abs(39.568, 134.917)
    p.line_to_abs(39.568, 134.917)
    p.close_path()
    
    p.end()
    
    # path3764
    p = Path()
    
    g.add(p)
    p.fill("#B2DB1F")
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(109.932, 112.386)
    p.curve_to_cubic_rel(-0.117, 11.762, 0.000, 0.000, 1.999, 5.882)
    p.curve_to_cubic_rel(-7.174, 13.292, -2.118, 5.882, -4.235, 10.704)
    p.curve_to_cubic_rel(-11.999, 7.176, -2.941, 2.588, -1.648, 4.823)
    p.curve_to_cubic_rel(-15.057, 3.292, -10.352, 2.353, -10.703, 3.176)
    p.curve_to_cubic_rel(-20.231, -3.528, -4.352, 0.118, -13.409, -0.706)
    p.curve_to_cubic_rel(-19.055, -14.351, -6.822, -2.823, -17.408, -8.586)
    p.curve_to_cubic_rel(-2.940, -14.467, -1.647, -5.763, -3.412, -10.233)
    p.curve_to_cubic_rel(0.471, -6.588, 0.471, -4.235, 0.471, -6.588)
    p.curve_to_cubic_smooth_rel(9.880, 10.939, 5.529, 8.586)
    p.curve_to_cubic_rel(20.585, 7.174, 4.352, 2.353, 12.469, 6.351)
    p.curve_to_cubic_rel(20.938, -0.940, 8.116, 0.824, 16.351, 0.706)
    p.curve_to_cubic_rel(17.408, -7.411, 4.588, -1.647, 15.174, -5.646)
    p.curve_to_cubic_abs(109.932, 112.386, 104.873, 116.974, 110.049, 112.269)
    p.line_to_abs(109.932, 112.386)
    p.close_path()
    
    p.end()
    
    # path3766
    p = Path()
    
    g.add(p)
    p.fill("#B2DB1F")
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(98.440, 142.128)
    p.curve_to_cubic_rel(1.410, 4.233, 0.000, 0.000, 1.176, 2.587)
    p.curve_to_cubic_rel(0.591, 4.235, 0.237, 1.647, 0.591, 4.235)
    p.curve_to_cubic_smooth_rel(-12.469, 4.116, -6.236, 3.765)
    p.curve_to_cubic_rel(-14.469, -2.823, -6.235, 0.354, -14.469, -1.411)
    p.curve_to_cubic_rel(0.823, -6.114, 0.000, -1.411, 1.294, -5.057)
    p.curve_to_cubic_rel(-0.470, -1.060, -0.470, -1.060, -0.470, -1.060)
    p.line_to_vertical_rel(-0.117)
    
    p.end()
    
    # path3819
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(33.687, 112.509)
    p.curve_to_cubic_rel(7.058, 8.292, 0.000, 0.000, 2.823, 5.763)
    p.curve_to_cubic_rel(20.113, 8.176, 4.234, 2.528, 13.115, 7.116)
    p.curve_to_cubic_rel(23.820, -0.296, 6.999, 1.058, 17.115, 1.940)
    p.curve_to_cubic_rel(18.526, -7.646, 6.704, -2.234, 15.525, -5.410)
    p.curve_to_cubic_rel(7.469, -5.998, 2.999, -2.234, 7.469, -5.998)
    
    p.end()
    
    # path3887
    p = Path()
    
    g.add(p)
    p.fill("#7352A3")
    p.stroke_color("#4D4987")
    p.stroke_width(0.6242)
    
    p.move_to_abs(105.317, 133.387)
    p.curve_to_cubic_rel(-7.735, 0.497, 0.000, 0.000, -5.239, -2.165)
    p.curve_to_cubic_rel(-4.574, 5.157, -2.494, 2.661, -4.574, 3.909)
    p.curve_to_cubic_rel(1.332, 2.245, 0.000, 1.247, 0.000, 1.580)
    p.curve_to_cubic_rel(2.746, 2.579, 1.330, 0.666, 3.160, 0.999)
    p.curve_to_cubic_rel(-1.416, 1.913, -0.417, 1.580, -0.335, 1.747)
    p.curve_to_cubic_rel(-3.409, -1.498, -1.080, 0.166, -1.912, -1.581)
    p.curve_to_cubic_rel(-3.411, 3.245, -1.498, 0.084, -3.411, 1.747)
    p.curve_to_cubic_rel(0.415, 6.153, 0.000, 1.497, -0.167, 5.073)
    p.curve_to_cubic_rel(0.831, 1.248, 0.583, 1.083, 0.831, 1.248)
    p.line_to_rel(6.073, -1.829)
    p.line_to_rel(4.075, -1.996)
    p.line_to_rel(-0.248, -5.323)
    p.line_to_rel(-1.497, -3.994)
    p.line_to_rel(3.659, -2.910)
    p.line_to_rel(2.578, -3.326)
    p.line_to_rel(1.248, -1.664)
    p.line_to_abs(105.317, 133.387)
    p.line_to_abs(105.317, 133.387)
    p.close_path()
    
    p.end()
    
    # path3889
    p = Path()
    
    g.add(p)
    p.fill("#7352A3")
    p.stroke_color("#594C90")
    p.stroke_width(0.6242)
    
    p.move_to_abs(68.138, 129.976)
    p.curve_to_cubic_rel(-1.331, 4.075, 0.000, 0.000, -0.666, 3.243)
    p.curve_to_cubic_rel(-4.158, 2.413, -0.665, 0.832, -2.246, 2.579)
    p.curve_to_cubic_rel(-3.161, -2.495, -1.914, -0.167, -2.911, -1.331)
    p.curve_to_cubic_rel(-1.580, -1.829, -0.250, -1.165, -0.666, -1.996)
    p.curve_to_cubic_rel(-0.832, 2.743, -0.915, 0.166, -0.998, 0.748)
    p.curve_to_cubic_rel(-1.997, 3.160, 0.167, 1.996, 0.000, 3.243)
    p.curve_to_cubic_rel(-7.402, -1.331, -1.996, -0.082, -6.071, -0.415)
    p.curve_to_cubic_rel(-4.159, -3.243, -1.331, -0.914, -3.743, -1.912)
    p.curve_to_cubic_rel(0.832, -3.493, -0.416, -1.331, -0.665, -1.996)
    p.curve_to_cubic_rel(1.997, -2.996, 1.498, -1.496, 2.579, -2.329)
    p.curve_to_cubic_rel(-2.246, -0.082, -0.583, -0.665, -1.165, -0.748)
    p.curve_to_cubic_rel(-2.746, 1.497, -1.082, 0.665, -1.664, 2.164)
    p.curve_to_cubic_rel(-1.913, -2.994, -1.081, -0.666, -1.913, -1.830)
    p.curve_to_cubic_rel(0.333, -5.322, 0.000, -1.165, 0.333, -5.322)
    p.curve_to_cubic_smooth_rel(10.479, 5.571, 3.409, 2.909)
    p.curve_to_cubic_abs(68.138, 129.976, 57.326, 128.312, 56.328, 128.480)
    p.line_to_abs(68.138, 129.976)
    p.close_path()
    
    p.end()
    
    # path3885
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(73.921, 147.992)
    p.curve_to_cubic_rel(-18.568, -3.611, -3.438, 0.035, -11.746, -0.789)
    p.curve_to_cubic_rel(-19.055, -14.351, -6.822, -2.823, -17.408, -8.586)
    p.curve_to_cubic_rel(-2.940, -14.468, -1.647, -5.764, -3.412, -10.232)
    p.curve_to_cubic_rel(0.471, -6.587, 0.471, -4.234, 0.471, -6.587)
    p.curve_to_cubic_smooth_rel(9.880, 10.939, 5.529, 8.586)
    p.curve_to_cubic_rel(20.585, 7.174, 4.352, 2.353, 12.468, 6.352)
    p.curve_to_cubic_rel(20.938, -0.940, 8.116, 0.823, 16.350, 0.705)
    p.curve_to_cubic_rel(17.408, -7.411, 4.588, -1.648, 15.174, -5.647)
    p.curve_to_cubic_smooth_rel(7.293, -6.351, 7.410, -6.469)
    p.line_to_rel(0.000, 0.000)
    p.line_to_rel(0.000, 0.000)
    p.curve_to_cubic_rel(-0.117, 11.761, 0.000, 0.000, 1.999, 5.881)
    p.curve_to_cubic_rel(-7.092, 13.790, -2.118, 5.882, -4.150, 11.203)
    p.curve_to_cubic_rel(-5.276, 4.710, -1.799, 1.585, -3.012, 3.284)
    
    p.end()
    
    # path3847
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(98.440, 142.128)
    p.curve_to_cubic_rel(1.410, 4.233, 0.000, 0.000, 1.176, 2.587)
    p.curve_to_cubic_rel(0.591, 4.235, 0.237, 1.647, 0.591, 4.235)
    p.curve_to_cubic_smooth_rel(-12.469, 4.116, -6.236, 3.765)
    p.curve_to_cubic_rel(-14.469, -2.823, -6.235, 0.354, -14.469, -1.411)
    p.curve_to_cubic_rel(0.823, -6.114, 0.000, -1.411, 1.294, -5.057)
    p.curve_to_cubic_rel(-0.470, -1.060, -0.470, -1.060, -0.470, -1.060)
    p.line_to_vertical_rel(-0.117)
    
    p.end()
    
    # path3849
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.6242)
    
    p.move_to_abs(33.687, 112.509)
    p.curve_to_cubic_rel(7.058, 8.292, 0.000, 0.000, 2.823, 5.763)
    p.curve_to_cubic_rel(20.113, 8.176, 4.234, 2.528, 13.115, 7.116)
    p.curve_to_cubic_rel(23.820, -0.296, 6.999, 1.058, 17.115, 1.940)
    p.curve_to_cubic_rel(18.526, -7.646, 6.704, -2.234, 15.525, -5.410)
    p.curve_to_cubic_rel(7.469, -5.998, 2.999, -2.234, 7.469, -5.998)
    
    p.end()
    #endregion drawing

# Squidward Tentacles
def person_c(x, y, scale_x, scale_y, crown):
    g = PathGroup()

    width = 150.000 * scale_x
    height = 167.160 * scale_y

    g.translate(-width / 2.0, -height)
    g.scale(scale_x, scale_y)
    g.translate(x, y)

    if crown:
        #region crown
        # path4672_1_
        p = Path()
    
        g.add(p)
        p.fill("#870303")
    
        p.move_to_abs(70.079, 0.000)
        p.line_to_rel(-0.371, 0.636)
        p.line_to_rel(-4.281, 7.311)
        p.line_to_rel(-7.173, -4.522)
        p.line_to_abs(57.634, 3.030)
        p.line_to_rel(-0.186, 0.714)
        p.line_to_rel(-2.154, 8.196)
        p.line_to_rel(-8.123, -2.419)
        p.line_to_rel(-0.704, -0.208)
        p.line_to_rel(0.009, 0.732)
        p.line_to_rel(0.139, 8.475)
        p.line_to_rel(-8.475, -0.140)
        p.line_to_rel(-0.736, -0.009)
        p.line_to_rel(0.213, 0.704)
        p.line_to_rel(2.418, 8.122)
        p.line_to_rel(-8.201, 2.154)
        p.line_to_rel(-0.709, 0.186)
        p.line_to_rel(0.394, 0.621)
        p.line_to_rel(4.522, 7.168)
        p.line_to_rel(-7.316, 4.285)
        p.line_to_rel(-0.635, 0.376)
        p.line_to_rel(0.546, 0.491)
        p.line_to_rel(6.288, 5.686)
        p.line_to_rel(-5.884, 6.097)
        p.line_to_rel(-0.509, 0.529)
        p.line_to_rel(0.658, 0.328)
        p.line_to_rel(7.589, 3.776)
        p.line_to_rel(-4.022, 7.460)
        p.line_to_rel(-0.352, 0.648)
        p.line_to_rel(0.723, 0.139)
        p.line_to_rel(8.326, 1.585)
        p.line_to_rel(-1.858, 8.271)
        p.line_to_rel(-0.162, 0.719)
        p.line_to_rel(0.732, -0.061)
        p.line_to_rel(8.442, -0.718)
        p.line_to_rel(0.445, 8.465)
        p.line_to_rel(0.037, 0.731)
        p.line_to_rel(0.690, -0.254)
        p.line_to_rel(7.937, -2.971)
        p.line_to_rel(2.706, 8.035)
        p.line_to_rel(0.236, 0.694)
        p.line_to_rel(0.593, -0.436)
        p.line_to_rel(6.843, -4.999)
        p.line_to_rel(4.777, 7.005)
        p.line_to_rel(0.412, 0.608)
        p.line_to_rel(0.454, -0.580)
        p.line_to_rel(5.240, -6.658)
        p.line_to_rel(6.487, 5.453)
        p.line_to_rel(0.565, 0.474)
        p.line_to_rel(0.283, -0.682)
        p.line_to_rel(3.248, -7.826)
        p.line_to_rel(7.719, 3.504)
        p.line_to_rel(0.668, 0.301)
        p.line_to_rel(0.088, -0.728)
        p.line_to_rel(1.020, -8.415)
        p.line_to_rel(8.377, 1.293)
        p.line_to_rel(0.723, 0.111)
        p.line_to_rel(-0.111, -0.728)
        p.line_to_rel(-1.293, -8.377)
        p.line_to_rel(8.419, -1.020)
        p.line_to_rel(0.728, -0.088)
        p.line_to_rel(-0.301, -0.667)
        p.line_to_rel(-3.504, -7.720)
        p.line_to_rel(7.826, -3.248)
        p.line_to_rel(0.682, -0.282)
        p.line_to_rel(-0.478, -0.561)
        p.line_to_rel(-5.453, -6.486)
        p.line_to_rel(6.662, -5.246)
        p.line_to_rel(0.575, -0.454)
        p.line_to_rel(-0.607, -0.412)
        p.line_to_rel(-7.001, -4.772)
        p.line_to_rel(4.999, -6.848)
        p.line_to_rel(0.436, -0.594)
        p.line_to_rel(-0.699, -0.231)
        p.line_to_rel(-8.029, -2.710)
        p.line_to_rel(2.965, -7.938)
        p.line_to_rel(0.260, -0.690)
        p.line_to_rel(-0.732, -0.037)
        p.line_to_rel(-8.470, -0.439)
        p.line_to_rel(0.718, -8.447)
        p.line_to_rel(0.065, -0.732)
        p.line_to_rel(-0.718, 0.162)
        p.line_to_rel(-8.267, 1.863)
        p.line_to_rel(-1.594, -8.331)
        p.line_to_rel(-0.140, -0.719)
        p.line_to_rel(-0.644, 0.349)
        p.line_to_rel(-7.460, 4.021)
        p.line_to_rel(-3.775, -7.590)
        p.line_to_rel(-0.330, -0.658)
        p.line_to_rel(-0.527, 0.510)
        p.line_to_rel(-6.103, 5.890)
        p.line_to_rel(-5.681, -6.293)
        p.line_to_abs(70.079, 0.000)
        p.line_to_abs(70.079, 0.000)
        p.close_path()
        p.move_to_abs(70.269, 1.812)
        p.line_to_rel(5.560, 6.158)
        p.line_to_rel(0.376, 0.412)
        p.line_to_rel(0.397, -0.389)
        p.line_to_rel(5.974, -5.760)
        p.line_to_rel(3.697, 7.428)
        p.line_to_rel(0.245, 0.500)
        p.line_to_rel(0.492, -0.264)
        p.line_to_rel(7.307, -3.938)
        p.line_to_rel(1.552, 8.149)
        p.line_to_rel(0.106, 0.548)
        p.line_to_rel(0.543, -0.121)
        p.line_to_rel(8.098, -1.820)
        p.line_to_rel(-0.703, 8.266)
        p.line_to_rel(-0.047, 0.556)
        p.line_to_rel(0.557, 0.028)
        p.line_to_rel(8.284, 0.431)
        p.line_to_rel(-2.905, 7.771)
        p.line_to_rel(-0.194, 0.523)
        p.line_to_rel(0.528, 0.176)
        p.line_to_rel(7.857, 2.650)
        p.line_to_rel(-4.893, 6.700)
        p.line_to_rel(-0.329, 0.449)
        p.line_to_rel(0.464, 0.315)
        p.line_to_rel(6.853, 4.675)
        p.line_to_rel(-6.519, 5.129)
        p.line_to_rel(-0.441, 0.343)
        p.line_to_rel(0.361, 0.427)
        p.line_to_rel(5.344, 6.353)
        p.line_to_rel(-7.670, 3.179)
        p.line_to_rel(-0.509, 0.217)
        p.line_to_rel(0.228, 0.506)
        p.line_to_rel(3.434, 7.557)
        p.line_to_rel(-8.244, 0.992)
        p.line_to_rel(-0.551, 0.069)
        p.line_to_rel(0.084, 0.551)
        p.line_to_rel(1.264, 8.201)
        p.line_to_rel(-8.200, -1.265)
        p.line_to_rel(-0.547, -0.088)
        p.line_to_rel(-0.069, 0.556)
        p.line_to_rel(-0.996, 8.233)
        p.line_to_rel(-7.553, -3.429)
        p.line_to_rel(-0.510, -0.227)
        p.line_to_rel(-0.213, 0.515)
        p.line_to_rel(-3.179, 7.663)
        p.line_to_rel(-6.353, -5.343)
        p.line_to_rel(-0.426, -0.355)
        p.line_to_rel(-0.344, 0.435)
        p.line_to_rel(-5.133, 6.520)
        p.line_to_rel(-4.671, -6.854)
        p.line_to_rel(-0.314, -0.458)
        p.line_to_rel(-0.450, 0.324)
        p.line_to_rel(-6.700, 4.897)
        p.line_to_rel(-2.650, -7.863)
        p.line_to_rel(-0.176, -0.527)
        p.line_to_rel(-0.523, 0.194)
        p.line_to_rel(-7.771, 2.905)
        p.line_to_rel(-0.431, -8.285)
        p.line_to_rel(-0.032, -0.556)
        p.line_to_rel(-0.552, 0.047)
        p.line_to_rel(-8.271, 0.704)
        p.line_to_rel(1.821, -8.100)
        p.line_to_rel(0.125, -0.542)
        p.line_to_rel(-0.546, -0.102)
        p.line_to_rel(-8.150, -1.558)
        p.line_to_rel(3.934, -7.307)
        p.line_to_rel(0.264, -0.486)
        p.line_to_rel(-0.496, -0.251)
        p.line_to_rel(-7.432, -3.692)
        p.line_to_rel(5.764, -5.973)
        p.line_to_rel(0.385, -0.403)
        p.line_to_rel(-0.413, -0.370)
        p.line_to_rel(-6.158, -5.564)
        p.line_to_rel(7.163, -4.198)
        p.line_to_rel(0.478, -0.278)
        p.line_to_rel(-0.296, -0.472)
        p.line_to_rel(-4.425, -7.016)
        p.line_to_rel(8.025, -2.113)
        p.line_to_rel(0.538, -0.139)
        p.line_to_rel(-0.157, -0.532)
        p.line_to_rel(-2.373, -7.951)
        p.line_to_rel(8.298, 0.134)
        p.line_to_rel(0.556, 0.010)
        p.line_to_abs(47.700, 19.063)
        p.line_to_rel(-0.130, -8.299)
        p.line_to_rel(7.951, 2.368)
        p.line_to_rel(0.533, 0.162)
        p.line_to_rel(0.139, -0.542)
        p.line_to_rel(2.108, -8.025)
        p.line_to_rel(7.020, 4.430)
        p.line_to_rel(0.468, 0.297)
        p.line_to_rel(0.283, -0.482)
        p.line_to_abs(70.269, 1.812)
        p.line_to_abs(70.269, 1.812)
        p.close_path()
    
        p.end()
    
        # path4662_2_
        p = Path()
    
        g.add(p)
        p.fill("#E60000")
    
        p.move_to_abs(107.514, 79.420)
        p.line_to_rel(-8.928, -1.376)
        p.line_to_rel(-1.084, 8.967)
        p.line_to_rel(-8.225, -3.732)
        p.line_to_rel(-3.463, 8.343)
        p.line_to_rel(-6.913, -5.814)
        p.line_to_rel(-5.585, 7.099)
        p.line_to_rel(-5.088, -7.464)
        p.line_to_rel(-7.293, 5.329)
        p.line_to_rel(-2.886, -8.560)
        p.line_to_rel(-8.460, 3.163)
        p.line_to_rel(-0.469, -9.020)
        p.line_to_rel(-9.000, 0.763)
        p.line_to_rel(1.982, -8.812)
        p.line_to_rel(-8.873, -1.693)
        p.line_to_rel(4.286, -7.951)
        p.line_to_rel(-8.087, -4.024)
        p.line_to_rel(6.272, -6.500)
        p.line_to_abs(29.000, 42.080)
        p.line_to_rel(7.793, -4.567)
        p.line_to_rel(-4.818, -7.640)
        p.line_to_rel(8.736, -2.294)
        p.line_to_rel(-2.579, -8.657)
        p.line_to_rel(9.032, 0.147)
        p.line_to_rel(-0.148, -9.032)
        p.line_to_rel(8.657, 2.579)
        p.line_to_rel(2.294, -8.736)
        p.line_to_rel(7.640, 4.818)
        p.line_to_rel(4.566, -7.793)
        p.line_to_rel(6.057, 6.701)
        p.line_to_rel(6.500, -6.272)
        p.line_to_rel(4.023, 8.087)
        p.line_to_rel(7.951, -4.285)
        p.line_to_rel(1.693, 8.872)
        p.line_to_rel(8.813, -1.982)
        p.line_to_rel(-0.764, 9.001)
        p.line_to_rel(9.021, 0.469)
        p.line_to_rel(-3.164, 8.461)
        p.line_to_rel(8.560, 2.886)
        p.line_to_rel(-5.329, 7.293)
        p.line_to_abs(121.000, 45.223)
        p.line_to_rel(-7.099, 5.586)
        p.line_to_rel(5.814, 6.912)
        p.line_to_rel(-8.344, 3.463)
        p.line_to_rel(3.734, 8.225)
        p.line_to_rel(-8.968, 1.084)
        p.line_to_abs(107.514, 79.420)
        p.close_path()
    
        p.end()
    
        # path4664_1_
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
        p.stroke_color("#4F3A02")
        p.stroke_width(1.4659)
    
        p.move_to_abs(104.520, 76.426)
        p.line_to_rel(-8.108, -1.250)
        p.line_to_rel(-0.984, 8.145)
        p.line_to_rel(-7.470, -3.391)
        p.line_to_rel(-3.146, 7.576)
        p.line_to_rel(-6.278, -5.280)
        p.line_to_rel(-5.072, 6.447)
        p.line_to_rel(-4.621, -6.778)
        p.line_to_rel(-6.625, 4.840)
        p.line_to_rel(-2.621, -7.773)
        p.line_to_rel(-7.684, 2.872)
        p.line_to_rel(-0.426, -8.191)
        p.line_to_rel(-8.174, 0.692)
        p.line_to_rel(1.800, -8.003)
        p.line_to_rel(-8.058, -1.538)
        p.line_to_rel(3.893, -7.222)
        p.line_to_rel(-7.345, -3.654)
        p.line_to_rel(5.697, -5.903)
        p.line_to_rel(-6.086, -5.501)
        p.line_to_rel(7.078, -4.147)
        p.line_to_rel(-4.376, -6.938)
        p.line_to_rel(7.935, -2.084)
        p.line_to_rel(-2.342, -7.862)
        p.line_to_rel(8.203, 0.134)
        p.line_to_rel(-0.134, -8.202)
        p.line_to_rel(7.862, 2.342)
        p.line_to_rel(2.084, -7.935)
        p.line_to_rel(6.939, 4.376)
        p.line_to_rel(4.147, -7.077)
        p.line_to_rel(5.501, 6.085)
        p.line_to_rel(5.903, -5.695)
        p.line_to_rel(3.654, 7.344)
        p.line_to_rel(7.222, -3.893)
        p.line_to_rel(1.537, 8.059)
        p.line_to_rel(8.004, -1.800)
        p.line_to_rel(-0.693, 8.174)
        p.line_to_rel(8.193, 0.426)
        p.line_to_rel(-2.873, 7.685)
        p.line_to_rel(7.773, 2.620)
        p.line_to_rel(-4.840, 6.624)
        p.line_to_rel(6.778, 4.621)
        p.line_to_rel(-6.447, 5.072)
        p.line_to_rel(5.280, 6.279)
        p.line_to_rel(-7.576, 3.145)
        p.line_to_rel(3.391, 7.471)
        p.line_to_rel(-8.145, 0.984)
        p.line_to_abs(104.520, 76.426)
        p.close_path()
    
        p.end()
    
        # path4666_1_
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
        p.stroke_color("#4F3A02")
        p.stroke_width(1.4659)
    
        p.move_to_abs(108.133, 72.305)
        p.line_to_rel(-8.201, -0.181)
        p.line_to_rel(0.087, 8.203)
        p.line_to_rel(-7.849, -2.386)
        p.line_to_rel(-2.129, 7.922)
        p.line_to_rel(-6.914, -4.416)
        p.line_to_rel(-4.188, 7.054)
        p.line_to_rel(-5.467, -6.117)
        p.line_to_rel(-5.936, 5.663)
        p.line_to_rel(-3.613, -7.365)
        p.line_to_rel(-7.243, 3.853)
        p.line_to_rel(-1.492, -8.067)
        p.line_to_rel(-8.014, 1.755)
        p.line_to_rel(0.740, -8.171)
        p.line_to_rel(-8.190, -0.473)
        p.line_to_rel(2.917, -7.667)
        p.line_to_rel(-7.759, -2.665)
        p.line_to_rel(4.877, -6.597)
        p.line_to_rel(-6.752, -4.659)
        p.line_to_rel(6.476, -5.036)
        p.line_to_rel(-5.244, -6.308)
        p.line_to_rel(7.594, -3.103)
        p.line_to_rel(-3.348, -7.489)
        p.line_to_rel(8.150, -0.938)
        p.line_to_rel(-1.203, -8.114)
        p.line_to_rel(8.100, 1.296)
        p.line_to_rel(1.031, -8.139)
        p.line_to_rel(7.451, 3.434)
        p.line_to_rel(3.188, -7.560)
        p.line_to_rel(6.248, 5.316)
        p.line_to_rel(5.110, -6.418)
        p.line_to_rel(4.582, 6.804)
        p.line_to_rel(6.650, -4.801)
        p.line_to_rel(2.577, 7.788)
        p.line_to_rel(7.700, -2.829)
        p.line_to_rel(0.380, 8.194)
        p.line_to_rel(8.178, -0.646)
        p.line_to_rel(-1.845, 7.993)
        p.line_to_rel(8.049, 1.583)
        p.line_to_rel(-3.934, 7.200)
        p.line_to_rel(7.323, 3.696)
        p.line_to_rel(-5.729, 5.870)
        p.line_to_rel(6.055, 5.536)
        p.line_to_rel(-7.102, 4.106)
        p.line_to_rel(4.336, 6.964)
        p.line_to_rel(-7.945, 2.038)
        p.line_to_abs(108.133, 72.305)
        p.close_path()
    
        p.end()
    
        # path4658_1_
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
    
        p.move_to_abs(104.520, 76.426)
        p.line_to_rel(-8.108, -1.250)
        p.line_to_rel(-0.984, 8.145)
        p.line_to_rel(-7.470, -3.391)
        p.line_to_rel(-3.146, 7.576)
        p.line_to_rel(-6.278, -5.280)
        p.line_to_rel(-5.072, 6.447)
        p.line_to_rel(-4.621, -6.778)
        p.line_to_rel(-6.625, 4.840)
        p.line_to_rel(-2.621, -7.773)
        p.line_to_rel(-7.684, 2.872)
        p.line_to_rel(-0.426, -8.191)
        p.line_to_rel(-8.174, 0.692)
        p.line_to_rel(1.800, -8.003)
        p.line_to_rel(-8.058, -1.538)
        p.line_to_rel(3.893, -7.222)
        p.line_to_rel(-7.345, -3.654)
        p.line_to_rel(5.697, -5.903)
        p.line_to_rel(-6.086, -5.501)
        p.line_to_rel(7.078, -4.147)
        p.line_to_rel(-4.376, -6.938)
        p.line_to_rel(7.935, -2.084)
        p.line_to_rel(-2.342, -7.862)
        p.line_to_rel(8.203, 0.134)
        p.line_to_rel(-0.134, -8.202)
        p.line_to_rel(7.862, 2.342)
        p.line_to_rel(2.084, -7.935)
        p.line_to_rel(6.939, 4.376)
        p.line_to_rel(4.147, -7.077)
        p.line_to_rel(5.501, 6.085)
        p.line_to_rel(5.903, -5.695)
        p.line_to_rel(3.654, 7.344)
        p.line_to_rel(7.222, -3.893)
        p.line_to_rel(1.537, 8.059)
        p.line_to_rel(8.004, -1.800)
        p.line_to_rel(-0.693, 8.174)
        p.line_to_rel(8.193, 0.426)
        p.line_to_rel(-2.873, 7.685)
        p.line_to_rel(7.773, 2.620)
        p.line_to_rel(-4.840, 6.624)
        p.line_to_rel(6.778, 4.621)
        p.line_to_rel(-6.447, 5.072)
        p.line_to_rel(5.280, 6.279)
        p.line_to_rel(-7.576, 3.145)
        p.line_to_rel(3.391, 7.471)
        p.line_to_rel(-8.145, 0.984)
        p.line_to_abs(104.520, 76.426)
        p.close_path()
    
        p.end()
    
        # path4660_1_
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
    
        p.move_to_abs(108.133, 72.305)
        p.line_to_rel(-8.201, -0.181)
        p.line_to_rel(0.087, 8.203)
        p.line_to_rel(-7.849, -2.386)
        p.line_to_rel(-2.129, 7.922)
        p.line_to_rel(-6.914, -4.416)
        p.line_to_rel(-4.188, 7.054)
        p.line_to_rel(-5.467, -6.117)
        p.line_to_rel(-5.936, 5.663)
        p.line_to_rel(-3.613, -7.365)
        p.line_to_rel(-7.243, 3.853)
        p.line_to_rel(-1.492, -8.067)
        p.line_to_rel(-8.014, 1.755)
        p.line_to_rel(0.740, -8.171)
        p.line_to_rel(-8.190, -0.473)
        p.line_to_rel(2.917, -7.667)
        p.line_to_rel(-7.759, -2.665)
        p.line_to_rel(4.877, -6.597)
        p.line_to_rel(-6.752, -4.659)
        p.line_to_rel(6.476, -5.036)
        p.line_to_rel(-5.244, -6.308)
        p.line_to_rel(7.594, -3.103)
        p.line_to_rel(-3.348, -7.489)
        p.line_to_rel(8.150, -0.938)
        p.line_to_rel(-1.203, -8.114)
        p.line_to_rel(8.100, 1.296)
        p.line_to_rel(1.031, -8.139)
        p.line_to_rel(7.451, 3.434)
        p.line_to_rel(3.188, -7.560)
        p.line_to_rel(6.248, 5.316)
        p.line_to_rel(5.110, -6.418)
        p.line_to_rel(4.582, 6.804)
        p.line_to_rel(6.650, -4.801)
        p.line_to_rel(2.577, 7.788)
        p.line_to_rel(7.700, -2.829)
        p.line_to_rel(0.380, 8.194)
        p.line_to_rel(8.178, -0.646)
        p.line_to_rel(-1.845, 7.993)
        p.line_to_rel(8.049, 1.583)
        p.line_to_rel(-3.934, 7.200)
        p.line_to_rel(7.323, 3.696)
        p.line_to_rel(-5.729, 5.870)
        p.line_to_rel(6.055, 5.536)
        p.line_to_rel(-7.102, 4.106)
        p.line_to_rel(4.336, 6.964)
        p.line_to_rel(-7.945, 2.038)
        p.line_to_abs(108.133, 72.305)
        p.close_path()
    
        p.end()
    
        # path4676_1_
        p = Path()
    
        g.add(p)
    
        p.move_to_abs(46.203, 46.784)
        p.curve_to_cubic_rel(28.923, -27.672, 0.346, -15.629, 13.294, -28.018)
        p.curve_to_cubic_rel(27.673, 28.921, 15.627, 0.345, 28.017, 13.292)
        p.curve_to_cubic_rel(-28.920, 27.675, -0.345, 15.627, -13.292, 28.018)
        p.curve_to_cubic_abs(46.203, 46.789, 58.251, 75.364, 45.860, 62.417)
    
        p.end()
    
        # path4695_1_
        p = Path()
    
        g.add(p)
        p.fill("#E6B52D")
        p.stroke_color("#E6B52D")
        p.stroke_width(1.0602)
    
        p.move_to_abs(65.488, 78.297)
        p.curve_to_cubic_rel(-21.875, -39.898, -17.058, -4.978, -26.851, -22.840)
        p.curve_to_cubic_abs(83.510, 16.522, 48.590, 21.341, 66.452, 11.547)
        p.curve_to_cubic_rel(21.878, 39.896, 17.059, 4.975, 26.854, 22.837)
        p.curve_to_cubic_rel(-39.895, 21.880, -4.975, 17.059, -22.836, 26.854)
    
        p.end()
    
        # path4693_1_
        p = Path()
    
        g.add(p)
        p.fill("#FFFBCC")
    
        p.move_to_abs(65.488, 78.297)
        p.curve_to_cubic_rel(-21.875, -39.898, -17.058, -4.978, -26.851, -22.840)
        p.curve_to_cubic_abs(83.510, 16.522, 48.590, 21.341, 66.452, 11.547)
        p.curve_to_cubic_rel(21.878, 39.896, 17.059, 4.975, 26.854, 22.837)
        p.curve_to_cubic_rel(-39.895, 21.880, -4.975, 17.059, -22.836, 26.854)
    
        p.end()
        #endregion crown

    #region drawing
    # path4627
    p = Path()
    
    g.add(p)
    p.fill("#ADD1C5")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(74.996, 111.717)
    p.line_to_rel(5.492, 2.269)
    p.curve_to_cubic_rel(-0.896, 11.106, 0.000, 0.000, -0.955, 8.240)
    p.curve_to_cubic_smooth_rel(0.180, 19.646, -0.357, 16.899)
    p.curve_to_cubic_rel(1.672, 10.032, 0.537, 2.747, 0.179, 8.300)
    p.curve_to_cubic_rel(4.119, 3.045, 1.492, 1.731, 2.328, 3.642)
    p.curve_to_cubic_rel(4.240, -3.643, 1.793, -0.596, 3.345, -3.104)
    p.curve_to_cubic_rel(1.793, 0.538, 0.896, -0.537, 1.732, -0.239)
    p.curve_to_cubic_rel(0.536, 1.852, 0.059, 0.775, 0.536, 1.852)
    p.curve_to_cubic_smooth_rel(2.149, -1.912, 1.075, -2.211)
    p.curve_to_cubic_rel(2.031, 1.971, 1.075, 0.300, 1.911, 0.896)
    p.curve_to_cubic_rel(-0.418, 7.764, 0.118, 1.076, 1.313, 6.510)
    p.curve_to_cubic_rel(-8.957, 2.687, -1.732, 1.253, -5.256, 3.225)
    p.curve_to_cubic_rel(-12.660, -3.344, -3.702, -0.537, -12.361, -2.985)
    p.curve_to_cubic_rel(-0.060, -0.357, -0.299, -0.357, -0.060, -0.357)
    p.curve_to_cubic_smooth_rel(-7.762, 2.327, -4.956, 2.088)
    p.curve_to_cubic_rel(-11.943, -0.537, -2.807, 0.239, -11.227, 0.060)
    p.curve_to_cubic_rel(-4.121, -4.001, -0.717, -0.598, -4.717, -0.837)
    p.curve_to_cubic_rel(2.986, -6.091, 0.597, -3.164, 2.449, -5.793)
    p.curve_to_cubic_rel(2.209, -0.060, 0.538, -0.298, 1.553, -1.135)
    p.curve_to_cubic_rel(2.926, 3.523, 0.656, 1.076, 1.672, 3.164)
    p.curve_to_cubic_rel(1.254, 0.357, 1.254, 0.357, 1.254, 0.357)
    p.curve_to_cubic_smooth_rel(0.060, -4.776, -0.657, -3.701)
    p.curve_to_cubic_rel(1.374, -1.731, 0.716, -1.075, 0.716, -2.448)
    p.curve_to_cubic_rel(2.149, 2.746, 0.656, 0.717, 0.776, 2.269)
    p.curve_to_cubic_rel(3.284, 1.075, 1.374, 0.479, 2.090, 1.016)
    p.curve_to_cubic_rel(2.926, -2.805, 1.194, 0.061, 2.807, -2.029)
    p.curve_to_cubic_rel(1.433, -14.930, 0.119, -0.777, 1.433, -12.243)
    p.curve_to_cubic_rel(-1.254, -21.078, 0.000, -2.688, -1.374, -20.063)
    p.curve_to_cubic_rel(0.180, -3.345, 0.120, -1.015, 0.180, -3.345)
    p.line_to_abs(74.996, 111.717)
    p.line_to_abs(74.996, 111.717)
    p.close_path()
    
    p.end()
    
    # path4631
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(72.785, 114.404)
    p.line_to_rel(1.493, 49.263)
    
    p.end()
    
    # path4633
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(67.112, 156.084)
    p.curve_to_cubic_rel(-3.403, 2.149, 0.000, 0.000, -2.090, 1.672)
    p.curve_to_cubic_rel(-4.598, 0.596, -1.314, 0.476, -4.598, 0.596)
    p.line_to_rel(3.105, 1.792)
    
    p.end()
    
    # path4635
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(78.279, 114.702)
    p.curve_to_cubic_rel(-0.955, 19.167, 0.000, 0.000, -0.955, 16.958)
    p.curve_to_cubic_rel(0.478, 16.422, 0.000, 2.210, 0.060, 14.511)
    p.curve_to_cubic_rel(4.479, 8.479, 0.418, 1.910, 0.597, 6.568)
    p.curve_to_cubic_rel(6.329, 1.015, 3.881, 1.910, 4.956, 1.730)
    p.curve_to_cubic_rel(2.084, -1.106, 0.524, -0.273, 1.509, -0.626)
    p.curve_to_cubic_rel(1.380, -2.178, 0.937, -0.779, 1.380, -2.178)
    
    p.end()
    
    # path4637
    p = Path()
    
    g.add(p)
    p.fill("#7A9CD9")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(95.894, 158.233)
    p.curve_to_cubic_rel(-1.791, -1.374, 0.000, 0.000, -0.656, -1.554)
    p.curve_to_cubic_smooth_rel(-4.062, 4.179, -3.284, 2.866)
    p.curve_to_cubic_rel(-3.820, 5.196, -0.775, 1.314, -3.820, 5.196)
    p.curve_to_cubic_smooth_rel(6.449, -0.716, 2.746, 0.956)
    p.curve_to_cubic_rel(3.045, -1.972, 3.702, -1.674, 2.687, -1.554)
    p.curve_to_cubic_smooth_rel(0.478, -3.344, 0.776, -1.134)
    p.curve_to_cubic_abs(95.894, 158.233, 95.993, 158.724, 95.775, 158.292)
    p.line_to_abs(95.894, 158.233)
    p.close_path()
    
    p.end()
    
    # path4662
    p = Path()
    
    g.add(p)
    p.fill("#7A9CD9")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(54.035, 155.425)
    p.curve_to_cubic_rel(2.269, 5.554, 0.000, 0.000, 0.956, 3.226)
    p.curve_to_cubic_rel(4.001, 4.121, 1.313, 2.329, 4.001, 4.121)
    p.line_to_rel(-2.029, -0.017)
    p.line_to_rel(-3.345, -0.342)
    p.curve_to_cubic_rel(-3.643, -1.852, 0.000, 0.000, -3.105, -0.837)
    p.curve_to_cubic_rel(0.537, -4.062, -0.538, -1.015, -0.538, -1.374)
    p.curve_to_cubic_abs(54.035, 155.425, 52.900, 156.143, 53.856, 155.365)
    p.line_to_abs(54.035, 155.425)
    p.close_path()
    
    p.end()
    
    # path4600-6-1
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(53.429, 160.776)
    p.curve_to_cubic_rel(-1.126, -1.149, -0.429, 0.110, -0.933, -0.403)
    p.curve_to_cubic_rel(0.428, -1.549, -0.193, -0.743, -0.002, -1.437)
    p.curve_to_cubic_rel(1.125, 1.146, 0.428, -0.111, 0.932, 0.402)
    p.curve_to_cubic_abs(53.429, 160.776, 54.050, 159.970, 53.859, 160.664)
    p.close_path()
    
    p.end()
    
    # path4600-6-1-8
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(56.490, 163.924)
    p.curve_to_cubic_rel(-1.446, -0.703, -0.366, 0.248, -1.014, -0.066)
    p.curve_to_cubic_rel(-0.120, -1.603, -0.433, -0.636, -0.486, -1.354)
    p.curve_to_cubic_rel(1.447, 0.701, 0.367, -0.248, 1.015, 0.064)
    p.curve_to_cubic_abs(56.490, 163.924, 56.803, 162.957, 56.856, 163.674)
    p.close_path()
    
    p.end()
    
    # path4600-6-1-2
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(53.128, 163.550)
    p.curve_to_cubic_rel(-1.504, -0.567, -0.342, 0.280, -1.016, 0.026)
    p.curve_to_cubic_rel(-0.264, -1.587, -0.489, -0.596, -0.607, -1.305)
    p.curve_to_cubic_rel(1.504, 0.567, 0.342, -0.280, 1.016, -0.027)
    p.curve_to_cubic_abs(53.128, 163.550, 53.353, 162.557, 53.471, 163.268)
    p.close_path()
    
    p.end()
    
    # path4600-6-1-9
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(92.750, 162.028)
    p.curve_to_cubic_rel(0.074, -1.836, -0.441, -0.270, -0.408, -1.092)
    p.curve_to_cubic_smooth_rel(1.675, -0.859, 1.233, -1.128)
    p.curve_to_cubic_rel(-0.075, 1.837, 0.441, 0.270, 0.409, 1.093)
    p.curve_to_cubic_abs(92.750, 162.028, 93.942, 161.914, 93.193, 162.299)
    p.close_path()
    
    p.end()
    
    # path4600-6-1-4
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(88.782, 165.989)
    p.curve_to_cubic_rel(0.383, -1.563, -0.320, -0.306, -0.149, -1.007)
    p.curve_to_cubic_rel(1.541, -0.454, 0.530, -0.556, 1.221, -0.761)
    p.curve_to_cubic_rel(-0.381, 1.562, 0.320, 0.306, 0.149, 1.005)
    p.curve_to_cubic_abs(88.782, 165.989, 89.793, 166.091, 89.102, 166.294)
    p.close_path()
    
    p.end()
    
    # path4600-6-1-1
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(92.629, 165.235)
    p.curve_to_cubic_rel(0.342, -1.571, -0.328, -0.297, -0.175, -1.001)
    p.curve_to_cubic_rel(1.529, -0.491, 0.518, -0.568, 1.203, -0.790)
    p.curve_to_cubic_rel(-0.341, 1.569, 0.329, 0.297, 0.176, 0.999)
    p.curve_to_cubic_smooth_abs(92.629, 165.235, 92.958, 165.533)
    p.close_path()
    
    p.end()
    
    # path4598
    p = Path()
    
    g.add(p)
    p.fill("#7A9CD9")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(92.002, 109.296)
    p.curve_to_cubic_rel(-0.967, -3.793, 0.000, 0.000, 0.047, -3.879)
    p.curve_to_cubic_rel(-2.576, 1.477, -1.014, 0.084, -1.900, 1.435)
    p.curve_to_cubic_rel(-3.082, 0.170, -0.674, 0.043, -3.082, 0.170)
    p.line_to_rel(-0.169, 3.589)
    p.line_to_rel(1.689, 1.393)
    p.line_to_rel(3.546, -0.506)
    p.line_to_abs(92.002, 109.296)
    p.line_to_abs(92.002, 109.296)
    p.close_path()
    
    p.end()
    
    # path4600
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(90.833, 107.648)
    p.curve_to_cubic_rel(-0.772, 1.410, 0.230, 0.379, -0.115, 1.010)
    p.curve_to_cubic_rel(-1.608, 0.040, -0.658, 0.400, -1.378, 0.418)
    p.curve_to_cubic_rel(0.773, -1.410, -0.230, -0.380, 0.115, -1.011)
    p.curve_to_cubic_abs(90.833, 107.648, 89.882, 107.288, 90.602, 107.271)
    p.close_path()
    
    p.end()
    
    # path4602
    p = Path()
    
    g.add(p)
    p.fill("#7A9CD9")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(58.056, 110.345)
    p.curve_to_cubic_rel(-0.380, -2.468, 0.000, 0.000, -0.507, -1.117)
    p.curve_to_cubic_rel(0.472, -2.452, 0.126, -1.352, 0.472, -2.452)
    p.curve_to_cubic_smooth_rel(2.952, 1.133, 1.812, 0.669)
    p.curve_to_cubic_rel(5.024, 1.226, 1.140, 0.465, 5.024, 1.226)
    p.line_to_rel(-2.660, 3.166)
    p.line_to_rel(-1.858, 1.225)
    p.line_to_rel(-2.375, -0.532)
    p.line_to_abs(58.056, 110.345)
    p.close_path()
    
    p.end()
    
    # path4600-6
    p = Path()
    
    g.add(p)
    p.fill("#2F51A8")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(61.295, 108.839)
    p.curve_to_cubic_rel(-1.605, -0.089, -0.242, 0.371, -0.960, 0.331)
    p.curve_to_cubic_rel(-0.729, -1.434, -0.645, -0.421, -0.970, -1.063)
    p.curve_to_cubic_rel(1.606, 0.090, 0.243, -0.370, 0.961, -0.331)
    p.curve_to_cubic_abs(61.295, 108.839, 61.211, 107.827, 61.537, 108.468)
    p.close_path()
    
    p.end()
    
    # path4426
    p = Path()
    
    g.add(p)
    p.fill("#ADD1C5")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(73.125, 23.892)
    p.curve_to_cubic_rel(-21.445, 14.725, -10.986, -0.206, -21.547, 7.884)
    p.curve_to_cubic_rel(9.632, 11.094, 0.104, 6.841, 9.632, 11.094)
    p.curve_to_cubic_rel(0.629, 1.962, 0.104, -0.104, 0.214, 1.341)
    p.curve_to_cubic_rel(1.202, 8.008, 0.414, 0.623, 1.202, 8.008)
    p.line_to_rel(2.449, -0.422)
    p.curve_to_cubic_rel(-7.076, 2.161, 0.000, 0.000, -5.106, 1.229)
    p.curve_to_cubic_rel(-1.142, 3.938, -1.969, 0.934, -1.452, 2.694)
    p.curve_to_cubic_rel(3.424, 1.450, 0.311, 1.245, 2.284, 2.176)
    p.curve_to_cubic_rel(7.041, -1.976, 1.141, -0.726, 7.041, -1.976)
    p.line_to_rel(4.977, -0.615)
    p.line_to_rel(0.513, 16.583)
    p.line_to_rel(-1.129, 1.244)
    p.line_to_rel(-6.323, 3.207)
    p.curve_to_cubic_rel(-7.464, 1.462, 0.000, 0.000, -4.977, 1.255)
    p.curve_to_cubic_rel(-8.093, 3.719, -2.487, 0.207, -7.989, 2.890)
    p.curve_to_cubic_smooth_rel(1.141, 1.770, 1.141, 1.770)
    p.line_to_rel(13.890, 12.120)
    p.curve_to_cubic_rel(-1.449, 1.565, 0.000, 0.000, 0.002, 0.527)
    p.curve_to_cubic_rel(-2.693, 5.386, -1.451, 1.035, -0.725, 5.179)
    p.curve_to_cubic_rel(-3.104, -0.834, -1.970, 0.208, -3.208, -1.144)
    p.curve_to_cubic_rel(5.694, 3.527, 0.104, 0.312, 2.171, 3.217)
    p.curve_to_cubic_rel(5.031, -1.605, 3.524, 0.311, 5.031, -1.605)
    p.curve_to_cubic_smooth_rel(0.458, 1.400, -0.060, 0.675)
    p.curve_to_cubic_rel(6.747, 2.488, 0.518, 0.726, 2.186, 2.384)
    p.curve_to_cubic_rel(5.797, -3.219, 4.560, 0.104, 5.797, -3.219)
    p.curve_to_cubic_smooth_rel(1.141, 0.628, 0.415, 0.317)
    p.curve_to_cubic_rel(5.912, 0.103, 0.727, 0.312, 2.700, 0.103)
    p.curve_to_cubic_rel(2.797, -4.566, 3.213, 0.000, 3.211, -5.085)
    p.curve_to_cubic_rel(-3.629, 1.771, -0.415, 0.520, -2.594, 1.978)
    p.curve_to_cubic_rel(-1.871, -3.743, -1.038, -0.207, -1.871, -3.743)
    p.line_to_rel(-1.349, -2.797)
    p.curve_to_cubic_rel(11.722, -10.568, 0.000, 0.000, 9.716, -8.301)
    p.curve_to_cubic_rel(2.424, -4.549, 3.340, -3.776, 2.570, -4.261)
    p.curve_to_cubic_rel(-4.193, -1.672, -0.575, -1.123, -3.054, -1.257)
    p.curve_to_cubic_rel(-7.567, -2.385, -1.141, -0.414, -7.567, -2.385)
    p.curve_to_cubic_smooth_rel(-4.759, -1.027, -2.788, -0.716)
    p.curve_to_cubic_rel(-6.322, -0.320, -1.969, -0.311, -6.322, -0.320)
    p.line_to_rel(0.718, -19.174)
    p.curve_to_cubic_rel(10.158, 3.015, 0.000, 0.000, 7.981, 3.325)
    p.curve_to_cubic_smooth_rel(0.526, -4.874, 1.563, -3.423)
    p.curve_to_cubic_smooth_rel(-6.952, -2.181, -6.952, -2.181)
    p.line_to_rel(2.386, 0.418)
    p.line_to_rel(0.308, -9.845)
    p.curve_to_cubic_rel(4.566, -1.552, 0.000, 0.000, 1.767, -0.411)
    p.curve_to_cubic_rel(6.733, -11.723, 2.798, -1.140, 6.628, -4.156)
    p.curve_to_cubic_abs(73.125, 23.892, 94.686, 30.422, 84.112, 24.100)
    p.close_path()
    p.move_to_abs(70.637, 85.878)
    p.line_to_rel(13.582, 1.039)
    p.line_to_rel(2.796, 1.756)
    p.curve_to_cubic_rel(7.978, 2.489, 0.000, 0.000, 7.563, 2.074)
    p.curve_to_cubic_rel(-0.821, 0.205, 0.414, 0.414, -0.821, 0.205)
    p.curve_to_cubic_smooth_rel(-6.425, 5.604, -4.870, 4.567)
    p.curve_to_cubic_rel(-7.979, 4.758, -1.555, 1.036, -7.979, 4.758)
    p.line_to_rel(-10.478, -0.615)
    p.curve_to_cubic_rel(-7.567, -4.566, 0.000, 0.000, -5.184, -2.597)
    p.curve_to_cubic_rel(-6.208, -4.976, -2.384, -1.969, -6.208, -4.976)
    p.line_to_rel(-0.583, -0.444)
    p.curve_to_cubic_rel(7.830, -2.455, 0.000, 0.000, 5.136, -2.351)
    p.curve_to_cubic_abs(70.637, 85.878, 65.458, 88.570, 70.637, 85.878)
    p.close_path()
    
    p.end()
    
    # path4593
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(81.835, 113.238)
    p.curve_to_cubic_rel(0.052, -2.747, 0.000, 0.000, 0.362, -1.141)
    p.curve_to_cubic_smooth_rel(-3.834, -5.700, -0.518, -5.700)
    p.curve_to_cubic_rel(-7.618, 0.415, -3.317, 0.000, -6.271, -1.296)
    p.curve_to_cubic_rel(-1.386, 1.093, -0.452, 0.573, -1.201, 0.563)
    p.curve_to_cubic_rel(-0.169, 2.586, -0.367, 1.048, 0.008, 1.877)
    p.curve_to_cubic_rel(-0.052, 3.108, -0.052, 0.207, -0.207, 1.657)
    
    p.end()
    
    # path4432
    p = Path()
    
    g.add(p)
    p.fill("#DB8E18")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(67.325, 107.641)
    p.curve_to_cubic_rel(7.255, 1.866, 0.000, 0.000, 4.249, 2.177)
    p.curve_to_cubic_rel(7.773, -2.072, 3.006, -0.312, 7.773, -2.072)
    p.line_to_rel(-0.829, -13.060)
    p.line_to_rel(-0.312, -8.706)
    p.line_to_rel(0.415, 3.108)
    p.curve_to_cubic_rel(5.597, 0.519, 0.000, 0.000, 4.975, 1.452)
    p.curve_to_cubic_rel(0.830, -3.006, 0.623, -0.933, 0.830, -3.006)
    p.curve_to_cubic_smooth_rel(-2.695, -2.591, 0.311, -2.072)
    p.curve_to_cubic_smooth_rel(-6.322, -2.384, -6.322, -2.384)
    p.curve_to_cubic_smooth_rel(-1.865, -3.368, 0.080, -1.812)
    p.curve_to_cubic_rel(-0.416, 0.519, -0.260, -0.208, -0.416, 0.519)
    p.curve_to_cubic_smooth_rel(-0.207, 2.124, 0.934, 1.709)
    p.curve_to_cubic_rel(-1.865, 3.523, -1.140, 0.414, -1.865, 3.523)
    p.line_to_rel(-1.555, -3.109)
    p.line_to_vertical_rel(-2.798)
    p.curve_to_cubic_rel(-2.591, 1.555, 0.000, 0.000, -2.177, 0.206)
    p.curve_to_cubic_rel(0.000, 1.969, -0.415, 1.348, 0.000, 1.969)
    p.line_to_rel(-6.736, 2.072)
    p.curve_to_cubic_rel(-2.281, 1.971, 0.000, 0.000, -2.384, 0.312)
    p.curve_to_cubic_rel(2.695, 3.834, 0.104, 1.657, 0.311, 4.457)
    p.curve_to_cubic_rel(4.249, -1.555, 2.384, -0.622, 4.249, -1.555)
    p.curve_to_cubic_smooth_rel(0.032, -2.536, 0.014, -3.021)
    p.curve_to_cubic_rel(-0.032, 11.450, 0.071, 1.854, 0.215, 9.807)
    p.curve_to_cubic_abs(67.325, 107.641, 68.155, 99.038, 67.325, 107.538)
    p.line_to_abs(67.325, 107.641)
    p.close_path()
    
    p.end()
    
    # path4595
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(70.924, 81.916)
    p.line_to_rel(1.160, 2.107)
    p.line_to_rel(1.589, -1.827)
    p.line_to_rel(0.803, 1.529)
    p.line_to_rel(1.529, -2.669)
    p.line_to_rel(1.581, 2.358)
    p.line_to_rel(1.373, -2.100)
    
    p.end()
    
    # path4440
    p = Path()
    
    g.add(p)
    p.fill("#FFF6AF")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(82.389, 48.668)
    p.curve_to_cubic_rel(-4.699, 6.255, 0.000, 3.454, -2.104, 6.255)
    p.curve_to_cubic_rel(-4.700, -6.255, -2.597, 0.000, -4.700, -2.801)
    p.curve_to_cubic_smooth_rel(4.700, -6.255, 2.104, -6.255)
    p.curve_to_cubic_abs(82.389, 48.668, 80.286, 42.413, 82.389, 45.213)
    p.close_path()
    
    p.end()
    
    # path4440-5
    p = Path()
    
    g.add(p)
    p.fill("#FFF6AF")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(72.543, 48.771)
    p.curve_to_cubic_rel(-4.699, 6.256, 0.000, 3.455, -2.104, 6.256)
    p.curve_to_cubic_smooth_rel(-4.700, -6.256, -4.700, -2.801)
    p.curve_to_cubic_rel(4.700, -6.254, 0.000, -3.453, 2.104, -6.254)
    p.curve_to_cubic_abs(72.543, 48.771, 70.439, 42.517, 72.543, 45.317)
    p.close_path()
    
    p.end()
    
    # path4464
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(60.796, 64.110)
    p.curve_to_cubic_rel(11.815, -1.762, 0.000, 0.000, 6.736, -1.969)
    p.curve_to_cubic_rel(9.846, 1.348, 5.079, 0.208, 8.810, 0.933)
    p.curve_to_cubic_rel(2.758, 1.395, 1.037, 0.414, 2.758, 1.395)
    
    p.end()
    
    # path4466
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(60.588, 63.178)
    p.line_to_vertical_rel(1.969)
    
    p.end()
    
    # path4468
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(85.048, 63.696)
    p.line_to_rel(0.519, 2.280)
    
    p.end()

    p = Path()

    g.add(p)
    p.fill("#95583B")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)

    rect(p, 67.598, 46.03, 1.759, 4.909)

    p.end()

    p = Path()

    g.add(p)
    p.fill("#95583B")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)

    rect(p, 76.246, 46.286, 1.759, 4.91)

    p.end()
    
    # path4437
    p = Path()
    
    g.add(p)
    p.fill("#ADD1C5")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(72.301, 51.466)
    p.curve_to_cubic_rel(3.419, 2.695, 0.000, 0.000, 2.073, -0.828)
    p.curve_to_cubic_rel(2.384, 10.882, 1.348, 3.523, 2.690, 8.564)
    p.curve_to_cubic_rel(-5.597, 6.115, -0.414, 3.139, -1.104, 6.013)
    p.curve_to_cubic_rel(-5.700, -6.426, -2.075, 0.049, -6.115, -1.450)
    p.curve_to_cubic_rel(3.524, -11.400, 0.415, -4.975, 0.820, -6.271)
    p.curve_to_cubic_abs(72.301, 51.466, 71.332, 51.434, 72.404, 51.414)
    p.line_to_abs(72.301, 51.466)
    p.close_path()
    
    p.end()
    
    # path4472
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(59.656, 30.736)
    p.curve_to_cubic_rel(-0.700, 0.675, 0.000, 0.372, -0.313, 0.675)
    p.curve_to_cubic_rel(-0.699, -0.675, -0.386, 0.000, -0.699, -0.303)
    p.curve_to_cubic_smooth_rel(0.699, -0.673, 0.313, -0.673)
    p.curve_to_cubic_abs(59.656, 30.736, 59.343, 30.063, 59.656, 30.364)
    p.close_path()
    
    p.end()
    
    # path4472-1
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(64.864, 27.421)
    p.curve_to_cubic_rel(-0.699, 0.674, 0.000, 0.371, -0.313, 0.674)
    p.curve_to_cubic_smooth_rel(-0.699, -0.674, -0.699, -0.303)
    p.curve_to_cubic_rel(0.699, -0.674, 0.000, -0.373, 0.313, -0.674)
    p.curve_to_cubic_smooth_abs(64.864, 27.421, 64.864, 27.048)
    p.close_path()
    
    p.end()
    
    # path4472-11
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(67.817, 28.924)
    p.curve_to_cubic_rel(-0.699, 0.673, 0.000, 0.372, -0.313, 0.673)
    p.curve_to_cubic_rel(-0.700, -0.673, -0.387, 0.000, -0.700, -0.301)
    p.curve_to_cubic_smooth_rel(0.700, -0.674, 0.313, -0.674)
    p.curve_to_cubic_abs(67.817, 28.924, 67.504, 28.250, 67.817, 28.552)
    p.close_path()
    
    p.end()
    
    # path4472-2
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(74.088, 26.229)
    p.curve_to_cubic_rel(-0.700, 0.674, 0.000, 0.372, -0.313, 0.674)
    p.curve_to_cubic_smooth_rel(-0.699, -0.674, -0.699, -0.302)
    p.curve_to_cubic_smooth_rel(0.699, -0.674, 0.313, -0.674)
    p.curve_to_cubic_smooth_abs(74.088, 26.229, 74.088, 25.856)
    p.close_path()
    
    p.end()
    
    # path4472-14
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(76.057, 29.027)
    p.curve_to_cubic_rel(-0.699, 0.673, 0.000, 0.372, -0.313, 0.673)
    p.curve_to_cubic_rel(-0.700, -0.673, -0.387, 0.000, -0.700, -0.301)
    p.curve_to_cubic_smooth_rel(0.700, -0.674, 0.313, -0.674)
    p.curve_to_cubic_abs(76.057, 29.027, 75.744, 28.354, 76.057, 28.655)
    p.close_path()
    
    p.end()
    
    # path4472-3
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(83.208, 30.840)
    p.curve_to_cubic_rel(-0.698, 0.675, 0.000, 0.373, -0.312, 0.675)
    p.curve_to_cubic_smooth_rel(-0.699, -0.675, -0.699, -0.302)
    p.curve_to_cubic_rel(0.699, -0.673, 0.000, -0.371, 0.313, -0.673)
    p.curve_to_cubic_smooth_abs(83.208, 30.840, 83.208, 30.469)
    p.close_path()
    
    p.end()
    
    # path4472-16
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(86.940, 29.545)
    p.curve_to_cubic_rel(-0.700, 0.674, 0.000, 0.372, -0.313, 0.674)
    p.curve_to_cubic_rel(-0.699, -0.674, -0.386, 0.000, -0.699, -0.302)
    p.curve_to_cubic_smooth_rel(0.699, -0.673, 0.313, -0.673)
    p.curve_to_cubic_abs(86.940, 29.545, 86.626, 28.872, 86.940, 29.173)
    p.close_path()
    
    p.end()
    
    # path4472-5
    p = Path()
    
    g.add(p)
    p.fill("#006740")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(90.620, 33.069)
    p.curve_to_cubic_rel(-0.698, 0.674, 0.000, 0.372, -0.313, 0.674)
    p.curve_to_cubic_rel(-0.700, -0.674, -0.388, 0.000, -0.700, -0.302)
    p.curve_to_cubic_smooth_rel(0.700, -0.674, 0.313, -0.674)
    p.curve_to_cubic_abs(90.620, 33.069, 90.306, 32.396, 90.620, 32.697)
    p.close_path()
    
    p.end()
    
    # path4577
    p = Path()
    
    g.add(p)
    p.fill("#ADD1C5")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(83.061, 47.129)
    p.curve_to_cubic_rel(-4.983, -6.669, 0.000, 0.000, -0.807, -6.816)
    p.curve_to_cubic_rel(-5.204, 5.496, -4.178, 0.146, -5.204, 5.496)
    p.curve_to_cubic_smooth_rel(-5.276, -4.984, -1.099, -5.130)
    p.curve_to_cubic_rel(-4.837, 5.131, -4.177, 0.147, -4.837, 4.545)
    p.curve_to_cubic_smooth_rel(1.100, 0.659, 1.100, 0.659)
    p.curve_to_cubic_smooth_rel(-1.979, 0.367, -1.979, -0.366)
    p.curve_to_cubic_rel(1.540, 0.952, 0.000, 0.732, 0.073, 0.952)
    p.curve_to_cubic_rel(19.568, 0.732, 1.465, 0.000, 19.568, 0.732)
    p.curve_to_cubic_smooth_rel(1.392, -0.879, 1.611, -0.293)
    p.curve_to_cubic_rel(-2.126, -0.879, -0.220, -0.587, -2.126, -0.879)
    p.line_to_abs(83.061, 47.129)
    p.line_to_abs(83.061, 47.129)
    p.close_path()
    
    p.end()
    
    # path4579
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(72.874, 45.736)
    p.curve_to_cubic_rel(-0.366, 1.173, 0.000, 0.000, 0.367, 0.733)
    p.curve_to_cubic_rel(-0.732, 1.173, -0.733, 0.439, -0.732, 1.173)
    
    p.end()
    
    # path4581
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(64.886, 46.688)
    p.line_to_rel(5.863, 0.073)
    
    p.end()

    p = Path()

    g.add(p)
    p.fill("#ADD1C5")
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)

    polygon(p, [(81.212, 85.669), (81.248, 86.69), (81.35, 86.698)])

    p.end()
    
    # path4583
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(75.953, 47.056)
    p.line_to_rel(5.057, 0.073)
    
    p.end()
    
    # path4587
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(62.027, 40.387)
    p.curve_to_cubic_rel(5.570, 0.513, 0.000, 0.000, 3.079, 0.732)
    p.curve_to_cubic_rel(5.057, -0.073, 2.493, -0.220, 5.057, -0.073)
    
    p.end()
    
    # path4589
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(75.000, 37.309)
    p.curve_to_cubic_rel(4.031, -1.759, 0.000, 0.000, 2.199, -2.126)
    p.curve_to_cubic_rel(2.565, 1.905, 1.832, 0.366, 2.124, 1.245)
    p.curve_to_cubic_rel(0.658, 1.832, 0.438, 0.659, 0.658, 1.832)
    
    p.end()
    
    # path4591
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.7164)
    
    p.move_to_abs(77.418, 34.229)
    p.curve_to_cubic_rel(3.006, -0.512, 2.052, -0.585, 1.832, -0.806)
    p.curve_to_cubic_rel(1.978, 1.465, 1.172, 0.292, 1.978, 1.465)
    
    p.end()
    #endregion drawing

# Sandy Cheeks
def person_d(x, y, scale_x, scale_y, crown):
    g = PathGroup()

    width = 150.000 * scale_x
    height = 167.160 * scale_y

    g.translate(-width / 2.0, -height)
    g.scale(scale_x, scale_y)
    g.translate(x, y)

    if crown:
        #region crown
        # path4672_3_
        p = Path()
    
        g.add(p)
        p.fill("#870303")
    
        p.move_to_abs(76.682, 0.000)
        p.line_to_rel(-0.447, 0.767)
        p.line_to_rel(-5.173, 8.834)
        p.line_to_rel(-8.667, -5.464)
        p.line_to_rel(-0.750, -0.476)
        p.line_to_rel(-0.224, 0.863)
        p.line_to_rel(-2.604, 9.903)
        p.line_to_rel(-9.813, -2.922)
        p.line_to_rel(-0.851, -0.252)
        p.line_to_rel(0.011, 0.884)
        p.line_to_rel(0.168, 10.240)
        p.line_to_rel(-10.239, -0.168)
        p.line_to_rel(-0.891, -0.011)
        p.line_to_rel(0.257, 0.851)
        p.line_to_rel(2.922, 9.814)
        p.line_to_rel(-9.908, 2.603)
        p.line_to_rel(-0.857, 0.223)
        p.line_to_rel(0.476, 0.751)
        p.line_to_rel(5.464, 8.660)
        p.line_to_rel(-8.839, 5.179)
        p.line_to_rel(-0.767, 0.452)
        p.line_to_rel(0.661, 0.594)
        p.line_to_rel(7.597, 6.868)
        p.line_to_rel(-7.110, 7.367)
        p.line_to_rel(-0.616, 0.640)
        p.line_to_rel(0.795, 0.397)
        p.line_to_rel(9.170, 4.563)
        p.line_to_rel(-4.859, 9.012)
        p.line_to_rel(-0.426, 0.786)
        p.line_to_rel(0.873, 0.167)
        p.line_to_rel(10.061, 1.916)
        p.line_to_rel(-2.245, 9.993)
        p.line_to_abs(39.655, 93.900)
        p.line_to_rel(0.885, -0.072)
        p.line_to_rel(10.200, -0.867)
        p.line_to_rel(0.538, 10.229)
        p.line_to_rel(0.044, 0.883)
        p.line_to_rel(0.834, -0.307)
        p.line_to_rel(9.590, -3.589)
        p.line_to_rel(3.270, 9.707)
        p.line_to_rel(0.285, 0.841)
        p.line_to_rel(0.717, -0.527)
        p.line_to_rel(8.269, -6.041)
        p.line_to_rel(5.771, 8.465)
        p.line_to_rel(0.498, 0.734)
        p.line_to_rel(0.549, -0.701)
        p.line_to_rel(6.332, -8.044)
        p.line_to_rel(7.838, 6.590)
        p.line_to_rel(0.683, 0.571)
        p.line_to_rel(0.341, -0.824)
        p.line_to_rel(3.925, -9.455)
        p.line_to_rel(9.327, 4.233)
        p.line_to_rel(0.806, 0.362)
        p.line_to_rel(0.106, -0.879)
        p.line_to_rel(1.232, -10.166)
        p.line_to_rel(10.121, 1.562)
        p.line_to_rel(0.874, 0.134)
        p.line_to_rel(-0.135, -0.879)
        p.line_to_rel(-1.562, -10.121)
        p.line_to_rel(10.172, -1.231)
        p.line_to_rel(0.879, -0.106)
        p.line_to_rel(-0.364, -0.806)
        p.line_to_rel(-4.231, -9.327)
        p.line_to_rel(9.455, -3.924)
        p.line_to_rel(0.822, -0.342)
        p.line_to_rel(-0.576, -0.677)
        p.line_to_rel(-6.590, -7.838)
        p.line_to_rel(8.051, -6.337)
        p.line_to_rel(0.695, -0.548)
        p.line_to_rel(-0.734, -0.499)
        p.line_to_rel(-8.459, -5.767)
        p.line_to_rel(6.041, -8.273)
        p.line_to_rel(0.525, -0.717)
        p.line_to_rel(-0.846, -0.280)
        p.line_to_rel(-9.701, -3.275)
        p.line_to_rel(3.583, -9.589)
        p.line_to_rel(0.313, -0.834)
        p.line_to_rel(-0.885, -0.044)
        p.line_to_abs(118.910, 24.790)
        p.line_to_rel(0.868, -10.206)
        p.line_to_rel(0.078, -0.884)
        p.line_to_rel(-0.868, 0.196)
        p.line_to_rel(-9.987, 2.250)
        p.line_to_abs(107.075, 6.080)
        p.line_to_rel(-0.168, -0.868)
        p.line_to_rel(-0.778, 0.420)
        p.line_to_rel(-9.013, 4.860)
        p.line_to_rel(-4.563, -9.170)
        p.line_to_rel(-0.398, -0.795)
        p.line_to_rel(-0.639, 0.616)
        p.line_to_rel(-7.372, 7.116)
        p.line_to_rel(-6.863, -7.603)
        p.line_to_abs(76.682, 0.000)
        p.line_to_abs(76.682, 0.000)
        p.close_path()
        p.move_to_abs(76.912, 2.189)
        p.line_to_rel(6.718, 7.440)
        p.line_to_rel(0.453, 0.499)
        p.line_to_rel(0.481, -0.470)
        p.line_to_rel(7.216, -6.958)
        p.line_to_rel(4.467, 8.974)
        p.line_to_rel(0.298, 0.604)
        p.line_to_rel(0.594, -0.319)
        p.line_to_rel(8.827, -4.758)
        p.line_to_rel(1.877, 9.848)
        p.line_to_rel(0.129, 0.661)
        p.line_to_rel(0.654, -0.146)
        p.line_to_rel(9.786, -2.200)
        p.line_to_rel(-0.852, 9.988)
        p.line_to_rel(-0.056, 0.672)
        p.line_to_rel(0.672, 0.034)
        p.line_to_rel(10.010, 0.520)
        p.line_to_rel(-3.510, 9.388)
        p.line_to_rel(-0.235, 0.634)
        p.line_to_rel(0.638, 0.213)
        p.line_to_rel(9.494, 3.202)
        p.line_to_rel(-5.912, 8.094)
        p.line_to_rel(-0.396, 0.543)
        p.line_to_rel(0.561, 0.380)
        p.line_to_rel(8.279, 5.649)
        p.line_to_rel(-7.877, 6.198)
        p.line_to_rel(-0.531, 0.415)
        p.line_to_rel(0.437, 0.515)
        p.line_to_rel(6.454, 7.675)
        p.line_to_rel(-9.265, 3.840)
        p.line_to_rel(-0.616, 0.264)
        p.line_to_rel(0.274, 0.611)
        p.line_to_rel(4.149, 9.129)
        p.line_to_rel(-9.960, 1.198)
        p.line_to_rel(-0.667, 0.084)
        p.line_to_rel(0.102, 0.666)
        p.line_to_rel(1.527, 9.908)
        p.line_to_rel(-9.908, -1.527)
        p.line_to_rel(-0.660, -0.105)
        p.line_to_rel(-0.084, 0.672)
        p.line_to_rel(-1.204, 9.947)
        p.line_to_rel(-9.125, -4.143)
        p.line_to_rel(-0.616, -0.273)
        p.line_to_rel(-0.258, 0.621)
        p.line_to_rel(-3.840, 9.259)
        p.line_to_rel(-7.676, -6.454)
        p.line_to_rel(-0.515, -0.432)
        p.line_to_rel(-0.414, 0.527)
        p.line_to_rel(-6.203, 7.877)
        p.line_to_rel(-5.643, -8.280)
        p.line_to_rel(-0.381, -0.556)
        p.line_to_rel(-0.543, 0.393)
        p.line_to_rel(-8.095, 5.918)
        p.line_to_rel(-3.203, -9.501)
        p.line_to_rel(-0.213, -0.638)
        p.line_to_rel(-0.633, 0.234)
        p.line_to_rel(-9.388, 3.510)
        p.line_to_abs(52.010, 92.221)
        p.line_to_rel(-0.039, -0.672)
        p.line_to_rel(-0.667, 0.056)
        p.line_to_rel(-9.993, 0.852)
        p.line_to_rel(2.200, -9.786)
        p.line_to_rel(0.152, -0.655)
        p.line_to_rel(-0.661, -0.124)
        p.line_to_rel(-9.847, -1.880)
        p.line_to_rel(4.752, -8.829)
        p.line_to_rel(0.320, -0.588)
        p.line_to_rel(-0.599, -0.303)
        p.line_to_rel(-8.979, -4.461)
        p.line_to_rel(6.964, -7.216)
        p.line_to_rel(0.464, -0.487)
        p.line_to_rel(-0.499, -0.448)
        p.line_to_rel(-7.440, -6.724)
        p.line_to_rel(8.655, -5.072)
        p.line_to_rel(0.577, -0.336)
        p.line_to_rel(-0.358, -0.571)
        p.line_to_rel(-5.346, -8.475)
        p.line_to_rel(9.696, -2.553)
        p.line_to_rel(0.649, -0.168)
        p.line_to_rel(-0.190, -0.644)
        p.line_to_rel(-2.867, -9.606)
        p.line_to_rel(10.027, 0.162)
        p.line_to_rel(0.672, 0.011)
        p.line_to_rel(-0.011, -0.671)
        p.line_to_rel(-0.156, -10.027)
        p.line_to_rel(9.605, 2.861)
        p.line_to_rel(0.645, 0.196)
        p.line_to_rel(0.167, -0.655)
        p.line_to_rel(2.547, -9.696)
        p.line_to_rel(8.481, 5.352)
        p.line_to_rel(0.565, 0.358)
        p.line_to_rel(0.342, -0.582)
        p.line_to_abs(76.912, 2.189)
        p.line_to_abs(76.912, 2.189)
        p.close_path()
    
        p.end()
    
        # path4662_4_
        p = Path()
    
        g.add(p)
        p.fill("#E60000")
    
        p.move_to_abs(121.913, 95.958)
        p.line_to_rel(-10.787, -1.662)
        p.line_to_rel(-1.309, 10.834)
        p.line_to_rel(-9.938, -4.510)
        p.line_to_rel(-4.185, 10.080)
        p.line_to_rel(-8.352, -7.025)
        p.line_to_rel(-6.749, 8.577)
        p.line_to_rel(-6.147, -9.018)
        p.line_to_rel(-8.813, 6.438)
        p.line_to_rel(-3.486, -10.342)
        p.line_to_rel(-10.223, 3.820)
        p.line_to_rel(-0.566, -10.897)
        p.line_to_rel(-10.875, 0.923)
        p.line_to_rel(2.394, -10.647)
        p.line_to_rel(-10.720, -2.046)
        p.line_to_rel(5.179, -9.607)
        p.line_to_rel(-9.771, -4.863)
        p.line_to_rel(7.579, -7.853)
        p.line_to_rel(-8.097, -7.318)
        p.line_to_rel(9.417, -5.518)
        p.line_to_rel(-5.822, -9.230)
        p.line_to_rel(10.556, -2.772)
        p.line_to_rel(-3.116, -10.460)
        p.line_to_rel(10.913, 0.178)
        p.line_to_rel(-0.178, -10.912)
        p.line_to_rel(10.459, 3.116)
        p.line_to_rel(2.772, -10.556)
        p.line_to_rel(9.231, 5.822)
        p.line_to_rel(5.517, -9.417)
        p.line_to_rel(7.318, 8.097)
        p.line_to_rel(7.854, -7.579)
        p.line_to_rel(4.862, 9.771)
        p.line_to_rel(9.607, -5.178)
        p.line_to_rel(2.045, 10.720)
        p.line_to_rel(10.649, -2.395)
        p.line_to_rel(-0.924, 10.875)
        p.line_to_rel(10.899, 0.566)
        p.line_to_rel(-3.821, 10.223)
        p.line_to_rel(10.341, 3.487)
        p.line_to_rel(-6.438, 8.812)
        p.line_to_rel(9.018, 6.147)
        p.line_to_rel(-8.577, 6.748)
        p.line_to_rel(7.025, 8.352)
        p.line_to_rel(-10.079, 4.185)
        p.line_to_rel(4.510, 9.938)
        p.line_to_rel(-10.834, 1.310)
        p.line_to_abs(121.913, 95.958)
        p.close_path()
    
        p.end()
    
        # path4664_3_
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
        p.stroke_color("#4F3A02")
        p.stroke_width(1.7712)
    
        p.move_to_abs(118.294, 92.341)
        p.line_to_rel(-9.795, -1.510)
        p.line_to_rel(-1.190, 9.840)
        p.line_to_rel(-9.024, -4.097)
        p.line_to_rel(-3.801, 9.153)
        p.line_to_rel(-7.586, -6.379)
        p.line_to_rel(-6.129, 7.789)
        p.line_to_rel(-5.583, -8.189)
        p.line_to_rel(-8.003, 5.848)
        p.line_to_rel(-3.167, -9.393)
        p.line_to_rel(-9.284, 3.471)
        p.line_to_rel(-0.515, -9.898)
        p.line_to_rel(-9.876, 0.838)
        p.line_to_rel(2.174, -9.670)
        p.line_to_rel(-9.736, -1.858)
        p.line_to_rel(4.703, -8.726)
        p.line_to_rel(-8.874, -4.416)
        p.line_to_rel(6.882, -7.132)
        p.line_to_rel(-7.353, -6.646)
        p.line_to_rel(8.552, -5.012)
        p.line_to_rel(-5.288, -8.383)
        p.line_to_rel(9.587, -2.519)
        p.line_to_rel(-2.830, -9.500)
        p.line_to_rel(9.911, 0.162)
        p.line_to_rel(-0.162, -9.911)
        p.line_to_rel(9.500, 2.830)
        p.line_to_rel(2.518, -9.586)
        p.line_to_rel(8.384, 5.288)
        p.line_to_rel(5.010, -8.552)
        p.line_to_rel(6.646, 7.354)
        p.line_to_rel(7.133, -6.882)
        p.line_to_rel(4.416, 8.874)
        p.line_to_rel(8.726, -4.703)
        p.line_to_rel(1.857, 9.736)
        p.line_to_rel(9.671, -2.175)
        p.line_to_rel(-0.838, 9.876)
        p.line_to_rel(9.898, 0.515)
        p.line_to_rel(-3.471, 9.285)
        p.line_to_rel(9.393, 3.166)
        p.line_to_rel(-5.848, 8.004)
        p.line_to_rel(8.189, 5.583)
        p.line_to_rel(-7.789, 6.129)
        p.line_to_rel(6.379, 7.586)
        p.line_to_rel(-9.154, 3.800)
        p.line_to_rel(4.097, 9.026)
        p.line_to_rel(-9.841, 1.189)
        p.line_to_abs(118.294, 92.341)
        p.close_path()
    
        p.end()
    
        # path4666_3_
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
        p.stroke_color("#4F3A02")
        p.stroke_width(1.7712)
    
        p.move_to_abs(122.661, 87.362)
        p.line_to_rel(-9.910, -0.218)
        p.line_to_rel(0.105, 9.910)
        p.line_to_rel(-9.483, -2.883)
        p.line_to_rel(-2.572, 9.571)
        p.line_to_rel(-8.354, -5.334)
        p.line_to_rel(-5.060, 8.522)
        p.line_to_rel(-6.604, -7.391)
        p.line_to_rel(-7.173, 6.842)
        p.line_to_rel(-4.365, -8.898)
        p.line_to_rel(-8.752, 4.652)
        p.line_to_rel(-1.802, -9.746)
        p.line_to_rel(-9.683, 2.120)
        p.line_to_rel(0.894, -9.872)
        p.line_to_rel(-9.896, -0.570)
        p.line_to_rel(3.524, -9.266)
        p.line_to_rel(-9.374, -3.219)
        p.line_to_rel(5.893, -7.970)
        p.line_to_rel(-8.158, -5.630)
        p.line_to_rel(7.825, -6.085)
        p.line_to_rel(-6.337, -7.622)
        p.line_to_rel(9.176, -3.748)
        p.line_to_rel(-4.045, -9.049)
        p.line_to_rel(9.846, -1.133)
        p.line_to_rel(-1.454, -9.805)
        p.line_to_rel(9.788, 1.566)
        p.line_to_rel(1.245, -9.833)
        p.line_to_rel(9.002, 4.148)
        p.line_to_rel(3.852, -9.133)
        p.line_to_rel(7.550, 6.423)
        p.line_to_rel(6.173, -7.754)
        p.line_to_rel(5.536, 8.222)
        p.line_to_rel(8.037, -5.801)
        p.line_to_rel(3.111, 9.410)
        p.line_to_rel(9.305, -3.417)
        p.line_to_rel(0.459, 9.901)
        p.line_to_rel(9.881, -0.781)
        p.line_to_rel(-2.229, 9.657)
        p.line_to_rel(9.726, 1.913)
        p.line_to_rel(-4.753, 8.698)
        p.line_to_rel(8.849, 4.467)
        p.line_to_rel(-6.924, 7.093)
        p.line_to_rel(7.316, 6.688)
        p.line_to_rel(-8.581, 4.962)
        p.line_to_rel(5.241, 8.414)
        p.line_to_rel(-9.602, 2.464)
        p.line_to_abs(122.661, 87.362)
        p.close_path()
    
        p.end()
    
        # path4658_3_
        p = Path()
    
        g.add(p)
        p.fill("#E69B00")
    
        p.move_to_abs(118.294, 92.341)
        p.line_to_rel(-9.795, -1.510)
        p.line_to_rel(-1.190, 9.840)
        p.line_to_rel(-9.024, -4.097)
        p.line_to_rel(-3.801, 9.153)
        p.line_to_rel(-7.586, -6.379)
        p.line_to_rel(-6.129, 7.789)
        p.line_to_rel(-5.583, -8.189)
        p.line_to_rel(-8.003, 5.848)
        p.line_to_rel(-3.167, -9.393)
        p.line_to_rel(-9.284, 3.471)
        p.line_to_rel(-0.515, -9.898)
        p.line_to_rel(-9.876, 0.838)
        p.line_to_rel(2.174, -9.670)
        p.line_to_rel(-9.736, -1.858)
        p.line_to_rel(4.703, -8.726)
        p.line_to_rel(-8.874, -4.416)
        p.line_to_rel(6.882, -7.132)
        p.line_to_rel(-7.353, -6.646)
        p.line_to_rel(8.552, -5.012)
        p.line_to_rel(-5.288, -8.383)
        p.line_to_rel(9.587, -2.519)
        p.line_to_rel(-2.830, -9.500)
        p.line_to_rel(9.911, 0.162)
        p.line_to_rel(-0.162, -9.911)
        p.line_to_rel(9.500, 2.830)
        p.line_to_rel(2.518, -9.586)
        p.line_to_rel(8.384, 5.288)
        p.line_to_rel(5.010, -8.552)
        p.line_to_rel(6.646, 7.354)
        p.line_to_rel(7.133, -6.882)
        p.line_to_rel(4.416, 8.874)
        p.line_to_rel(8.726, -4.703)
        p.line_to_rel(1.857, 9.736)
        p.line_to_rel(9.671, -2.175)
        p.line_to_rel(-0.838, 9.876)
        p.line_to_rel(9.898, 0.515)
        p.line_to_rel(-3.471, 9.285)
        p.line_to_rel(9.393, 3.166)
        p.line_to_rel(-5.848, 8.004)
        p.line_to_rel(8.189, 5.583)
        p.line_to_rel(-7.789, 6.129)
        p.line_to_rel(6.379, 7.586)
        p.line_to_rel(-9.154, 3.800)
        p.line_to_rel(4.097, 9.026)
        p.line_to_rel(-9.841, 1.189)
        p.line_to_abs(118.294, 92.341)
        p.close_path()
    
        p.end()
    
        # path4660_3_
        p = Path()
    
        g.add(p)
        p.fill("#FFDD55")
    
        p.move_to_abs(122.661, 87.362)
        p.line_to_rel(-9.910, -0.218)
        p.line_to_rel(0.105, 9.910)
        p.line_to_rel(-9.483, -2.883)
        p.line_to_rel(-2.572, 9.572)
        p.line_to_rel(-8.354, -5.335)
        p.line_to_rel(-5.060, 8.522)
        p.line_to_rel(-6.604, -7.391)
        p.line_to_rel(-7.173, 6.842)
        p.line_to_rel(-4.365, -8.898)
        p.line_to_rel(-8.752, 4.652)
        p.line_to_rel(-1.802, -9.746)
        p.line_to_rel(-9.683, 2.120)
        p.line_to_rel(0.894, -9.872)
        p.line_to_rel(-9.896, -0.570)
        p.line_to_rel(3.524, -9.266)
        p.line_to_rel(-9.374, -3.219)
        p.line_to_rel(5.893, -7.970)
        p.line_to_rel(-8.158, -5.629)
        p.line_to_rel(7.825, -6.086)
        p.line_to_rel(-6.337, -7.622)
        p.line_to_rel(9.176, -3.748)
        p.line_to_rel(-4.045, -9.049)
        p.line_to_rel(9.846, -1.133)
        p.line_to_rel(-1.454, -9.805)
        p.line_to_rel(9.788, 1.566)
        p.line_to_rel(1.245, -9.833)
        p.line_to_rel(9.002, 4.148)
        p.line_to_rel(3.852, -9.132)
        p.line_to_rel(7.550, 6.422)
        p.line_to_rel(6.173, -7.754)
        p.line_to_rel(5.536, 8.222)
        p.line_to_rel(8.037, -5.801)
        p.line_to_rel(3.111, 9.410)
        p.line_to_rel(9.305, -3.417)
        p.line_to_rel(0.459, 9.901)
        p.line_to_rel(9.881, -0.781)
        p.line_to_rel(-2.230, 9.657)
        p.line_to_rel(9.727, 1.915)
        p.line_to_rel(-4.753, 8.697)
        p.line_to_rel(8.849, 4.467)
        p.line_to_rel(-6.924, 7.093)
        p.line_to_rel(7.316, 6.688)
        p.line_to_rel(-8.581, 4.962)
        p.line_to_rel(5.241, 8.414)
        p.line_to_rel(-9.602, 2.464)
        p.line_to_abs(122.661, 87.362)
        p.close_path()
    
        p.end()
    
        # path4676_3_
        p = Path()
    
        g.add(p)
    
        p.move_to_abs(47.833, 56.526)
        p.curve_to_cubic_rel(34.945, -33.435, 0.418, -18.882, 16.063, -33.851)
        p.curve_to_cubic_smooth_rel(33.437, 34.944, 33.853, 16.061)
        p.curve_to_cubic_rel(-34.942, 33.437, -0.416, 18.882, -16.060, 33.853)
        p.curve_to_cubic_rel(-33.439, -34.940, -18.882, -0.414, -33.854, -16.057)
    
        p.end()
    
        # path4695_3_
        p = Path()
    
        g.add(p)
        p.fill("#E6B52D")
        p.stroke_color("#E6B52D")
        p.stroke_width(1.2809)
    
        p.move_to_abs(71.134, 94.601)
        p.curve_to_cubic_rel(-26.429, -48.206, -20.609, -6.014, -32.442, -27.596)
        p.curve_to_cubic_rel(48.205, -26.433, 6.013, -20.610, 27.594, -32.445)
        p.curve_to_cubic_rel(26.435, 48.204, 20.610, 6.011, 32.444, 27.593)
        p.curve_to_cubic_rel(-48.203, 26.437, -6.012, 20.611, -27.592, 32.446)
    
        p.end()
    
        # path4693_3_
        p = Path()
    
        g.add(p)
        p.fill("#FFFBCC")
    
        p.move_to_abs(71.134, 94.601)
        p.curve_to_cubic_rel(-26.429, -48.206, -20.609, -6.014, -32.442, -27.596)
        p.curve_to_cubic_rel(48.205, -26.433, 6.013, -20.610, 27.594, -32.445)
        p.curve_to_cubic_rel(26.435, 48.204, 20.610, 6.011, 32.444, 27.593)
        p.curve_to_cubic_rel(-48.203, 26.437, -6.012, 20.611, -27.592, 32.446)
    
        p.end()
        #endregion crown
    
    #region drawing
    # path3861
    p = Path()
    
    g.add(p)
    p.fill("#75CCDD")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(115.005, 57.899)
    p.curve_to_cubic_rel(-32.375, 32.029, 0.000, 17.689, -14.494, 32.029)
    p.curve_to_cubic_rel(-32.375, -32.029, -17.880, 0.000, -32.375, -14.340)
    p.curve_to_cubic_rel(32.375, -32.027, 0.000, -17.688, 14.496, -32.027)
    p.curve_to_cubic_abs(115.005, 57.899, 100.511, 25.873, 115.005, 40.211)
    p.line_to_abs(115.005, 57.899)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(105.345, 51.538)
    p.curve_to_cubic_rel(4.798, 10.558, 1.193, 3.315, 0.959, 11.134)
    p.curve_to_cubic_rel(0.384, -12.286, 3.840, -0.576, 2.112, -7.871)
    p.curve_to_cubic_rel(-7.678, -7.485, -1.727, -4.415, -3.838, -10.173)
    p.curve_to_cubic_abs(105.345, 51.538, 99.010, 45.012, 104.149, 48.223)
    p.line_to_abs(105.345, 51.538)
    p.close_path()
    
    p.end()
    
    # path3873
    p = Path()
    
    g.add(p)
    p.fill("#95A2AA")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(57.933, 79.754)
    p.curve_to_cubic_rel(20.729, -0.768, 0.000, 0.000, 12.669, -2.879)
    p.curve_to_cubic_rel(18.620, 5.951, 8.063, 2.112, 17.085, 4.991)
    p.curve_to_cubic_rel(2.303, 1.535, 1.536, 0.959, 2.303, 1.535)
    p.line_to_rel(-4.223, 9.406)
    p.line_to_rel(-35.701, -4.223)
    p.line_to_abs(57.933, 79.754)
    p.close_path()
    
    p.end()
    
    # path3875
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(96.515, 88.968)
    p.curve_to_cubic_rel(-17.853, -6.718, 0.000, 0.000, -7.679, -5.374)
    p.curve_to_cubic_rel(-17.466, -0.192, -10.173, -1.343, -17.466, -0.192)
    p.line_to_rel(0.768, 4.990)
    p.line_to_rel(1.151, 9.789)
    p.line_to_rel(27.257, 0.960)
    p.line_to_abs(96.515, 88.968)
    p.close_path()
    
    p.end()
    
    # path3782_1_
    p = Path()
    
    g.add(p)
    p.fill("#E57AB0")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(63.938, 33.099)
    p.curve_to_cubic_rel(-0.831, 8.614, 0.000, 0.000, -5.346, 7.724)
    p.curve_to_cubic_rel(8.496, -4.812, 4.515, 0.892, 8.733, -3.683)
    p.curve_to_cubic_rel(-3.149, -4.932, -0.237, -1.129, -3.149, -4.932)
    p.curve_to_cubic_smooth_rel(6.477, 4.337, 3.089, 6.001)
    p.curve_to_cubic_rel(4.695, -8.080, 3.386, -1.663, 6.595, -7.426)
    p.curve_to_cubic_rel(-7.961, 0.416, -1.901, -0.654, -7.961, 0.416)
    p.curve_to_cubic_smooth_rel(8.733, -3.031, 8.377, -0.296)
    p.curve_to_cubic_rel(-5.466, -3.385, 0.357, -2.732, -3.861, -3.148)
    p.curve_to_cubic_rel(-4.574, 1.307, -1.603, -0.238, -4.100, -0.713)
    p.curve_to_cubic_rel(-0.119, 3.922, -0.477, 2.021, -0.119, 3.922)
    p.curve_to_cubic_smooth_rel(-3.269, -4.932, 0.355, -4.397)
    p.curve_to_cubic_rel(-8.258, 5.585, -3.624, -0.534, -9.102, 4.323)
    p.curve_to_cubic_rel(4.396, 2.615, 0.792, 1.186, 4.520, 1.875)
    p.curve_to_cubic_rel(-5.347, 0.654, 0.000, 0.000, -0.951, -2.376)
    p.curve_to_cubic_rel(-2.497, 5.704, -4.397, 3.030, -2.497, 3.862)
    p.curve_to_cubic_smooth_rel(3.388, 2.198, 0.772, 3.327)
    p.curve_to_cubic_abs(63.938, 33.099, 61.267, 38.150, 63.938, 33.099)
    p.line_to_abs(63.938, 33.099)
    p.close_path()
    
    p.end()
    
    # path3784_1_
    p = Path()
    
    g.add(p)
    p.fill("#FDB813")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(69.262, 33.040)
    p.curve_to_cubic_rel(-5.976, -0.308, -2.429, 1.374, -5.104, 1.236)
    p.curve_to_cubic_rel(2.819, -5.278, -0.872, -1.542, 0.390, -3.906)
    p.curve_to_cubic_rel(5.975, 0.307, 2.428, -1.373, 5.102, -1.234)
    p.curve_to_cubic_abs(69.262, 33.040, 72.951, 29.304, 71.689, 31.668)
    p.close_path()
    
    p.end()
    
    # path3789_1_
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(53.131, 140.927)
    p.line_to_rel(1.548, -13.821)
    p.line_to_rel(32.730, 5.087)
    p.line_to_rel(1.438, 8.845)
    p.line_to_rel(-11.057, 1.106)
    p.line_to_rel(-1.549, -8.183)
    p.line_to_rel(-11.499, 0.553)
    p.line_to_rel(-0.885, 7.408)
    p.line_to_abs(53.131, 140.927)
    p.close_path()
    
    p.end()
    
    # path3791
    p = Path()
    
    g.add(p)
    p.fill("#A7B0B7")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(49.815, 155.745)
    p.curve_to_cubic_rel(0.332, -9.400, 0.000, 0.000, 0.111, -6.193)
    p.curve_to_cubic_rel(4.534, -6.854, 0.221, -3.206, 1.216, -6.302)
    p.curve_to_cubic_rel(11.057, 3.980, 3.316, -0.554, 10.834, 1.105)
    p.curve_to_cubic_rel(0.221, 13.490, 0.221, 2.874, 0.111, 10.946)
    p.curve_to_cubic_rel(-0.773, 6.966, 0.110, 2.543, 0.000, 5.418)
    p.curve_to_cubic_rel(-17.582, 0.553, -0.773, 1.547, -17.582, 0.553)
    p.line_to_abs(49.815, 155.745)
    p.close_path()
    
    p.end()
    
    # path3794
    p = Path()
    
    g.add(p)
    p.fill("#A7B0B7")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(56.228, 151.100)
    p.curve_to_cubic_rel(-11.167, -0.995, 0.000, 0.000, -7.335, -2.592)
    p.curve_to_cubic_rel(-5.970, 9.177, -3.981, 1.659, -6.082, 4.865)
    p.curve_to_cubic_rel(0.109, 6.083, 0.109, 4.313, 0.109, 6.083)
    p.line_to_rel(20.015, -1.217)
    
    p.end()
    
    # path3796
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(46.718, 152.095)
    p.curve_to_cubic_rel(9.732, 3.096, 0.000, 0.000, 6.856, -1.328)
    p.curve_to_cubic_rel(0.994, 6.304, 2.874, 4.424, 0.994, 6.304)
    
    p.end()
    
    # path3798
    p = Path()
    
    g.add(p)
    p.fill("#94A1AA")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(51.031, 162.821)
    p.curve_to_cubic_rel(16.144, 2.433, 5.442, 0.048, 17.186, -0.844)
    p.curve_to_cubic_rel(-22.778, 1.769, -0.860, 2.703, -13.883, 1.728)
    p.curve_to_cubic_rel(-7.519, -2.320, -2.622, 0.012, -7.484, 0.302)
    p.curve_to_cubic_abs(51.031, 162.821, 36.833, 161.394, 46.271, 162.779)
    p.close_path()
    
    p.end()
    
    # path3800
    p = Path()
    
    g.add(p)
    p.fill("#F04A3E")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(64.521, 151.875)
    p.curve_to_cubic_rel(-1.768, 4.201, 0.000, 2.320, -0.792, 4.201)
    p.curve_to_cubic_rel(-1.769, -4.201, -0.977, 0.000, -1.769, -1.881)
    p.curve_to_cubic_rel(1.769, -4.202, 0.000, -2.321, 0.792, -4.202)
    p.curve_to_cubic_abs(64.521, 151.875, 63.729, 147.672, 64.521, 149.553)
    p.close_path()
    
    p.end()
    
    # path3802
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(57.555, 163.706)
    p.curve_to_cubic_rel(0.553, 1.216, 0.000, 0.000, 0.664, 0.774)
    p.curve_to_cubic_rel(-0.332, 1.328, -0.110, 0.444, -0.332, 1.328)
    
    p.end()
    
    # path3831
    p = Path()
    
    g.add(p)
    p.fill("#A7B0B7")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(92.229, 155.745)
    p.curve_to_cubic_rel(-0.332, -9.400, 0.000, 0.000, -0.109, -6.193)
    p.curve_to_cubic_rel(-4.533, -6.854, -0.221, -3.206, -1.217, -6.302)
    p.curve_to_cubic_rel(-11.057, 3.980, -3.317, -0.554, -10.837, 1.105)
    p.curve_to_cubic_rel(-0.223, 13.490, -0.223, 2.874, -0.111, 10.946)
    p.curve_to_cubic_rel(0.775, 6.966, -0.109, 2.543, 0.000, 5.418)
    p.curve_to_cubic_rel(17.580, 0.553, 0.773, 1.547, 17.580, 0.553)
    p.line_to_abs(92.229, 155.745)
    p.close_path()
    
    p.end()
    
    # path3833_1_
    p = Path()
    
    g.add(p)
    p.fill("#A7B0B7")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(85.815, 151.100)
    p.curve_to_cubic_rel(11.168, -0.995, 0.000, 0.000, 7.337, -2.592)
    p.curve_to_cubic_rel(5.971, 9.177, 3.980, 1.659, 6.082, 4.865)
    p.curve_to_cubic_rel(-0.109, 6.083, -0.109, 4.313, -0.109, 6.083)
    p.line_to_rel(-20.015, -1.217)
    
    p.end()
    
    # path3835_1_
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(95.325, 152.095)
    p.curve_to_cubic_rel(-9.730, 3.096, 0.000, 0.000, -6.854, -1.328)
    p.curve_to_cubic_rel(-0.996, 6.304, -2.874, 4.424, -0.996, 6.304)
    
    p.end()
    
    # path3837_1_
    p = Path()
    
    g.add(p)
    p.fill("#94A1AA")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(91.013, 162.821)
    p.curve_to_cubic_rel(-16.144, 2.433, -5.441, 0.048, -17.185, -0.844)
    p.curve_to_cubic_rel(22.778, 1.769, 0.860, 2.703, 13.883, 1.728)
    p.curve_to_cubic_rel(7.520, -2.320, 2.623, 0.013, 7.484, 0.302)
    p.curve_to_cubic_abs(91.013, 162.821, 105.210, 161.394, 95.772, 162.779)
    p.close_path()
    
    p.end()
    
    # path3839_1_
    p = Path()
    
    g.add(p)
    p.fill("#F04A3E")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(77.524, 151.875)
    p.curve_to_cubic_rel(1.768, 4.201, 0.000, 2.320, 0.791, 4.201)
    p.curve_to_cubic_rel(1.770, -4.201, 0.978, 0.000, 1.770, -1.881)
    p.curve_to_cubic_rel(-1.770, -4.202, 0.000, -2.321, -0.792, -4.202)
    p.curve_to_cubic_abs(77.524, 151.875, 78.315, 147.672, 77.524, 149.553)
    p.close_path()
    
    p.end()
    
    # path3841_1_
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(84.490, 163.706)
    p.curve_to_cubic_rel(-0.554, 1.216, 0.000, 0.000, -0.665, 0.774)
    p.curve_to_cubic_rel(0.332, 1.328, 0.110, 0.444, 0.332, 1.328)
    
    p.end()
    
    # path3765
    p = Path()
    
    g.add(p)
    p.fill("#DAA476")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(52.934, 123.346)
    p.curve_to_cubic_rel(-5.419, -3.561, 0.000, 0.000, -4.644, -1.394)
    p.curve_to_cubic_rel(-0.929, -3.405, -0.773, -2.168, -0.929, -3.405)
    p.curve_to_cubic_smooth_rel(-4.953, -0.155, -3.095, 1.084)
    p.curve_to_cubic_rel(-5.263, -11.610, -1.858, -1.238, -5.107, -4.644)
    p.curve_to_cubic_smooth_rel(6.037, -18.420, 3.406, -17.183)
    p.curve_to_cubic_rel(6.501, -1.240, 2.632, -1.240, 6.501, -1.240)
    p.curve_to_cubic_smooth_rel(-0.309, -2.321, -1.394, -1.858)
    p.curve_to_cubic_rel(5.727, -0.464, 1.083, -0.464, 4.334, -1.239)
    p.curve_to_cubic_rel(17.338, 7.430, 1.393, 0.774, 17.338, 7.430)
    p.curve_to_cubic_smooth_rel(3.096, -5.418, 3.096, -3.869)
    p.curve_to_cubic_rel(-0.929, -15.945, 0.000, -1.548, -0.929, -15.945)
    p.line_to_rel(-2.322, -8.979)
    p.curve_to_cubic_rel(3.251, -5.108, 0.000, 0.000, 2.477, -3.560)
    p.curve_to_cubic_rel(0.709, -4.645, 0.773, -1.548, 0.914, -3.106)
    p.curve_to_cubic_rel(1.539, -5.235, -0.205, -1.540, 0.205, -5.235)
    p.curve_to_cubic_rel(3.285, 1.231, 1.336, 0.000, 2.566, 0.205)
    p.curve_to_cubic_rel(0.205, 2.977, 0.719, 1.027, 0.616, 2.464)
    p.curve_to_cubic_rel(-1.026, 2.566, -0.410, 0.513, -1.026, 2.566)
    p.curve_to_cubic_smooth_rel(7.700, 1.129, 4.724, -0.308)
    p.curve_to_cubic_rel(7.596, 4.722, 2.977, 1.437, 7.596, 4.722)
    p.curve_to_cubic_smooth_rel(4.207, -3.181, 2.873, -3.181)
    p.curve_to_cubic_rel(2.156, 3.181, 1.336, 0.000, 3.489, 1.231)
    p.curve_to_cubic_rel(-5.748, 2.565, -1.334, 1.950, -5.748, 2.565)
    p.line_to_rel(-1.643, 9.546)
    p.line_to_abs(82.655, 82.351)
    p.curve_to_cubic_rel(-0.513, 4.106, 0.000, 0.000, -0.513, 2.566)
    p.curve_to_cubic_rel(-0.103, 3.285, 0.000, 1.539, -0.103, 3.285)
    p.line_to_abs(52.934, 123.346)
    p.close_path()
    
    p.end()
    
    # path3769
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(46.688, 116.574)
    p.curve_to_cubic_rel(-0.069, -6.717, 0.000, 0.000, 0.475, -5.021)
    p.curve_to_cubic_rel(-2.781, -3.123, -0.542, -1.697, -1.990, -2.684)
    p.curve_to_cubic_rel(-2.918, 0.611, -1.222, -0.678, -2.580, 0.340)
    
    p.end()
    
    # path3771
    p = Path()
    
    g.add(p)
    p.fill("#FFFBCC")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(94.191, 67.917)
    p.curve_to_cubic_rel(-8.957, -0.067, 0.000, 0.000, -4.750, 1.425)
    p.curve_to_cubic_rel(-8.755, -5.293, -4.208, -1.493, -7.330, -3.598)
    p.curve_to_cubic_rel(-8.686, -4.412, -1.427, -1.697, -3.936, -5.973)
    p.curve_to_cubic_smooth_rel(-4.479, 6.921, -4.547, 5.972)
    p.curve_to_cubic_smooth_rel(4.886, 9.366, 2.104, 5.769)
    p.curve_to_cubic_rel(10.315, 8.889, 2.784, 3.597, 6.448, 8.823)
    p.curve_to_cubic_rel(11.471, -2.307, 3.869, 0.068, 10.181, -1.695)
    p.curve_to_cubic_rel(7.668, -5.293, 1.289, -0.611, 6.900, -3.554)
    p.curve_to_cubic_rel(-1.492, -6.041, 1.020, -2.308, -0.610, -5.293)
    p.curve_to_cubic_abs(94.191, 67.917, 95.276, 68.934, 94.191, 67.917)
    p.line_to_abs(94.191, 67.917)
    p.close_path()
    
    p.end()
    
    # path3793
    p = Path()
    
    g.add(p)
    p.fill("#753337")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(70.643, 64.591)
    p.curve_to_cubic_rel(2.919, 12.283, 0.000, 0.000, 0.543, 9.366)
    p.curve_to_cubic_rel(8.685, 4.546, 2.375, 2.918, 5.021, 5.293)
    p.curve_to_cubic_rel(8.213, -4.478, 3.664, -0.746, 5.702, -2.171)
    p.curve_to_cubic_rel(2.646, -3.529, 2.510, -2.307, 2.646, -3.529)
    p.curve_to_cubic_smooth_rel(-10.451, -0.407, -6.312, 1.290)
    p.curve_to_cubic_smooth_rel(-8.211, -4.411, -7.058, -2.986)
    p.curve_to_cubic_rel(-3.326, -4.208, -1.153, -1.425, -3.326, -4.208)
    p.line_to_abs(70.643, 64.591)
    p.close_path()
    
    p.end()
    
    # path3797
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(68.540, 64.591)
    p.curve_to_cubic_rel(2.510, -0.204, 0.000, 0.000, 1.627, 0.272)
    p.curve_to_cubic_rel(1.628, -1.018, 0.882, -0.475, 1.628, -1.018)
    
    p.end()
    
    # path3799
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(91.952, 71.174)
    p.curve_to_cubic_rel(0.949, 2.239, 0.000, 0.000, 0.068, 1.154)
    p.curve_to_cubic_rel(1.223, 1.494, 0.883, 1.086, 1.223, 1.494)
    
    p.end()
    
    # path3801
    p = Path()
    
    g.add(p)
    p.fill("#F7ABAD")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(81.704, 66.084)
    p.curve_to_cubic_rel(0.815, 2.986, -0.189, 0.586, -0.338, 1.425)
    p.curve_to_cubic_rel(3.868, 1.968, 1.153, 1.560, 1.968, 2.715)
    p.curve_to_cubic_smooth_rel(2.986, -2.579, 4.003, -2.104)
    p.curve_to_cubic_rel(-1.710, -0.992, -0.396, -0.185, -0.988, -0.648)
    p.curve_to_cubic_rel(-3.109, -1.112, -1.135, -0.542, -2.486, -0.988)
    p.curve_to_cubic_abs(81.704, 66.084, 83.538, 66.152, 82.116, 65.829)
    p.line_to_abs(81.704, 66.084)
    p.close_path()
    
    p.end()
    
    # path3803
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(93.091, 62.696)
    p.curve_to_cubic_rel(-4.255, -4.229, 0.000, -2.335, -1.905, -4.229)
    p.curve_to_cubic_rel(-4.252, 4.229, -2.349, 0.000, -4.252, 1.894)
    p.curve_to_cubic_rel(4.252, 4.230, 0.000, 2.336, 1.903, 4.230)
    p.curve_to_cubic_abs(93.091, 62.696, 91.186, 66.926, 93.091, 65.031)
    p.close_path()
    
    p.end()
    
    # path3807
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(89.712, 62.497)
    p.curve_to_cubic_rel(-1.222, -1.222, 0.000, -0.675, -0.546, -1.222)
    p.curve_to_cubic_rel(-1.221, 1.222, -0.674, 0.000, -1.221, 0.547)
    p.curve_to_cubic_rel(1.221, 1.221, 0.000, 0.674, 0.547, 1.221)
    p.curve_to_cubic_abs(89.712, 62.497, 89.166, 63.718, 89.712, 63.171)
    p.close_path()
    
    p.end()
    
    # path3832
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(86.185, 60.520)
    p.curve_to_cubic_rel(-4.276, 4.276, 0.000, 2.362, -1.916, 4.276)
    p.curve_to_cubic_rel(-4.274, -4.276, -2.361, 0.000, -4.274, -1.914)
    p.curve_to_cubic_rel(4.274, -4.275, 0.000, -2.361, 1.913, -4.275)
    p.curve_to_cubic_abs(86.185, 60.520, 84.269, 56.244, 86.185, 58.158)
    p.close_path()
    
    p.end()
    
    # path3834
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(82.865, 60.486)
    p.curve_to_cubic_rel(-1.228, 1.194, 0.000, 0.660, -0.550, 1.194)
    p.curve_to_cubic_rel(-1.229, -1.194, -0.680, 0.000, -1.229, -0.534)
    p.curve_to_cubic_smooth_rel(1.229, -1.194, 0.549, -1.194)
    p.curve_to_cubic_abs(82.865, 60.486, 82.315, 59.292, 82.865, 59.826)
    p.close_path()
    
    p.end()
    
    # path3836
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(80.958, 54.343)
    p.line_to_vertical_rel(1.764)
    
    p.end()
    
    # path3838
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(84.012, 54.547)
    p.line_to_rel(-0.747, 1.697)
    
    p.end()
    
    # path3840
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(86.252, 56.108)
    p.line_to_rel(-1.222, 1.019)
    
    p.end()
    
    # path3842
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(88.830, 56.720)
    p.line_to_rel(-0.067, 1.832)
    
    p.end()
    
    # path3844
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(91.343, 57.127)
    p.line_to_rel(-0.680, 1.696)
    
    p.end()
    
    # path3846
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(93.311, 58.688)
    p.line_to_rel(-1.154, 1.289)
    
    p.end()
    
    # path3850
    p = Path()
    
    g.add(p)
    p.fill("#FFA8AC")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(72.480, 74.577)
    p.curve_to_cubic_rel(7.710, 1.030, 0.000, 0.000, 4.259, -0.404)
    p.curve_to_cubic_rel(5.557, 2.644, 3.450, 1.434, 5.019, 2.152)
    p.curve_to_cubic_rel(1.255, 1.300, 0.538, 0.493, 1.255, 1.300)
    p.curve_to_cubic_smooth_rel(-7.529, 1.881, -3.809, 2.510)
    p.curve_to_cubic_rel(-6.632, -5.647, -3.719, -0.627, -6.274, -5.199)
    p.curve_to_cubic_abs(72.480, 74.577, 72.480, 75.339, 72.480, 74.577)
    p.line_to_abs(72.480, 74.577)
    p.close_path()
    
    p.end()
    
    # path3852
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(79.294, 71.574)
    p.curve_to_cubic_rel(-1.301, 3.047, 0.000, 0.000, -0.717, 1.522)
    p.curve_to_cubic_rel(-1.433, 2.645, -0.582, 1.523, -1.433, 2.645)
    p.curve_to_cubic_smooth_rel(4.034, 1.389, 2.599, 1.030)
    p.curve_to_cubic_rel(2.912, 0.717, 1.432, 0.358, 2.912, 0.717)
    p.curve_to_cubic_smooth_rel(1.838, -3.407, 1.434, -2.555)
    p.curve_to_cubic_rel(0.717, -2.151, 0.402, -0.852, 0.717, -2.151)
    p.curve_to_cubic_smooth_rel(-3.855, -0.986, -1.837, -0.269)
    p.curve_to_cubic_abs(79.294, 71.574, 80.190, 72.111, 79.294, 71.574)
    p.line_to_abs(79.294, 71.574)
    p.close_path()
    
    p.end()
    
    # path3854
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(82.654, 72.829)
    p.curve_to_cubic_rel(-0.761, 1.927, 0.000, 0.000, -0.536, 1.478)
    p.curve_to_cubic_rel(-0.988, 1.703, -0.226, 0.448, -0.988, 1.703)
    
    p.end()
    
    # path3856
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(77.904, 46.162)
    p.curve_to_cubic_rel(0.226, 1.927, 0.000, 0.000, 0.448, 1.256)
    p.curve_to_cubic_rel(-0.629, 1.345, -0.226, 0.672, -0.629, 1.345)
    
    p.end()
    
    # path3858
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(96.146, 58.308)
    p.curve_to_cubic_rel(1.299, -0.763, 0.000, 0.000, 0.716, -0.404)
    p.curve_to_cubic_rel(1.031, -0.627, 0.582, -0.358, 1.031, -0.627)
    
    p.end()
    
    # path3821_1_
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(95.433, 89.328)
    p.curve_to_cubic_rel(13.267, 5.842, 0.000, 0.000, 6.832, -1.387)
    p.curve_to_cubic_rel(2.178, 17.920, 6.437, 7.228, 4.950, 13.465)
    p.curve_to_cubic_rel(-8.218, 7.823, -2.771, 4.457, -6.138, 7.129)
    p.curve_to_cubic_rel(-3.367, 0.692, -2.079, 0.692, -3.367, 0.692)
    p.curve_to_cubic_smooth_rel(0.893, 2.180, 0.992, 1.287)
    p.curve_to_cubic_rel(-0.693, 2.375, -0.100, 0.890, -0.693, 2.375)
    p.line_to_rel(0.594, -1.980)
    p.line_to_rel(1.881, 0.693)
    p.line_to_rel(-1.881, -0.693)
    p.curve_to_cubic_rel(-0.494, -2.078, 0.000, 0.000, -0.197, -1.584)
    p.curve_to_cubic_rel(3.365, -1.089, -0.299, -0.496, 2.178, -0.496)
    p.curve_to_cubic_rel(1.584, -1.188, 1.188, -0.595, 1.584, -1.188)
    p.curve_to_cubic_smooth_rel(-0.594, 7.328, 0.891, 5.545)
    p.curve_to_cubic_rel(-8.615, 3.068, -1.486, 1.781, -5.545, 4.355)
    p.curve_to_cubic_rel(-6.336, -5.545, -3.068, -1.287, -6.336, -5.545)
    p.line_to_rel(5.247, -12.971)
    p.curve_to_cubic_rel(6.731, -5.742, 0.000, 0.000, 6.833, -3.762)
    p.curve_to_cubic_rel(-2.871, -3.365, -0.098, -1.980, 0.102, -2.971)
    p.curve_to_cubic_rel(-1.979, -0.100, -2.970, -0.396, -1.979, -0.100)
    p.line_to_abs(95.433, 89.328)
    p.close_path()
    
    p.end()
    
    # path3823
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(100.284, 121.506)
    p.curve_to_cubic_rel(-1.387, -7.427, 0.000, 0.000, 0.990, -5.446)
    p.curve_to_cubic_rel(-3.961, -2.376, -2.377, -1.979, -3.961, -2.376)
    
    p.end()
    
    # path3827
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(108.028, 115.962)
    p.curve_to_cubic_rel(-2.734, -5.811, 0.000, 0.000, -0.113, -3.646)
    p.curve_to_cubic_rel(-5.186, -1.824, -2.621, -2.164, -5.186, -1.824)
    
    p.end()
    
    # path3845
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(101.591, 105.023)
    p.curve_to_cubic_rel(5.811, -1.537, 0.000, 0.000, 2.277, -2.107)
    p.curve_to_cubic_rel(4.956, 2.961, 3.533, 0.569, 4.956, 2.961)
    
    p.end()
    
    # path3857
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(100.108, 102.518)
    p.curve_to_cubic_rel(2.279, -4.501, 0.000, 0.000, 0.172, -2.280)
    p.curve_to_cubic_rel(5.812, -2.279, 2.107, -2.223, 5.812, -2.279)
    
    p.end()
    
    # path3804
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(56.925, 83.801)
    p.curve_to_cubic_rel(-2.472, 17.591, 0.000, 0.000, -3.199, 13.956)
    p.curve_to_cubic_rel(-2.180, 15.554, 0.728, 3.633, -1.599, 12.064)
    p.curve_to_cubic_rel(0.435, 11.193, -0.583, 3.489, -2.182, 7.123)
    p.curve_to_cubic_rel(19.189, 9.159, 2.616, 4.070, 13.229, 9.159)
    p.curve_to_cubic_smooth_rel(19.333, -8.577, 18.463, -1.018)
    p.curve_to_cubic_rel(6.544, -28.784, 0.873, -7.559, 6.398, -22.677)
    p.curve_to_cubic_rel(0.727, -11.193, 0.145, -6.105, 0.727, -11.193)
    p.line_to_rel(-13.520, 2.035)
    p.line_to_rel(-13.374, -1.018)
    p.curve_to_cubic_abs(56.925, 83.801, 66.756, 87.662, 61.859, 85.688)
    p.line_to_abs(56.925, 83.801)
    p.close_path()
    
    p.end()
    
    # path3806
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(57.651, 79.731)
    p.line_to_rel(-1.309, 4.942)
    p.curve_to_cubic_rel(27.039, 8.432, 0.000, 0.000, 13.084, 8.723)
    p.curve_to_cubic_smooth_rel(16.281, -2.908, 16.281, -2.908)
    p.line_to_rel(0.291, -4.215)
    p.curve_to_cubic_rel(-18.316, 2.616, 0.000, 0.000, -5.669, 3.635)
    p.curve_to_cubic_abs(57.651, 79.731, 68.991, 87.581, 57.651, 79.731)
    p.line_to_abs(57.651, 79.731)
    p.close_path()
    
    p.end()
    
    # path3808
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(80.765, 102.119)
    p.curve_to_cubic_rel(0.873, 4.506, 0.000, 0.000, 2.328, 2.035)
    p.curve_to_cubic_rel(-0.873, 6.105, -1.454, 2.471, -1.454, 3.488)
    p.curve_to_cubic_rel(-1.889, 5.379, 0.582, 2.617, -1.018, 4.070)
    p.curve_to_cubic_rel(0.000, 5.525, -0.873, 1.309, -0.582, 3.779)
    p.curve_to_cubic_rel(-1.019, 4.796, 0.580, 1.744, 0.436, 2.906)
    
    p.end()
    
    # path3810
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(82.363, 94.995)
    p.curve_to_cubic_rel(-3.052, 4.798, 0.000, 0.000, -1.745, 2.325)
    p.curve_to_cubic_rel(-1.600, 3.053, -1.309, 2.471, -1.600, 3.053)
    p.curve_to_cubic_smooth_rel(3.779, 0.580, 2.617, 0.580)
    p.curve_to_cubic_rel(3.199, -0.727, 1.163, 0.000, 3.199, -0.727)
    p.line_to_rel(-1.746, -6.979)
    p.line_to_abs(82.363, 94.995)
    p.close_path()
    
    p.end()
    
    # path3812
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(84.108, 94.895)
    p.curve_to_cubic_rel(-1.691, 1.698, 0.000, 0.937, -0.757, 1.698)
    p.curve_to_cubic_rel(-1.691, -1.698, -0.934, 0.000, -1.691, -0.762)
    p.curve_to_cubic_rel(1.691, -1.699, 0.000, -0.938, 0.759, -1.699)
    p.curve_to_cubic_abs(84.108, 94.895, 83.352, 93.197, 84.108, 93.957)
    p.close_path()
    
    p.end()
    
    # path3814_1_
    p = Path()
    
    g.add(p)
    p.fill("#FFEB95")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(97.468, 97.209)
    p.curve_to_cubic_rel(-6.374, 1.706, 0.000, 0.000, -3.502, 1.706)
    p.curve_to_cubic_smooth_rel(-3.590, 0.000, -3.590, 0.000)
    p.curve_to_cubic_smooth_rel(0.089, 6.912, 0.269, 5.926)
    p.curve_to_cubic_rel(-0.538, 5.746, -0.180, 0.988, -0.538, 5.746)
    p.curve_to_cubic_smooth_rel(5.296, -0.180, 3.412, 0.359)
    p.curve_to_cubic_rel(3.143, -1.258, 1.887, -0.539, 3.143, -1.258)
    p.curve_to_cubic_smooth_rel(1.617, -7.182, 1.346, -4.757)
    p.curve_to_cubic_abs(97.468, 97.209, 97.378, 100.531, 97.468, 97.209)
    p.close_path()
    
    p.end()
    
    # path3816_1_
    p = Path()
    
    g.add(p)
    p.fill("#FFB917")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(90.735, 103.943)
    p.curve_to_cubic_rel(0.987, 3.682, 0.000, 0.000, 0.000, 2.783)
    p.curve_to_cubic_rel(2.065, 0.537, 0.987, 0.896, 1.078, 1.256)
    p.curve_to_cubic_rel(1.436, -2.873, 0.987, -0.718, 1.527, -1.705)
    p.curve_to_cubic_rel(-0.270, -1.885, -0.090, -1.167, -0.270, -1.885)
    p.line_to_abs(90.735, 103.943)
    p.close_path()
    
    p.end()
    
    # path3818
    p = Path()
    
    g.add(p)
    p.fill("#DCAC7E")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(92.979, 103.978)
    p.curve_to_cubic_rel(2.783, -0.663, 2.227, -0.066, 3.148, 0.844)
    p.curve_to_cubic_rel(-1.615, -0.809, -0.270, -1.112, -1.615, -0.809)
    p.curve_to_cubic_smooth_rel(-0.629, -1.885, 0.270, -1.885)
    p.curve_to_cubic_rel(-0.897, 1.885, -1.347, 0.000, -0.897, 1.885)
    p.curve_to_cubic_smooth_rel(-2.603, 1.130, -1.777, 0.024)
    p.curve_to_cubic_abs(92.979, 103.978, 90.284, 105.269, 91.657, 104.092)
    p.line_to_abs(92.979, 103.978)
    p.close_path()
    
    p.end()
    
    # path3820
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(60.892, 83.848)
    p.curve_to_cubic_rel(-0.207, 0.879, 0.000, 0.000, -0.568, 0.311)
    p.curve_to_cubic_rel(1.189, -0.052, 0.362, 0.569, 1.189, -0.052)
    
    p.end()
    
    # path3826
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(69.111, 87.931)
    p.curve_to_cubic_rel(0.568, 0.982, 0.000, 0.000, -0.051, 0.982)
    p.curve_to_cubic_rel(0.568, -1.033, 0.620, 0.000, 0.568, -1.033)
    
    p.end()
    
    # path3828
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(80.224, 90.051)
    p.curve_to_cubic_rel(0.777, 0.880, 0.000, 0.000, -0.049, 0.880)
    p.curve_to_cubic_smooth_rel(0.414, -1.293, 0.414, -1.293)
    
    p.end()
    
    # path3830
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(89.479, 90.310)
    p.curve_to_cubic_rel(0.465, 0.827, 0.000, 0.000, -0.259, 0.827)
    p.curve_to_cubic_rel(0.518, -1.138, 0.723, 0.000, 0.518, -1.138)
    
    p.end()
    
    # path3843
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(95.734, 88.863)
    p.curve_to_cubic_rel(0.257, 1.034, 0.000, 0.000, -0.207, 1.034)
    p.curve_to_cubic_rel(0.777, -0.931, 0.467, 0.000, 0.777, -0.931)
    
    p.end()
    
    # path3847_1_
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(23.043, 95.318)
    p.curve_to_cubic_rel(15.565, -5.447, 0.000, 0.000, 10.117, -4.670)
    p.curve_to_cubic_rel(17.121, -3.269, 5.447, -0.778, 13.229, -3.269)
    p.curve_to_cubic_rel(8.093, 3.892, 3.891, 0.000, 8.249, 0.000)
    p.curve_to_cubic_rel(-5.759, 8.404, -0.155, 3.891, 0.622, 6.691)
    p.curve_to_cubic_rel(-18.364, 5.447, -6.380, 1.713, -16.186, 4.047)
    p.curve_to_cubic_rel(-10.739, 3.892, -2.180, 1.401, -10.739, 3.892)
    p.line_to_abs(23.043, 95.318)
    p.close_path()
    
    p.end()
    
    # path3851
    p = Path()
    
    g.add(p)
    p.fill("#FFFFFF")
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(13.028, 113.855)
    p.curve_to_cubic_rel(-1.790, -8.234, 0.000, 0.000, -2.902, -3.178)
    p.curve_to_cubic_rel(5.729, -8.770, 0.438, -1.991, 5.907, -6.979)
    p.curve_to_cubic_rel(-2.424, -3.618, -0.180, -1.789, -1.631, -2.631)
    p.curve_to_cubic_rel(0.992, -6.942, -1.234, -1.534, -3.362, -3.702)
    p.curve_to_cubic_rel(4.833, 3.222, 1.323, -0.984, 4.654, 0.184)
    p.curve_to_cubic_rel(4.833, 4.476, 0.210, 3.606, 1.610, 4.296)
    p.curve_to_cubic_rel(7.517, 3.400, 3.222, 0.180, 6.085, 0.000)
    p.curve_to_cubic_rel(0.895, 9.307, 1.431, 3.400, 3.042, 6.980)
    p.curve_to_cubic_rel(-7.696, 6.444, -2.148, 2.328, -4.833, 2.864)
    p.curve_to_cubic_rel(-9.666, 3.580, -2.865, 3.580, -7.063, 4.618)
    p.curve_to_cubic_abs(13.028, 113.855, 14.517, 116.028, 13.028, 113.855)
    p.close_path()
    
    p.end()
    
    # path3853
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(20.546, 104.548)
    p.curve_to_cubic_rel(2.148, -4.654, 0.000, 0.000, 0.715, -3.580)
    p.curve_to_cubic_rel(4.295, -2.148, 1.432, -1.074, 4.295, -2.148)
    
    p.end()
    
    # path3855
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(40.715, 103.132)
    p.curve_to_cubic_rel(0.469, -6.336, 0.000, 0.000, 1.643, -2.347)
    p.curve_to_cubic_rel(-2.425, -4.931, -1.173, -3.992, -1.564, -4.147)
    p.curve_to_cubic_rel(-1.721, -1.174, -0.861, -0.782, -1.721, -1.174)
    
    p.end()
    
    # path3859_1_
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(44.940, 89.285)
    p.curve_to_cubic_rel(3.365, 4.146, 0.000, 0.000, 2.269, 0.390)
    p.curve_to_cubic_rel(-0.078, 7.434, 1.096, 3.756, -0.078, 7.434)
    
    p.end()
    
    # path3862
    p = Path()
    
    g.add(p)
    p.stroke_color("#231F20")
    p.stroke_width(0.5806)
    
    p.move_to_abs(52.139, 87.562)
    p.curve_to_cubic_rel(3.834, 4.617, 0.000, 0.000, 2.660, 1.018)
    p.curve_to_cubic_rel(-0.470, 6.729, 1.173, 3.599, -0.470, 6.729)
    
    p.end()
    #endregion drawing

# Gary the Snail
def pet(x, y, scale_x, scale_y, crown):
    g = PathGroup()

    width = 150.000 * scale_x
    height = 167.160 * scale_y

    g.translate(-width / 2.0, -height)
    g.scale(scale_x, scale_y)
    g.translate(x, y)

    #region drawing
    # path3772
    p = Path()
    
    g.add(p)
    p.fill("#F2B8D0")
    p.stroke_color("#000000")
    p.stroke_width(0.3343)
    
    p.move_to_abs(70.076, 161.131)
    p.line_to_rel(12.522, -3.594)
    p.line_to_rel(8.695, -2.783)
    p.curve_to_cubic_rel(-2.783, -4.521, 0.000, 0.000, -0.695, -2.781)
    p.curve_to_cubic_rel(-4.869, -2.203, -2.087, -1.740, -4.869, -2.203)
    p.curve_to_cubic_smooth_rel(3.478, -29.334, 4.638, -19.596)
    p.curve_to_cubic_rel(-22.609, -34.088, -1.159, -9.739, -5.913, -29.102)
    p.curve_to_cubic_rel(-33.507, 14.841, -16.696, -4.986, -31.421, 9.508)
    p.curve_to_cubic_rel(-4.639, 17.044, -2.087, 5.334, -4.639, 7.305)
    p.curve_to_cubic_rel(5.682, 23.305, 0.000, 9.740, 2.668, 17.045)
    p.curve_to_cubic_rel(8.696, 13.566, 3.015, 6.262, 8.696, 13.566)
    p.curve_to_cubic_smooth_rel(-0.696, 2.318, -1.043, 0.580)
    p.curve_to_cubic_rel(2.203, 2.319, 0.349, 1.740, 2.203, 2.319)
    p.curve_to_cubic_abs(70.076, 161.131, 43.441, 162.503, 64.085, 160.812)
    p.close_path()
    
    p.end()
    
    # path3776
    p = Path()
    
    g.add(p)
    p.fill("#E20005")
    
    p.move_to_abs(59.873, 160.318)
    p.curve_to_cubic_rel(4.290, -17.159, 0.000, 0.000, 5.682, -7.883)
    p.curve_to_cubic_rel(-6.262, -23.073, -1.392, -9.275, -3.015, -17.275)
    p.curve_to_cubic_rel(-12.753, -7.420, -3.246, -5.798, -8.695, -8.000)
    p.curve_to_cubic_rel(-7.421, 14.492, -4.059, 0.578, -8.349, 8.928)
    p.curve_to_cubic_rel(7.188, 13.566, 0.928, 5.565, 2.898, 12.174)
    p.curve_to_cubic_rel(4.290, -5.565, 4.290, 1.392, 5.217, -3.478)
    p.curve_to_cubic_rel(-2.666, -4.870, -0.928, -2.087, -2.666, -4.870)
    p.curve_to_cubic_smooth_rel(-2.667, 3.131, 0.000, 6.262)
    p.curve_to_cubic_rel(-1.739, -9.276, -2.666, -3.131, -1.971, -7.536)
    p.curve_to_cubic_rel(6.029, -3.362, 0.232, -1.739, 2.436, -6.028)
    p.curve_to_cubic_rel(6.841, 11.711, 3.594, 2.666, 5.102, 4.870)
    p.curve_to_cubic_rel(1.855, 17.625, 1.705, 6.706, 3.942, 10.667)
    p.curve_to_cubic_rel(-4.290, 7.768, -2.087, 6.955, -4.290, 7.768)
    p.line_to_abs(59.873, 160.318)
    p.close_path()
    
    p.end()
    
    # path3778
    p = Path()
    
    g.add(p)
    p.fill("#1F5AA6")
    
    p.move_to_abs(74.315, 121.178)
    p.curve_to_cubic_rel(-0.044, 5.003, 1.230, 1.987, 1.209, 4.227)
    p.curve_to_cubic_rel(-4.493, -2.199, -1.252, 0.772, -3.265, -0.210)
    p.curve_to_cubic_rel(0.044, -5.002, -1.229, -1.988, -1.209, -4.228)
    p.curve_to_cubic_abs(74.315, 121.178, 71.074, 118.204, 73.085, 119.189)
    p.close_path()
    
    p.end()
    
    # path3780
    p = Path()
    
    g.add(p)
    p.fill("#1F5AA6")
    
    p.move_to_abs(65.516, 104.059)
    p.curve_to_cubic_rel(-0.455, 5.576, 1.360, 2.104, 1.157, 4.602)
    p.curve_to_cubic_rel(-5.383, -2.043, -1.612, 0.976, -4.022, 0.061)
    p.curve_to_cubic_rel(0.455, -5.575, -1.361, -2.104, -1.157, -4.601)
    p.curve_to_cubic_abs(65.516, 104.059, 61.746, 101.040, 64.155, 101.955)
    p.close_path()
    
    p.end()
    
    # path3782
    p = Path()
    
    g.add(p)
    p.fill("#1F5AA6")
    
    p.move_to_abs(52.115, 92.519)
    p.curve_to_cubic_rel(-3.474, 4.571, 0.553, 1.739, -1.002, 3.785)
    p.curve_to_cubic_rel(-5.477, -1.727, -2.472, 0.785, -4.923, 0.013)
    p.curve_to_cubic_rel(3.475, -4.572, -0.553, -1.738, 1.003, -3.786)
    p.curve_to_cubic_abs(52.115, 92.519, 49.111, 90.006, 51.562, 90.779)
    p.close_path()
    
    p.end()
    
    # path3784
    p = Path()
    
    g.add(p)
    p.fill("#1F5AA6")
    
    p.move_to_abs(37.422, 109.008)
    p.curve_to_cubic_rel(-4.103, 1.650, -1.121, 1.678, -2.958, 2.416)
    p.curve_to_cubic_rel(-0.042, -4.421, -1.144, -0.766, -1.162, -2.744)
    p.curve_to_cubic_rel(4.103, -1.651, 1.121, -1.677, 2.958, -2.416)
    p.curve_to_cubic_abs(37.422, 109.008, 38.524, 105.352, 38.543, 107.331)
    p.close_path()
    
    p.end()
    
    # path3786
    p = Path()
    
    g.add(p)
    p.fill("#1F5AA6")
    
    p.move_to_abs(35.060, 119.796)
    p.curve_to_cubic_rel(-2.783, 3.652, 0.000, 2.018, -1.246, 3.652)
    p.curve_to_cubic_smooth_rel(-2.783, -3.652, -2.783, -1.635)
    p.curve_to_cubic_rel(2.783, -3.652, 0.000, -2.017, 1.246, -3.652)
    p.curve_to_cubic_abs(35.060, 119.796, 33.814, 116.145, 35.060, 117.779)
    p.close_path()
    
    p.end()
    
    # path3768_1_
    p = Path()
    
    g.add(p)
    p.fill("#7DCBB1")
    p.stroke_color("#000000")
    p.stroke_width(0.3343)
    
    p.move_to_abs(108.801, 105.709)
    p.curve_to_cubic_rel(1.392, 11.016, 0.000, 0.000, 1.544, 8.770)
    p.curve_to_cubic_rel(-0.927, 20.407, -0.170, 2.496, -0.694, 17.625)
    p.curve_to_cubic_rel(-1.740, 13.913, -0.234, 2.782, -1.393, 12.637)
    p.curve_to_cubic_rel(-1.393, 4.174, -0.349, 1.275, -1.393, 4.174)
    p.line_to_rel(7.072, 0.348)
    p.curve_to_cubic_rel(-0.695, -16.696, 0.000, 0.000, -1.971, -6.956)
    p.curve_to_cubic_rel(1.493, -18.340, 0.605, -4.622, 0.941, -11.932)
    p.curve_to_cubic_rel(1.406, -13.082, 0.610, -7.096, 1.406, -13.082)
    p.curve_to_cubic_abs(108.801, 105.709, 112.466, 105.552, 112.049, 105.459)
    p.line_to_abs(108.801, 105.709)
    p.close_path()
    
    p.end()
    
    # path3760
    p = Path()
    
    g.add(p)
    p.fill("#7DCBB1")
    
    p.move_to_abs(84.684, 106.753)
    p.curve_to_cubic_rel(8.928, 22.029, 0.000, 0.000, 7.536, 14.608)
    p.curve_to_cubic_rel(2.086, 15.651, 1.393, 7.421, 2.435, 12.638)
    p.curve_to_cubic_rel(-0.463, 10.090, -0.346, 3.016, -0.463, 10.090)
    p.line_to_rel(0.117, -1.623)
    p.curve_to_cubic_rel(-7.188, 0.579, 0.000, 0.000, -3.479, 1.275)
    p.curve_to_cubic_rel(-9.972, 2.552, -3.711, -0.696, -7.770, 0.231)
    p.curve_to_cubic_rel(-16.349, 2.203, -2.203, 2.319, -9.391, 3.594)
    p.curve_to_cubic_rel(-18.203, -1.043, -6.956, -1.393, -11.826, -2.088)
    p.curve_to_cubic_rel(-7.769, 1.969, -6.377, 1.043, -3.941, 2.201)
    p.curve_to_cubic_rel(-0.463, 3.828, -3.826, -0.231, -2.782, 3.828)
    p.curve_to_cubic_rel(5.564, 0.928, 2.319, 0.000, 4.637, -0.813)
    p.curve_to_cubic_rel(12.291, 1.971, 0.928, 1.739, 10.551, 0.231)
    p.curve_to_cubic_rel(10.667, 0.231, 1.739, 1.738, 8.928, 1.158)
    p.curve_to_cubic_rel(6.841, -0.231, 1.739, -0.931, 5.796, -1.044)
    p.curve_to_cubic_rel(6.840, 0.000, 1.043, 0.812, 5.681, 0.580)
    p.curve_to_cubic_rel(7.188, 0.231, 1.160, -0.580, 6.029, -0.580)
    p.curve_to_cubic_smooth_rel(9.509, -0.118, 7.653, 0.349)
    p.curve_to_cubic_rel(6.260, 0.118, 1.854, -0.463, 5.217, -0.230)
    p.curve_to_cubic_smooth_rel(8.697, -1.507, 7.420, -0.812)
    p.curve_to_cubic_rel(6.492, -0.233, 1.275, -0.695, 4.868, -0.813)
    p.curve_to_cubic_rel(5.217, -1.738, 1.623, 0.579, 4.174, -0.696)
    p.curve_to_cubic_rel(1.624, -2.435, 1.043, -1.044, 1.624, -2.435)
    p.curve_to_cubic_smooth_rel(-5.798, -1.276, -4.407, 0.463)
    p.curve_to_cubic_smooth_rel(-5.218, -4.405, -1.738, -3.593)
    p.curve_to_cubic_rel(-6.841, -0.348, -3.477, -0.813, -6.841, -0.348)
    p.curve_to_cubic_smooth_rel(-5.217, -14.031, -4.174, -8.117)
    p.curve_to_cubic_rel(-4.639, -22.145, -1.044, -5.912, -4.639, -20.174)
    p.curve_to_cubic_smooth_rel(-1.971, -14.609, -1.971, -14.609)
    p.line_to_abs(84.684, 106.753)
    p.close_path()
    
    p.end()
    
    # path3766_1_
    p = Path()
    
    g.add(p)
    p.fill("#CCE954")
    
    p.move_to_abs(38.885, 158.695)
    p.line_to_rel(-3.130, 0.582)
    p.line_to_rel(-2.436, 0.231)
    p.line_to_rel(-0.580, 1.854)
    p.line_to_rel(1.972, 1.738)
    p.line_to_rel(4.290, -0.463)
    p.line_to_rel(1.623, 1.043)
    p.line_to_rel(1.276, 1.043)
    p.line_to_rel(8.581, 0.350)
    p.line_to_rel(2.666, 1.158)
    p.line_to_rel(5.334, 0.928)
    p.line_to_rel(4.754, -0.695)
    p.line_to_rel(3.709, -1.043)
    p.line_to_horizontal_rel(2.435)
    p.line_to_rel(3.247, 1.158)
    p.line_to_rel(3.246, -0.348)
    p.line_to_rel(4.405, -0.927)
    p.line_to_rel(4.175, 0.579)
    p.line_to_rel(3.478, 0.813)
    p.line_to_rel(4.406, -0.465)
    p.line_to_rel(3.246, -0.348)
    p.line_to_rel(2.435, -0.229)
    p.line_to_rel(2.899, 0.693)
    p.line_to_rel(6.494, -1.161)
    p.line_to_rel(3.131, -0.926)
    p.line_to_rel(2.549, -0.348)
    p.line_to_rel(2.784, 0.580)
    p.line_to_rel(2.317, -0.231)
    p.line_to_rel(2.552, -1.274)
    p.line_to_rel(2.087, -2.898)
    p.line_to_rel(-4.173, -0.119)
    p.line_to_rel(-2.088, -1.390)
    p.curve_to_cubic_rel(-10.783, 2.665, 0.000, 0.000, -8.001, 3.710)
    p.curve_to_cubic_rel(-15.188, -1.158, -2.782, -1.043, -12.175, -2.551)
    p.curve_to_cubic_rel(-19.711, 1.971, -3.015, 1.391, -14.494, 3.826)
    p.curve_to_cubic_rel(-15.769, 0.000, -5.218, -1.855, -13.450, 0.812)
    p.curve_to_cubic_rel(-12.406, -1.160, -2.319, -0.813, -10.203, 0.349)
    p.curve_to_cubic_abs(38.885, 158.695, 40.509, 159.393, 38.885, 158.695)
    p.close_path()
    
    p.end()
    
    # path3764_1_
    p = Path()
    
    g.add(p)
    p.stroke_color("#000000")
    p.stroke_width(0.3343)
    
    p.move_to_abs(84.684, 106.753)
    p.curve_to_cubic_rel(8.928, 22.029, 0.000, 0.000, 7.536, 14.608)
    p.curve_to_cubic_rel(2.086, 15.651, 1.393, 7.421, 2.435, 12.638)
    p.curve_to_cubic_rel(-0.463, 10.090, -0.346, 3.016, -0.463, 10.090)
    p.line_to_abs(95.120, 152.900)
    p.curve_to_cubic_rel(-6.957, 0.579, 0.000, 0.000, -3.246, 1.275)
    p.curve_to_cubic_rel(-9.972, 2.552, -3.712, -0.696, -7.769, 0.231)
    p.curve_to_cubic_rel(-16.348, 2.203, -2.202, 2.319, -9.391, 3.594)
    p.curve_to_cubic_rel(-18.203, -1.043, -6.957, -1.393, -11.826, -2.088)
    p.curve_to_cubic_rel(-7.768, 1.969, -6.377, 1.043, -3.942, 2.201)
    p.curve_to_cubic_rel(-0.464, 3.828, -3.827, -0.231, -2.783, 3.828)
    p.curve_to_cubic_smooth_rel(5.565, 0.928, 4.637, -0.813)
    p.curve_to_cubic_rel(12.290, 1.971, 0.927, 1.739, 10.551, 0.231)
    p.curve_to_cubic_rel(10.667, 0.231, 1.739, 1.738, 8.928, 1.158)
    p.curve_to_cubic_rel(6.841, -0.231, 1.739, -0.931, 5.796, -1.044)
    p.curve_to_cubic_rel(6.841, 0.000, 1.043, 0.812, 5.681, 0.580)
    p.curve_to_cubic_rel(7.188, 0.231, 1.159, -0.580, 6.029, -0.580)
    p.curve_to_cubic_rel(9.508, -0.118, 1.160, 0.812, 7.652, 0.349)
    p.curve_to_cubic_rel(6.262, 0.118, 1.856, -0.463, 5.218, -0.230)
    p.curve_to_cubic_rel(8.695, -1.507, 1.043, 0.349, 7.420, -0.812)
    p.curve_to_cubic_smooth_rel(6.492, -0.233, 4.870, -0.813)
    p.curve_to_cubic_rel(5.219, -1.738, 1.624, 0.579, 4.175, -0.696)
    p.curve_to_cubic_rel(1.623, -2.435, 1.043, -1.044, 1.623, -2.435)
    p.curve_to_cubic_smooth_rel(-5.797, -1.276, -4.406, 0.463)
    p.curve_to_cubic_rel(-5.218, -4.405, -1.392, -1.739, -1.740, -3.593)
    p.curve_to_cubic_smooth_rel(-6.841, -0.348, -6.841, -0.348)
    p.curve_to_cubic_smooth_rel(-5.218, -14.031, -4.174, -8.117)
    p.curve_to_cubic_rel(-4.638, -22.145, -1.044, -5.912, -4.638, -20.174)
    p.curve_to_cubic_smooth_rel(-1.972, -14.609, -1.972, -14.609)
    p.line_to_abs(84.684, 106.753)
    p.close_path()
    
    p.end()
    
    # path3789
    p = Path()
    
    g.add(p)
    p.fill("#CCE954")
    p.stroke_color("#000000")
    p.stroke_width(0.3343)
    
    p.move_to_abs(98.481, 99.448)
    p.curve_to_cubic_rel(-11.129, 10.319, 0.000, 5.698, -4.982, 10.319)
    p.curve_to_cubic_rel(-11.131, -10.319, -6.148, 0.000, -11.131, -4.621)
    p.curve_to_cubic_rel(11.131, -10.319, 0.000, -5.699, 4.982, -10.319)
    p.curve_to_cubic_abs(98.481, 99.448, 93.499, 89.129, 98.481, 93.749)
    p.close_path()
    
    p.end()
    
    # path3813
    p = Path()
    
    g.add(p)
    p.fill("#CCE954")
    p.stroke_color("#000000")
    p.stroke_width(0.3343)
    
    p.move_to_abs(123.636, 98.725)
    p.curve_to_cubic_rel(-10.626, 9.909, 0.000, 5.472, -4.757, 9.909)
    p.curve_to_cubic_rel(-10.627, -9.909, -5.870, 0.000, -10.627, -4.437)
    p.curve_to_cubic_smooth_rel(10.627, -9.908, 4.757, -9.908)
    p.curve_to_cubic_abs(123.636, 98.725, 118.879, 88.816, 123.636, 93.252)
    p.close_path()
    
    p.end()
    
    # path3815
    p = Path()
    
    g.add(p)
    p.fill("#FE2606")
    
    p.move_to_abs(95.927, 97.336)
    p.curve_to_cubic_rel(-4.215, 4.662, 0.000, 2.574, -1.887, 4.662)
    p.curve_to_cubic_smooth_rel(-4.214, -4.662, -4.214, -2.088)
    p.curve_to_cubic_rel(4.214, -4.662, 0.000, -2.576, 1.886, -4.662)
    p.curve_to_cubic_smooth_abs(95.927, 97.336, 95.927, 94.760)
    p.close_path()
    
    p.end()
    
    # path3817
    p = Path()
    
    g.add(p)
    p.fill("#FE2606")
    
    p.move_to_abs(120.946, 96.215)
    p.curve_to_cubic_rel(-3.767, 4.349, 0.000, 2.401, -1.687, 4.349)
    p.curve_to_cubic_rel(-3.767, -4.349, -2.081, 0.000, -3.767, -1.946)
    p.curve_to_cubic_rel(3.767, -4.350, 0.000, -2.403, 1.686, -4.350)
    p.curve_to_cubic_abs(120.946, 96.215, 119.259, 91.865, 120.946, 93.813)
    p.close_path()
    
    p.end()
    
    # path3819_1_
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    
    p.move_to_abs(93.776, 97.201)
    p.curve_to_cubic_rel(-1.794, 1.927, 0.000, 1.064, -0.804, 1.927)
    p.curve_to_cubic_smooth_rel(-1.794, -1.927, -1.794, -0.862)
    p.curve_to_cubic_rel(1.794, -1.929, 0.000, -1.065, 0.803, -1.929)
    p.curve_to_cubic_abs(93.776, 97.201, 92.972, 95.273, 93.776, 96.137)
    p.close_path()
    
    p.end()
    
    # path3821
    p = Path()
    
    g.add(p)
    p.fill("#000000")
    
    p.move_to_abs(119.153, 96.215)
    p.curve_to_cubic_rel(-1.660, 1.568, 0.000, 0.865, -0.744, 1.568)
    p.curve_to_cubic_rel(-1.658, -1.568, -0.915, 0.000, -1.658, -0.702)
    p.curve_to_cubic_rel(1.658, -1.570, 0.000, -0.867, 0.743, -1.570)
    p.curve_to_cubic_abs(119.153, 96.215, 118.409, 94.645, 119.153, 95.348)
    p.close_path()
    
    p.end()
    #endregion drawing

def custom_background():
    g = PathGroup()

    width = 900.000
    height = 595.016

    scale_x = width / window_width
    scale_y = height / window_height

    width *= scale_x
    height *= scale_y

    g.scale(scale_x, scale_y)
    g.translate(-width / 2, height - grass_height)
    g.translate(-12.0, 50.0)
    g.scale(1.04)
    g.scale(1.0, -1.0)

    #region drawing
    p = Path()
    
    g.add(p)
    p.fill("#D09728")
    
    p.move_to_abs(899.900, 496.566)
    p.line_to_rel(-0.021, -0.006)
    p.curve_to_cubic_rel(-54.328, -16.322, -17.809, -6.387, -35.998, -11.662)
    p.curve_to_cubic_rel(-55.411, -12.225, -18.338, -4.646, -36.832, -8.666)
    p.curve_to_cubic_rel(-112.229, -16.744, -37.163, -7.098, -74.642, -12.469)
    p.curve_to_cubic_rel(-113.076, -9.631, -37.594, -4.264, -75.310, -7.395)
    p.curve_to_cubic_rel(-113.416, -4.033, -37.769, -2.232, -75.588, -3.561)
    p.curve_to_cubic_rel(-226.808, 7.063, -75.657, -0.938, -151.369, 1.186)
    p.curve_to_cubic_rel(-112.834, 12.072, -37.714, 2.961, -75.361, 6.871)
    p.curve_to_cubic_rel(-111.635, 20.250, -37.464, 5.223, -74.793, 11.617)
    p.line_to_rel(-0.097, 0.021)
    p.line_to_vertical_rel(0.102)
    p.line_to_abs(0.001, 594.729)
    p.line_to_vertical_rel(0.170)
    p.line_to_horizontal_rel(0.170)
    p.line_to_rel(449.849, 0.117)
    p.line_to_rel(449.853, -0.158)
    p.line_to_horizontal_abs(900.000)
    p.line_to_vertical_rel(-0.129)
    p.line_to_abs(899.900, 496.566)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#72AA8B")
    p.stroke_color("#3C5D6A")
    p.stroke_width(2.3835)
    
    p.move_to_abs(25.276, 473.615)
    p.curve_to_cubic_rel(33.815, 20.289, 3.747, 14.287, 25.936, 10.133)
    p.curve_to_cubic_rel(6.763, 31.563, 7.229, 5.543, -4.214, 29.762)
    p.curve_to_cubic_rel(0.000, -54.104, 6.616, -15.682, -0.992, -36.547)
    p.curve_to_cubic_rel(18.035, -24.799, 4.680, -9.598, 17.101, -11.455)
    p.curve_to_cubic_rel(-22.543, 15.779, -12.924, -0.148, -16.063, 9.486)
    p.curve_to_cubic_rel(4.508, -51.852, -16.094, -17.801, -2.932, -34.545)
    p.curve_to_cubic_rel(-20.289, 15.781, -14.197, -2.174, -13.952, 10.098)
    p.curve_to_cubic_rel(6.763, -45.088, -16.983, -16.852, 7.860, -32.719)
    p.curve_to_cubic_rel(-20.290, 18.035, -10.920, 1.854, -12.580, 12.969)
    p.curve_to_cubic_rel(9.018, -40.578, -8.581, -18.971, 6.943, -25.609)
    p.curve_to_cubic_rel(-15.779, 13.525, -10.364, -0.598, -9.521, 10.020)
    p.curve_to_cubic_rel(15.779, -38.324, -4.591, -22.625, 17.667, -18.403)
    p.curve_to_cubic_rel(-15.779, 13.527, -10.167, -0.396, -10.783, 8.756)
    p.curve_to_cubic_rel(4.509, -33.816, -1.952, -14.729, 2.862, -22.688)
    p.curve_to_cubic_rel(-13.526, 40.578, -16.771, 1.268, -11.639, 24.432)
    p.curve_to_cubic_rel(-13.525, -11.271, -6.590, -1.676, -4.362, -12.170)
    p.curve_to_cubic_rel(15.779, 38.322, -4.891, 14.433, 18.760, 18.431)
    p.curve_to_cubic_rel(-15.779, -9.017, -6.545, -1.720, -5.849, -10.685)
    p.curve_to_cubic_rel(29.306, 47.340, 5.537, 20.012, 24.313, 26.785)
    p.curve_to_cubic_rel(-18.034, -6.764, -6.346, -1.920, -9.250, -7.283)
    p.curve_to_cubic_rel(33.815, 40.578, 6.479, 16.834, 41.700, 16.889)
    p.curve_to_cubic_rel(-29.307, -11.271, -8.323, -5.203, -15.088, -11.964)
    p.curve_to_cubic_rel(38.323, 42.834, 8.252, 17.314, 44.106, 18.996)
    p.curve_to_cubic_abs(25.276, 473.615, 47.549, 480.830, 34.992, 469.941)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#72AA8B")
    p.stroke_color("#3C5D6A")
    p.stroke_width(2.3835)
    
    p.move_to_abs(828.907, 468.852)
    p.curve_to_cubic_rel(38.323, -42.832, -5.783, -23.838, 30.071, -25.520)
    p.curve_to_cubic_rel(-29.310, 11.271, -14.221, -0.689, -20.983, 6.068)
    p.curve_to_cubic_rel(33.815, -40.578, -7.885, -23.689, 27.336, -23.744)
    p.curve_to_cubic_rel(-18.036, 6.764, -8.786, -0.521, -11.688, 4.844)
    p.curve_to_cubic_rel(29.308, -47.340, 4.993, -20.555, 23.771, -27.328)
    p.curve_to_cubic_rel(-15.777, 9.016, -9.933, -1.668, -9.232, 7.297)
    p.curve_to_cubic_rel(15.777, -38.322, -2.979, -19.895, 20.670, -23.891)
    p.curve_to_cubic_rel(-13.523, 11.271, -9.163, -0.896, -6.938, 9.598)
    p.curve_to_cubic_rel(-13.524, -40.579, -1.889, -16.146, 3.244, -39.313)
    p.curve_to_cubic_rel(4.508, 33.815, 1.646, 11.127, 6.459, 19.088)
    p.curve_to_cubic_rel(-15.778, -13.525, -4.996, -4.771, -5.610, -13.926)
    p.curve_to_cubic_rel(15.778, 38.324, -1.889, 19.922, 20.369, 15.699)
    p.curve_to_cubic_rel(-15.778, -13.527, -6.260, -3.510, -5.416, -14.123)
    p.curve_to_cubic_rel(9.019, 40.580, 2.073, 14.971, 17.599, 21.609)
    p.curve_to_cubic_rel(-20.289, -18.035, -7.709, -5.066, -9.369, -16.182)
    p.curve_to_cubic_rel(6.764, 45.088, -1.098, 12.369, 23.746, 28.234)
    p.curve_to_cubic_rel(-20.290, -15.779, -6.338, -5.688, -6.094, -17.955)
    p.curve_to_cubic_rel(4.510, 51.852, 7.438, 17.307, 20.604, 34.049)
    p.curve_to_cubic_rel(-22.543, -15.779, -6.479, -6.293, -9.618, -15.932)
    p.curve_to_cubic_rel(18.033, 24.797, 0.935, 13.344, 13.354, 15.201)
    p.curve_to_cubic_rel(0.000, 54.104, 0.991, 17.559, -6.613, 38.428)
    p.curve_to_cubic_rel(6.765, -31.561, 10.978, -1.799, -0.468, -26.018)
    p.curve_to_cubic_rel(33.814, -20.289, 7.880, -10.156, 30.066, -6.002)
    p.curve_to_cubic_abs(828.907, 468.852, 850.751, 453.906, 838.195, 464.797)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#72AA8B")
    p.stroke_color("#3C5D6A")
    p.stroke_width(2.3835)
    
    p.move_to_abs(89.820, 520.049)
    p.curve_to_cubic_rel(1.701, -12.189, 1.317, -2.605, 1.701, -12.189)
    p.curve_to_cubic_rel(19.522, -24.371, -4.256, -15.822, 15.915, -16.670)
    p.curve_to_cubic_rel(-18.223, 3.695, -7.104, -2.660, -11.914, 3.352)
    p.curve_to_cubic_rel(19.307, -20.924, 1.448, -14.186, 12.926, -12.773)
    p.curve_to_cubic_rel(-14.000, 2.578, -5.933, -3.920, -9.084, 2.654)
    p.curve_to_cubic_rel(22.534, -17.264, 5.068, -14.977, 16.796, -4.816)
    p.curve_to_cubic_rel(-13.999, 2.578, -5.883, -3.734, -9.397, 1.473)
    p.curve_to_cubic_rel(14.308, -18.473, 3.913, -9.393, 9.503, -12.447)
    p.curve_to_cubic_rel(-21.976, 19.373, -10.365, -5.021, -15.300, 10.461)
    p.curve_to_cubic_rel(-4.128, -11.330, -3.324, -3.262, 1.605, -8.707)
    p.curve_to_cubic_rel(-3.847, 28.123, -7.862, 6.863, 4.767, 17.367)
    p.curve_to_cubic_rel(-6.240, -10.771, -3.284, -3.271, 0.215, -8.338)
    p.curve_to_cubic_rel(1.060, 38.119, -3.609, 13.758, 5.176, 24.229)
    p.curve_to_cubic_abs(89.820, 520.049, 83.878, 520.811, 87.496, 524.648)
    p.close_path()
    
    p.end()
    
    # path3952
    p = Path()
    
    g.add(p)
    p.fill("#D04D31")
    p.stroke_color("#303030")
    p.stroke_width(2.3835)
    
    p.move_to_abs(129.527, 86.203)
    p.curve_to_cubic_rel(8.137, 16.719, 4.110, 3.808, 3.124, 18.931)
    p.curve_to_cubic_rel(6.492, -16.438, 3.540, -1.563, 1.735, -10.850)
    p.curve_to_cubic_rel(16.314, 2.217, 5.470, -2.040, 14.797, 5.377)
    p.curve_to_cubic_rel(-10.218, -14.808, 2.601, -5.404, -10.243, -13.296)
    p.curve_to_cubic_rel(8.750, -13.093, 0.029, -1.689, 10.505, -11.008)
    p.curve_to_cubic_rel(-18.507, 2.335, -2.771, -3.292, -16.945, 2.521)
    p.curve_to_cubic_rel(-14.534, -8.527, -1.346, -0.162, -12.084, -9.566)
    p.curve_to_cubic_rel(1.031, 16.403, -3.145, 1.333, 1.755, 15.054)
    p.curve_to_cubic_rel(-12.772, 12.104, -0.757, 1.410, -14.229, 8.337)
    p.curve_to_cubic_abs(129.527, 86.203, 115.563, 86.584, 123.691, 84.087)
    p.line_to_abs(129.527, 86.203)
    p.close_path()
    
    p.end()
    
    # path3954
    p = Path()
    
    g.add(p)
    p.fill("#E49982")
    
    p.move_to_abs(122.623, 83.476)
    p.curve_to_cubic_rel(12.514, -5.909, 6.535, -3.748, 11.453, -4.557)
    p.curve_to_cubic_rel(-5.964, -16.030, 1.063, -1.351, -5.964, -16.030)
    p.curve_to_cubic_smooth_rel(12.302, 12.302, 8.683, 13.364)
    p.curve_to_cubic_rel(16.304, -10.528, 3.619, -1.063, 9.292, -5.740)
    p.curve_to_cubic_rel(-13.321, 16.120, -5.736, 6.294, -13.917, 14.144)
    p.curve_to_cubic_smooth_rel(14.167, 10.439, 7.609, 5.173)
    p.curve_to_cubic_rel(-16.403, -4.102, -6.903, -2.000, -14.106, -7.531)
    p.curve_to_cubic_rel(-4.417, 16.578, -2.295, 3.431, -2.433, 5.518)
    p.curve_to_cubic_rel(-1.549, -18.069, -1.103, -12.693, 1.438, -16.097)
    p.curve_to_cubic_abs(122.623, 83.476, 133.271, 82.305, 130.087, 82.215)
    p.line_to_abs(122.623, 83.476)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(570.068, 141.750)
    p.curve_to_cubic_rel(34.217, -3.555, 8.561, 4.286, 18.221, -2.223)
    p.curve_to_cubic_rel(39.992, 15.999, 15.996, -1.330, 32.434, 3.106)
    p.curve_to_cubic_rel(-0.441, 37.773, 7.553, 12.886, 8.438, 29.330)
    p.curve_to_cubic_rel(-29.770, 36.880, -8.887, 8.443, -29.770, 22.665)
    p.curve_to_cubic_rel(7.994, 28.886, 0.000, 14.222, 3.549, 18.658)
    p.curve_to_cubic_rel(-9.326, 36.880, 4.446, 10.221, 1.786, 29.772)
    p.curve_to_cubic_rel(-39.994, 2.223, -11.109, 7.111, -23.107, 7.562)
    p.curve_to_cubic_rel(-67.547, -5.333, -16.887, -5.333, -49.771, -10.669)
    p.curve_to_cubic_rel(-38.213, 24.003, -17.771, 5.333, -26.656, 12.444)
    p.curve_to_cubic_rel(-38.217, 5.771, -11.558, 11.553, -25.776, 11.553)
    p.curve_to_cubic_rel(-47.102, -14.222, -12.440, -5.771, -41.766, -15.557)
    p.curve_to_cubic_rel(-26.664, 15.110, -5.336, 1.333, -19.553, 11.552)
    p.curve_to_cubic_rel(-49.769, -1.330, -7.106, 3.555, -34.659, 13.330)
    p.curve_to_cubic_rel(-12.442, -37.774, -15.109, -14.667, -12.442, -29.773)
    p.curve_to_cubic_rel(-13.335, -23.106, 0.000, -7.995, -6.221, -19.548)
    p.curve_to_cubic_rel(-28.881, -37.771, -7.108, -3.553, -34.658, -18.213)
    p.curve_to_cubic_rel(32.886, -36.881, 5.777, -19.558, 27.553, -29.327)
    p.curve_to_cubic_rel(33.770, -43.104, 5.333, -7.553, 13.330, -38.658)
    p.curve_to_cubic_rel(54.663, 11.108, 20.440, -4.446, 36.884, -3.994)
    p.curve_to_cubic_rel(63.101, 8.440, 17.771, 15.106, 39.104, 18.222)
    p.curve_to_cubic_rel(45.316, -52.880, 23.997, -9.775, 25.322, -39.546)
    p.curve_to_cubic_rel(52.881, -11.553, 19.992, -13.331, 41.773, -18.219)
    p.curve_to_cubic_rel(23.998, 29.327, 11.115, 6.665, 19.109, 16.883)
    p.curve_to_cubic_abs(570.068, 141.750, 562.074, 139.088, 564.738, 139.082)
    p.line_to_abs(570.068, 141.750)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#D0E9FB")
    
    p.move_to_abs(483.111, 112.862)
    p.curve_to_cubic_rel(-17.924, 23.069, -8.049, 5.365, -12.845, 13.966)
    p.curve_to_cubic_rel(-28.275, 30.270, -6.646, 11.923, -13.521, 24.265)
    p.curve_to_cubic_rel(-68.107, -9.243, -25.309, 10.312, -48.858, 7.114)
    p.curve_to_cubic_rel(-50.459, -10.058, -16.404, -13.948, -31.469, -14.189)
    p.curve_to_cubic_rel(-25.807, 31.282, -13.028, 2.831, -20.718, 19.950)
    p.curve_to_cubic_rel(-5.008, 9.860, -1.918, 4.257, -3.429, 7.626)
    p.curve_to_cubic_rel(-10.180, 9.284, -2.136, 3.022, -5.863, 5.930)
    p.curve_to_cubic_rel(-22.007, 26.167, -8.254, 6.427, -18.533, 14.422)
    p.curve_to_cubic_rel(26.381, 32.014, -4.492, 15.211, 19.056, 28.348)
    p.curve_to_cubic_rel(16.031, 27.482, 9.180, 4.591, 16.031, 18.297)
    p.line_to_rel(-0.083, 3.334)
    p.curve_to_cubic_rel(11.044, 30.924, -0.295, 8.239, -0.704, 19.524)
    p.curve_to_cubic_rel(44.174, 0.467, 12.525, 12.157, 36.699, 4.212)
    p.line_to_rel(10.499, -6.237)
    p.curve_to_cubic_rel(17.168, -9.240, 7.980, -4.984, 13.485, -8.318)
    p.curve_to_cubic_rel(50.339, 14.525, 7.989, -1.996, 40.896, 10.143)
    p.curve_to_cubic_rel(32.701, -4.800, 8.693, 4.033, 21.424, 6.480)
    p.curve_to_cubic_rel(40.269, -25.217, 12.453, -12.446, 22.101, -19.768)
    p.curve_to_cubic_rel(70.420, 5.351, 18.916, -5.676, 52.567, -0.291)
    p.curve_to_cubic_rel(35.893, -1.677, 15.828, 4.998, 26.227, 4.519)
    p.curve_to_cubic_rel(7.482, -30.816, 9.015, -5.771, 10.980, -22.780)
    p.line_to_rel(-2.271, -4.992)
    p.curve_to_cubic_rel(-6.139, -25.842, -3.428, -7.335, -6.139, -13.131)
    p.curve_to_cubic_rel(25.010, -34.905, 0.000, -13.643, 14.459, -25.936)
    p.line_to_rel(6.285, -5.521)
    p.curve_to_cubic_rel(-0.408, -31.754, 6.668, -6.340, 6.498, -19.994)
    p.curve_to_cubic_rel(-35.367, -13.602, -5.789, -9.881, -19.010, -14.964)
    p.curve_to_cubic_rel(-15.391, 2.851, -5.858, 0.488, -10.922, 1.742)
    p.curve_to_cubic_rel(-21.414, 0.204, -7.828, 1.943, -14.584, 3.616)
    p.line_to_rel(-1.572, -0.757)
    p.curve_to_cubic_rel(-13.674, -16.938, -5.342, -2.520, -8.866, -4.682)
    p.curve_to_cubic_rel(-21.961, -26.925, -4.684, -11.932, -12.080, -20.992)
    p.curve_to_cubic_abs(483.111, 112.862, 521.451, 95.851, 501.412, 100.657)
    p.line_to_abs(483.111, 112.862)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#7CC6F2")
    
    p.move_to_abs(261.868, 237.463)
    p.curve_to_cubic_rel(-1.120, 2.956, -0.426, 0.963, -0.775, 1.958)
    p.curve_to_cubic_rel(20.983, 15.086, 6.521, 7.344, 16.619, 12.909)
    p.curve_to_cubic_rel(6.105, 4.666, 2.189, 1.094, 4.241, 2.720)
    p.curve_to_cubic_rel(0.062, -0.081, 0.018, -0.023, 0.047, -0.055)
    p.curve_to_cubic_rel(19.240, -29.985, 5.094, -6.788, 19.240, -21.498)
    p.curve_to_cubic_rel(19.806, 25.464, 0.000, 0.000, 27.727, 13.015)
    p.curve_to_cubic_rel(-28.862, 42.018, -4.933, 7.745, -20.590, 25.568)
    p.curve_to_cubic_rel(10.637, 19.662, 0.960, 6.104, 3.626, 12.860)
    p.curve_to_cubic_rel(27.272, 5.733, 7.076, 6.874, 17.873, 7.319)
    p.curve_to_cubic_rel(-10.180, -22.713, -6.749, -8.412, -11.635, -16.896)
    p.curve_to_cubic_rel(26.025, -56.588, 3.957, -15.845, 30.554, -39.042)
    p.curve_to_cubic_rel(-6.223, -41.309, -4.527, -17.541, -17.541, -24.332)
    p.curve_to_cubic_rel(32.259, -38.917, 9.318, -13.980, 24.383, -26.427)
    p.curve_to_cubic_rel(-9.066, -6.497, -3.113, -1.871, -6.146, -4.016)
    p.curve_to_cubic_rel(-18.665, -10.535, -6.320, -5.374, -12.441, -8.693)
    p.curve_to_cubic_rel(-2.828, 2.196, -0.918, 0.722, -1.852, 1.446)
    p.curve_to_cubic_abs(261.868, 237.463, 330.338, 161.637, 270.922, 217.091)
    p.line_to_abs(261.868, 237.463)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#7CC6F2")
    
    p.move_to_abs(570.592, 147.112)
    p.curve_to_cubic_rel(-0.902, 0.941, -0.309, 0.312, -0.588, 0.629)
    p.curve_to_cubic_rel(-6.782, 49.229, -14.709, 14.714, -24.893, 28.859)
    p.curve_to_cubic_rel(10.739, 57.718, 18.106, 20.372, 29.420, 28.862)
    p.curve_to_cubic_rel(-18.321, 32.493, -7.809, 12.068, -14.291, 22.831)
    p.curve_to_cubic_rel(18.975, 4.605, 7.155, 1.335, 13.750, 2.953)
    p.curve_to_cubic_rel(1.176, 0.334, 0.414, 0.128, 0.773, 0.213)
    p.curve_to_cubic_rel(4.970, -6.874, 1.000, -2.432, 2.591, -4.754)
    p.curve_to_cubic_rel(32.399, -36.688, 17.444, -15.563, 29.754, -22.895)
    p.curve_to_cubic_rel(-3.578, -20.099, -2.123, -5.205, -3.578, -10.797)
    p.curve_to_cubic_rel(0.150, -2.322, 0.000, -0.780, 0.060, -1.551)
    p.curve_to_cubic_rel(-18.219, -41.046, -7.041, -15.355, -20.865, -29.580)
    p.curve_to_cubic_rel(16.520, -42.517, 2.672, -11.548, 5.377, -23.823)
    p.curve_to_cubic_rel(-2.926, 0.104, -0.971, 0.038, -1.926, 0.021)
    p.curve_to_cubic_rel(-15.391, 2.852, -5.859, 0.489, -10.922, 1.743)
    p.curve_to_cubic_abs(570.592, 147.112, 582.563, 147.537, 576.551, 149.027)
    p.line_to_abs(570.592, 147.112)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#7CC6F2")
    
    p.move_to_abs(374.473, 178.613)
    p.curve_to_cubic_rel(-6.791, 46.968, -10.749, 15.277, -19.239, 33.389)
    p.curve_to_cubic_rel(14.151, 46.967, 12.452, 13.584, 29.427, 35.082)
    p.curve_to_cubic_rel(-23.324, 41.835, -12.173, 9.462, -28.978, 25.030)
    p.line_to_rel(4.888, -2.902)
    p.curve_to_cubic_rel(17.168, -9.241, 7.979, -4.983, 13.484, -8.318)
    p.curve_to_cubic_rel(34.346, 8.188, 5.260, -1.314, 21.291, 3.493)
    p.curve_to_cubic_rel(2.568, -5.627, 0.352, -2.145, 1.154, -4.065)
    p.curve_to_cubic_rel(22.634, -56.021, 10.748, -11.882, 29.421, -36.781)
    p.curve_to_cubic_rel(-27.726, -42.439, -6.788, -19.240, -23.763, -24.893)
    p.curve_to_cubic_rel(4.385, -34.757, -2.834, -12.552, -1.013, -23.651)
    p.curve_to_cubic_rel(-35.079, -5.999, -12.461, 1.554, -24.268, -0.466)
    p.curve_to_cubic_abs(374.473, 178.613, 379.814, 169.879, 377.458, 174.371)
    p.line_to_abs(374.473, 178.613)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#7CC6F2")
    
    p.move_to_abs(494.998, 129.382)
    p.curve_to_cubic_rel(-39.045, 59.414, -7.918, 22.636, -43.572, 49.229)
    p.curve_to_cubic_rel(37.346, 43.005, 4.533, 10.184, 45.266, 29.994)
    p.curve_to_cubic_rel(-17.438, 69.076, -7.186, 11.810, -45.100, 41.309)
    p.curve_to_cubic_rel(28.014, -14.125, 7.799, -6.130, 16.065, -10.537)
    p.curve_to_cubic_rel(2.746, -0.689, 0.879, -0.262, 1.813, -0.478)
    p.curve_to_cubic_rel(-3.695, -18.606, -3.644, -6.421, -5.627, -13.002)
    p.curve_to_cubic_rel(25.465, -43.007, 6.222, -18.105, 28.285, -30.558)
    p.curve_to_cubic_rel(-24.899, -38.478, -2.827, -12.447, -27.733, -23.765)
    p.curve_to_cubic_rel(40.744, -49.226, 2.828, -14.711, 40.744, -31.117)
    p.curve_to_cubic_rel(-9.990, -33.014, 0.000, -9.112, -5.017, -22.226)
    p.curve_to_cubic_rel(-3.469, -2.296, -1.123, -0.809, -2.275, -1.577)
    p.curve_to_cubic_rel(-41.232, 7.495, -8.229, -4.935, -24.843, -1.742)
    p.curve_to_cubic_abs(494.998, 129.382, 494.621, 115.251, 497.484, 122.289)
    p.line_to_abs(494.998, 129.382)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(306.830, 243.651)
    p.line_to_rel(-0.889, 10.663)
    p.line_to_rel(5.333, 18.219)
    p.line_to_rel(-2.220, 24.438)
    p.line_to_rel(12.886, 6.666)
    p.curve_to_cubic_rel(51.103, -2.227, 0.000, 0.000, 37.772, -1.336)
    p.curve_to_cubic_rel(83.541, -13.775, 13.331, -0.884, 53.768, -9.330)
    p.curve_to_cubic_rel(141.756, -14.664, 29.774, -4.443, 78.213, -13.776)
    p.line_to_rel(3.998, -1.777)
    p.line_to_rel(3.996, -21.777)
    p.line_to_rel(-10.660, -41.769)
    p.line_to_rel(-59.104, 8.443)
    p.line_to_rel(-51.096, 3.107)
    p.line_to_rel(-23.549, 8.889)
    p.line_to_rel(-99.984, 6.220)
    p.line_to_abs(306.830, 243.651)
    p.line_to_abs(306.830, 243.651)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(325.959, 277.721)
    p.line_to_rel(-8.146, 0.742)
    p.line_to_rel(1.205, 12.961)
    p.line_to_rel(8.979, 2.869)
    p.line_to_rel(7.872, -1.850)
    p.curve_to_cubic_rel(3.426, -7.682, 0.000, 0.000, 3.426, -2.866)
    p.curve_to_cubic_rel(-4.075, -15.926, 0.000, -4.813, -1.948, -14.262)
    p.curve_to_cubic_rel(-8.977, -2.497, -2.128, -1.667, -7.402, -1.574)
    p.curve_to_cubic_rel(-2.779, -2.962, -1.576, -0.928, -2.779, -2.962)
    p.line_to_rel(-0.093, -6.020)
    p.line_to_rel(4.165, -0.648)
    p.line_to_rel(1.299, 6.203)
    p.line_to_rel(6.572, -0.926)
    p.line_to_rel(-0.649, -10.462)
    p.line_to_rel(-9.350, -3.794)
    p.line_to_rel(-9.353, 4.998)
    p.curve_to_cubic_rel(-0.092, 12.127, 0.000, 0.000, -1.569, 7.219)
    p.curve_to_cubic_rel(3.699, 7.963, 1.478, 4.905, 1.478, 7.317)
    p.curve_to_cubic_rel(10.648, 4.996, 2.226, 0.646, 9.350, 1.016)
    p.curve_to_cubic_rel(0.742, 6.947, 1.297, 3.982, 0.742, 6.947)
    p.line_to_horizontal_abs(326.700)
    p.line_to_abs(325.959, 277.721)
    p.line_to_abs(325.959, 277.721)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(363.179, 287.697)
    p.curve_to_cubic_rel(1.845, -19.973, 0.679, -4.774, 1.845, -19.973)
    p.curve_to_cubic_smooth_rel(-5.461, -18.796, -4.166, -15.552)
    p.curve_to_cubic_rel(-8.799, -3.518, -1.300, -3.238, -8.799, -3.518)
    p.line_to_rel(-7.218, 3.148)
    p.line_to_rel(-2.223, 16.293)
    p.line_to_rel(2.223, 9.721)
    p.line_to_rel(1.023, 9.440)
    p.line_to_rel(6.014, 6.850)
    p.curve_to_cubic_rel(6.481, -1.758, 0.000, 0.000, 6.203, -1.664)
    p.curve_to_cubic_rel(2.221, 6.203, 0.278, -0.093, 2.221, 6.203)
    p.line_to_rel(7.223, -2.502)
    p.line_to_abs(363.179, 287.697)
    p.line_to_abs(363.179, 287.697)
    p.close_path()
    p.move_to_abs(352.061, 281.148)
    p.line_to_rel(-1.203, -6.110)
    p.line_to_rel(-0.925, -9.443)
    p.line_to_rel(-0.275, -11.854)
    p.line_to_rel(3.705, -0.648)
    p.line_to_rel(2.312, 11.757)
    p.curve_to_cubic_rel(1.296, 12.127, 0.000, 0.000, 1.296, 8.798)
    p.curve_to_cubic_rel(-0.461, 4.094, 0.000, 1.973, -0.250, 3.290)
    p.line_to_rel(-3.148, 0.817)
    p.line_to_abs(352.061, 281.148)
    p.line_to_abs(352.061, 281.148)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(384.458, 287.162)
    p.line_to_rel(8.146, -1.201)
    p.curve_to_cubic_rel(-3.237, -22.307, 0.000, 0.000, -2.496, -13.698)
    p.curve_to_cubic_rel(-1.302, -21.108, -0.745, -8.609, -1.302, -21.108)
    p.line_to_rel(-9.717, 1.388)
    p.curve_to_cubic_rel(4.720, 34.069, 0.000, 0.000, 4.626, 29.438)
    p.line_to_rel(-4.164, 1.019)
    p.curve_to_cubic_rel(-1.667, -14.626, 0.000, 0.000, -1.205, -10.366)
    p.curve_to_cubic_rel(-2.779, -21.570, -0.467, -4.259, -2.779, -21.570)
    p.line_to_rel(-8.145, 1.111)
    p.curve_to_cubic_rel(2.776, 18.332, 0.000, 0.000, 2.041, 12.229)
    p.curve_to_cubic_rel(2.042, 21.476, 0.739, 6.107, 1.019, 20.175)
    p.curve_to_cubic_rel(5.551, 4.353, 1.020, 1.294, 5.551, 4.353)
    p.line_to_rel(7.314, -2.686)
    p.line_to_abs(384.458, 287.162)
    p.line_to_abs(384.458, 287.162)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(416.951, 271.980)
    p.curve_to_cubic_rel(-2.775, -23.793, -0.557, -5.554, -2.775, -22.589)
    p.curve_to_cubic_rel(-2.683, -3.518, 0.000, -1.202, -2.683, -3.518)
    p.line_to_rel(-5.001, -3.608)
    p.line_to_rel(-7.221, 1.202)
    p.line_to_rel(-5.834, 3.519)
    p.line_to_rel(1.577, 7.035)
    p.curve_to_cubic_rel(6.203, -2.683, 0.000, 0.000, 4.073, -2.683)
    p.curve_to_cubic_smooth_rel(4.629, 0.646, 4.079, -0.094)
    p.curve_to_cubic_rel(0.929, 6.093, 0.550, 0.729, 0.917, 5.996)
    p.curve_to_cubic_rel(-9.444, 3.628, -3.573, 0.969, -9.316, 2.671)
    p.curve_to_cubic_rel(-1.757, 14.344, -0.192, 1.388, -1.757, 14.344)
    p.line_to_rel(6.849, 12.965)
    p.line_to_rel(9.072, -2.590)
    p.line_to_rel(0.462, 1.479)
    p.curve_to_cubic_rel(7.498, -1.294, 0.000, 0.000, 5.089, -1.661)
    p.curve_to_cubic_abs(416.951, 271.980, 419.453, 285.405, 417.504, 277.535)
    p.line_to_abs(416.951, 271.980)
    p.close_path()
    p.move_to_abs(404.545, 275.682)
    p.line_to_rel(-0.739, -8.423)
    p.line_to_rel(4.144, -0.873)
    p.line_to_rel(1.132, 9.112)
    p.line_to_abs(404.545, 275.682)
    p.line_to_abs(404.545, 275.682)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(425.278, 238.097)
    p.line_to_rel(0.651, 3.428)
    p.line_to_rel(3.056, -2.686)
    p.line_to_rel(5.736, -0.184)
    p.line_to_rel(3.891, 3.982)
    p.line_to_rel(1.940, 18.142)
    p.line_to_rel(-7.867, 1.577)
    p.curve_to_cubic_rel(-2.127, -16.110, 0.000, 0.000, -1.016, -15.368)
    p.curve_to_cubic_rel(-3.150, 1.851, -1.110, -0.744, -3.338, 0.276)
    p.curve_to_cubic_rel(2.497, 19.441, 0.184, 1.574, 0.923, 12.593)
    p.curve_to_cubic_rel(3.334, 14.626, 1.575, 6.852, 3.334, 14.626)
    p.line_to_rel(-8.700, 1.300)
    p.curve_to_cubic_rel(-2.968, -20.549, 0.000, 0.000, -1.855, -12.679)
    p.curve_to_cubic_rel(-3.421, -22.865, -1.111, -7.870, -3.421, -22.865)
    p.line_to_abs(425.278, 238.097)
    p.line_to_abs(425.278, 238.097)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(464.338, 268.277)
    p.line_to_rel(-7.959, 0.928)
    p.line_to_rel(-2.223, -1.019)
    p.curve_to_cubic_rel(-0.396, -7.140, 0.000, 0.000, -0.135, -3.797)
    p.curve_to_cubic_rel(8.361, -1.379, 1.961, -0.526, 4.918, -1.173)
    p.line_to_rel(2.217, -13.325)
    p.line_to_rel(-6.289, -10.835)
    p.line_to_rel(-11.109, 1.111)
    p.line_to_rel(-3.891, 12.127)
    p.line_to_rel(3.607, 23.881)
    p.line_to_rel(7.871, 8.146)
    p.line_to_rel(11.389, -2.037)
    p.line_to_abs(464.338, 268.277)
    p.line_to_abs(464.338, 268.277)
    p.close_path()
    p.move_to_abs(452.119, 244.117)
    p.line_to_rel(2.316, -0.279)
    p.line_to_rel(1.477, 7.594)
    p.line_to_rel(-3.264, 1.123)
    p.curve_to_cubic_rel(-0.623, -5.383, -0.345, -2.731, -0.623, -5.383)
    p.line_to_abs(452.119, 244.117)
    p.line_to_abs(452.119, 244.117)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(489.150, 250.966)
    p.curve_to_cubic_rel(-2.961, -13.607, -0.560, -1.943, -2.961, -13.607)
    p.line_to_rel(-6.763, -5.461)
    p.line_to_rel(-13.424, 2.778)
    p.curve_to_cubic_rel(3.240, 22.592, 0.000, 0.000, 2.041, 13.890)
    p.curve_to_cubic_rel(1.758, 21.847, 1.199, 8.702, 1.758, 21.847)
    p.line_to_rel(9.904, -2.592)
    p.curve_to_cubic_rel(-1.857, -12.979, 0.000, 0.000, -1.119, -7.820)
    p.curve_to_cubic_rel(6.769, -3.040, 2.170, -0.648, 5.236, -1.742)
    p.curve_to_cubic_abs(489.150, 250.966, 488.313, 258.376, 489.697, 252.912)
    p.line_to_abs(489.150, 250.966)
    p.close_path()
    p.move_to_abs(481.371, 254.861)
    p.curve_to_cubic_rel(-3.660, -0.069, 0.000, 0.000, -1.867, -0.241)
    p.curve_to_cubic_rel(-2.357, -14.280, -0.955, -5.854, -2.357, -14.280)
    p.line_to_rel(3.980, -0.928)
    p.line_to_rel(2.043, 13.145)
    p.line_to_vertical_rel(2.133)
    p.line_to_horizontal_rel(-0.006)
    p.line_to_vertical_abs(254.861)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(513.492, 247.917)
    p.curve_to_cubic_rel(-2.596, -19.528, -1.305, -10.644, -2.596, -19.528)
    p.line_to_rel(-7.402, -6.023)
    p.line_to_rel(-6.668, 0.373)
    p.curve_to_cubic_rel(-6.197, 3.427, 0.000, 0.000, -2.584, 2.412)
    p.line_to_rel(1.105, 7.405)
    p.line_to_rel(4.719, -2.223)
    p.line_to_rel(6.576, 0.372)
    p.curve_to_cubic_rel(0.639, 6.500, 0.000, 0.000, 0.319, 3.535)
    p.line_to_rel(-8.967, 2.758)
    p.line_to_rel(-2.310, 14.445)
    p.line_to_rel(7.314, 13.146)
    p.line_to_rel(8.699, -2.319)
    p.line_to_rel(0.459, 1.667)
    p.curve_to_cubic_rel(8.146, -0.646, 0.000, 0.000, 4.071, -1.480)
    p.curve_to_cubic_abs(513.492, 247.917, 517.012, 267.268, 514.789, 258.568)
    p.line_to_abs(513.492, 247.917)
    p.close_path()
    p.move_to_abs(502.568, 257.273)
    p.line_to_rel(-0.931, -0.651)
    p.curve_to_cubic_rel(-0.926, -8.423, 0.000, 0.000, -0.646, -6.018)
    p.line_to_rel(3.928, -1.071)
    p.curve_to_cubic_rel(1.433, 9.124, 0.314, 2.875, 0.732, 6.232)
    p.line_to_abs(502.568, 257.273)
    p.line_to_abs(502.568, 257.273)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(524.873, 236.069)
    p.line_to_rel(3.992, 33.049)
    p.line_to_rel(-6.769, 1.297)
    p.curve_to_cubic_rel(-2.223, -22.219, 0.000, 0.000, -1.575, -14.812)
    p.curve_to_cubic_rel(-1.111, -11.661, -0.646, -7.408, -1.111, -11.661)
    p.curve_to_cubic_smooth_rel(-1.938, -10.835, -1.938, -4.539)
    p.line_to_rel(9.252, -2.406)
    p.line_to_rel(4.260, 0.739)
    p.line_to_rel(8.885, 30.828)
    p.curve_to_cubic_rel(-1.198, -11.943, 0.000, 0.000, -0.373, -5.557)
    p.curve_to_cubic_rel(-3.240, -19.255, -0.832, -6.383, -3.240, -19.255)
    p.line_to_rel(8.053, -1.946)
    p.curve_to_cubic_rel(1.570, 20.925, 0.000, 0.000, 0.559, 12.598)
    p.curve_to_cubic_rel(2.869, 23.049, 1.020, 8.327, 2.869, 23.049)
    p.curve_to_cubic_smooth_rel(-12.308, 2.130, -7.310, 0.189)
    p.curve_to_cubic_abs(524.873, 236.069, 534.969, 267.826, 526.078, 237.367)
    p.line_to_abs(524.873, 236.069)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(551.441, 234.126)
    p.line_to_horizontal_rel(-4.072)
    p.line_to_rel(1.670, 9.071)
    p.line_to_rel(2.316, -0.460)
    p.line_to_rel(3.786, 22.770)
    p.line_to_rel(9.726, 2.037)
    p.line_to_rel(6.936, -3.238)
    p.line_to_rel(-2.305, -15.730)
    p.line_to_rel(-6.109, 0.087)
    p.line_to_rel(1.664, 9.811)
    p.line_to_rel(-1.297, 0.929)
    p.line_to_rel(-1.391, -0.739)
    p.line_to_rel(-2.312, -16.293)
    p.line_to_rel(8.054, -1.108)
    p.curve_to_cubic_rel(-0.832, -9.261, 0.000, 0.000, -0.560, -9.261)
    p.curve_to_cubic_rel(-8.240, 1.757, -0.279, 0.000, -8.240, 1.757)
    p.line_to_rel(-0.285, -12.493)
    p.curve_to_cubic_rel(-9.811, 0.646, 0.000, 0.000, -4.346, 1.108)
    p.line_to_abs(551.441, 234.126)
    p.line_to_abs(551.441, 234.126)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(583.098, 249.956)
    p.line_to_rel(1.205, 7.035)
    p.curve_to_cubic_rel(3.888, -0.646, 0.000, 0.000, 2.781, 0.003)
    p.curve_to_cubic_rel(-0.646, -7.405, 0.000, 0.000, 0.094, -6.297)
    p.curve_to_cubic_rel(-6.947, -3.150, -0.744, -1.111, -3.979, -2.315)
    p.curve_to_cubic_rel(-5.364, -1.761, -2.963, -0.832, -5.364, -1.761)
    p.line_to_rel(-2.869, -9.997)
    p.curve_to_cubic_rel(0.553, -7.594, 0.000, 0.000, -0.006, -6.296)
    p.curve_to_cubic_rel(6.488, -6.199, 0.564, -1.294, 4.074, -5.641)
    p.curve_to_cubic_rel(12.399, 2.865, 2.401, -0.556, 4.160, -0.094)
    p.curve_to_cubic_rel(1.298, 10.835, 0.000, 0.000, 0.373, 8.705)
    p.line_to_rel(-7.400, 0.925)
    p.line_to_rel(-1.025, -6.665)
    p.line_to_rel(-3.701, 0.559)
    p.curve_to_cubic_rel(-0.826, 5.274, 0.000, 0.000, -1.569, 2.965)
    p.curve_to_cubic_rel(6.203, 4.720, 0.740, 2.316, 2.306, 3.521)
    p.curve_to_cubic_rel(7.595, 3.893, 3.890, 1.204, 5.371, -0.273)
    p.curve_to_cubic_rel(2.498, 13.887, 2.219, 4.163, 2.590, 9.721)
    p.curve_to_cubic_rel(-3.058, 7.588, -0.095, 4.164, -1.853, 7.029)
    p.curve_to_cubic_rel(-7.959, 2.040, -1.197, 0.556, -7.959, 2.040)
    p.line_to_rel(-9.166, -2.313)
    p.line_to_rel(-1.111, -13.334)
    p.line_to_abs(583.098, 249.956)
    p.line_to_abs(583.098, 249.956)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(303.661, 177.968)
    p.curve_to_cubic_rel(-7.873, 9.615, -6.286, 2.202, -7.873, 5.886)
    p.curve_to_cubic_rel(0.976, 6.177, 0.000, 2.136, 0.518, 4.286)
    p.line_to_rel(0.125, 0.519)
    p.curve_to_cubic_rel(12.886, 10.777, 1.603, 6.672, 6.311, 9.130)
    p.curve_to_cubic_rel(9.293, 4.053, 5.940, 1.486, 8.673, 3.261)
    p.curve_to_cubic_rel(-17.103, 0.471, -1.148, 1.310, -6.883, 3.939)
    p.line_to_rel(-2.842, -0.960)
    p.line_to_rel(1.731, 19.604)
    p.line_to_rel(18.765, -3.853)
    p.line_to_rel(1.658, -0.384)
    p.curve_to_cubic_rel(10.873, -11.440, 5.229, -1.188, 10.643, -2.418)
    p.curve_to_cubic_rel(-9.938, -13.397, 0.125, -4.870, -1.497, -11.143)
    p.curve_to_cubic_rel(-14.690, -5.071, -12.774, -3.404, -14.533, -4.908)
    p.curve_to_cubic_rel(0.074, -1.170, -0.086, -0.110, -0.164, -0.550)
    p.curve_to_cubic_rel(3.837, -2.674, 0.404, -1.041, 1.621, -2.290)
    p.curve_to_cubic_rel(14.009, 3.072, 3.552, -0.616, 11.318, 2.008)
    p.line_to_rel(2.936, 1.164)
    p.line_to_rel(-1.455, -17.172)
    p.line_to_rel(-1.490, -0.256)
    p.curve_to_cubic_abs(303.661, 177.968, 324.914, 176.952, 312.525, 174.869)
    p.line_to_abs(303.661, 177.968)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(326.165, 191.487)
    p.line_to_rel(-1.062, -12.522)
    p.curve_to_cubic_rel(-20.792, 0.850, 0.000, 0.000, -12.307, -2.120)
    p.curve_to_cubic_rel(-5.518, 14.007, -8.485, 2.971, -6.790, 8.699)
    p.curve_to_cubic_rel(11.458, 9.336, 1.274, 5.304, 4.668, 7.637)
    p.curve_to_cubic_rel(10.822, 6.578, 6.791, 1.693, 11.882, 4.454)
    p.curve_to_cubic_rel(-19.732, 1.696, -1.062, 2.121, -7.852, 5.729)
    p.line_to_rel(1.273, 14.432)
    p.curve_to_cubic_rel(16.552, -3.396, 0.000, 0.000, 10.396, -1.912)
    p.curve_to_cubic_rel(11.033, -9.974, 6.152, -1.487, 10.820, -1.696)
    p.curve_to_cubic_rel(-8.488, -11.458, 0.215, -8.277, -5.304, -10.614)
    p.curve_to_cubic_rel(-15.704, -5.726, -3.182, -0.850, -14.214, -3.820)
    p.curve_to_cubic_rel(5.094, -7.006, -1.484, -1.911, 0.212, -6.156)
    p.curve_to_cubic_abs(326.165, 191.487, 315.979, 187.455, 326.165, 191.487)
    p.line_to_abs(326.165, 191.487)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(333.727, 191.080)
    p.line_to_rel(-1.689, 0.448)
    p.line_to_rel(0.256, 1.731)
    p.curve_to_cubic_rel(3.375, 34.634, 0.038, 0.256, 3.787, 25.591)
    p.line_to_rel(-0.083, 1.842)
    p.line_to_rel(1.829, 0.195)
    p.curve_to_cubic_rel(8.676, -0.457, 0.179, 0.017, 4.389, 0.441)
    p.line_to_rel(1.833, -0.384)
    p.curve_to_cubic_rel(-2.754, -16.503, 0.000, 0.000, -2.140, -12.825)
    p.curve_to_cubic_rel(9.892, -0.063, 2.840, 0.358, 6.004, 0.451)
    p.curve_to_cubic_rel(12.063, -5.854, 9.619, -1.269, 11.900, -1.729)
    p.line_to_rel(0.029, -0.605)
    p.curve_to_cubic_rel(-3.781, -16.511, 0.012, -0.140, 0.786, -14.052)
    p.curve_to_cubic_abs(333.727, 191.080, 360.107, 187.793, 348.750, 187.103)
    p.line_to_abs(333.727, 191.080)
    p.close_path()
    p.move_to_abs(356.229, 196.644)
    p.curve_to_cubic_rel(0.770, 5.114, 0.379, 0.797, 0.770, 3.319)
    p.curve_to_cubic_rel(-0.179, 1.385, 0.000, 0.614, -0.070, 1.063)
    p.curve_to_cubic_rel(-6.048, 1.266, -1.053, 0.620, -4.022, 1.374)
    p.curve_to_cubic_rel(-0.947, -7.218, -0.516, -2.811, -0.947, -5.815)
    p.curve_to_cubic_rel(0.018, -0.207, 0.000, -0.091, 0.012, -0.128)
    p.curve_to_cubic_abs(356.229, 196.644, 351.083, 196.384, 355.010, 196.235)
    p.line_to_abs(356.229, 196.644)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(362.450, 191.275)
    p.curve_to_cubic_rel(-28.224, 1.699, -2.757, -1.487, -13.792, -2.121)
    p.curve_to_cubic_rel(3.397, 35.009, 0.000, 0.000, 3.819, 25.676)
    p.curve_to_cubic_rel(8.062, -0.425, 0.000, 0.000, 4.032, 0.425)
    p.line_to_rel(-2.863, -17.180)
    p.curve_to_cubic_rel(11.988, 0.206, 2.199, 0.573, 5.926, 1.007)
    p.curve_to_cubic_rel(10.399, -4.669, 11.250, -1.486, 10.185, -1.911)
    p.curve_to_cubic_abs(362.450, 191.275, 365.419, 203.157, 365.209, 192.759)
    p.line_to_abs(362.450, 191.275)
    p.close_path()
    p.move_to_abs(358.206, 204.642)
    p.curve_to_cubic_rel(-9.125, 1.483, -1.486, 1.059, -6.578, 2.336)
    p.curve_to_cubic_rel(-1.058, -10.183, 0.000, 0.000, -1.694, -8.490)
    p.curve_to_cubic_rel(9.549, -0.850, 0.636, -1.699, 8.488, -1.912)
    p.curve_to_cubic_abs(358.206, 204.642, 358.629, 196.154, 359.689, 203.582)
    p.line_to_abs(358.206, 204.642)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(377.487, 181.520)
    p.curve_to_cubic_rel(-9.055, 4.902, -4.874, 1.161, -7.664, 2.671)
    p.curve_to_cubic_rel(-1.292, 4.740, -0.945, 1.511, -1.292, 3.047)
    p.curve_to_cubic_rel(0.926, 6.365, 0.000, 1.879, 0.432, 3.947)
    p.line_to_rel(0.316, 1.563)
    p.curve_to_cubic_rel(7.462, 20.279, 3.078, 15.392, 5.210, 19.237)
    p.curve_to_cubic_rel(17.509, -0.516, 3.235, 1.489, 11.702, 2.880)
    p.curve_to_cubic_rel(7.339, -22.903, 4.865, -2.839, 7.339, -10.546)
    p.curve_to_cubic_rel(-6.750, -15.396, 0.000, -8.545, -2.212, -13.581)
    p.curve_to_cubic_abs(377.487, 181.520, 389.661, 178.834, 380.270, 180.856)
    p.line_to_abs(377.487, 181.520)
    p.close_path()
    p.move_to_abs(380.656, 190.763)
    p.curve_to_cubic_rel(6.837, 1.583, 6.095, -0.616, 6.386, -0.387)
    p.curve_to_cubic_rel(0.160, 1.752, 0.110, 0.498, 0.160, 1.091)
    p.curve_to_cubic_rel(-2.061, 10.972, 0.000, 3.313, -1.229, 8.158)
    p.curve_to_cubic_rel(-3.459, 0.122, -1.219, 0.046, -2.313, 0.081)
    p.curve_to_cubic_rel(-2.737, -7.239, -0.684, -1.490, -1.899, -4.292)
    p.curve_to_cubic_rel(-0.723, -5.795, -0.573, -2.016, -0.723, -4.160)
    p.curve_to_cubic_rel(0.041, -1.211, 0.000, -0.498, 0.029, -0.830)
    p.curve_to_cubic_abs(380.656, 190.763, 379.681, 190.856, 380.656, 190.763)
    p.line_to_abs(380.656, 190.763)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(393.216, 182.360)
    p.curve_to_cubic_rel(-15.273, 1.063, -3.183, -1.274, -10.819, 0.000)
    p.curve_to_cubic_rel(-7.851, 4.032, -4.452, 1.059, -6.791, 2.333)
    p.curve_to_cubic_rel(0.209, 11.245, -1.763, 2.813, -0.850, 5.941)
    p.curve_to_cubic_rel(6.366, 18.885, 1.063, 5.307, 3.608, 17.614)
    p.curve_to_cubic_smooth_rel(15.705, -0.424, 10.614, 2.543)
    p.curve_to_cubic_rel(6.360, -21.219, 5.092, -2.971, 6.360, -12.520)
    p.curve_to_cubic_abs(393.216, 182.360, 398.732, 187.242, 396.398, 183.635)
    p.line_to_abs(393.216, 182.360)
    p.close_path()
    p.move_to_abs(387.061, 206.978)
    p.line_to_rel(-6.151, 0.210)
    p.curve_to_cubic_rel(-3.393, -8.700, 0.000, 0.000, -2.121, -4.242)
    p.curve_to_cubic_rel(-0.640, -9.336, -1.273, -4.457, -0.640, -9.336)
    p.curve_to_cubic_rel(12.521, 2.758, 8.065, -0.635, 11.460, -1.909)
    p.curve_to_cubic_abs(387.061, 206.978, 390.460, 196.579, 387.061, 206.978)
    p.line_to_abs(387.061, 206.978)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(412.773, 181.351)
    p.line_to_rel(-10.004, 3.253)
    p.line_to_rel(0.176, 1.580)
    p.curve_to_cubic_rel(0.237, 16.162, 0.011, 0.113, 1.228, 11.219)
    p.line_to_rel(-3.224, 19.846)
    p.line_to_rel(2.752, -0.562)
    p.line_to_rel(14.943, -2.893)
    p.curve_to_cubic_rel(-2.142, -18.175, 0.000, 0.000, -1.815, -15.436)
    p.curve_to_cubic_rel(3.891, -1.080, 1.304, -0.361, 2.322, -0.646)
    p.curve_to_cubic_rel(2.741, 18.568, 0.503, 3.416, 2.741, 18.568)
    p.line_to_rel(11.949, -2.691)
    p.line_to_rel(0.121, -1.429)
    p.curve_to_cubic_rel(-0.262, -18.864, 0.041, -0.544, 1.068, -13.319)
    p.curve_to_cubic_rel(-18.864, -8.589, -1.623, -6.765, -5.399, -10.341)
    p.curve_to_cubic_rel(0.465, -6.022, 0.116, -1.530, 0.465, -6.022)
    p.line_to_abs(412.773, 181.351)
    p.line_to_abs(412.773, 181.351)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(412.948, 188.729)
    p.line_to_rel(0.425, -5.520)
    p.line_to_rel(-8.487, 2.759)
    p.curve_to_cubic_rel(0.212, 16.764, 0.000, 0.000, 1.277, 11.460)
    p.curve_to_cubic_rel(-2.758, 16.977, -1.059, 5.304, -2.758, 16.977)
    p.line_to_rel(13.157, -2.546)
    p.line_to_rel(-2.118, -18.038)
    p.line_to_rel(7.637, -2.121)
    p.line_to_rel(2.762, 18.676)
    p.line_to_rel(8.482, -1.911)
    p.curve_to_cubic_rel(-0.209, -18.248, 0.000, 0.000, 1.065, -12.941)
    p.curve_to_cubic_abs(412.948, 188.729, 430.771, 190.213, 428.441, 186.181)
    p.line_to_abs(412.948, 188.729)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(453.883, 171.022)
    p.curve_to_cubic_rel(-0.344, 2.182, 0.000, 0.000, -0.176, 1.103)
    p.curve_to_cubic_rel(-14.648, 1.263, -5.927, -1.003, -13.085, 0.003)
    p.curve_to_cubic_rel(-3.487, 15.825, -2.252, 1.802, -3.479, 15.687)
    p.curve_to_cubic_rel(6.609, 11.949, -0.250, 3.785, 1.304, 10.090)
    p.curve_to_cubic_rel(14.675, 0.456, 2.319, 0.809, 7.425, 0.916)
    p.curve_to_cubic_rel(0.145, 2.366, 0.063, 1.164, 0.145, 2.366)
    p.curve_to_cubic_smooth_rel(-0.506, 5.949, -0.371, 4.367)
    p.curve_to_cubic_rel(-3.584, 1.129, -1.000, 0.314, -1.955, 0.617)
    p.curve_to_cubic_rel(1.455, -3.078, 0.000, -0.003, 1.455, -3.078)
    p.line_to_rel(1.180, -2.549)
    p.line_to_rel(-15.085, -1.163)
    p.line_to_rel(-2.066, 3.706)
    p.line_to_rel(4.341, 15.568)
    p.line_to_rel(1.862, -0.482)
    p.curve_to_cubic_rel(24.875, -7.513, 23.425, -6.075, 24.438, -7.082)
    p.curve_to_cubic_rel(0.310, -13.706, 2.338, -2.345, 0.326, -13.596)
    p.curve_to_cubic_rel(-2.084, -13.346, -0.617, -2.674, -1.664, -9.409)
    p.curve_to_cubic_rel(0.221, -16.674, -0.400, -3.835, 0.215, -16.543)
    p.line_to_rel(0.088, -1.771)
    p.line_to_rel(-13.639, -2.033)
    p.line_to_abs(453.883, 171.022)
    p.line_to_abs(453.883, 171.022)
    p.close_path()
    p.move_to_abs(450.668, 185.424)
    p.curve_to_cubic_rel(0.092, -1.801, 0.000, -0.625, 0.033, -1.233)
    p.curve_to_cubic_rel(2.512, -1.588, 0.104, -1.056, 1.365, -1.445)
    p.curve_to_cubic_rel(-0.012, 0.150, 0.000, 0.055, -0.012, 0.093)
    p.curve_to_cubic_rel(1.949, 11.961, 0.000, 4.004, 1.123, 9.456)
    p.curve_to_cubic_rel(-2.857, -0.319, -1.420, -0.157, -2.648, -0.297)
    p.curve_to_cubic_abs(450.668, 185.424, 451.525, 193.015, 450.668, 188.936)
    p.line_to_abs(450.668, 185.424)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(467.697, 203.367)
    p.curve_to_cubic_rel(-2.125, -13.579, -0.642, -2.759, -1.699, -9.546)
    p.curve_to_cubic_rel(0.209, -16.977, -0.431, -4.032, 0.209, -16.977)
    p.line_to_rel(-9.979, -1.486)
    p.line_to_rel(-0.635, 4.032)
    p.curve_to_cubic_rel(-15.063, 0.635, -5.938, -1.699, -14.004, -0.212)
    p.curve_to_cubic_rel(-2.759, 14.428, -1.060, 0.850, -2.543, 11.248)
    p.curve_to_cubic_rel(5.308, 9.974, -0.209, 3.183, 1.061, 8.489)
    p.curve_to_cubic_rel(15.854, 0.265, 3.031, 1.062, 11.339, 0.608)
    p.curve_to_cubic_rel(0.269, 4.405, 0.164, 1.458, 0.269, 2.938)
    p.curve_to_cubic_rel(-0.633, 7.428, 0.000, 4.032, -0.633, 7.428)
    p.line_to_rel(-7.419, 2.336)
    p.line_to_rel(-1.483, -1.062)
    p.line_to_rel(1.906, -2.759)
    p.line_to_rel(1.274, -2.758)
    p.line_to_rel(-11.031, -0.850)
    p.line_to_rel(-1.060, 1.908)
    p.line_to_rel(3.607, 12.944)
    p.curve_to_cubic_rel(23.979, -7.003, 0.000, 0.000, 22.914, -5.940)
    p.curve_to_cubic_abs(467.697, 203.367, 468.971, 214.193, 468.330, 206.128)
    p.line_to_abs(467.697, 203.367)
    p.close_path()
    p.move_to_abs(451.781, 195.729)
    p.curve_to_cubic_rel(-2.969, -12.307, -2.334, -0.428, -3.396, -8.274)
    p.curve_to_cubic_rel(6.576, -3.398, 0.429, -4.036, 6.576, -3.398)
    p.curve_to_cubic_rel(1.693, 13.581, -0.639, 3.183, 0.636, 10.398)
    p.curve_to_cubic_rel(0.758, 2.796, 0.285, 0.864, 0.541, 1.804)
    p.curve_to_cubic_abs(451.781, 195.729, 455.529, 196.329, 453.213, 195.991)
    p.line_to_abs(451.781, 195.729)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(484.670, 167.051)
    p.curve_to_cubic_rel(-13.965, 4.938, -10.480, 1.164, -12.988, 3.375)
    p.curve_to_cubic_rel(-0.488, 20.206, -1.629, 2.604, -1.176, 15.525)
    p.line_to_rel(0.209, 1.493)
    p.curve_to_cubic_rel(9.426, 11.853, 0.697, 5.108, 1.664, 12.103)
    p.curve_to_cubic_rel(18.539, -2.365, 6.646, -0.215, 18.058, -2.275)
    p.line_to_rel(1.449, -0.262)
    p.line_to_rel(1.432, -14.970)
    p.line_to_rel(-15.967, 2.194)
    p.curve_to_cubic_rel(1.433, 2.868, 0.000, 0.000, 1.379, 2.749)
    p.curve_to_cubic_rel(-5.586, 1.051, -2.281, 0.597, -4.563, 1.054)
    p.curve_to_cubic_rel(-1.043, -4.300, -0.455, -0.689, -0.845, -3.009)
    p.curve_to_cubic_rel(20.493, -5.849, 5.604, -0.920, 14.176, -2.688)
    p.line_to_rel(1.353, -0.678)
    p.line_to_rel(-0.310, -1.480)
    p.curve_to_cubic_rel(-3.957, -11.376, -0.188, -0.870, -1.846, -8.565)
    p.curve_to_cubic_abs(484.670, 167.051, 495.074, 166.871, 492.398, 166.192)
    p.line_to_abs(484.670, 167.051)
    p.close_path()
    p.move_to_abs(476.441, 181.936)
    p.curve_to_cubic_rel(4.854, -2.511, 0.000, -1.038, 0.000, -1.932)
    p.curve_to_cubic_rel(4.656, 0.603, 4.398, -0.529, 4.533, 0.070)
    p.curve_to_cubic_rel(0.109, 0.733, 0.068, 0.343, 0.109, 0.570)
    p.curve_to_cubic_rel(-0.121, 0.384, 0.000, 0.180, -0.048, 0.282)
    p.curve_to_cubic_rel(-8.688, 2.240, -0.304, 0.401, -1.929, 1.676)
    p.curve_to_cubic_abs(476.441, 181.936, 476.697, 182.858, 476.441, 182.544)
    p.line_to_abs(476.441, 181.936)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(489.553, 194.246)
    p.curve_to_cubic_rel(-9.125, 1.699, 0.000, 0.000, -7.012, 2.121)
    p.curve_to_cubic_rel(-2.555, -7.801, -1.711, -0.344, -2.047, -5.080)
    p.curve_to_cubic_rel(21.867, -5.993, 4.818, -0.716, 14.955, -2.546)
    p.curve_to_cubic_rel(-3.607, -10.611, 0.000, 0.000, -1.697, -8.063)
    p.curve_to_cubic_rel(-11.248, -2.543, -1.914, -2.543, -3.606, -3.393)
    p.curve_to_cubic_rel(-12.516, 4.030, -7.633, 0.847, -11.457, 2.334)
    p.curve_to_cubic_rel(-0.215, 18.885, -1.059, 1.699, -1.059, 13.156)
    p.curve_to_cubic_rel(7.639, 11.670, 0.850, 5.729, 1.063, 11.883)
    p.curve_to_cubic_rel(18.250, -2.336, 6.582, -0.215, 18.250, -2.336)
    p.line_to_rel(1.064, -11.033)
    p.line_to_rel(-10.824, 1.487)
    p.line_to_abs(489.553, 194.246)
    p.line_to_abs(489.553, 194.246)
    p.close_path()
    p.move_to_abs(481.068, 177.481)
    p.curve_to_cubic_rel(6.785, 2.121, 5.301, -0.637, 6.364, 0.212)
    p.curve_to_cubic_rel(-11.313, 5.827, 0.399, 1.821, 0.971, 4.986)
    p.curve_to_cubic_rel(-2.049, -3.494, -0.932, -0.910, -2.049, -1.644)
    p.curve_to_cubic_abs(481.068, 177.481, 474.492, 179.390, 475.756, 178.115)
    p.line_to_abs(481.068, 177.481)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(503.023, 161.171)
    p.line_to_rel(-1.611, 0.454)
    p.line_to_rel(0.203, 1.664)
    p.curve_to_cubic_rel(4.863, 48.817, 0.047, 0.384, 4.660, 38.638)
    p.line_to_rel(0.059, 2.578)
    p.line_to_rel(2.467, -0.742)
    p.curve_to_cubic_rel(29.387, -7.151, 0.193, -0.063, 19.691, -5.912)
    p.line_to_rel(2.056, -0.262)
    p.line_to_rel(-0.379, -2.033)
    p.curve_to_cubic_rel(-4.837, -18.670, -0.933, -4.929, -3.236, -16.604)
    p.curve_to_cubic_rel(-6.645, -2.822, -0.977, -1.260, -3.719, -2.156)
    p.curve_to_cubic_rel(3.299, -2.234, 1.291, -0.698, 2.520, -1.443)
    p.curve_to_cubic_rel(2.008, -7.117, 1.426, -1.420, 2.008, -4.193)
    p.curve_to_cubic_rel(-1.641, -8.298, 0.000, -3.075, -0.646, -6.311)
    p.line_to_rel(-0.432, -1.056)
    p.curve_to_cubic_abs(503.023, 161.171, 529.877, 158.916, 526.205, 154.628)
    p.line_to_abs(503.023, 161.171)
    p.close_path()
    p.move_to_abs(516.588, 167.897)
    p.curve_to_cubic_rel(1.768, 9.153, 0.721, 1.792, 1.762, 7.122)
    p.curve_to_cubic_rel(-4.153, 0.710, -0.838, 0.294, -2.584, 0.570)
    p.curve_to_cubic_rel(-1.064, -9.462, -0.256, -2.270, -0.803, -7.169)
    p.curve_to_cubic_abs(516.588, 167.897, 514.521, 168.084, 515.789, 167.927)
    p.line_to_abs(516.588, 167.897)
    p.close_path()
    p.move_to_abs(526.984, 191.816)
    p.curve_to_cubic_rel(0.967, 4.469, 0.291, 1.315, 0.604, 2.787)
    p.curve_to_cubic_rel(-13.582, 2.459, -2.723, 0.495, -10.801, 1.955)
    p.curve_to_cubic_rel(-0.809, -6.538, -0.256, -2.078, -0.570, -4.661)
    p.curve_to_cubic_abs(526.984, 191.816, 518.012, 191.278, 524.268, 191.590)
    p.line_to_abs(526.984, 191.816)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(533.689, 187.030)
    p.curve_to_cubic_rel(-11.675, -3.187, -1.490, -1.914, -11.675, -3.187)
    p.curve_to_cubic_smooth_rel(8.490, -4.458, 6.373, -2.334)
    p.curve_to_cubic_rel(0.000, -13.156, 2.123, -2.120, 1.693, -9.758)
    p.curve_to_cubic_rel(-26.940, -3.180, -1.692, -3.396, -0.635, -10.610)
    p.curve_to_cubic_rel(4.877, 49.013, 0.000, 0.000, 4.659, 38.617)
    p.curve_to_cubic_rel(29.705, -7.213, 0.000, 0.000, 19.735, -5.941)
    p.curve_to_cubic_abs(533.689, 187.030, 538.141, 204.854, 535.172, 188.938)
    p.line_to_abs(533.689, 187.030)
    p.close_path()
    p.move_to_abs(517.773, 166.024)
    p.curve_to_cubic_rel(2.334, 12.307, 1.061, 0.422, 3.184, 11.242)
    p.curve_to_cubic_rel(-7.642, 1.486, -0.851, 1.059, -6.365, 1.486)
    p.line_to_rel(-1.479, -13.156)
    p.curve_to_cubic_abs(517.773, 166.024, 510.988, 166.658, 516.715, 165.600)
    p.line_to_abs(517.773, 166.024)
    p.close_path()
    p.move_to_abs(512.682, 201.036)
    p.line_to_rel(-1.272, -10.398)
    p.curve_to_cubic_rel(17.188, -0.637, 5.940, -1.908, 17.188, -0.637)
    p.line_to_rel(1.693, 7.850)
    p.line_to_abs(512.682, 201.036)
    p.line_to_abs(512.682, 201.036)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(536.650, 171.578)
    p.curve_to_cubic_rel(1.983, 15.473, -0.955, 4.804, 0.926, 12.499)
    p.line_to_rel(0.867, 2.994)
    p.curve_to_cubic_rel(4.865, 9.255, 1.373, 5.117, 2.455, 8.530)
    p.curve_to_cubic_rel(9.926, 0.450, 3.514, 1.050, 6.762, 1.198)
    p.line_to_rel(1.584, -0.322)
    p.curve_to_cubic_rel(9.351, -6.428, 3.183, -0.611, 7.541, -1.446)
    p.curve_to_cubic_rel(2.194, -19.563, 1.682, -4.591, 3.416, -14.197)
    p.curve_to_cubic_rel(-10.608, -8.737, -1.182, -5.243, -3.451, -8.737)
    p.curve_to_cubic_abs(536.650, 171.578, 552.408, 164.703, 537.932, 165.200)
    p.line_to_abs(536.650, 171.578)
    p.close_path()
    p.move_to_abs(553.514, 173.976)
    p.line_to_rel(0.711, -0.062)
    p.curve_to_cubic_rel(1.029, 0.053, 0.000, 0.000, 0.871, 0.044)
    p.curve_to_cubic_rel(0.064, 0.529, 0.041, 0.125, 0.064, 0.288)
    p.curve_to_cubic_rel(-0.188, 2.226, 0.000, 0.629, -0.105, 1.545)
    p.line_to_rel(-0.272, 3.733)
    p.curve_to_cubic_rel(-2.420, 5.690, 0.000, 3.663, -0.810, 5.580)
    p.curve_to_cubic_rel(-2.916, -2.330, -1.853, 0.122, -2.164, -0.268)
    p.curve_to_cubic_rel(-2.229, -8.845, -1.029, -2.840, -2.218, -7.344)
    p.curve_to_cubic_abs(553.514, 173.976, 548.072, 174.450, 551.186, 174.174)
    p.line_to_abs(553.514, 173.976)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(565.518, 173.874)
    p.curve_to_cubic_rel(-8.705, -7.216, -1.063, -4.670, -2.764, -7.216)
    p.curve_to_cubic_rel(-18.248, 5.304, -5.940, 0.000, -17.397, 1.059)
    p.curve_to_cubic_rel(1.914, 14.432, -0.850, 4.248, 0.851, 11.461)
    p.curve_to_cubic_rel(4.453, 11.035, 1.062, 2.970, 2.334, 10.396)
    p.curve_to_cubic_rel(8.914, 0.422, 2.123, 0.634, 5.308, 1.271)
    p.curve_to_cubic_rel(9.549, -5.517, 3.404, -0.800, 7.851, -0.850)
    p.curve_to_cubic_abs(565.518, 173.874, 565.094, 187.664, 566.578, 178.540)
    p.line_to_abs(565.518, 173.874)
    p.close_path()
    p.move_to_abs(556.813, 180.452)
    p.curve_to_cubic_rel(-4.241, 7.637, 0.000, 4.879, -1.420, 7.448)
    p.curve_to_cubic_rel(-4.888, -3.607, -3.183, 0.213, -4.037, -1.273)
    p.curve_to_cubic_rel(-2.334, -9.971, -0.850, -2.336, -2.543, -8.064)
    p.curve_to_cubic_rel(8.699, -2.549, 0.215, -1.911, 3.824, -2.121)
    p.curve_to_cubic_abs(556.813, 180.452, 558.938, 171.540, 556.813, 175.573)
    p.line_to_abs(556.813, 180.452)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(581.514, 154.174)
    p.line_to_rel(-14.656, 4.326)
    p.line_to_rel(0.349, 1.755)
    p.curve_to_cubic_rel(5.481, 38.347, 0.047, 0.232, 4.656, 23.380)
    p.line_to_rel(0.089, 1.527)
    p.line_to_rel(1.500, 0.288)
    p.curve_to_cubic_rel(14.840, 0.651, 0.331, 0.061, 8.239, 1.530)
    p.curve_to_cubic_rel(12.899, -5.758, 10.733, -1.432, 12.498, -3.972)
    p.curve_to_cubic_rel(0.447, -16.177, 0.459, -2.074, 0.906, -12.761)
    p.line_to_rel(-0.150, -1.448)
    p.curve_to_cubic_rel(-2.102, -5.828, -0.188, -2.072, -0.391, -4.420)
    p.curve_to_cubic_rel(-3.922, -0.989, -1.000, -0.823, -2.316, -1.158)
    p.curve_to_cubic_rel(-11.039, 2.668, -2.461, 0.262, -6.820, 1.486)
    p.curve_to_cubic_rel(-1.227, 0.341, 0.000, 0.000, -0.686, 0.189)
    p.curve_to_cubic_rel(0.000, -20.445, 0.000, -3.902, 0.000, -20.445)
    p.line_to_abs(581.514, 154.174)
    p.line_to_abs(581.514, 154.174)
    p.close_path()
    p.move_to_abs(587.584, 182.506)
    p.curve_to_cubic_rel(0.873, 5.770, 0.541, 0.225, 0.676, 2.133)
    p.curve_to_cubic_rel(0.064, 1.117, 0.000, 0.000, 0.029, 0.579)
    p.curve_to_cubic_rel(-7.205, 2.040, -1.677, 0.478, -4.697, 1.330)
    p.curve_to_cubic_rel(0.116, -7.431, 0.041, -2.631, 0.082, -5.857)
    p.curve_to_cubic_abs(587.584, 182.506, 585.262, 182.692, 587.148, 182.425)
    p.line_to_abs(587.584, 182.506)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#FFF22D")
    
    p.move_to_abs(600.525, 179.390)
    p.curve_to_cubic_rel(-4.033, -6.578, -0.424, -3.180, 0.000, -7.000)
    p.curve_to_cubic_rel(-14.447, 3.643, -3.025, 0.317, -9.514, 2.308)
    p.line_to_rel(0.016, -0.034)
    p.line_to_vertical_rel(-20.369)
    p.line_to_rel(-12.938, 3.819)
    p.curve_to_cubic_rel(5.516, 38.617, 0.000, 0.000, 4.660, 23.340)
    p.curve_to_cubic_rel(14.218, 0.638, 0.000, 0.000, 7.855, 1.487)
    p.curve_to_cubic_rel(11.241, -4.242, 6.364, -0.850, 10.821, -2.336)
    p.curve_to_cubic_abs(600.525, 179.390, 600.525, 192.972, 600.949, 182.573)
    p.line_to_abs(600.525, 179.390)
    p.close_path()
    p.move_to_abs(579.309, 194.030)
    p.line_to_rel(0.188, -11.438)
    p.curve_to_cubic_rel(8.723, -1.927, 2.926, -1.063, 7.344, -2.482)
    p.curve_to_cubic_rel(2.332, 10.184, 2.123, 0.847, 1.914, 3.393)
    p.line_to_abs(579.309, 194.030)
    p.line_to_abs(579.309, 194.030)
    p.close_path()
    
    p.end()
    
    p = Path()
    
    g.add(p)
    p.fill("#2566AF")
    
    p.move_to_abs(526.695, 127.928)
    p.curve_to_cubic_rel(6.225, -9.922, 4.084, -1.263, 8.076, -5.645)
    p.curve_to_cubic_rel(-11.084, -3.794, -1.850, -4.279, -7.588, -6.903)
    p.curve_to_cubic_rel(-8.949, 13.521, -3.504, 3.110, -6.715, 12.645)
    p.curve_to_cubic_rel(-1.461, -4.279, -2.240, 0.876, -3.016, 0.972)
    p.curve_to_cubic_rel(-1.752, -13.227, 1.560, -5.255, 1.176, -10.695)
    p.curve_to_cubic_rel(-10.793, 3.110, -2.916, -2.528, -9.432, -2.915)
    p.curve_to_cubic_rel(3.887, 10.896, -1.363, 6.031, 1.844, 8.560)
    p.curve_to_cubic_rel(1.664, 4.277, 2.047, 2.333, 2.438, 3.306)
    p.curve_to_cubic_rel(-3.893, -1.941, -0.479, 0.593, -1.360, 0.296)
    p.curve_to_cubic_rel(-13.129, -3.794, -2.532, -2.237, -9.922, -5.254)
    p.curve_to_cubic_rel(-4.666, 9.532, -3.211, 1.461, -5.646, 7.294)
    p.curve_to_cubic_rel(9.334, 4.960, 0.973, 2.237, 3.602, 5.932)
    p.curve_to_cubic_rel(12.842, -3.599, 5.736, -0.975, 11.574, -3.599)
    p.curve_to_cubic_rel(0.000, 2.822, 1.270, 0.000, 2.432, 1.266)
    p.curve_to_cubic_rel(-11.375, 8.848, -2.432, 1.554, -9.525, 5.248)
    p.curve_to_cubic_rel(1.652, 11.382, -1.852, 3.599, -3.213, 9.147)
    p.curve_to_cubic_rel(12.735, -5.156, 4.863, 2.234, 9.246, 1.848)
    p.curve_to_cubic_rel(2.916, -13.907, 3.505, -7.003, 1.753, -13.520)
    p.curve_to_cubic_rel(4.382, 8.071, 1.171, -0.387, 2.632, 5.447)
    p.curve_to_cubic_rel(13.034, 4.570, 1.752, 2.624, 7.688, 9.436)
    p.curve_to_cubic_rel(-4.184, -13.130, 5.349, -4.861, -1.176, -11.669)
    p.curve_to_cubic_rel(-6.228, -4.472, -3.015, -1.458, -7.199, -2.915)
    p.curve_to_cubic_abs(526.695, 127.928, 518.822, 131.143, 522.609, 129.193)
    p.line_to_abs(526.695, 127.928)
    p.close_path()
    p.move_to_abs(521.568, 138.163)
    p.line_to_rel(1.646, 0.762)
    p.curve_to_cubic_rel(5.074, 6.506, 1.553, 0.751, 4.660, 3.646)
    p.curve_to_cubic_rel(-1.351, 3.422, 0.190, 1.318, -0.232, 2.406)
    p.curve_to_cubic_rel(-3.219, 1.169, -1.020, 0.928, -2.071, 1.312)
    p.curve_to_cubic_rel(-6.871, -5.379, -2.834, -0.349, -5.736, -3.671)
    p.line_to_rel(-1.852, -3.916)
    p.curve_to_cubic_rel(-4.783, -4.926, -1.268, -3.075, -2.361, -5.729)
    p.curve_to_cubic_rel(-1.844, 4.483, -1.723, 0.579, -1.779, 2.386)
    p.curve_to_cubic_rel(-2.193, 10.404, -0.070, 2.549, -0.193, 6.392)
    p.curve_to_cubic_rel(-10.178, 4.253, -3.021, 6.028, -6.256, 6.061)
    p.curve_to_cubic_rel(-1.979, -2.024, -1.025, -0.465, -1.676, -1.132)
    p.curve_to_cubic_rel(1.250, -6.684, -0.554, -1.595, -0.082, -4.091)
    p.curve_to_cubic_rel(9.014, -7.078, 1.274, -2.479, 6.309, -5.470)
    p.line_to_rel(1.676, -1.016)
    p.curve_to_cubic_rel(2.205, -4.195, 2.514, -1.606, 2.463, -3.319)
    p.curve_to_cubic_rel(-3.264, -2.231, -0.389, -1.336, -1.703, -2.231)
    p.line_to_rel(-4.033, 1.085)
    p.curve_to_cubic_rel(-9.129, 2.540, -2.467, 0.838, -5.842, 1.984)
    p.curve_to_cubic_rel(-7.221, -3.809, -4.510, 0.766, -6.453, -2.057)
    p.curve_to_cubic_rel(3.684, -6.971, -0.438, -1.024, 1.190, -5.839)
    p.curve_to_cubic_rel(11.025, 3.479, 2.070, -0.940, 8.617, 1.344)
    p.curve_to_cubic_rel(4.889, 2.688, 2.397, 2.118, 3.631, 2.796)
    p.line_to_rel(1.820, -0.992)
    p.curve_to_cubic_rel(-1.709, -6.785, 2.020, -2.522, -0.228, -5.089)
    p.line_to_rel(-0.759, -0.835)
    p.curve_to_cubic_rel(-2.698, -8.339, -1.891, -2.051, -3.678, -3.988)
    p.curve_to_cubic_rel(2.549, -3.104, 0.370, -1.629, 1.227, -2.673)
    p.curve_to_cubic_rel(5.067, 1.038, 1.819, -0.600, 3.975, 0.087)
    p.curve_to_cubic_rel(1.158, 11.193, 2.129, 1.845, 2.588, 6.343)
    p.curve_to_cubic_rel(-0.022, 6.584, -0.902, 3.043, -1.432, 5.295)
    p.curve_to_cubic_rel(4.061, 0.072, 1.268, 1.169, 2.942, 0.506)
    p.curve_to_cubic_rel(4.965, -6.729, 1.705, -0.669, 2.939, -2.874)
    p.curve_to_cubic_rel(4.572, -7.148, 1.436, -2.724, 3.066, -5.811)
    p.curve_to_cubic_rel(3.363, -0.751, 1.117, -0.989, 2.445, -0.957)
    p.curve_to_cubic_rel(4.639, 3.858, 1.961, 0.438, 3.817, 1.987)
    p.curve_to_cubic_rel(-0.111, 3.194, 0.430, 1.013, 0.400, 2.086)
    p.curve_to_cubic_rel(-4.904, 4.082, -0.820, 1.786, -2.799, 3.428)
    p.curve_to_cubic_rel(-9.928, 5.598, -1.327, 0.413, -8.077, 2.621)
    p.line_to_rel(-0.320, 2.311)
    p.curve_to_cubic_abs(521.568, 138.163, 516.430, 135.838, 518.822, 136.918)
    p.line_to_abs(521.568, 138.163)
    p.close_path()
    
    p.end()
    #endregion drawing

# Draw the stick figures as per the provided data set
def draw_portrait(portraits):
    # convert an "image" into a function
    drawing_lookup = {
        "Person A": person_a,
        "Person B": person_b,
        "Person C": person_c,
        "Person D": person_d,
        "Pet": pet
    }

    # convert a "position" into an x coordinate
    place_lookup = {
        0: -300,
        1: -150,
        2: 0,
        3: 150,
        4: 300
    }
    
    # draw all the images in the specified portrait
    for portrait, place, scale_y, crown in portraits:
        fn = drawing_lookup[portrait]
        # scale_y is negative because my drawing library expects 0, 0 at the top-left of the window
        fn(place_lookup[place], 0, 1.0, -scale_y, crown == "*")

#
#--------------------------------------------------------------------#

#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your stick figures.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing window with a blue background representing
# the sky, and with the "home" coordinate set to the middle of the
# area where the stick figures will stand
setup(window_width, window_height)
setworldcoordinates(-window_width / 2, grass_offset,
                    window_width / 2, window_height + grass_offset)
bgcolor('sky blue')

# Draw the grass (with animation turned off to make it faster)
tracer(False)
#draw_grass()
penup()
custom_background()

# Give the window a title
# ***** Replace this title with one that describes your choice
# ***** of individuals
title('My Stretchy Family (Spongebob Squarepants, Patrick Star, Squidward Tentacles, Sandy Cheeks and Gary the Snail)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Draw the locations to stand, their labels and selected coordinates
# ***** If you don't want to display these background elements,
# ***** to make your portrait look nicer, change the corresponding
# ***** argument(s) below to False
draw_locations(True)
draw_labels(True)
mark_coords(False)

# Call the student's function to display the stick figures
# ***** If you want to turn off animation while drawing your
# ***** stick figures, to make your program draw faster, change
# ***** the following argument to False
tracer(False)
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_portrait(portrait_11)

# Test code for debugging
"""import time

for i in xrange(1, 24):
    portrait = globals()["portrait_%02d" % i]
    print "portrait %d" % i

    draw_portrait(portrait)
    update()
    time.sleep(1)"""

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#


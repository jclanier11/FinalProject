"""
Program: LanierJoshFinalProject2.py
Author: Josh Lanier
Contains the FloorKit and Trailer classes to create data objects for the Trailer Floor Repository program.
"""


class FloorKit(object):
    """Contains the methods for creating FloorKit objects with attributes: kit name, length in feet, cinch heights for a strap tightened \
        4 kit high load at the back, middle, and front pillars of the trailer, Boolean variable that holds True for wood only kits and \
        False for combo aluminum and wood. Also contains string method for FloorKit object."""

    def __init__(self, name, length, cinchBack, cinchMiddle, cinchFront, woodOnly = False):
        """Runs and instantiates FloorKit object."""
        self.name = str(name)
        self.length = float(length)
        self.cinchBack = float(cinchBack)
        self.cinchMiddle = float(cinchMiddle)
        self.cinchFront = float(cinchFront)
        self.woodOnly = woodOnly
        
    def __str__(self) -> str:
        """Outputs string representation of FloorKit method."""
        return str("Floor Kit: " + self.name + "\n" + "Length in feet: " + "%.2f" % self.length + " feet\n" + "Load height with straps cinched, 4 kits high: " + "\n"\
            + "  At back pillar: " + "%.2f" % self.cinchBack + " inches\n" + "  At middle pillar: " + "%.2f" % self.cinchMiddle + " inches\n" + "  At front pillar: " + \
                "%.2f" % self.cinchFront + " inches \n")

class Trailer(object):
    """Contains the methods for creating Trailer objects with attributes: trailer name, length in feet, height from base to top of pillar in inches,\
        from base to slant at top of pillar in inches, Boolean for presence of bulkhead, Boolean for presence of brackets, color notes, and \
            general notes. Also contains string method for Trailer object."""

    def __init__(self, name, length, pToTop, pToSlant, bulkhead=False, brackets=False, color=None, notes=None):
        """Runs and instantiates Trailer object."""
        self.name = str(name)
        self.length = float(length)
        self.pToTop = float(pToTop)
        self.pToSlant = float(pToSlant)
        self.bulkhead = bulkhead
        self.brackets = brackets
        self.color =str(color)
        self.notes = str(notes)

    def __str__(self) -> str:
        """Outputs string representation of Trailer object."""
        if self.bulkhead == True: #selection statment replaces Boolean value with user interpretable string
            bulkhead = "Yes"
        else:
            bulkhead = "No"
        if self.brackets == True: #selection statment replaces Boolean value with user interpretable string
            brackets = "Yes"
        else:
            brackets = "No"
        return str("Trailer name: " + self.name + "\n" + "Length in feet: " + "%.2f" % self.length + " feet\n" + "Pillar height: " + "\n"\
            + "  Base to beginning of top slant: " + "%.2f" % self.pToSlant + " inches\n" + "  Base to top: " + "%.2f" % self.pToTop + " inches\n" + \
                "Bulkhead? " + bulkhead + "\n" + "Brackets? " + brackets + "\n" + "Color: " + self.color \
                    + "\n" + "Extra notes : " + self.notes + "\n")





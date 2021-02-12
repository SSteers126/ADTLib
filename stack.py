# This Repo is going to show implementations of different ADT's

# Prerequisites and class for stack implementation

class StackError(Exception):
    """Attributes:
        args[0] = Error Message
        args[1] = Issue (Add/Remove)
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.issue = args[1]
        else:
            self.message = None
            self.issue = None

        if self.issue == 0:
            self.issue = "Add"
        elif self.issue == 1:
            self.issue = "Remove"
        else:
            raise DataError

    def __str__(self):
        if self.message:
            return "StackError, Failed to {0}, message: {1}".format(self.issue, self.message)
            # raise
        else:
            return "StackError, has been raised."
            # raise


class DataError(Exception):
    pass

# This class essentially uses a list as inside storage, and adds functions to make it act as a stack.
# You could directly edit the list, but this makes the entire use of the class pointless.

class Stack:
    """Stack ADT. data type is based on the type of data input, or alternatively "string", "integer", "float", or "boolean"."""

    def __init__(self, data_type="string"):
        self.temp = []
        if data_type == "string" or data_type == "str":
            self.data_type = str
        elif data_type == "integer" or data_type == "int":
            self.data_type = int
        elif data_type == "float" or data_type == "double":
            self.data_type = float
        elif data_type == "boolean" or data_type == "bool":
            self.data_type = bool
        elif data_type == "list" or data_type == "array":
            self.data_type = list
        elif data_type == "tuple":
            self.data_type = tuple
        else:
            self.data_type = type(data_type)  # In the case we don't find a suitable string, we use the type of what they put in as the datatype to use (i.e putting in 0.5 would make it float)

        self.vals = []

    def push(self, value):
        try:
            if type(value) != self.data_type:
                raise DataError("Incorrect data type added.")
            self.vals.insert(0, value)
        except StackError:
            raise StackError("Failed to add %s" % value, 0)
        except DataError:
            raise DataError("Incorrect data type added.")

    def pop(self):
        try:
            removed = self.vals[0]
            self.vals.remove(removed)
            return removed
        except:
            raise StackError("Failed to remove value.", 1)

    def peek(self):
        try:
            return self.vals[0]
        except:
            return None  # Returns none if the list is empty

    def isEmpty(self):
        if len(self.vals) == 0:
            return True
        else:
            return False

    def pop_all(self, recursed=False):
        try:
            if self.temp != [] and recursed == False:
                self.temp = []
            return self.pop_all(self.temp.append(self.pop()), True)  # Recursively popping all items. It is worth noting that python is smart anough to put everything in a list.
        except:
            return self.temp  # This ends the loop by waiting for the list in the stack to empty, because then self.vals[0] throws an error, which is caught and then used to work out when it is done.

    def length(self):
        return len(self.vals)

    def temp_purge(self):
        self.temp = []
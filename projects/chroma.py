# MCS 275 Spring 2021 Project 3 Solution
# David Dumas

# Project description:
# https://www.dumas.io/teaching/2021/spring/mcs275/nbview/projects/project3.html

"""Classes for working with chromaticities (r,g,b tuples that sum to 255)
mappings from chromaticities to names."""


class Chroma:
    """A chromaticity (r,g,b tuple summing to 255)"""

    def __init__(self, r, g, b):
        """Initialize chromaticity with red component r, green component g, and
        blue component b."""
        self.r = r
        self.g = g
        self.b = b
        if self.r+self.g+self.b != 255:
            raise ValueError("r+g+b must equal 255")
        if min(self.r, self.g, self.b) < 0:
            raise ValueError("r,g,b must be nonnegative")

    def __repr__(self):
        """Unambiguous string representation of a chromaticity"""
        # This method was NOT required
        return str(self)

    def __str__(self):
        """Human-readable string representation of a chromaticity"""
        # This method was NOT required
        return "Chroma({},{},{})".format(self.r, self.g, self.b)

    def more_red_than(self, other):
        """Is this chromaticity more red than `other`?"""
        return self.r > other.r

    def more_green_than(self, other):
        """Is this chromaticity more green than `other`?"""
        return self.g > other.g

    def more_blue_than(self, other):
        """Is this chromaticity more blue than `other`?"""
        return self.b > other.b

    def __eq__(self, other):
        """Equality of chromaticities means equality of
        r, g, and b components"""
        # We choose to make a `Chroma` compare as unequal to anything that is
        # not an instance of `Chroma`, but that behavior is not required in the
        # project description or autograder.
        if not isinstance(other, Chroma):
            return False
        return self.r == other.r and self.b == other.b and self.g == other.g


class ChromaNode:
    """Node object for a tree of chromaticity-name pairs"""

    def __init__(self, key, name, red=None, green=None, blue=None, parent=None):
        """Initialize a node with a given key (a `Chroma` object), name (string),
        and optional parent and child nodes."""
        self.red = red      # red child
        self.green = green  # green child
        self.blue = blue    # blue child
        self.parent = parent
        self.name = name
        self.key = key
        # NOTE: The occasional confusion I saw between `ChromaNode.red` (the red
        # child, `ChromaNode`) and `Chroma.r` (an integer) probably means that
        # better names for the child attributes would be red_child, green_child,
        # blue_child.

    def __repr__(self):
        """Unambiguous string representation"""
        # This method was NOT required
        return str(self)

    def __str__(self):
        """Human-readable string representation"""
        # This method was NOT required
        return "ChromaNode({},{},{},{})".format(
            self.key.r,
            self.key.g,
            self.key.b,
            self.name
        )

    def set_red(self, other):
        """Make `other` the red child of this node"""
        self.red = other
        other.parent = self

    def set_green(self, other):
        """Make `other` the green child of this node"""
        self.green = other
        other.parent = self

    def set_blue(self, other):
        """Make `other` the blue child of this node"""
        self.blue = other
        other.parent = self

    def nodes_in_subtree(self):
        """Return the total number of nodes in the subtree that has this node as
        its root."""
        # This method was NOT required, but is used by `ChromaTree.__len__` and
        # hence is an essential part of the implementation of a required method.
        
        # The number of nodes is of course
        #   1 + nodes in red subtree
        #     + nodes in green subtree
        #     + nodes in blue subtree
        # But we can't call .nodes_in_subtree on None so we test for existence
        # of each child as we add to the count of nodes.

        count = 1  # for this node
        for x in (self.red, self.green, self.blue):
            if x:
                count += x.nodes_in_subtree()
        return count

    def depth_in_nodes(self):
        """Return the length, measured in NODES, of the longest descending path
        from this node."""
        # This method was NOT required, but is used by `ChromaTree.depth` and
        # hence is an essential part of the implementation of a required method.

        # The depth is 1+max(depth of red child,
        #                    depth of green child,
        #                    depth of blue child)
        # But similar to nodes_in_subtree, some of the children may be None,
        # meaning we can't call .depth_in_nodes on them unconditionally. Here we
        # use a list comprehension with a filter to get the child depths.  A
        # helper function could also be created to return 0 if called on None.
        child_depths = [
            x.depth_in_nodes()
            for x in (self.red, self.green, self.blue)
            if x != None
        ]  # NOTE: The line breaks in the list comprehension are totally optional

        return 1+max(child_depths, default=0)
        # The `default` kwarg indicates what max() should give if the iterable
        # is empty.  We didn't cover this in lecture, so a natural way to do the
        # same thing without that construction would be:
        #     max([0]+child_depths)


class ChromaTree:
    """Search tree of ChromaNode objects.  For each node, the keys in the
    subtree of its red child all have larger r component, the keys in the
    subtree of its green child all have larger g component, and the keys in the
    subtree of its blue child all have larger b component."""

    def __init__(self):
        """Create a new empty tree"""
        self.root = None

    def __len__(self):
        """Return total number of nodes"""
        if self.root == None:
            return 0
        return self.root.nodes_in_subtree()

    def depth(self):
        """Depth measured in EDGES"""
        if self.root == None:
            return 0
        return self.root.depth_in_nodes()-1

    def search(self, key):
        """Locate node with given key, or return None if no such node exists."""
        # This is just a wrapper around the actual recursive implemention,
        # _search, making it start at the root node.
        return self._search(key, base=self.root)

    def _search(self, key, base):
        """Look for a node with key `key` in the subtree with `base` as its root
        and return it, or return None if no such node exists.  The argument
        `base` can also be None, which is understood to mean that we search the
        empty tree (thus returning None)."""
        # NOTE:
        #  1) This could be done recursively or iteratively.  We choose to do it
        #     recursively, which leads to somewhat simpler code.
        #  2) We use a method that will find the key in *any* tree that obeys the
        #     chromaticity tree definition, even if it was built using a key
        #     insertion strategy different than the two that are supported by
        #     the `insert` method (i.e. `dir` 0 and 1).  This decouples the two
        #     methods without complicating either one, so it seems like a good idea.

        if base == None:
            # Empty subtree, so key is not found
            return None

        if key == base.key:
            # This is the node we're looking for.
            return base

        # At this point, `base` is a node, but it isn't the one we want.  We
        # should determine which subtrees might contain the key, and search each
        # of them, stopping as soon as we find something.

        if key.more_red_than(base.key):
            # key may be in the red subtree
            res = self._search(key, base.red)
            # if found there, return it now. Otherwise, continue searching
            if res != None:
                return res

        if key.more_green_than(base.key):
            # key may be in the green subtree
            res = self._search(key, base.green)
            # if found there, return it now. Otherwise, continue searching
            if res != None:
                return res

        if key.more_blue_than(base.key):
            # key may be in the blue subtree
            res = self._search(key, base.blue)
            # if found there, return it now. Otherwise, continue searching
            if res != None:
                return res

        # We searched every subtree where the node might be, and found nothing.
        # So the key is not present.
        return None

    def insert(self, node, dir=0):
        """Insert the ChromaNode object `node` into the search tree. The flag
        `dir` indicates the order of preference of subtrees in which to insert
        the node. If `dir` is 0, they are considered in the order red, green,
        blue.  Otherwise, they are considered in the order blue, green, red."""

        # NOTE:
        # 1) dir is also the name of a built-in Python function, and in
        #    retrospect this was not a good chocse for theargument name!
        # 2) This mtehod could be implemented recursively or iteratively.  We
        #    choose to do it iteratively in this solution set.

        # The insert algorithm is very similar to the case of a BST, where we
        # keep passing to children according to key comparisons, stopping when
        # we reach a missing child (None).

        # In the BST implementation we discussed, after the loop we did some
        # further comparisons to check whether the node should be added as a
        # left or right child of the last actual node we visited.  We could do
        # that here, but it would be a little longer due to the `dir` flag and
        # the number of children.

        # Instead, we take a slightly different approach.  Every time we pass
        # from a node to one of its children (which might be None), we also keep
        # track of the function which would add a new child in the place of the
        # one we are moving to.  So if that child turns out to be missing, we
        # have the function (a .set_red, .set_green, or .set_blue method)
        # available to add the node in the proper place.

        prev = None
        cur = self.root
        set_child = None  # will store the function to add the node as the proper child
        while cur != None:
            # First, move `prev` down.
            prev = cur

            # Now move `cur` down, deciding which branch to take based on key
            # comparisons:
            if dir == 0:
                if node.key.more_red_than(prev.key):
                    cur = prev.red
                    set_child = prev.set_red
                elif node.key.more_green_than(prev.key):
                    cur = prev.green
                    set_child = prev.set_green
                elif node.key.more_blue_than(prev.key):
                    cur = prev.blue
                    set_child = prev.set_blue
            else:
                if node.key.more_blue_than(prev.key):
                    cur = prev.blue
                    set_child = prev.set_blue
                elif node.key.more_green_than(prev.key):
                    cur = prev.green
                    set_child = prev.set_green
                elif node.key.more_red_than(prev.key):
                    set_child = prev.set_red
                    cur = prev.red

        if prev == None:
            # self.root was None, so set it to node and we're done.
            self.root = node
            return

        # If we get here, then self.root was not None, so we took at least one
        # step down into the tree and stored a function in set_child. We call it
        # here to link `node` into the tree.
        set_child(node)
        # NOTE: The previous line actually decodes to exactly one of these three
        # statements:
        #     prev.set_red(node)
        #     prev.set_green(node)
        #     prev.set_blue(node)
        # depending on which branch we took in the conditionals inside the last
        # loop iteration.


class ChromaNameMapping:
    """Mapping from `Chroma` keys to names, using a `ChromaTree` as the backing
    data structure."""

    def __init__(self):
        """Initialize empty mapping"""
        self.T = ChromaTree()

    def __setitem__(self, c, name):
        """Set a key"""
        self.T.insert(ChromaNode(key=c, name=name))

    def __getitem__(self, c):
        """Get a key"""
        x = self.T.search(c)
        if x == None:
            raise KeyError("{} not found".format(c))
        return x.name

    def __len__(self):
        """Number of keys"""
        # NOTE: This required method was inadvertently left out of the
        # autograder tests.
        if self.T == None:
            return 0
        return len(self.T)

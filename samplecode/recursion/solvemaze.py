"""Solve a maze by depth first search"""
# MCS 275 Spring 2021 Lecture 15

def solvemaze(M,path=None):
    """Solve the maze `M` by continuing path `path`"""
    # Initialize the path with starting point if none
    # is given
    if path == None:
        path = [ M.start ]
    print("Path under consideration:",path)
    # Check whether we have already found a solution
    if path[-1] == M.goal:
        return path
    # Get current position
    x,y = path[-1]
    for next_step in M.free_neighbors(x,y):
        if next_step in path:
            # This would be backtracking; don't do it!
            continue
        solution = solvemaze(M,path + [next_step])
        if solution != None:
            # recursive call succeeded, so we return
            # the solution that it found to our caller
            return solution
    # path is a total dead end; indicate that to our called
    return None

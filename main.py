from gameoflife import width, height, stage, print_stage, count_neighbors

# initialize, stage set up
def init_stage(stage):
    for v_pos in range(0, height):
      for h_pos in range(0, width):
        if h_pos == 1:
          stage[v_pos][h_pos] = True
        else:
          stage[v_pos][h_pos] = False

# Generation Rules:
# 1. Any live cell with < 2 neighbors dies
# 2. Any live cell with 2-3 neighbors lives
# 3. Any live cell with > 3 neighbors dies
# 4. Any dead cell with 3 neighbors comes alive

# TODO: update alive and dead cells, turn cells on and off
# INPUT: stage -> data type
# OUTPUT: update stage
def one_generation(stage):
    # 2. logic error - not printing update/2nd generation stage
    # solution: copy stage object
    # create a copy, row by row, appending each row
    stage_copy = []
    for v_pos in range(len(stage)):
        new_row = []
        for h_pos in range(len(stage[0])):
            new_row.append(stage[v_pos][h_pos])
        stage_copy.append(new_row)

    # 1. TypeError: object of type 'int' has no len() -- error in for loop below
    # for h_pos in range(len(v_pos)):
    # solution: change len input to stage[0], which accesses inner list
    for v_pos in range(len(stage)):
        for h_pos in range(len(stage[0])):
            neighbors = count_neighbors(stage_copy, v_pos, h_pos)
            if not stage[v_pos][h_pos] and neighbors == 3:
            # if item/cell not False AND has 3 neighbors, cell turns True
                stage[v_pos][h_pos] = True
            elif stage[v_pos][h_pos] and neighbors < 2:
                stage[v_pos][h_pos] = False
            elif stage[v_pos][h_pos] and (neighbors == 2 or neighbors == 3):
                stage[v_pos][h_pos] = True
            elif stage[v_pos][h_pos] and neighbors > 3:
                stage[v_pos][h_pos] = False

# create/initiliaze a stage
init_stage(stage)
print("First Generation:")
print_stage(stage)
# run generation
one_generation(stage)
# print again
print("Second Generation:")
print_stage(stage)


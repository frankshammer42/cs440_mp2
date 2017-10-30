from GameNode import Node
import game_utility
import time

# TODO: add parameter for H function offset
# TODO: add player and initial node
def minimax_tree_search(root_node, depth, player, heuristic):
    depth_0_node = [root_node]
    nodes_by_depth = {}
    nodes_by_depth[0] = depth_0_node

    for i in range(1,depth+1):
        # print nodes_by_depth
        if player == 'B':
            if i%2 == 1:
                side = 'B'
            else:
                side = 'W'
        else:
            if i%2 == 1:
                side = 'W'
            else:
                side = 'B'
        nodes_to_expand = nodes_by_depth[i-1]
        children_nodes = []
        for j in range(len(nodes_to_expand)):
            node = nodes_to_expand[j]
            # print node
            expanded_children = game_utility.get_minimax_children(node, side)
            children_nodes += expanded_children
        nodes_by_depth[i] = children_nodes

    game_utility.calculate_depth_n(nodes_by_depth, heuristic, player, depth)
    game_utility.populate_value(nodes_by_depth, player, depth)
    root_value = nodes_by_depth[0][0].value

    total_number_of_nodes = 0
    for key in nodes_by_depth:
        total_number_of_nodes += len(nodes_by_depth[key])
    # print root_value
    # print "its frist floor values are"
    # for node in nodes_by_depth[1]:
    #     print node.value
    next_node = game_utility.get_node_by_value(nodes_by_depth[1], root_value)
    return next_node, total_number_of_nodes


# TODO: add parameter for H function
# TODO: add player and initial node


#Doing 3 up B down W (92,97)
#Doing 4 up W down B (92,97)
def alpha_beta_tree_search(root_node,depth, player, heuristic, off_or_def):
    depth_0_node = [root_node]
    nodes_by_depth = {}
    nodes_by_depth[0] = depth_0_node

    for i in range(1,depth+1):
        children_nodes = []
        side = ''
        pruning_value = 0
        if player == 'B':
            if i%2 == 1:
                side = 'B'
            else:
                side = 'W'
        else:
            if i%2 == 1:
                side = 'W'
            else:
                side = 'B'
        if i == depth:
            nodes_to_expand = nodes_by_depth[i-1]

            # first_node_children = game_utility.get_minimax_children(first_node, side)
            # children_nodes += first_node_children
            max_or_min = 0
            if side == 'B':
                max_or_min = 1
            else:
                max_or_min = 0

            if side == 'B':
                pruning_value = 99999
            else:
                pruning_value = 0

            # pruning_value = first_node.value
            for j in range (0,len(nodes_to_expand)):
                pruned_children = None
                node_to_expand = nodes_to_expand[j]
                if side == 'B':
                    pruned_children, branch_temp_min = game_utility.get_alpha_children(node_to_expand, side, pruning_value, heuristic)
                    if branch_temp_min > pruning_value:
                        pruning_value = branch_temp_min
                    children_nodes += pruned_children
                if side == 'W':
                    pruned_children, branch_temp_max = game_utility.get_beta_children(node_to_expand, side, pruning_value, heuristic)
                    if branch_temp_max < pruning_value:
                        pruning_value = branch_temp_max
                    children_nodes += pruned_children
            nodes_by_depth[i] = children_nodes
        else:
            nodes_to_expand = nodes_by_depth[i-1]
            for j in range(0,len(nodes_to_expand)):
                node = nodes_to_expand[j]
                expanded_children = game_utility.get_minimax_children(node, side)
                children_nodes += expanded_children
            nodes_by_depth[i] = children_nodes

            # if i == 1:
            #     for node in nodes_by_depth[1]:
            #         print node.value
            #     print "---------------------------------"
            #     for child_node in nodes_by_depth[0][0].children:
            #         print child_node.value





    game_utility.calculate_depth_n(nodes_by_depth, heuristic, player, depth)
    game_utility.populate_value(nodes_by_depth, player, depth)
    root_value = nodes_by_depth[0][0].value

    total_number_of_nodes = 0
    for key in nodes_by_depth:
        total_number_of_nodes += len(nodes_by_depth[key])







    # print root_value
    # print "its frist floor values are for alpha pruning"
    # for node in nodes_by_depth[1]:
    #     print node.value
    # print "its children value"


    next_node = game_utility.get_node_by_value(nodes_by_depth[1], root_value)
    return next_node, total_number_of_nodes



def main():
    init_board = game_utility.create_init_board()
    current_node = Node(init_board)
    player_flag = 0
    side = 'B'
    start_time = time.time()
    total_number_of_nodes_black = 0
    total_number_of_nodes_white = 0
    black_number_of_moves = 0
    white_number_of_moves = 0
    black_time = 0.0
    white_time = 0.0
    while not game_utility.goal_chess_board(current_node):
        if player_flag%2 == 0:
            side = 'B'
        else:
            side = 'W'

        # print "Current player is " + side
        # print current_node.print_board()
        # print "----------------------------"
        if side == 'B':
            # current_node, expanded_nodes_number = alpha_beta_tree_search(current_node, 4, side, game_utility.calculate_block_num_defensive,0)
            move_start_time = time.time()
            current_node, expanded_nodes_number = minimax_tree_search(current_node, 3, side, game_utility.offensive_heuristic)
            black_time += time.time() - move_start_time
            total_number_of_nodes_black += expanded_nodes_number
            current_board = current_node.chess_board
            current_node = Node(current_board)
            black_number_of_moves += 1
        else:
            move_start_time = time.time()
            current_node, expanded_nodes_number = alpha_beta_tree_search(current_node, 4, side, game_utility.offensive_heuristic, 1)
            white_time += time.time() - move_start_time
            total_number_of_nodes_white += expanded_nodes_number
            #print current_node.value
            #current_node = alpha_beta_tree_search(current_node, 4, side, game_utility.offensive_heuristic, 1)
            current_board = current_node.chess_board
            current_node = Node(current_board)
            white_number_of_moves += 1

        print current_node.print_board()
        print "\n\n"
        player_flag += 1

    spend_time = time.time() - start_time
    white_captures, black_captures = game_utility.get_number_of_captured(current_node.chess_board)
    print "Spend " + str(time.time()-start_time) + "seconds"

    print "Black expanded " + str(total_number_of_nodes_black) + " nodes"
    print "White expanded " + str(total_number_of_nodes_white) + " nodes"

    print "Black's total number of moves is " + str(black_number_of_moves)
    print "White's total number of moves is " + str(white_number_of_moves)

    print "Black expanded " + str(total_number_of_nodes_black/float(black_number_of_moves)) + " number of nodes expanded per move"
    print "White expanded " + str(total_number_of_nodes_white/float(white_number_of_moves)) + " number of nodes expanded per move"

    print "Black spends " + str(black_time/float(black_number_of_moves)) + " seconds per move"
    print "White spends " + str(white_time/float(white_number_of_moves)) + " seconds per move"

    print "White captures " + str(white_captures) + " black nodes"
    print "Black captures " + str(black_captures) + " white nodes"
    print side + " won the game"
    print current_node.print_board()



if __name__=='__main__':
    main()













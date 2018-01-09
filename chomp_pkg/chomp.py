from __future__ import print_function
from copy import deepcopy
from abc import ABCMeta, abstractmethod
import utils
import random
import chomp_pkg

logger = chomp_pkg.choco_chomp_logger


class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement
    legal_moves, make_move, utility, and terminal_test. You may
    override display and successors or you can inherit their default
    methods. You will also need to set the .initial attribute to the
    initial state; this can be done in the constructor."""

    # http://aima.cs.berkeley.edu/python/games.html
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_move(self, move):
        """Return the state that results from making a move from a state."""

    def terminal_test(self):
        """Return True if this is a final state for the game."""
        return not self.legal_moves()

    @abstractmethod
    def legal_moves(self):
        """
        This function provides the list of legal moves
        :return: legal_moves_ : list of legal moves
        """

    @abstractmethod
    def display(self):
        """
        This is a diplay function used to calculate the
        :return:
        """
        s = [[str(e) for e in row] for row in self.board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        logger.info('\n' + '\n'.join(table))

    @abstractmethod
    def utility(self):
        """
        This is heuristic function that provides the score for the game
        :return:
        """

    def successors(self):
        """Return a list of legal (move, state) pairs."""
        return list(set([(move, self.make_move(move)) for move in self.legal_moves()]))

    def __repr__(self):
        return '<%s>' % self.__class__.__name__


class Chomp(Game):
    """
    This class maintains the status of the game. This class inherits Game class and there are several abstract methods
    that we implement from Game
    For example. If we want to look save the previosly checked loops
    """

    def __init__(self, rows, columns, *players):
        """

        :param rows: number of rows our Chocolate has
        :param columns: number of columns our Chocolate has
        :param players: pass the parameters as a player1, player2 and they will be
        """
        logger.debug("Initializing Chomp class")
        if rows and columns and players:
            self.moves_cnt = 0
            self.rows = rows
            self.columns = columns
            self.players = players
            self.board = self.initialize_chocolate()
        else:
            logger.error("Invalid rows, columns, *players while initializing Chomp class,SyntaxError")
            raise SyntaxError("Please provide rows, columns, *players in the format 3,4,player1, player2 ")

    def initialize_chocolate(self):
        """
        This function initializes the chocolate with the first bit alone as poison.
        No exception needs to be handled as it handled in the class initialization phase
        :return: matrix -> Chocolate is identified as matrix here
        """
        logger.debug("Initializing chocolate for Chomp")
        matrix = [[utils.ChompConstants.CHOCOLATE_SWEET_VALUE for _ in range(self.columns)] for _ in range(self.rows)]
        matrix[0][0] = utils.ChompConstants.CHOCOLATE_POISON_VALUE
        return matrix

    def legal_moves(self):
        """
        This function provides the list of legal moves that has chocolate and not poison.
        This is achieved by depth first search
        :return: legal_moves_ : list of legal moves
        """
        legal_moves_ = []
        for col in range(self.columns):
            for row in range(self.rows):
                if self.board[row][col] == utils.ChompConstants.CHOCOLATE_SWEET_VALUE:
                    legal_moves_.append((row, col))
        return legal_moves_

    def display(self):
        """
        Source: Stackoverflow
        This is a diplay function used to calculate the
        :return None :
        """
        s = [[str(e) for e in row] for row in self.board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        logger.info('\n' + '\n'.join(table))

    def make_move(self, move):
        """ Applying a move to the game state. This will allow us to eat all the down/right pieces of chocolate
        :param move: move or chocolate bit that we want to select
        :param state:
        :return: state after making the desired legal move. This is different object from actual state passed
        """
        state = deepcopy(self)
        for i in range(move[1], state.columns):
            for j in range(move[0], state.rows):
                state.board[j][i] = '.'
        state.moves_cnt += 1
        return state

    def utility(self):
        """
        This function changes sign with respect to the which player is playing the game.
        1st player always wants to maximize the winning score
        :return: The utils value (Heuristic function)
        """
        if self.moves_cnt % 2 == 1:
            return self.utils()
        else:
            return -self.utils()

    def utils(self):
        """ Return value of game position from the point of view the
            player whose turn it is to move.
             value > 0 means winning,
             value < 0 means losing, and
             larger  is better. """
        # win_value is a positive number which is larger earlier in the game,
        # so that the algorithm chooses earlier wins over later wins.
        return self.columns * self.rows - self.moves_cnt
        # if self.terminal_test():
        #     return win_value
        # else:
        #     return 0


class Player:
    """
    This class consists of player indices
    We do not need class for this.I have implemented just so that we can add more properties for
    each player in future.
    """

    def __init__(self, index, player_type):
        logger.debug("Initializing player class for %s", player_type)
        self.player_cnt = index
        self.player_type = player_type

    def get_move(self, game):
        logger.debug("Obtaining step for the  player %s", self.player_type)
        if self.player_type == utils.ChompConstants.ALPHABETA_PLAYER:
            return alphabeta_search(game)
        elif self.player_type == utils.ChompConstants.ACTUAL_PLAYER:
            print("please enter an input", game.legal_moves())
            line = raw_input()
            try:
                move=(int(line.split(',')[0]), int(line.split(',')[1]))
                return move, None
            except IndexError:
                print ("please enter the move in the format 1,2")
                return self.get_move(game=game)


        elif self.player_type == utils.ChompConstants.MINIMAL_STEP_PLAYER:
            logger.debug("Obtaining unique step for minimal step player")
            for move in game.legal_moves():
                counter = 0
                for j in range(move[1], game.columns):
                    for i in range(move[0], game.rows):
                        if game.board[i][j] == utils.ChompConstants.CHOCOLATE_SWEET_VALUE:
                            counter += 1
                if counter == 1:
                    logger.debug("The unique step for minimal step player is %s", move)
                    return move, None
            logger.error("Unable to find the minimalstep for player %ss ", move)
            raise NotImplemented("Minimal Step Player Crashed: Please fix it!!")
        elif self.player_type == utils.ChompConstants.RANDOM_PLAYER:
            return random.choice(game.legal_moves()), None
        else:
            # TODO:WE NEED TO HAVE ALL THE EXCEPTIONS IN A SEPARATE FILE
            raise Exception("Invalid_Player_Exception")
        return None


def play(rows, columns, *players):
    """
    :param rows: number of rows in chocolate
    :param columns: number of columns in chocolate
    :param players: Players in the way player A , Player B
                    these should be passed using utils.ChompConstants.*PLAYER
    :return: player.player_type :The name of final winner

    Note:
    we are not checking for rows, columns, *players as the exceptions are handled in State Class
    """
    logger.info(
        "\n----------------------------------------------------------------------------------------------------\n")
    logger.info("Starting the game with players %s", players)

    game = Chomp(rows, columns, *players)
    players_objs = [Player(i, players[i]) for i in range(0, len(players))]
    moves = []
    # This is unconditional loop as we want our players to loop until the game ends
    while True:
        for player in players_objs:
            logger.info("player %s is about to play", player.player_type)
            action, value = player.get_move(game)
            logger.info("player %s is eating %s ", player.player_type, action)
            if not action:
                logger.error("Unable to get the next move: System Crashed while %s playing", player.player_type)
                raise Exception("Unable to Get next move: System Crashed")
            game = game.make_move(action)
            moves.append(action)
            game.display()
            if game.terminal_test():
                logger.info("No more moves left for the other player than to eat the poison. %s won",
                            player.player_type)
                # Required to execute the tests. Do not remove this
                print(moves, end='')
                return player.player_type,moves


def alphabeta_search(game, d=4):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function.
    :return action -> This  is the best possible action for our computer to win
    """

    logger.info("Starting alpha beta pruning to find the best possible player")

    def max_value(state_max, alpha, beta, depth):
        logger.debug("Finding max value alpha: %s beta:%s depth: %s", alpha, beta, depth)
        if depth > d or state_max.terminal_test():
            return state_max.utility()
        v = -utils.inf
        for (a, s) in state_max.successors():

            logger.debug("Finding max of min value in successors alpha: %s beta:%s depth: %s move: %s", alpha, beta,
                         depth, a)
            v = max(v, min_value(s, alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state_min, alpha, beta, depth):
        logger.debug("Finding min value alpha: %s beta: %s depth: %s", alpha, beta, depth)
        if depth > d or state_min.terminal_test():
            return state_min.utility()
        v = utils.inf
        for (a, s) in state_min.successors():
            logger.debug("Finding min of max value in successors alpha: %s beta:%s depth: %s move: %s", alpha, beta,
                         depth, a)
            v = min(v, max_value(s, alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Getting the utility function as well just in case if I need it in future
    (action, state), value = utils.argmax(game.successors(), lambda ((a, s)): min_value(s, -utils.inf, utils.inf, 0))
    return action, value

import random

PRUNEDEPTH = 4
MAXSIZE = float(9223372036854775807)
MINSIZE = -float(9223372036854775807)


class Player:
    def __init__(self, isFirst, array):
        """Initialization

        :param isFirst: who the player is
        :type isFirst: bool
        :param array: the random sequence given at the start of the game
        :type array: Tuple[int]
        """
        self.isFirst = isFirst
        self.array = array
        self.bestMove = None

    def output(self, currentRound, board, mode):
        """Decision made by the player

        :type currentRound: int
        :type board: Chessboard
        :param mode: What is the player supposed to do:
            can be "direction", "position", "_direction", "_position".
        :type mode: str
        """

        if self.isFirst:
            if mode == 'position':
                bestMove = self.__alphabeta(board, 0, MINSIZE, MAXSIZE, currentRound)
                return bestMove
            elif mode == 'direction':
                bestMove = self.__alphabeta(board, 2, MINSIZE, MAXSIZE, currentRound)
                return bestMove
            else:
                return

        elif not self.isFirst:
            if mode == 'position':
                bestMove = self.__alphabeta(board, 1, MINSIZE, MAXSIZE, currentRound)
                return bestMove
            elif mode == 'direction':
                bestMove = self.__alphabeta(board, 3, MINSIZE, MAXSIZE, currentRound)
                return bestMove
            else:
                return

    def __alphabeta(self, board, phase, alpha, beta, currentRound, depth=0):
        """Alpha-beta pruning method.

        :param board: Chessboard class
        :param phase: current phase, can be 0-3.
                        0, 1 and 2, 3 corresponds to "position" and "direction" respectively;
                        0, 2 are first person's turn, whereas 1, 3 are second person's turn.
        :param depth:
        :return: int
        """

        newBoard = board.copy()
        directionList = [0, 1, 2, 3]
        bestMove = None

        if depth == PRUNEDEPTH:  # 遇到叶节点的结束条件
            value = self.__evaluate(board)
            return value

        if self.isFirst:  # 己方为先手，主导 phase 0, 2
            if phase == 0:  # position for us
                bestMove = newBoard.getNext(self.isFirst, currentRound)
                if bestMove != ():  # 己方棋盘未满
                    newBoard.add(self.isFirst, bestMove)
                    value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)
                    if value is not None and value > alpha:
                        alpha = value

                elif newBoard.getNone(not self.isFirst):  # 己方棋盘满了，到对方棋盘下棋
                    posList = newBoard.getNone(not self.isFirst)

                    for pos in posList:
                        newBoard = board.copy()
                        newBoard.add(not self.isFirst, pos)
                        value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)

                        if value is not None:
                            bestMove = pos
                            if value > alpha:
                                alpha = value
                                if alpha >= beta:
                                    break

                else:  # 己方、对方的期盘都满了而无法下棋，跳过下棋回合
                    value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)
                    if value is not None and value > alpha:
                        alpha = value

                if depth == 0 and bestMove is not None:
                    return bestMove

                return alpha

            elif phase == 1:  # position for enemy
                bestMove = newBoard.getNext(not self.isFirst, currentRound)
                if bestMove != ():
                    newBoard.add(not self.isFirst, bestMove)
                else:
                    posList = newBoard.getNone(self.isFirst)
                    if posList:
                        bestMove = random.choice(posList)
                        newBoard.add(self.isFirst, bestMove)

                # 需要增添负数的原因，见链接
                value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)

                if value is not None and value > alpha:
                    alpha = value

                return alpha

            elif phase == 2:  # direction for us
                for direction in directionList:
                    value = None
                    newBoard = board.copy()
                    if newBoard.move(self.isFirst, direction):  # 可进行合并
                        value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)

                    if value is not None and value > alpha:
                        alpha = value
                        bestMove = direction
                        if alpha >= beta:
                            break

                if depth == 0 and bestMove is not None:
                    return bestMove

                return alpha

            elif phase == 3:  # direction for enemy
                for direction in directionList:
                    value = None
                    newBoard = board.copy()
                    if newBoard.move(not self.isFirst, direction):
                        # 需要增添负数的原因，见链接
                        value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound + 1, depth + 1)

                    if value is not None and value > alpha:
                        alpha = value
                        if alpha >= beta:
                            break

                return alpha

        # ------------------------------------------------------ #
        elif not self.isFirst:  # 己方为后手，主导 phase 1, 3
            if phase == 0:  # position for enemy
                bestMove = newBoard.getNext(not self.isFirst, currentRound)
                if bestMove != ():
                    newBoard.add(not self.isFirst, bestMove)
                else:
                    posList = newBoard.getNone(self.isFirst)
                    if posList:
                        bestMove = random.choice(posList)
                        newBoard.add(self.isFirst, bestMove)

                # 需要增添负数的原因，见链接
                value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)

                if value is not None and value > alpha:
                    alpha = value

                return alpha

            elif phase == 1:  # position for us
                bestMove = newBoard.getNext(self.isFirst, currentRound)
                if bestMove != ():  # 己方棋盘未满
                    newBoard.add(self.isFirst, bestMove)
                    value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)
                    if value is not None and value > alpha:
                        alpha = value

                elif newBoard.getNone(not self.isFirst):  # 己方棋盘满了，到对方棋盘下棋
                    posList = newBoard.getNone(not self.isFirst)

                    for pos in posList:
                        newBoard = board.copy()
                        newBoard.add(not self.isFirst, pos)
                        value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)

                        if value is not None:
                            bestMove = pos
                            if value > alpha:
                                alpha = value
                                if alpha >= beta:
                                    break

                else:  # 己方、对方的期盘都满了而无法下棋，跳过下棋回合
                    value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)
                    if value is not None and value > alpha:
                        alpha = value

                if depth == 0 and bestMove is not None:
                    return bestMove

                return alpha

            elif phase == 2:  # direction for enemy
                for direction in directionList:
                    value = None
                    newBoard = board.copy()

                    if newBoard.move(not self.isFirst, direction):  # 可进行合并
                        # 需要增添负数的原因，见链接
                        value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound, depth + 1)

                    if value is not None and value > alpha:
                        alpha = value
                        if alpha >= beta:
                            break

                return alpha

            elif phase == 3:  # direction for us
                for direction in directionList:
                    value = None
                    newBoard = board.copy()

                    if newBoard.move(self.isFirst, direction):  # 可进行合并
                        # 需要增添负数的原因，见链接
                        value = -self.__alphabeta(newBoard, (phase + 1) % 4, -beta, -alpha, currentRound + 1, depth + 1)

                    if value is not None and value > alpha:
                        alpha = value
                        bestMove = direction
                        if alpha >= beta:
                            break

                if depth == 0 and bestMove is not None:
                    return bestMove

                return alpha

    def __evaluate(self, board):
        """
        各指标的定义：（棋子的级别：棋子取以2为底的对数）

        max_num_value：我方棋盘最大棋子级别-对方棋盘最大棋子级别

        empty_num_value：我方空位数-对方空位数

        smoothness_num_value：对方平滑指数-我方平滑指数（保证该指数越大越平滑）
        对于任意一枚棋子a，它的平滑指数定义为a和与它相邻的所有棋子的级别差的绝对值之和。
        某方的平滑指数指的是某方所有棋子的平滑指数的和。
        “相邻”定义为在某个方向（上下左右）上最近的棋子（如果最近的棋子是墙壁或对方棋子，则该方向上不存在相邻棋子）
        寻找相邻棋子由get_near函数实现。

        iso_value：孤立棋子，对方孤立棋子数-我方孤立棋子数
        孤立棋子定义为四个方向都不存在直接相邻（挨着的）棋子。
        """

        board = board.copy()
        bls = board.getRaw()

        def get_near(pos, direction):
            """
            该函数的功能：寻找某棋子在给定方向上的“相邻”棋子
            把空格跳过，遇到对手棋子和边界则返回None
            遇到本方棋子则返回该棋子的坐标（二元元组）
            pos：待判断格子的坐标，二元元组
            direction：待判断方向，int，0/1/2/3
            """
            r = pos[0]
            c = pos[1]
            move_row = [-1, 1, 0, 0]
            move_column = [0, 0, -1, 1]
            belong = bls[r][c][1]

            current_pos = pos
            while True:
                # 向特定方向移动一步
                current_pos = current_pos[0] + move_row[direction], current_pos[1] + move_column[direction]

                if (current_pos[0] > 3 or current_pos[1] > 7 or current_pos[0] < 0 or current_pos[1] < 0) \
                        or bls[current_pos[0]][current_pos[1]][1] != belong:
                    return None
                else:
                    if bls[current_pos[0]][current_pos[1]][0] != 0:
                        return current_pos
                    else:
                        continue

        # 权重
        smoothWeight = 0.1
        emptyWeight = 2.7
        maxWeight = 1.0

        # 棋子最大值
        if board.getScore(self.isFirst):
            max_num_self = board.getScore(self.isFirst)[-1]
        else:
            max_num_self = 0
        if board.getScore(not self.isFirst):
            max_num_opponent = board.getScore(not self.isFirst)[-1]
        else:
            max_num_opponent = 0

        # 棋子最大值的估值：本方最大级别-对方最大级别
        max_num_value = max_num_self - max_num_opponent

        # 空位数
        empty_num_self = len(board.getNone(self.isFirst))
        empty_num_opponent = len(board.getNone(not self.isFirst))

        # 空位数的估值：本方空位数-对方空位数
        empty_num_value = empty_num_self - empty_num_opponent

        # 平滑性：遍历所有棋子，对于每个棋子，如果它存在相邻棋子，那么计算它与相邻棋子的对数差（取绝对值），然后加在一起，这就是平滑性的定义。
        smoothness_num_value = 0
        for row in range(4):
            for column in range(8):
                pos = (row, column)

                if bls[row][column][0] != 0:
                    for direction in range(4):
                        near = get_near(pos, direction)

                        if near:
                            # 对我方来说，差异越大越不平滑，平滑系数变小；反之亦然。
                            tmp = bls[row][column][1] == self.isFirst

                            # 1-2*tmp是把1映射到-1,0映射到1
                            smoothness_num_value += (1 - 2 * tmp) * abs(bls[row][column][0] - bls[near[0]][near[1]][0])

        # 两两成对，去除重复
        smoothness_num_value /= 2
        score = smoothWeight * smoothness_num_value + emptyWeight * empty_num_value + maxWeight * max_num_value
        return score

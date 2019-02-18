# https://leetcode.com/problems/word-search/submissions/
class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        num_of_row = len(board) - 1
        if num_of_row >= 0:
            num_of_col = len(board[0]) - 1
        N = len(word)

        def get_neigbours(row_pos, col_pos):
            neighbours = []
            if col_pos < num_of_col:
                neighbours.append((row_pos, col_pos+1))
            if col_pos > 0:
                neighbours.append((row_pos, col_pos-1))
            if row_pos < num_of_row:
                neighbours.append((row_pos+1, col_pos))
            if row_pos > 0:
                neighbours.append((row_pos-1, col_pos))
            return neighbours

        def exist(word, curr_row, curr_col, wrd_start, N, path):
            if wrd_start == N:
                return True
            if board[curr_row][curr_col] != word[wrd_start]:
                return False
            neighbours = get_neigbours(curr_row, curr_col)
            for neigbour in neighbours:
                if neigbour in path:
                    continue
                path.append(neigbour)
                is_exist = exist(
                    word, neigbour[0], neigbour[1], wrd_start+1, N, path)
                if is_exist:
                    return True
                path.pop()

            return N-1 == wrd_start

        for i in range(num_of_row + 1):
            for j in range(num_of_col + 1):
                path = [(i, j)]
                is_exist = exist(word, i, j, 0, N, path)
                if is_exist:
                    return True
        return False


assert(Solution().exist([["A", "B", "C", "E"], [
    "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
assert(Solution().exist([["a", "a"]], "aaa") == False)

assert(Solution().exist([["A", "B", "C", "E"],
                         ["S", "F", "E", "S"],
                         ["A", "D", "E", "E"]], "ABCESEEEFS"))

import java.util.Scanner;
public class TicTacToe {
    static char[] board = new char[9];
    static char player = 'X';

    public static void main(String[] args) {
        initializeBoard();
        printBoard();

        while (true) {
            int move = getMove();
            makeMove(move);
            printBoard();

            if (isGameOver()) {
                break;
            }

            switchPlayer();
        }

        declareWinner();
    }

    static void initializeBoard() {
        for (int i = 0; i < 9; i++) {
            board[i] = ' ';
        }
    }

    static void printBoard() {
        System.out.println("-------------");
        for (int i = 0; i < 9; i++) {
            System.out.print("| " + board[i] + " ");
            if (i % 3 == 2) {
                System.out.println("|");
                System.out.println("-------------");
            }
        }
    }

    static int getMove() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Player " + player + ", enter your move (1-9): ");
        int move = scanner.nextInt() - 1;
        while (move < 0 || move >= 9 || board[move] != ' ') {
            System.out.println("Invalid move. Try again.");
            move = scanner.nextInt() - 1;
        }
        return move;
    }

    static void makeMove(int move) {
        board[move] = player;
    }

    static boolean isGameOver() {
        // Check rows
        for (int i = 0; i < 9; i += 3) {
            if (board[i] != ' ' && board[i] == board[i + 1] && board[i] == board[i + 2]) {
                return true;
            }
        }

        // Check columns
        for (int i = 0; i < 3; i++) {
            if (board[i] != ' ' && board[i] == board[i + 3] && board[i] == board[i + 6]) {
                return true;
            }
        }

        // Check diagonals
        if (board[0] != ' ' && board[0] == board[4] && board[0]   
 == board[8]) {
            return true;
        }
        if (board[2] != ' ' && board[2] == board[4] && board[2] == board[6]) {
            return true;
        }

        // Check for   a draw
                              
        for (int i = 0; i < 9; i++) {
            if (board[i] == ' ') {
                return false;
            }
        }
        return true;
    }

    static void switchPlayer() {
        player = (player == 'X') ? 'O' : 'X';
    }

    static void declareWinner() {
        if (isGameOver() && board[0] != ' ') {
            System.out.println("Player " + player + " wins!");
        } else {
            System.out.println("It's a draw!");
        }
    }
}

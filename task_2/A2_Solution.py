import cv2
import numpy as np

def create_checkerboard(size, square_size):
    board = np.zeros((size * square_size, size * square_size), dtype=np.uint8)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                board[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size] = 255
    return board

# Parameters
board_size = 4  # 4x4 checkerboard
square_size = 100  # pixels
fps = 30
duration = 10  # seconds

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('checkerboard.mp4', fourcc, fps, (board_size * square_size, board_size * square_size))

board = create_checkerboard(board_size, square_size)

for frame_num in range(fps * duration):
    if (frame_num // fps) % 2 == 0:
        current_board = board
    else:
        current_board = cv2.bitwise_not(board)
    board_color = cv2.cvtColor(current_board, cv2.COLOR_GRAY2BGR)
    
    cv2.imshow("output", current_board)
    out.write(board_color)
    
    # Add a delay and check for 'q' key to exit
    if cv2.waitKey(100 // fps) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
print("Video created successfully!")
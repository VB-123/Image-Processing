import cv2
import numpy as np
import time
import random

def dino_game(score, obs_x, obs_y, dino_y, game_speed):
    line = np.zeros((500,500,3), dtype=np.uint8)
    line[:] = (255,255,255)

    cv2.putText(line,f"Score: {score}",(300,75),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0))
    cv2.putText(line,f"Speed: {game_speed}",(300,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0))

    # Draw ground
    cv2.line(line, (0, 400), (500, 400), (0,0,0), 2)

    # Draw obstacle
    cv2.rectangle(line, (obs_x, obs_y), (obs_x+20, 400), (0,0,0), -1)

    # Draw dino
    cv2.circle(line, (100, dino_y), 25, (0,0,0), -1)

    return line

def main():
    score = 0
    dino_y = 375  # Initial y position of dino
    obs_x = 500   # Initial x position of obstacle
    game_speed = 5
    jump_speed = 15
    is_jumping = False

    while True:
        frame = dino_game(score, obs_x, 375, dino_y, game_speed)
        cv2.imshow("Dino Game", frame)

        # Handle jumping
        if is_jumping:
            dino_y -= jump_speed
            jump_speed -= 1
            if dino_y >= 375:
                dino_y = 375
                is_jumping = False
                jump_speed = 15

        # Move obstacle
        obs_x -= game_speed
        if obs_x < 0:
            obs_x = 500
            score += 1
            if score % 10 == 0:
                game_speed += 1

        # Check for collision
        if 365 <= dino_y <= 375 and obs_x <= 125 <= obs_x + 20:
            cv2.putText(frame, "GAME OVER", (200,250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
            cv2.imshow("Dino Game", frame)
            cv2.waitKey(2000)
            break

        key = cv2.waitKey(1) & 0xFF
        if key == ord(' ') and not is_jumping:
            is_jumping = True
        elif key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":                                          
    main()
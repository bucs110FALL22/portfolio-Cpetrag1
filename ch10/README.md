Pygame

## List of Classes
* Runner - Displays board on screen with markers
* Board - Checks events in the game and runs the game

## Project Structure and File List
The project is broken down into the following structure:
  * main.py
  * src
    * runner class
    * board class
  * assets
    * TTTBoard.png
    * X.png
    * O.png
    * Owins.png
    * Xwins.png
  * etc
    * README.md

# Tasks and Responsibilities
Eva Okon - Wrote the original code. Ran and tested it to be sure everything was working.

Christian Petragnani - Improvised the code into classes so that the code matched the rubric. Also desinged all GUI pictures in a design software for gameplay.

# Testing
To test the code, we wrote a bit of code then ran it. We debugged errors and continued coding. To test the game, we made sure that two X's or O's couldn't be placed in the same cell. We then checked that the three combinations for winning worked.

# ATP
Step | Procedure | Expected Result
--- | --- | ---
1 | Run main.py | Board will appear on screen
2 | Click a cell on the screen | An "X" or "O" will appear in that cell
3 | Repeat step 2 until a player wins or there's a tie | A message will appear on screen saying which player won or there's a tie
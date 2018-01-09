[![CircleCI](https://circleci.com/gh/TejjeT/Choco_chomp.svg?style=svg)](https://circleci.com/gh/TejjeT/Choco_chomp)
## Chomp Problem:
  Designing a chomp as described https://en.wikipedia.org/wiki/Chomp with top left bit as poison

#### ENVIRONMENT:
    PYTHON:2.7
    TESTS: pytest
#### Installing Required packages:
    pip install -r requirements.txt

    
#### Solution:
 Please refer to the following image (Chomp.jpeg) for the Class diagram
 
 ![IMAGE](https://github.com/TejjeT/Choco_chomp/blob/master/chomp.jpeg) 
 
  
  The solution used alpha beta pruning approach (optimized version of minimax) to calculate all the possible moves
  of an existing state of the game and take a step based on the heuristic function(named as <b>utility</b> in our case).
  
  <b><u>Heuristic function</u></b>:
   <p>A function named utility is created to give the positive value if Player 1 wins and negative value if the
   (Player 1 is assumed always to be computer and we can add logic to take the input as who is playing 1st)
   player 2 wins. Player 1 and player 2 are calculated by using a variable with in the class called Chomp.
   This is always calculated when the terminal condition is satisfied i.e with the board has no legal moves
   and it is a winning condition for player 1 or player 2.</p>
   
   <b><u>Alpha Beta Search</u></b>:
   <p>
   Source: <a href="https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning"> Wikipedia </a>
   <p>This is a seperate function that gives the best possible next move by searching through 
   the possible winnig conditions for player 1
   </p>
   
    01 function alphabeta(node, depth, α, β, maximizingPlayer)
    02      if depth = 0 or node is a terminal node
    03          return the heuristic value of node
    04      if maximizingPlayer
    05          v := -∞
    06          for each child of node
    07              v := max(v, alphabeta(child, depth – 1, α, β, FALSE))
    08              α := max(α, v)
    09              if β ≤ α
    10                  break (* β cut-off *)
    11          return v
    12      else
    13          v := +∞
    14          for each child of node
    15              v := min(v, alphabeta(child, depth – 1, α, β, TRUE))
    16              β := min(β, v)
    17              if β ≤ α
    18                  break (* α cut-off *)
    19          return v

   </p>
  

  
  How to run Simulations:

  * For running automated testing please look below
  * For manually running the app 
    * Run ```python main.py```
    * The System will ask for user_input ```please enter number of rows and columns in the format rows,columns```
    * Enter rows,columns ```Example: 3,4```
    * The System will ask for the 2nd player
        ```
          * Enter 1 for manually playing the game
          * Enter 2 for random player
          * Enter 3 for Minimal Step player
          * Enter 4 to play against computer  
        ```
  * Example output:
  ```
  please enter number of rows and columns in the format rows,columns
3,4
Please enter whether you want to play or you want computer play. Press 1 if you want to play , 2 if you want to play random computer startergy,3 if you want to play minimal strategy, 4 if you want to play minimal strategy
1
please enter an input [(1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (1, 3)]
2,0
please enter an input [(1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
0,2
please enter an input [(1, 0), (0, 1)]
1,0
[(2, 3), (2, 0), (0, 3), (0, 2), (1, 1), (1, 0), (0, 1)]_alpha_beta has won the game

```
  * The sys.out will only show who has one the game.. For complete moves please take a look at the log folder located at <project_dir>/logs/choco_chomp.log
        
#### Testing Scenarios:
How to test:
```
* CD to the project dir
* Run pytest -vv
```

* Testing Scenario 1:
    ```
    val = chomp.play(2, 3, utils.ChompConstants.ALPHABETA_PLAYER, utils.ChompConstants.RANDOM_PLAYER)
    test_data = [[(1, 2), (1, 0), (0, 1)],
                 [(1, 2), (0, 1), (1, 0)],
                 [(1, 2), (1, 1), (0, 2), (1, 0), (0, 1)],
                 [(1, 2), (0, 2), (1, 1), (1, 0), (0, 1)],
                 [(1, 2), (1, 1), (0, 2), (0, 1), (1, 0)],
                 [(1, 2), (0, 2), (1, 1), (0, 1), (1, 0)]]
    These are all possible cases that can occur for 2,3 sized chocolate. Our assertions will test if one of 
    the above sequence has occured. If not the assertions fails
                 
     ```

* Testing Scenario 2:
    ```
    val = chomp.play(3, 2, utils.ChompConstants.ALPHABETA_PLAYER, utils.ChompConstants.RANDOM_PLAYER)
    test_data = [[(2, 1), (0, 1), (1, 0)], [(2, 1), (1, 0), (0, 1)], [(2, 1), (1, 1), (2, 0), (1, 0), (0, 1)],
                 [(2, 1), (1, 1), (2, 0), (0, 1), (1, 0)], [(2, 1), (2, 0), (1, 1), (0, 1), (1, 0)],
                 [(2, 1), (2, 0), (1, 1), (1, 0), (0, 1)]]
    These are all possible cases that can occur for 3,2 sized chocolate. Our assertions will test if one of 
    the above sequence has occured. If not the assertions fails
                 
     ```



** Please note that I have taken several snippets of code from 
http://aima.cs.berkeley.edu/python/games.html. 
This is also available in several CS classes including in Udacity's github location.
This structure primarily helps us in maintaining fixed game structure


### TODO's

- [ ] Unit Tests
- [ ] User Defined Exceptions
- [x] CircleCI integration
- [x] pytest
- [ ] Better exception handling and doc Strings may be?

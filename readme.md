# Repository created for the reasoning part of the AI Discipline

## Problem modelling
### Search problem
- **The base of the search problem is the tree that the algorithm is going to iterate over**

#### GRID
    - Initial state: the grid starts with no words added to them -> grid.generated_grid = {} | 
    - IMPORTANT! -> to generate the grid that will control the completion rules of this problem you need to input the required variables and call the grid.generate_grid(grid_input)
    - Actions: for each turn you need to choose a word from the dictionaries of words and a position of the grid to add them to it -> grid.addNodeToGrid(Node)
    - Cost: at this moment there is no cost associated to the actions
    - Completeness test: every word added to the grid satisfies the given conditions attributed to them -> grid.check_stopping_condition() = True

#### The grid input:
```
grid_input_example = {
    1: [
            ("A",3,{
                1:"1D(1)"
                }
            ),
            ("d",3,{
                1:"1A(1)",
                3:"2A(1)"
                }
            )
        ],
    2: [
            ("A",3,
                {
                    1:"1D(3)"
                }
            )
        ]
}
```
- **The keys** of the grid input are the slots where the words are going to begin
- **The values** of the grid input are a list of tuples that contains information about the words that are going to be placed in that specific slot
    - **The elements** of the values list are tuples composed of three values: (Direction, Lenght, Cross Positions)
        - **Direction**: a string that represents the direction on which the word is going to unfold. There are only two possible values: A -> accross(horizontal) and D -> down(vertical)
        - **Lenght**: a integer that represents the total lenght of the word for that direction
        - **Cross Positions**: a dictionary that maps the crossing positions. Each key, a integer, of the **Cross Positions** corresponsds to a char position of the word and the value, a string, correspond to the char localization in the word that crosses the word in the key position.
        - **Visual breakdown**: 
        
            - Lets think about the grid_input_example presented, that input represents a three word crossword puzzle that has 1 word across, one word down and 1 other word accross. (the x's are blocked slots)
            - | d | o | g |
            - | a | x | x |
            - | d | a | y | 
            - This crossword has two slots, 1 and 2
                - On the slot 1, we have two words, one in the A direction and another one in the D direction
                    - A -> lenght = 3, the first char of the 1A word, 1A(1) is the same as 1D(1) -> {1:"1D(1)"}
                    - D -> dad, lenght = 3, the first char of the 1D word, 1D(1) is the same as 1A(1) and the third char of 1D word 1D(3) is the same as 2D(1) -> {1:"1A(1)",3:"2A(1)"}
                - On the slot 2, we have one word in the A direction
                    - A -> day, lenght =3, the first char of the 2A word, 2A(1) is the same as 1D(3) -> {1:"1D(3)"}

#### GRID
    - Initial state: the grid starts with no words added to them -> grid.generated_grid = {}
    - Actions: for each turn you need to choose a word from the dictionaries of words and a position of the grid to add them to it -> grid.addNodeToGrid(Node)
    - Cost: at this moment there is no cost associated to the actions
    - Completeness test: every word added to the grid satisfies the given conditions attributed to them -> grid.check_stopping_condition() = True


### Constraint Satisfaction problem (CSP)
#### TODO

## How to contribute to the repository
### Clone the repository (if you don't have the repo locally)
1. Clone the remote repository to your machine via ``` git clone https://github.com/SamuelMalaga/AI-Reasoning.git ```

### If you already have the repo locally
### Obs: If you are not sure how to use git, before commiting do a local backup of what you have 
1. Check for changes in the main branch (important step to not overwrite the latest changes) ```git fetch```
2. Create a branch to carry on with your contribution ```git checkout -b <branch_name>```
3. After you finish the modifications, do the following sequence
    1. Add all the modifications to the commit ```git add .```
    2. Add a message to the commit ```git commit -m "<your_message>"```
    3. If you want your commit to be reviewed ```git push origin <branch_name>```
4. (Optional) To commit directly to the main branch ```git checkout main```
5. (Optional) Merge the changes in the branch to the main ```git merge <branch_name>```
6. (Optional) Push the changes to origin ```git push origin main```
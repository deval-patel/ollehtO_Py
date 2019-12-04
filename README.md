# Othello_Py
A GUI version of the board game Othello. Coded in Python.

**How to install and run the game:**

 
**How to play the game**
The goal of this game is to have as many of your own type of tokens as possible. 

When it is your turn, you can place a token on the board to capture one or more of the other player's token by clicking the board. The way you capture the tokens is like making a sandwich, we want our sandwich to be filled with the other player's tokens with no empty spaces in between. 

For example, for a player X, to make a successful move, 
let's examine two pictures. 

The picture below is the state of the game at the beginning, 
when the game has just been started. 
![Pre Move:](/images/preMove.jpg)

Now, Let's see what happens if Player X, places a token below
the bottom-left "O" Token. 

![Post Move:](/images/postMove.jpg)

Then, this new "X" token placed will sandwich the previous "O" token, making it an "X" token!

Player X, will go first, followed by Player 0. They will 
alternate turns as they play the game. If a player can not 
make a successful move, then it will go to the other player's
turn. In addition to this, if neither player can make a turn,
the game will end. 

When the game ends, the winner is determined by going back
to the goal of the game. Whichever player has the most tokens
will win.

If you want a visual representation of the rules of this game
check this video out! [Othello Rules](https://youtu.be/lO2pEK33SSw)


**High-Level Documentation**
 
*othello.Application:* The package which contains the view component:

	*.Application:*
 	    This file is used to set up the GUI. It initializes all of the main widgets (Labels and Frames) with help from classes in the package .Widget. The 		    function set_message() should be used to update the message displayed at the bottom of the screen. 
	
	*.ColourScheme:* 
	    Contains the colour scheme of the GUI. The ColourScheme class should be used to customize widgets. Should the colour scheme change, the background,
	    text-colour and button-colour can be changed with their respective setter functions.

	*.Pictures: (Package)*
	    Contains the pictures for the ollehtO Board. 
	    *.Pictures:* A class to handle the conversion of PNG images to ImageTK objects. Use get_image() to get the ImageTK of the PNG files.

	*.Widgets: (Package)*

	    *.Token:* 
	        A widget used as the tokens for ollehtO which is a child of the Button class. 
	        It contains the x,y value as attributes for simplicity to access them, use the appropriate getters. The set_image() function is to update the image of 			this Token, it takes in a String which has the name of the image file (excluding “.png”). When the Token is clicked, it calls update_parent()(an 			instance of ImageFrame) passing an instance of itself, letting the ImageFrame know that it got clicked.
	    
	    *.ButtonFrame:*
	        Initializes the Buttons for Game Modes, Settings, and Exit. 
	        The functionality of these buttons are not implemented yet.

	    *.ImageFrame:*
	        Initializes the Buttons for the ollehtO game board.
 	        Use the  update_othello()  function to communicate with the othello class. When a Token is clicked, the instance will try to make a move with the
      		clicked Token’s x and y coordinates. If a move is made, the instance will update all of the Tokens it contains with their new images through 			Token.set_image() according to the newly updated ollehtO board. If a valid move is not made, nothing happens. 

*othello.Player:* The package which contains the player components:

	*.move:*
 	    Contains row and column information for players that wants to make a move.
	    get_row: return row of move.
	    get_col: return column of move.
	    to_string: return string representation of move.
	    
	*.player:* 
	    The abstract class of the player classes.
	    
	*.player_easy:*
 	    An AI that makes moves at an easy difficulty.
 	    get_move: return worst_move.
	
	*.player_medium:* 
	    An AI that makes moves at an medium difficulty.
 	    get_move: return random_move.
	
	*.player_hard:*
 	    An AI that makes moves at an hard difficulty.
 	    get_move: return best_move or random_move.
 	    
	*.player_human:* 
	    The human player.
 	    get_move: return a move object of where the user wants to move.
 	    
	*.player_moves:* 
	    Contains move algorithms.
 	    random_move: return a move object with a random valid row and column.
 	    best_move: return a move object for a move with the most returns.
 	    worst_move: return a move object for a move with the fewest returns.
	    
**Addendum**

*Deval Patel:*

I created the LICENSE.md file for this repository. In addition to this, I am responsible for all of the code and files in *othello.Application*. As for the README, 
the High-Level Documentation for everything under *othello.Application* is written by me. The section *How to play the game* is written by me.

*Mevan Rajakaruna:*

I am responsible for the *othello.Player* package and all the code/classes within it. I also created the High-Level Documentation for *othello.Player*.

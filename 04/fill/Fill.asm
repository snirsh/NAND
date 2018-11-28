// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

@SCREEN
D=A
@8192
D=D+A
@SCREEN_SIZE
M=D

(RESTART)
	@SCREEN
	D=A
	@pixel
	M=D	

(LOOP)
	// checking keyboard input
	@KBD
	D=M
	@BLACK 	// if keyboard != 0 goto BLACK else goto WHITE
	D;JGT	
	@WHITE
	D;JEQ	
	@LOOP
	0;JMP

(BLACK) 
	@color
	M=-1	// this sets the RAM[color] to -1 which is 11111111111111 and represents black
	@DRAW	// paint the screen in the selected color
	0;JMP

(WHITE)
	@color
	M=0		// this sets RAM[color] to 0 which will represent white 
	@DRAW 	// paint the screen in the selected color
	0;JMP

(DRAW)
	@color 	//fetch color and put it in D
	D=M
	@pixel 	// fetch pixel to paint and painting it
	A=M
	M=D
	@pixel 	// moving to next pixel
	M=M+1
	D=M
	@SCREEN_SIZE //now we check if we finished painting the screen if we do we reset the pixel and continue the loop
	D=D-M
	@RESTART
	D;JEQ
	@DRAW
	0;JMP
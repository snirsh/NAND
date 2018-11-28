// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// this program will add R0 to itself R1 times, thus multiplying R0 and R1.
	@R2
	M=0	//initializing R2 to be 0 R2 will represent our result
	@R1
	D=M 
	@counter
	M=D	//counter will count down from R1 to 0
(LOOP)
	@counter
	D=M
	@END
	D;JEQ // if the counter reached 0 then we finished
	@R0
	D=M
	@R2
	M=M+D	//	Sum += R0
	@counter
	M=M-1 	//	counter--
	@LOOP
	0;JMP
(END)
	
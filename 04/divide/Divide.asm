// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/divide/Divide.asm

// Dividing R13 and R14 and storing the result in R15.
// (R13, R14, R15 refer to RAM[13], RAM[14], and RAM[15], respectively.)

@R15
D=M
@s0
M=D
@s1
M=0
@s2
M=0
@s3
M=1
@s4
M=0

(LOOP)
	@s4
	D=M
	@s2
	D=M<<
	@s4
	M=D
	D=M
	@s1
	D=D-M
	@LOOP2
	D;JGT
	@s2
	M=M<<
	@s3
	M=M<<
	@LOOP
	0;JEQ

(LOOP2)
	@s3
	D=M
	@END
	
	
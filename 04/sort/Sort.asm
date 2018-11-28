// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/sort/Sort.asm

// that's my implementation of sort algorithm
@R15
D=M
@n	//length of array
M=D
@i
M=0
(i_LOOP)
	//if i == n then we finished
	@i
	D=M
	@n
	D=M-D	//n-i
	@END
	D;JEQ
	// initializing for 2nd loop with j=0 and k=n-i-1 which is the end of the 2nd loop
	@j
	M=0
	@i
	D=M
	@n
	D=M-D
	D=D-1
	@k
	M=D 
	@i
	M=M+1
	@j_LOOP
	0;JMP

(j_LOOP)
	//while (n-i-1)-j >0
	@j
	D=M
	@k
	D=M-D	
	@i_LOOP
	D;JLE
	// we need arr[j] and arr[j+1] and when we get there we'll swap if needed
	//fetching a[j] and a[j+1]
	@R14
	D=M
	@j
	A=D+M	//adress now is a[j]
	D=M		//D=a[j]
	@t1		//t1=a[j]
	M=D
	@R14
	D=M
	@j
	A=D+M
	A=A+1
	D=M		//D=a[j+1]
	@t2		//t2=a[j+1]
	M=D
	//	if a[j]-a[j+1]<=0 then we're ok
	D=M
	@t1
	D=D-M	//D=t1-t2(a[j+1]-a[j])
	@j
	M=M+1
	@j_LOOP
	D;JLE
	//	swap a[j] with a[j+1]
	@R14
	D=M
	@j
	D=D+M
	D=D-1
	A=D
	D=M		// A=j, D=a[j]
	A=A+1	// A=j+1, D=a[j]
	D=D+M	// A=j+1, D=a[j+1]+a[j]
	M=D-M	// A=j+1, a[j+1]=a[j+1]+a[j]-a[j+1]
	A=A-1	// A=j	, D=a[j+1]+a[j]
	M=D-M	// A=j	, a[j]=a[j+1]+a[j]-a[j]
	//this is it.. finally
	@j_LOOP
	0;JMP
@13
M=0
@14
M=0
@15
M=0
@13
M=0
@14
M=0
@15
M=0
//PUSHING: constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: local 0
@0
D=A
@LCL
A=M+D
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//PUSHING: constant 21
@21
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 22
@22
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: argument 2
@2
D=A
@ARG
A=M+D
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//POPPING: argument 1
@1
D=A
@ARG
A=M+D
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//PUSHING: constant 36
@36
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: this 6
@6
D=A
@THIS
A=M+D
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//PUSHING: constant 42
@42
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: that 5
@5
D=A
@THAT
A=M+D
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//POPPING: that 2
@2
D=A
@THAT
A=M+D
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//PUSHING: constant 510
@510
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: temp 6
@SP
AM=M-1
D=M
@11
M=D
//PUSHING: local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
//PUSHING: that 5
@5
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
//BINARY OP:add
@SP
AM=M-1
D=M
A=A-1
M=M+D
//PUSHING: argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
//BINARY OP:sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//PUSHING: this 6
@6
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
//PUSHING: this 6
@6
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
//BINARY OP:add
@SP
AM=M-1
D=M
A=A-1
M=M+D
//BINARY OP:sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//PUSHING: temp 6
@11
D=M
@SP
M=M+1
A=M-1
M=D
//BINARY OP:add
@SP
AM=M-1
D=M
A=A-1
M=M+D

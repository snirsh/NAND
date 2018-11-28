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
//PUSHING: constant 3030
@3030
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: pointer 0
@SP
AM=M-1
D=M
@3
M=D
//PUSHING: constant 3040
@3040
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: pointer 1
@SP
AM=M-1
D=M
@4
M=D
//PUSHING: constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: this 2
@2
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
//PUSHING: constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: that 6
@6
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
//PUSHING: pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
//PUSHING: pointer 1
@4
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
//PUSHING: this 2
@2
D=A
@THIS
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
//PUSHING: that 6
@6
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

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
//PUSHING: constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 333
@333
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 888
@888
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: static 8
@SP
AM=M-1
D=M
@StaticTest.8
M=D
//POPPING: static 3
@SP
AM=M-1
D=M
@StaticTest.3
M=D
//POPPING: static 1
@SP
AM=M-1
D=M
@StaticTest.1
M=D
//PUSHING: static 3
@StaticTest.3
D=M
@SP
M=M+1
A=M-1
M=D
//PUSHING: static 1
@StaticTest.1
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
//PUSHING: static 8
@StaticTest.8
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

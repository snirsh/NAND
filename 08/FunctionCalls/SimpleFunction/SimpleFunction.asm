(global.SimpleFunction.test)
//PUSHING: constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSHING: constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSHING: local 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSHING: local 1
@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//BINARY OP:add
@SP
AM=M-1
D=M
A=A-1
M=M+D
//UNARY OP:not
@SP
A=M-1
M=!M
//PUSHING: argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//BINARY OP:add
@SP
AM=M-1
D=M
A=A-1
M=M+D
//PUSHING: argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//BINARY OP:sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//RETURNING
@5
D=A
@LCL
A=M-D
D=M
@R13
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
A=A+1
D=A
@SP
M=D
@LCL
A=M-1
D=M
@THAT
M=D
@2
D=A
@LCL
A=M-D
D=M
@THIS
M=D
@3
D=A
@LCL
A=M-D
D=M
@ARG
M=D
@4
D=A
@LCL
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
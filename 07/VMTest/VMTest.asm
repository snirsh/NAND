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
//PUSHING: constant 17000
@17000
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 17001
@17001
D=A
@SP
M=M+1
A=M-1
M=D
//COMP OP:lt
//CHECKING FOR OVERFLOW ON CMD
@SP
AM=M-1
D=M
@R14
M=D
@FNEG.VMTest1
D;JLT
@SP
A=M-1
D=M
@SNEG.VMTest1
D;JLT
@CHCK.VMTest1
0;JMP
(FNEG.VMTest1)
@SP
A=M-1
D=M
@SPOS.VMTest1
D;JGT
@CHCK.VMTest1
0;JMP
(SPOS.VMTest1)
@R2
D=A
@ANS.VMTest1
0;JMP
(SNEG.VMTest1)
@R2
D=-A
@ANS.VMTest1
0;JMP
(CHCK.VMTest1)
@R14
D=D-M
(ANS.VMTest1)
@IF.VMTest1
D;JLT
@SP
A=M-1
M=0
@ELSE.VMTest1
0;JMP
(IF.VMTest1)
@SP
A=M-1
M=-1
(ELSE.VMTest1)
//PUSHING: constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 12
@12
D=A
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
//PUSHING: constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
//COMP OP:gt
//CHECKING FOR OVERFLOW ON CMD
@SP
AM=M-1
D=M
@R14
M=D
@FNEG.VMTest2
D;JLT
@SP
A=M-1
D=M
@SNEG.VMTest2
D;JLT
@CHCK.VMTest2
0;JMP
(FNEG.VMTest2)
@SP
A=M-1
D=M
@SPOS.VMTest2
D;JGT
@CHCK.VMTest2
0;JMP
(SPOS.VMTest2)
@R2
D=A
@ANS.VMTest2
0;JMP
(SNEG.VMTest2)
@R2
D=-A
@ANS.VMTest2
0;JMP
(CHCK.VMTest2)
@R14
D=D-M
(ANS.VMTest2)
@IF.VMTest2
D;JGT
@SP
A=M-1
M=0
@ELSE.VMTest2
0;JMP
(IF.VMTest2)
@SP
A=M-1
M=-1
(ELSE.VMTest2)
//PUSHING: constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
//UNARY OP:neg
D=0
@SP
A=M-1
M=D-M
//PUSHING: constant 2
@2
D=A
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
//PUSHING: constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
//COMP OP:eq
//CHECKING VALIDITY OF EQ
@SP
AM=M-1
D=M
A=A-1
D=M-D
@IF.VMTest3
D;JEQ
@SP
A=M-1
M=0
@ELSE.VMTest3
0;JMP
(IF.VMTest3)
@SP
A=M-1
M=-1
(ELSE.VMTest3)
//PUSHING: constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 2
@2
D=A
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
//COMP OP:eq
//CHECKING VALIDITY OF EQ
@SP
AM=M-1
D=M
A=A-1
D=M-D
@IF.VMTest4
D;JEQ
@SP
A=M-1
M=0
@ELSE.VMTest4
0;JMP
(IF.VMTest4)
@SP
A=M-1
M=-1
(ELSE.VMTest4)
//PUSHING: constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 2
@2
D=A
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
//COMP OP:gt
//CHECKING FOR OVERFLOW ON CMD
@SP
AM=M-1
D=M
@R14
M=D
@FNEG.VMTest5
D;JLT
@SP
A=M-1
D=M
@SNEG.VMTest5
D;JLT
@CHCK.VMTest5
0;JMP
(FNEG.VMTest5)
@SP
A=M-1
D=M
@SPOS.VMTest5
D;JGT
@CHCK.VMTest5
0;JMP
(SPOS.VMTest5)
@R2
D=A
@ANS.VMTest5
0;JMP
(SNEG.VMTest5)
@R2
D=-A
@ANS.VMTest5
0;JMP
(CHCK.VMTest5)
@R14
D=D-M
(ANS.VMTest5)
@IF.VMTest5
D;JGT
@SP
A=M-1
M=0
@ELSE.VMTest5
0;JMP
(IF.VMTest5)
@SP
A=M-1
M=-1
(ELSE.VMTest5)
//PUSHING: constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
//COMP OP:lt
//CHECKING FOR OVERFLOW ON CMD
@SP
AM=M-1
D=M
@R14
M=D
@FNEG.VMTest6
D;JLT
@SP
A=M-1
D=M
@SNEG.VMTest6
D;JLT
@CHCK.VMTest6
0;JMP
(FNEG.VMTest6)
@SP
A=M-1
D=M
@SPOS.VMTest6
D;JGT
@CHCK.VMTest6
0;JMP
(SPOS.VMTest6)
@R2
D=A
@ANS.VMTest6
0;JMP
(SNEG.VMTest6)
@R2
D=-A
@ANS.VMTest6
0;JMP
(CHCK.VMTest6)
@R14
D=D-M
(ANS.VMTest6)
@IF.VMTest6
D;JLT
@SP
A=M-1
M=0
@ELSE.VMTest6
0;JMP
(IF.VMTest6)
@SP
A=M-1
M=-1
(ELSE.VMTest6)
//PUSHING: constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
//UNARY OP:not
@SP
A=M-1
M=!M
//PUSHING: constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
//UNARY OP:neg
D=0
@SP
A=M-1
M=D-M
//BINARY OP:and
@SP
AM=M-1
D=M
A=A-1
M=M&D
//PUSHING: constant 1
@1
D=A
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
//PUSHING: constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
//COMP OP:eq
//CHECKING VALIDITY OF EQ
@SP
AM=M-1
D=M
A=A-1
D=M-D
@IF.VMTest7
D;JEQ
@SP
A=M-1
M=0
@ELSE.VMTest7
0;JMP
(IF.VMTest7)
@SP
A=M-1
M=-1
(ELSE.VMTest7)
//PUSHING: constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
//UNARY OP:neg
D=0
@SP
A=M-1
M=D-M
//BINARY OP:or
@SP
AM=M-1
D=M
A=A-1
M=M|D
//PUSHING: constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: argument 0
@0
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
//PUSHING: argument 0
@0
D=A
@ARG
A=M+D
D=M
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
//POPPING: static 2
@SP
AM=M-1
D=M
@VMTest.2
M=D
//PUSHING: static 2
@VMTest.2
D=M
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 4000
@4000
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
//PUSHING: constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: this 0
@0
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
//PUSHING: this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 5000
@5000
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
//PUSHING: constant 21
@21
D=A
@SP
M=M+1
A=M-1
M=D
//POPPING: that 0
@0
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
//PUSHING: that 0
@0
D=A
@THAT
A=M+D
D=M
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
//POPPING: temp 3
@SP
AM=M-1
D=M
@8
M=D
//PUSHING: temp 3
@8
D=M
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 30000
@30000
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 30000
@30000
D=A
@SP
M=M+1
A=M-1
M=D
//UNARY OP:neg
D=0
@SP
A=M-1
M=D-M
//COMP OP:gt
//CHECKING FOR OVERFLOW ON CMD
@SP
AM=M-1
D=M
@R14
M=D
@FNEG.VMTest8
D;JLT
@SP
A=M-1
D=M
@SNEG.VMTest8
D;JLT
@CHCK.VMTest8
0;JMP
(FNEG.VMTest8)
@SP
A=M-1
D=M
@SPOS.VMTest8
D;JGT
@CHCK.VMTest8
0;JMP
(SPOS.VMTest8)
@R2
D=A
@ANS.VMTest8
0;JMP
(SNEG.VMTest8)
@R2
D=-A
@ANS.VMTest8
0;JMP
(CHCK.VMTest8)
@R14
D=D-M
(ANS.VMTest8)
@IF.VMTest8
D;JGT
@SP
A=M-1
M=0
@ELSE.VMTest8
0;JMP
(IF.VMTest8)
@SP
A=M-1
M=-1
(ELSE.VMTest8)
//PUSHING: constant 30000
@30000
D=A
@SP
M=M+1
A=M-1
M=D
//PUSHING: constant 30000
@30000
D=A
@SP
M=M+1
A=M-1
M=D
//UNARY OP:neg
D=0
@SP
A=M-1
M=D-M
//BINARY OP:sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//PUSHING: constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
//COMP OP:gt
//CHECKING FOR OVERFLOW ON CMD
@SP
AM=M-1
D=M
@R14
M=D
@FNEG.VMTest9
D;JLT
@SP
A=M-1
D=M
@SNEG.VMTest9
D;JLT
@CHCK.VMTest9
0;JMP
(FNEG.VMTest9)
@SP
A=M-1
D=M
@SPOS.VMTest9
D;JGT
@CHCK.VMTest9
0;JMP
(SPOS.VMTest9)
@R2
D=A
@ANS.VMTest9
0;JMP
(SNEG.VMTest9)
@R2
D=-A
@ANS.VMTest9
0;JMP
(CHCK.VMTest9)
@R14
D=D-M
(ANS.VMTest9)
@IF.VMTest9
D;JGT
@SP
A=M-1
M=0
@ELSE.VMTest9
0;JMP
(IF.VMTest9)
@SP
A=M-1
M=-1
(ELSE.VMTest9)

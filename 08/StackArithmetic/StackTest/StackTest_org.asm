@17
D=A
@SP
M=M+1
A=M-1
M=D
@17
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE.StackTest1
D;JEQ
@SP
A=M-1
M=0
@NEXT.StackTest1
0;JMP
(TRUE.StackTest1)
@SP
A=M-1
M=-1
(NEXT.StackTest1)
@17
D=A
@SP
M=M+1
A=M-1
M=D
@16
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE.StackTest2
D;JEQ
@SP
A=M-1
M=0
@NEXT.StackTest2
0;JMP
(TRUE.StackTest2)
@SP
A=M-1
M=-1
(NEXT.StackTest2)
@16
D=A
@SP
M=M+1
A=M-1
M=D
@17
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE.StackTest3
D;JEQ
@SP
A=M-1
M=0
@NEXT.StackTest3
0;JMP
(TRUE.StackTest3)
@SP
A=M-1
M=-1
(NEXT.StackTest3)
@892
D=A
@SP
M=M+1
A=M-1
M=D
@891
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
@R14
M=D
@FIRST_NEG.StackTest4
D;JLT
@SP
A=M-1
D=M
@SEC_NEG.StackTest4
D;JLT
@EVALUATE_SUM.StackTest4
0;JMP
(FIRST_NEG.StackTest4)
@SP
A=M-1
D=M
@SEC_POSITIVE.StackTest4
D;JGT
@EVALUATE_SUM.StackTest4
0;JMP
(SEC_POSITIVE.StackTest4)
@R2
D=A
@EVALUATE.StackTest4
0;JMP
(SEC_NEG.StackTest4)
@R2
D=-A
@EVALUATE.StackTest4
0;JMP
(EVALUATE_SUM.StackTest4)
@R14
D=D-M
(EVALUATE.StackTest4)
@TRUE.StackTest4
D;JLT
@SP
A=M-1
M=0
@NEXT.StackTest4
0;JMP
(TRUE.StackTest4)
@SP
A=M-1
M=-1
(NEXT.StackTest4)
@891
D=A
@SP
M=M+1
A=M-1
M=D
@892
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
@R14
M=D
@FIRST_NEG.StackTest5
D;JLT
@SP
A=M-1
D=M
@SEC_NEG.StackTest5
D;JLT
@EVALUATE_SUM.StackTest5
0;JMP
(FIRST_NEG.StackTest5)
@SP
A=M-1
D=M
@SEC_POSITIVE.StackTest5
D;JGT
@EVALUATE_SUM.StackTest5
0;JMP
(SEC_POSITIVE.StackTest5)
@R2
D=A
@EVALUATE.StackTest5
0;JMP
(SEC_NEG.StackTest5)
@R2
D=-A
@EVALUATE.StackTest5
0;JMP
(EVALUATE_SUM.StackTest5)
@R14
D=D-M
(EVALUATE.StackTest5)
@TRUE.StackTest5
D;JLT
@SP
A=M-1
M=0
@NEXT.StackTest5
0;JMP
(TRUE.StackTest5)
@SP
A=M-1
M=-1
(NEXT.StackTest5)
@891
D=A
@SP
M=M+1
A=M-1
M=D
@891
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
@R14
M=D
@FIRST_NEG.StackTest6
D;JLT
@SP
A=M-1
D=M
@SEC_NEG.StackTest6
D;JLT
@EVALUATE_SUM.StackTest6
0;JMP
(FIRST_NEG.StackTest6)
@SP
A=M-1
D=M
@SEC_POSITIVE.StackTest6
D;JGT
@EVALUATE_SUM.StackTest6
0;JMP
(SEC_POSITIVE.StackTest6)
@R2
D=A
@EVALUATE.StackTest6
0;JMP
(SEC_NEG.StackTest6)
@R2
D=-A
@EVALUATE.StackTest6
0;JMP
(EVALUATE_SUM.StackTest6)
@R14
D=D-M
(EVALUATE.StackTest6)
@TRUE.StackTest6
D;JLT
@SP
A=M-1
M=0
@NEXT.StackTest6
0;JMP
(TRUE.StackTest6)
@SP
A=M-1
M=-1
(NEXT.StackTest6)
@32767
D=A
@SP
M=M+1
A=M-1
M=D
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
@R14
M=D
@FIRST_NEG.StackTest7
D;JLT
@SP
A=M-1
D=M
@SEC_NEG.StackTest7
D;JLT
@EVALUATE_SUM.StackTest7
0;JMP
(FIRST_NEG.StackTest7)
@SP
A=M-1
D=M
@SEC_POSITIVE.StackTest7
D;JGT
@EVALUATE_SUM.StackTest7
0;JMP
(SEC_POSITIVE.StackTest7)
@R2
D=A
@EVALUATE.StackTest7
0;JMP
(SEC_NEG.StackTest7)
@R2
D=-A
@EVALUATE.StackTest7
0;JMP
(EVALUATE_SUM.StackTest7)
@R14
D=D-M
(EVALUATE.StackTest7)
@TRUE.StackTest7
D;JGT
@SP
A=M-1
M=0
@NEXT.StackTest7
0;JMP
(TRUE.StackTest7)
@SP
A=M-1
M=-1
(NEXT.StackTest7)
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@32767
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
@R14
M=D
@FIRST_NEG.StackTest8
D;JLT
@SP
A=M-1
D=M
@SEC_NEG.StackTest8
D;JLT
@EVALUATE_SUM.StackTest8
0;JMP
(FIRST_NEG.StackTest8)
@SP
A=M-1
D=M
@SEC_POSITIVE.StackTest8
D;JGT
@EVALUATE_SUM.StackTest8
0;JMP
(SEC_POSITIVE.StackTest8)
@R2
D=A
@EVALUATE.StackTest8
0;JMP
(SEC_NEG.StackTest8)
@R2
D=-A
@EVALUATE.StackTest8
0;JMP
(EVALUATE_SUM.StackTest8)
@R14
D=D-M
(EVALUATE.StackTest8)
@TRUE.StackTest8
D;JGT
@SP
A=M-1
M=0
@NEXT.StackTest8
0;JMP
(TRUE.StackTest8)
@SP
A=M-1
M=-1
(NEXT.StackTest8)
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
@R14
M=D
@FIRST_NEG.StackTest9
D;JLT
@SP
A=M-1
D=M
@SEC_NEG.StackTest9
D;JLT
@EVALUATE_SUM.StackTest9
0;JMP
(FIRST_NEG.StackTest9)
@SP
A=M-1
D=M
@SEC_POSITIVE.StackTest9
D;JGT
@EVALUATE_SUM.StackTest9
0;JMP
(SEC_POSITIVE.StackTest9)
@R2
D=A
@EVALUATE.StackTest9
0;JMP
(SEC_NEG.StackTest9)
@R2
D=-A
@EVALUATE.StackTest9
0;JMP
(EVALUATE_SUM.StackTest9)
@R14
D=D-M
(EVALUATE.StackTest9)
@TRUE.StackTest9
D;JGT
@SP
A=M-1
M=0
@NEXT.StackTest9
0;JMP
(TRUE.StackTest9)
@SP
A=M-1
M=-1
(NEXT.StackTest9)
@57
D=A
@SP
M=M+1
A=M-1
M=D
@31
D=A
@SP
M=M+1
A=M-1
M=D
@53
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=M+D
@112
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=M-D
D=0
@SP
A=M-1
M=D-M
@SP
AM=M-1
D=M
A=A-1
M=M&D
@82
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=M|D
@SP
A=M-1
M=!M
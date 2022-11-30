#PTCS 1.2
import time
import webbrowser
script = []
variables = []
Input = ""
call = 0

print("LOADING... Select MODE $? for HELP")
time.sleep(1)
while Input != "end":
    Input = input("Select MODE $")
    
    if Input == "#":
        
        InputNum = int(input("Input Line INTEGER $"))
        InputJob = input("Input Job $")
        
        if InputJob=="GOTO":
                InputVar = int(input("Input Variable INTEGER $"))
        elif InputJob == "PRINT" or InputJob == "COM":
            InputVar = input("Input Variable STRING $")
        elif InputJob == "XSKUL":
            InputVar = [input("Input Job STRING $"), int(input("Input Storage INTEGER $"))]
        elif InputJob == "INTVAR":
            InputVar = int(input("Input Variable INTEGER $"))
            
        elif InputJob == "ADD" or InputJob == "SUB" or InputJob == "MUL" or InputJob == "DIV" or InputJob == "MOD":
            InputVar = [int(input("Input First INTEGER $")),
            int(input("Input Second INTEGER $")), int(input("Input Storage INTEGER $"))]
        
        elif InputJob == "ADDX" or InputJob == "SUBX" or InputJob == "MULX" or InputJob == "DIVX" or InputJob == "MODX":
            InputVar = [int(input("Input First Read INTEGER $")),
            int(input("Input Second Read INTEGER $")), int(input("Input Storage INTEGER $"))]
        
        elif InputJob == "GOTX" or InputJob == "PRINTX":
            InputVar = int(input("Input Read INTEGER $"))
        elif InputJob == "GOTOUCH":
            InputVar = int(input("Input Read INTEGER $"))
            
        elif InputJob == "SET":
            InputVar = [int(input("Input Storage INTEGER $")), input("Input Variable STRING $")] 
        elif InputJob == "SETINT":
            InputVar = [int(input("Input Storage INTEGER $")), int(input("Input Variable INTEGER $"))]
        elif InputJob == "SETX":
            InputVar = [int(input("Input Storage INTEGER $")), int(input("Input Read INTEGER $"))] 
        elif InputJob == "SETINX":
            InputVar = [int(input("Input Storage INTEGER $")), int(input("Input Read INTEGER $"))]
        elif InputJob == "SETCON":
            InputVar = [int(input("Input First Read INTEGER $")), input("Input Operator STRING $"), int(input("Input Second Read INTEGER $")), int(input("Input Storage INTEGER"))]
            
        elif InputJob == "SETCALL":
            InputVar = int(input("Input Read INTEGER $"))
        
        elif InputJob == "RETURN":
            InputVar = None
        else:
            print("UNKNOWN JOB")
            break
        if InputNum > len(script) - 1:
            for skippedLines in range(len(script), InputNum):
                script.insert(skippedLines, "...")
                variables.insert(skippedLines,"")
        if InputNum < len(script):
            script[InputNum] = InputJob
            variables[InputNum] = InputVar
        else:
            script.insert(InputNum, InputJob)
            variables.insert(InputNum, InputVar)
    if Input == "?":
        webbrowser.open("https://studentsfraserk12-my.sharepoint.com/:p:/g/personal/alexander_noble25_students_fraserk12_org/EevKdsJKtf1CrmG0omfEtxABv-JCEqjIMrdKCHbI758xGQ")
    if Input == "list":
        for i in range(0, len(script)):
            print(str(i) + ": " + script[i] + " " + str(variables[i]))
    if Input == "run":
        i = 0
        while i <= (len(script) - 1):
            time.sleep(0.1)
            iMemory = i
            if script[i] == "PRINT":
                print(str(variables[i]))
            elif script[i] == "GOTO":
                call = i
                i = variables[i]
            elif script[i] == "RETURN":
                if call != 0:
                    i = call + 1
            elif script[i] == "ADD":
                variables[i][2] = int(variables[i][0]) + int(variables[i][1])
            elif script[i] == "SUB":
                variables[i][2] = int(variables[i][0]) - int(variables[i][1])
            elif script[i] == "MUL":
                variables[i][2] = int(variables[i][0]) * int(variables[i][1])
            elif script[i] == "DIV":
                variables[i][2] = int(variables[i][0]) / int(variables[i][1])
            elif script[i] == "MOD":
                variables[i][2] = int(variables[i][0]) % int(variables[i][1])
                
            elif script[i] == "ADDX":
                variables[i][2] = int(variables[int(variables[i][0])]) + int(variables[int(variables[i][1])])
            elif script[i] == "SUBX":
                variables[i][2] = int(variables[int(variables[i][0])]) - int(variables[int(variables[i][1])])
            elif script[i] == "MULX":
                variables[i][2] = int(variables[int(variables[i][0])]) * int(variables[int(variables[i][1])])
            elif script[i] == "DIVX":
                variables[i][2] = int(variables[int(variables[i][0])]) / int(variables[int(variables[i][1])])
            elif script[i] == "MODX":
                variables[i][2] = int(variables[int(variables[i][0])]) % int(variables[int(variables[i][1])])
                
            elif script[i] == "GOTX":
                call = i
                i = int(variables[int(variables[i])])
            elif script[i] == "PRINTX":
                print(variables[int(variables[i])])
            elif script[i] == "SET":
                variables[variables[i][0]] = variables[i][1]
            elif script[i] == "SETINT":
                variables[variables[i][0]] = variables[i][1]
            elif script[i] == "SETX":
                variables[variables[i][0]] = variables[variables[i][1]]
            elif script[i] == "SETINX":
                variables[variables[i][0]] = variables[variables[i][1]]
            elif script[i] == "SETCON":
                if variables[i][1] == "==":
                    if variables[variables[i][0]] == variables[variables[i][2]]:
                        variables[variables[i][3]] = 1
                    else:
                        variables[variables[i][3]] = 0
                elif variables[i][1] == "<=":
                    if variables[variables[i][0]] <= variables[variables[i][2]]:
                        variables[variables[i][3]] = 1
                    else:
                        variables[variables[i][3]] = 0
                elif variables[i][1] == ">=":
                    if variables[variables[i][0]] >= variables[variables[i][2]]:
                        variables[variables[i][3]] = 1
                    else:
                        variables.insert(variables[variables[i][3]], 0)
                elif variables[i][1] == "!=":
                    if variables[variables[i][0]] != variables[variables[i][2]]:
                        variables[variables[i][3]] = 1
                    else:
                        variables[variables[i][3]] = 0
                elif variables[i][1] == "<":
                    if variables[variables[i][0]] < variables[variables[i][2]]:
                        variables[variables[i][3]] = 1
                    else:
                        variables[variables[i][3]] = 0
                elif variables[i][1] == ">":
                    if variables[variables[i][0]] > variables[variables[i][2]]:
                        variables[variables[i][3]] = 1
                    else:
                        variables[variables[i][3]] = 0
                else:
                    print("Unknown Operator")
            elif script[i] == "SETCALL":
                call = int(variables[variables[i]])
            elif script[i] == "GOTOUCH":
                i = int(variables[int(variables[i])])
            elif script[i] == "XSKUL":
                script[variables[i][1]] = variables[i][0]
            if iMemory == i:
                i = i + 1



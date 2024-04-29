import re
from enums import Languages

javaExp = r'^\s*(?:public|private|protected)?\s+(?:static\s+)?(?:\w+\s+)?\w+\s+\w+\s*\([^)]*\)\s*{'
pythonExp = r'^\s*def\s+\w+\s*\([^)]*\)\s*:\s*'
startIndexes = []
endIndexes = []


def getLengthOfFile(filepath):
    with open(filepath, 'r') as file:
        return len(file.readlines())



def getFunctionCode(filepath: str, language: str = "J"):
    functionCode = []
    last = getLengthOfFile(filepath)
    with open(filepath, 'r') as file:
        foundFunction = False
        stack = []
        function = []
       
        for i, line in enumerate(file):
            if re.match(javaExp, line):
                foundFunction = True
                stack.append("{")
                function.append(line)
                print(f"function starts here: {line}")
                print(i)
                startIndexes.append(i)
                continue

            if foundFunction and "{" in line:
                stack.append("{")
                function.append(line)
            if foundFunction and "}" in line and len(stack) == 1:
                stack.pop()
                foundFunction = False
                function.append(line)
                functionCode.append(function)
                print(f"function ends here: {line}")
                print(i)
                endIndexes.append(i)
                function = []
            elif foundFunction and "}" in line:
                stack.pop()
                function.append(line)
            elif foundFunction:
                function.append(line)
        print(f"There are {last} lines in the file")
        startIndexes.append(last)
    return functionCode

def commentCode(filepath: str, functionCode: list[str]):
    newCode = []
    with open(filepath, 'r') as file:
        content = file.read().splitlines(True)
        newCode = content[:startIndexes[0]] #all the code before the first function
        print(newCode)
        for i in range(len(functionCode)):
            if i == len(functionCode) -1:
               newCode+=functionCode[i]+"".join(content[endIndexes[i]])
            else: 
               newCode+= functionCode[i]+ "".join(content[endIndexes[i]: startIndexes[i+1]])
        #adds the function code and then what was left until the start of the next function 
        #it works but I'm not sure how
    with open(filepath, 'w') as file:
        file.writelines(newCode)   
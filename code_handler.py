import re
from enums import Languages

javaExp = r'^\s*(?:public|private|protected)?\s+(?:static\s+)?(?:\w+\s+)?\w+\s+\w+\s*\([^)]*\)\s*{'
pythonExp = r'^\s*def\s+\w+\s*\([^)]*\)\s*:\s*'



def getFunctionCode(filepath: str, language: str = "J"):
    functionCode = []
    with open(filepath, 'r') as file:
        foundFunction = False
        stack = []
        function = []
        for line in file:

            if re.match(javaExp, line):
                foundFunction = True
                stack.append("{")
                function.append(line)
                continue

            if foundFunction and "{" in line:
                stack.append("{")
                function.append(line)
            if foundFunction and "}" in line and len(stack) == 1:
                stack.pop()
                foundFunction = False
                function.append(line)
                functionCode.append(function)
                function = []
            elif foundFunction and "}" in line:
                stack.pop()
                function.append(line)
            elif foundFunction:
                function.append(line)
    return functionCode


            
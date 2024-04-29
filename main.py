from code_handler import getFunctionCode, commentCode
from ai_wrapper import getCommentedCode

def main():
    functions = getFunctionCode('Challenge.java')
    functionCode = []
    for function in functions:
        functionCode.append(getCommentedCode(''.join(function)).replace("```java", "").replace("```", ""))
    print(functionCode)
    
    commentCode('Challenge.java', functionCode)
main()
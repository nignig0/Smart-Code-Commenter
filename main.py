from code_handler import getFunctionCode, commentCode
from ai_wrapper import getCommentedCode

def main():
    functions = getFunctionCode('test.java')
    functionCode = []
    for function in functions:
        functionCode.append(getCommentedCode(''.join(function)).replace("```java", "").replace("```", ""))
    
    
    commentCode('test.java', functionCode)
main()
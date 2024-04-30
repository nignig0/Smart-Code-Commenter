from code_handler import getFunctionCode, commentCode
from ai_wrapper import getCommentedCode
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filepath>")
    filepath = sys.argv[1]
    functions = getFunctionCode(filepath)
    functionCode = []
    for function in functions:
        functionCode.append(getCommentedCode(''.join(function)).replace("```java", "").replace("```", ""))
    
    
    commentCode(filepath, functionCode)
main()
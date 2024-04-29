from code_handler import getFunctionCode
from ai_wrapper import getCommentedCode

def main():
    functions = getFunctionCode('test.java')
    for function in functions:
        print(getCommentedCode(''.join(function)))

main()
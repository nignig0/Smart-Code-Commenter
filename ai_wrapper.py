import google.generativeai as genai
import os

api_key=os.environ.get('GEMINI_KEY')
genai.configure(api_key=api_key)

def getCommentedCode(someCode):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Help me leave javadoc comments at the top of functions and then in the body of functions, you comment information about hard to understand lines or logic. Help me with this: {someCode}")
    return response.text
import os
try:
    if os.path.exists("E:\\Programming\\Data Analyst\\python programming\\programs\\fijhgle25.txt"):
        os.remove("E:\\Programming\\Data Analyst\\python programming\\programs\\file24.txt")
except:
    print("file not found")
else:
    print("file deleted successfully")
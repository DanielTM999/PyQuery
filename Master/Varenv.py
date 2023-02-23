import os
import dotenv

class DotEnv:
    def GetDotenv(env = list):
        dotenv.load_dotenv(dotenv.find_dotenv())
        dic = []
        for i in env:
            dic.append(os.getenv(i))
        
        return dic
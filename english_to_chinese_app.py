import evadb
import warnings
import os

cursor = evadb.connect().cursor()
warnings.filterwarnings("ignore")

params = {
    "user": "eva",
    "password": "password",
    "host": "localhost",
    "port": "5432",
    "database": "chinese",
}

query = f"CREATE DATABASE IF NOT EXISTS pg_db WITH ENGINE = 'postgres', PARAMETERS = {params};"
cursor.query(query).df()

cursor.query("""USE pg_db {CREATE TABLE IF NOT EXISTS english_chinese (english TEXT, chinese TEXT)}""").df()

cursor.query("""
USE pg_db {
  COPY english_chinese(english, chinese)
  FROM 'C:\\Users\Carolyn Yuan\Documents\GitHub\English_To_Chinese_App\output.csv'
  DELIMITER ',' CSV HEADER}
""").df()

# replace OpenAI key with your own

os.environ["OPENAI_KEY"] = "sk-..."

print("Welcome! Enter an english term/technical vocabulary in the artificial intelligence domain!")
ready = True
while ready:
    question = str(input("Word (enter 'exit' to exit): "))
    if question.lower() == "exit":
        ready = False
    else:
        # Generate response with chatgpt udf
        print("⏳ Generating response (may take a while)...")
        query = "USE pg_db {SELECT chinese FROM pg_db.chinese WHERE english = ", question, ";}"
        chinese = cursor.query(query).df()
        if len(chinese) == 1:
            prompt = "Identify and suggest 3 specialized terminology and technical terms commonly used in the subject matter of"
            response = cursor.table("Response").select(f"ChatGPT({prompt}, {chinese})").df()["chatgpt.response"][0]
        print("✅ Translation and background:", response)

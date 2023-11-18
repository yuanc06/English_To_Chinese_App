import warnings
import os
import sqlite3

warnings.filterwarnings("ignore")

params = {
    "user": "eva",
    "password": "password",
    "host": "localhost",
    "port": "5432",
    "database": "evadb.db",
}

query = f"CREATE DATABASE sqlite_data WITH ENGINE = 'sqlite', PARAMETERS = {params};"
con = sqlite3.connect("evadb.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS english_chinese(english TEXT, chinese TEXT)")

cur.execute("""
  COPY english_chinese(english, chinese)
  FROM 'C:\\Users\Carolyn Yuan\Documents\GitHub\English_To_Chinese_App\output.csv'
  DELIMITER ',' CSV HEADER}
""")
con.commit()

# can use executemany with ? to avoid SQL injection attacks for inserting multiple rows
# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data) 

#-------------------- TESTING --------------------#
res = cur.execute("SELECT english FROM english_chinese")
res.fetchall()

for row in cur.execute("SELECT english, chinese FROM english_chinese"):
    print(row)

con.close()
new_con = sqlite3.connect("evadb.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT english, chinese FROM english_chinese")
english, chinese = res.fetchone()
print(f'The term {english!r} is {chinese} in mandarin.')
#-------------------- TESTING --------------------#

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
        res = "SELECT chinese FROM sqlite_master WHERE english = ", question, ";}"
        chinese = res.fetchone()
        if len(chinese) == 1:
            prompt = "Identify and suggest 3 specialized terminology and technical terms commonly used in the subject matter of"
            response = cur.table("Response").select(f"ChatGPT({prompt}, {chinese})")["chatgpt.response"][0]
        print("✅ Translation and background:", response)

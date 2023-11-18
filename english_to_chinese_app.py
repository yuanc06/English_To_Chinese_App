import warnings
import os
import sqlite3
import csv

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

csv_file_path = 'C:\\Users\\Carolyn Yuan\\Documents\\GitHub\\English_To_Chinese_App\\output.csv'
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header row if it exists
    for row in csvreader:
        cur.execute('INSERT INTO english_chinese (english, chinese) VALUES (?, ?)', (row[0], row[1]))
con.commit()

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

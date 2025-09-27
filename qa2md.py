import csv
import re
import os


questions = []
answers = []


def doesFileExists(targetFile, dataFile):
    if(os.path.isfile(targetFile) and os.path.isfile(dataFile)):
        return True
    else:
        return False
    

def run(file_path, md_file):
    if(doesFileExists(file_path, md_file)):
        with open(file_path, mode='r', newline='', encoding='ISO-8859-1') as file:
            reader = csv.reader(file)
            next(reader)


            for row in reader:
                if len(row) >= 2:    
                    question = row[0]
                    answer   = row[1]

                    questions.append(question)
                    answers.append(answer)
                else:
                    print("err")

        print(questions)
        print(answers)

        #loop throu the arr and make a var with the text and html code and so on and vars

        for i in range(len(questions)):
            text_to_write = f"""{i+1}. {questions[i]}
                <details>
                <summary>Show Answer</summary>
                {answers[i]}
                </details>"""

            with open(md_file, "a") as file:
                file.write(f"{text_to_write}\n")

    else:
        print("MD or Data file does not exists or you entered the wrong path")
        askPath()


def askPath():
    try:
        file_path = input("Enter FULL file path to data: ")
        file_path = re.sub('"', '', file_path)
        md_file   = input("Enter FULL path to write to: ")
        md_file   = re.sub('"', '', md_file)
        run(file_path, md_file)
    except:
        print("\nProgramm stops on that request")
        quit()

#starting the program the first time
askPath()

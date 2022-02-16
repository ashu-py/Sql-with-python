

import time as t
print("this is made by ashu-py");t.sleep(1);

print("entre sql query : [remember to put ';' in the last of every line of your query and press entre twice to execute your query")

try:

        lines = [];
        while True:

                line=input()
                if line:
                        lines.append(line)
                else:
                        break
        text = '\n'.join(lines)

        import sqlite3 as s
        def query():

                file=input("entre path of file or db\n")
                c=s.connect(file);t.sleep(1);
                print("connection is satablished with database\n")
                cu=c.cursor()                                                                                                         cu.execute(text);
                c.commit()                                                                                                            print(cu.fetchall())
                for row in cu.execute(text):
                        print(row)
                c.close()
        query()
except Exception as e:
        print(e)

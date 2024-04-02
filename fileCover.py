import re
file_name = "1.txt"
file_newName = "2.txt"

def replace_string(text):
    pattern = r'\d+@(\w.+)@'
    replaced_text = re.sub(pattern, r'@\1~', text)
    return replaced_text
def file_write(file_name,file_newName):
    with open(file_name,"r",encoding="utf-8") as f1, open(file_newName,"w",encoding="utf-8") as f2:
        file_line = f1.read()
        f2.write(replace_string(file_line))
        print("格式转化完成")
        f1.close()
        f2.close()

if __name__ == "__main__":
    file_write(file_name=file_name,file_newName=file_newName)
    input("\n按任意键结束\n")


        

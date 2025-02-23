import re

# 使用正则表达式插入额外的字符
def insert_text(line, func_text=""):
    # 如果该行被双引号包含，则不进行替换
    if re.match(r'.*".*".*', line): return line

    if func_text == "": return line
    variable = get_variable_name(line)
    # 获取行首的空白字符
    indent = re.match(r"^\s*", line).group(0)  # 捕获行首的空白字符
    # 确保没有变量是 None
    if line is None or indent is None or variable is None or func_text is None:
        raise ValueError("One of the variables is None, cannot concatenate.")
    new_line = line + indent + variable + func_text + "\n"
    print(new_line)
    return new_line


def replace_text(line,old_pattern,new_pattern):
    if old_pattern in line:
        new_line = line.replace(old_pattern, new_pattern)
        print(new_line)
        return new_line, True
    return line, False


def get_variable_name(line):
    # 正则表达式匹配等号前的字符
    match = re.match(r"^\s*([a-zA-Z0-9_\.#][a-zA-Z0-9_\.]*)\s*=", line)  # 匹配等号前的变量名，允许有空白字符  # 匹配等号前的变量名
    if match:
        print(match.group(1))
        return match.group(1)
    return None

if __name__ == "__main__":
    target_file = r".\main\Ui_mainwindow.py"
    #target_file = r".\SmodernUI\component\ui\Ui_dialog.py"
    #target_file = r"test.py"

    old_pattern = "QPushButton"  # 捕获行首的空白字符
    #old_pattern = "QWidget"

    new_pattern = "CButton"
    #new_pattern = "CContainer"

    func_text = ".setTipText(\"\")"  # 你想插入的字符

    # 打开文件读取内容
    with open(target_file, "r", encoding="utf-8") as file:
        content = file.readlines()

    #遍历文件内容并进行替换
    new_content = []
    for line in content:
        # 如果 line 只有空格或者为空，直接返回改行
        if not line.strip():
            new_content.append(line)
            continue
        # 如果 line 是注释，直接返回改行
        if line.startswith("#"):
            new_content.append(line)
            continue

        # 替换文本
        replaced_line, flag = replace_text(line,old_pattern,new_pattern)

        if not flag:
            new_content.append(replaced_line)
            continue
        # 插入字符
        inserted_line = insert_text(replaced_line,func_text)
        new_content.append(inserted_line)


    #将修改后的内容写回文件
    with open(target_file, "w", encoding="utf-8") as file:
        file.writelines(new_content)
    print("替换并插入字符完成")

import re

def replace_and_insert(filename, target_char, replacement_char, insert_char):
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        if target_char not in line:
            new_lines.append(new_line)
        # 1. 替换目标字符
        new_line = line.replace(target_char, replacement_char)
        # 2. 判断当前行是否以引号开头和结尾
        if (new_line.startswith('"') and new_line.endswith('"')) and replacement_char in new_line:
            # 如果行以引号开头和结尾，直接添加该行
            new_lines.append(new_line)
        elif (not new_line.startswith('"') and not new_line.endswith('"')) and replacement_char in new_line:
            # 3. 获取当前行的空白字符
            leading_whitespace = len(new_line) - len(new_line.lstrip())
            # 4. 将修改后的当前行添加到新列表
            # new_lines.append(new_line)
            # 5. 新增一行并对齐
            new_inserted_line = new_line + "\n" + leading_whitespace + insert_char + "\n"
            #new_inserted_line = ' ' * leading_whitespace + insert_char
            new_lines.append(new_inserted_line)  # 在当前行后插入新行

    # 写回修改后的内容
    with open(filename, 'w') as file:
        file.writelines(new_lines)

# 调用示例
target_file = "test.py"
old_pattern = "QPushButton"  # 要替换的目标字符
new_pattern = "CButton"  # 替换后的字符
additional_text = "// Additional text"  # 要插入的字符
replace_and_insert(target_file, old_pattern, new_pattern, additional_text)

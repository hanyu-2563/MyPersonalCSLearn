import re

# 通过正则表达式提取英文单词
def extract_english_words(line):
    return re.findall(r'\b[a-zA-Z]+\b', line)

# 将单词写入txt文件
with open('input.txt', 'r') as input_file, \
        open('output.txt', 'w') as output_file:
    for line in input_file:
        words = extract_english_words(line)
        for word in words:
            output_file.write(word + '\n')

print("英文单词已提取到output.txt文件中。")


for i, line in enumerate(input_file):
    print(f'正在处理第 {i} 行')
    words = extract_english_words(line)
    for word in words:
        output_file.write(word + '\n')
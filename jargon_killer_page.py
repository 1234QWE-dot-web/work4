from PIL import Image, ImageTk
import random as rd

#复制列表
def copy_d(dictionary):
    """copy a dictionary."""
    new_dictionary = {}
    for keys, values in dictionary.items():
        new_dictionary[keys] = values
    return new_dictionary

#导入图片
def get_image(filename,width, height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

#导入单词数据
def file_access(file):
    dictionary = {}
    try:
        file_path = file
        with open(file_path, 'r', encoding='utf-8') as file_input:
            for words_meanings in file_input:
                word_meaning = words_meanings.split(':')       #储存jargons的文件形式必须是words: meanings（英文在前中文在后）
                word = word_meaning[0].strip()      #英文单词   #一个单词及中文意思对应一行，冒号必须为英文冒号
                meaning = word_meaning[1].strip()   #中文含义
                dictionary[word] = meaning
        return file_path, dictionary
    except:
        file_path = ''
        return file_path, dictionary

# all模块
#字母表
def alphabet(upper = False):
    """return the alphabet, 'True' as the upper form."""
    alphabet_initial = "abcdefghijklmnopqrstuvwxyz"
    if upper == True:
        alphabet = list(alphabet_initial.upper())
        return alphabet
    else:
        alphabet = list(alphabet_initial)
        return alphabet

#将列表元素按首字母归类
def classify(data):
    """classify elements of a list into groups distinguished by the first letter, return as a dictionary."""
    classify_result = {}
    alphabet_letters = alphabet()
    for letter in alphabet_letters:
        element_classified = []
        for element in data:
            if element[0].lower() == letter:
                element_classified.append(element)
        element_classified.sort()
        classify_result[letter.upper()] = element_classified
    return classify_result

#获取字典中的键（此种方法不同于.keys()，返回的是可编辑、可索引的列表）
def d_keys(dictionary):
    """access the keys of a dictionary, return as a list."""
    dictionary_keys = []
    for x in dictionary.keys():
        dictionary_keys.append(x)
    return dictionary_keys

#获取字典中的值
def d_values(dictionary):
    """access the values of a dictionary, return as a list."""
    dictionary_values = []
    for y in dictionary.values():
        dictionary_values.append(y)
    return dictionary_values

#search模块
def find(data, key_words):
    """find the elements in a list that contains the key_words desired, return as a list."""
    if key_words:
        find_result = []
        data_cp = data[:]
        data_cp.sort()
        for element in data_cp:
            if key_words.lower() in element.lower():
                find_result.append(element)
        return find_result
    else:
        return None

def index(element, data = []):
    """identify the index of an element first occur in a list."""
    if data:
        if element not in data:
            return None
        else:
            x = 0           #x计数索引
            for i in range(len(data)):
                if element == data[x]:
                    break
                else:
                    x += 1
            return x
    else:
        return None

#practise
#评价答题情况
def comment(answer_number):
    text = "Your performance this time: \n"
    correct_rate = (answer_number['c_number']/(answer_number['c_number'] + answer_number['w_number']))*100
    correct_rate_print = f"{round(correct_rate, 1)}%"
    text += f"\nCorrect: {answer_number['c_number']}    Wrong: {answer_number['w_number']}    Correct rate: {correct_rate_print}\n"
    if correct_rate < 60:
        text += "\nFailed, you need to study harder."
    elif 60 <= correct_rate < 80:
        text += "\nGood, you still need to practise more."
    elif 80 <= correct_rate < 90:
        text += "\nWell done! Keep moving forward."
    elif 90 <= correct_rate <= 100:
        text += "\nExcellent! Keep up the good work."
    return text

def copy_d(dictionary):
    """copy a dictionary."""
    new_dictionary = {}
    for keys, values in dictionary.items():
        new_dictionary[keys] = values
    return new_dictionary
#pratiseA模块
def answer_choose(correct_choice, choices):
    choice_options = ['A','B','C','D']
    choice = rd.sample(choices, 4)
    choice_with_xuhao = []
    while True:
        x = 0
        for letter in choice_options:           #显示题目
            choice_with_xuhao.append(f"{letter}  {choice[x]}")
            if choice[x] == correct_choice:
                correct_answer_num = x + 1
            x += 1
        break
    return correct_answer_num, choice

def E_meaning_select(dictionary):
    choice_library = d_keys(dictionary)
    correct_answer = rd.choice(choice_library)
    del dictionary[correct_answer]
    choice_library.remove(correct_answer)
    answers = rd.sample(choice_library, 3)
    answers.append(correct_answer)
    options = []
    for answer in answers:
        options.append(dictionary[answer])
    correct_answer_num,choice= answer_choose(dictionary[correct_answer], options)
    return correct_answer, correct_answer_num, choice, dictionary

#写入数据
def file_write(file_path, dictionary):
    """write the glossary to the original path."""
    with open(file_path, 'w', encoding='utf-8') as file_output:
        for word, meaning in dictionary.items():
            word_meaning = f"{word}: {meaning}\n"
            file_output.write(word_meaning)
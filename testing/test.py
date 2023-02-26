file = open('question.txt', 'r', encoding = "UTF-8").read()

true_answers_list = []
paragraphs_list = []
for paragraph in file.split('\n\n'):
    paragraphs_list.append(paragraph)
    for a in paragraph.split("\n"):
        if str(a)[0] == "+":
            true_answers_list.append(a[2:])

answer_number = 0
trueanswers = 0
for paragraph in paragraphs_list:
    answers = []
    for string in paragraph.split("\n"):
        if string[0] != "-" and string[0] != "+":
            print(string)
        else:
            answers.append(string[2:])
    print(" ".join(answers))
    print(" ")

    x = input("Введите номер ответа: ")
    
    while len(str(x)) > 1:
        print("Ответ должен быть однозначным, попробуйте снова.")
        x = input("Введите номер ответа: ")
    while x.isalpha() == False:
        print("Ответ должен состоять из однозначного числа, попробуйте снова.")
        x = input("Введите номер ответа: ")

    x = int(x)

    if (answers[x - 1])[0] == (true_answers_list[answer_number])[0]:
        print('Вы ответили правильно!')
        trueanswers += 1
    else:
        print("Вы ответили неправильно")

    print(" ")
    answer_number += 1

print(f"Тест пройден. Количество правильных ответов = {trueanswers}.")

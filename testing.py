with open('questions.txt', 'r', encoding = "UTF-8") as file:
    while True:
        try:
            answers = open("answers.txt", "r")

            trueanswers = 0
            
            # Первый вопрос 
            # 
            # 

            print("\n" + (file.read().split(', ')[0]))
            file.seek(0) 
            print("Варианты ответа:\n1. Кортеж неизменяемый\n2. Список неизменяемый\n3. Кортеж и список ничем не отличаются\n")
            userAnswer = int(input("Введите номер варианта ответа: "))

            if userAnswer == int(answers.read().split(', ')[0]):
                print("Ответ принят, переходим к следующему вопросу.")

                trueanswers += 1
            answers.seek(0)
            
            # Второй вопрос 
            # 
            # 

            print("\n" + (file.read().split(', ')[1]))
            file.seek(0) 
            print("Варианты ответа:\n1. Обновление синтаксика Python\n2. Функции\n3. Логарифмы\n")
            userAnswer = int(input("Введите номер варианта ответа: "))

            if userAnswer == int(answers.read().split(', ')[1]):
                print("Ответ принят, переходим к следующему вопросу.")

                trueanswers += 1
            answers.seek(0)    

            # Третий вопрос 
            # 
            # 

            print("\n" + (file.read().split(', ')[2]))
            file.seek(0) 
            print("Варианты ответа:\n1. Нет\n2. Да\n")
            userAnswer = int(input("Введите номер варианта ответа: "))

            if userAnswer == int(answers.read().split(', ')[2]):
                print("Ответ принят, переходим к следующему вопросу.")
            
                trueanswers += 1
            answers.seek(0)    

            # Четвёртый вопрос 
            # 
            # 

            print("\n" + (file.read().split(', ')[3]))
            file.seek(0) 
            print("Варианты ответа:\n1. input\n2. print\n3. split")
            userAnswer = int(input("Введите номер варианта ответа: "))
            
            if userAnswer == int(answers.read().split(', ')[3]):
                print("Ответ принят, переходим к следующему вопросу.")

                trueanswers += 1
            answers.seek(0)

            # Пятый вопрос 
            #  
            # 

            print("\n" + (file.read().split(', ')[4]))
            file.seek(0) 
            print("Варианты ответа:\n1. Компилируемый\n2. Интерпретируемый\n")
            userAnswer = int(input("Введите номер варианта ответа: "))

            if userAnswer == int(answers.read().split(', ')[4]):
                print("Ответ принят, переходим к подсчёту результатов.")
            
                trueanswers += 1
            answers.seek(0)
                
            print(f'Вы прошли тест! Количество правильных ответов = {trueanswers}')  
            break

        except ValueError:
            print("\n\nВы ввели не число, так что Вам придётся начать заново!")
            print("Вы ввели не число, так что Вам придётся начать заново!")
            print("Вы ввели не число, так что Вам придётся начать заново!\n\n")

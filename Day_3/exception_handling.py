try:
    age = int(input('Age: '))
    income=10000
    risk=income/age
    print(risk)
except ZeroDivisionError:
    print('Zero Division Error')
except ValueError:
    print('Value error')


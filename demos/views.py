from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def calculator(request):
    # return HttpResponse('게산기 구현기능')

    #데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    #계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    #응답
    return render(request, 'calculator.html', {'result': result})

def lotto(request):
    game = request.GET.get('game') #게임 수
    print(game)
    # lotto_list = []
    # for i in range(7):
    #     lotto_list.append(random.randint(1,45))
    # print(lotto_list)
    return render(request, 'lotto.html', {'game':game})
    
def lotto_result(request):
    game = request.GET.get('lotto') #게임 수를 받아옴
    lotto_list = []
    for i in range(int(game)):
        lotto = []
        for j in range(7):
            lotto.append(random.randint(1,45))
        lotto_list.append(lotto)
    print(lotto_list)
    return render(request, 'lotto_result.html', {'game':game, 'lotto_list': lotto_list})
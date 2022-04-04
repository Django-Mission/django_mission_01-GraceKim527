# [Django Mission 01] Challenge Mission Complete✨

--- 

## Result

### Challenge Mission
![Hnet-image](https://user-images.githubusercontent.com/80322308/161522129-810046f4-3324-443a-af8f-5f65b7518360.gif)

---

## Of Developement
### views.py
```python
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
```

# Python에서 언더스코어(_)는 문법적으로 굉장히 많은 곳에서 사용된다
# 첫째로 언더스코어는 '의미 없는 값'을 표현할 수 있으며, Unpacking 시 값을 무시하기 위해 사용할 수 있다

a, _, _, b = [1, 2, 3, 4]
print(_) # 3
# 언더스코어도 다른 변수들과 동일하게 바인딩이 이루어지지만,
# 의미 없는 값을 표현하기 위한 관례적인 요소다

a, *_, b = [1, 2, 3, 4, 5]
# extended unpacking에도 사용 가능

for _ in [1, 2, 3, 4, 5]:
    print('Not over yet')

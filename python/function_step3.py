# 함수3 : 함수 응용

def get_vat(price, vat_rate=0.1): # ... 매개변수(parameter) 사용
    return price*vat_rate

print(get_vat(10000)) # 1000.0
print(get_vat(10000, 0.2)) # 2000.0 ... 인자(argument) 전달
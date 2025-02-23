from main import add_one, division, is_palindrom

import pytest

def test_answer():
    # Оператов assert - это встроенный оператор в Python, позволяющий отслеживать код. Этот оператор принимает условие и необязательное сообщение, которое выходит при исключении AssertionError. Исключение AssertionError выходит когда assert встречает False, если assert True, то ничего не произойдет
    assert add_one(5) == 5,   'Тест не прошел проверку' 
    
def test_division():
    assert division(10, 5) == 2 , 'Удаление неправильно работает'
    
@pytest.mark.parametrize(
    'a, b, res',
    [(10, 5, 2), (12, 6, 2), (9, 3, 3)]
)
def test_division2(a, b, res):
    assert division(a, b) == res
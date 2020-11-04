______

## Задача 1

Имеем dictionary со следующей структурой и данными:
d = {
    "a": 5,
    "b": 6,
    "c": {
        "f": 9,
        "g": {
            "m": 17,
            "n": 3
        }
    }
}
Необходимо написать функцию flatten(d), которая на входе получает dictionary с указанной выше структурой и возвращает dictionary вида:
    {
        'a': 5,
        'b': 6,
        'c.f': 9,
        'c.g.m': 17,
        'c.g.n': 3
    }
Алгоритм должен работать для общего случая, т.е. превращать любой многоуровневый dictionary в одноуровневый, с ключами, как указано выше.

______

## Задача 2

Необходимо написать алгоритм (приложение, работающее из командной строки), который на входе получает валидный XML документ, и возвращает в виде результата максимальную глубину вложенности тегов в данном документе. Глубина измеряется в целых числах: 0, 1, 2 и т.д., при этом глубина корневого тэга принимается равной 0.
При написании алгоритма могут использоваться любые библиотеки для парсинга XML.
Пример:
Содержимое XML документа:
<feed xml:lang='en'>
    <title>NPBFX</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://npbfx.com/' />
    <updated>2020-10-28T12:00:00</updated>
</feed>
Результат работы алгоритма: 1
В данном примере тэг feed имеет глубину вложения: 0. Тэги title, subtitle, link и updated: 1. Поэтому максимальная глубина: 1.

______

## Запуск

1. Установка виртуального окружения.  
`python3 -m venv venv`
2. Активация и установка необходимыз библиотек.  
`source venv/bin/activate`  
`pip3 install -r requirements.txt`


### Задача 1

`python3 task_flatten.py`

### Задача 2

```
python3 task_xml.py "<feed xml:lang='en'>                 
                <title>
                    <a>kek</a>
                </title>
                <subtitle lang='en'>Programming challenges
                    <number>kek
                        <a>kek</a>
                    </number>
                </subtitle>
                <link rel='alternate' type='text/html' href='http://npbfx.com/' />
                <updated>2020-10-28T12:00:00</updated>
                </feed>"
```

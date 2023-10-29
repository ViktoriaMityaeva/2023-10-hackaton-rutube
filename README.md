| Организатор  | Кейсодержатель |
| ------------- | ------------- |
| <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/cplogo.jpg">  | <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/rutube-logo.jpg">  |

# Распознавание именованных сущностей в названиях и описаниях к видео

## Оглавление
1. [Задание](#zadanie)
2. [Описание решения](#solution)
3. [Запуск](#startup)
4. [Стек](#stack)
5. [Команда](#team)
6. [Ссылки](#urls)

## <a name="zadanie"> Задание </a>

В рамках развития рекомендательной системы и поискового движка RUTUBE важную роль играет работа c контентом, а именно с текстовым названием и описанием к видео. Анализируя данный контент, можно выявлять так называемые именованные сущности и определять, к какому классу они относятся.
Корректное извлечение данных именованных сущностей и распознавание их классов окажет существенную помощь в улучшении качества рекомендаций и поиске.
Участникам хакатона предлагается разработать прототип системы распознавания именованных сущностей в названиях и описаниях к видео.

## <a name="solution">Решение </a>


### Функциональная модель
<img width="900" height="400" alt="func_scheme" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/func_model.png"> 

<br>
<p>Пример обработки </p>

| INPUT  | Обработка |
| ------------- | ------------- |
| "<НАЗВАНИЕ:> БОЕЦ БЕЗ ПРАВИЛ, ТРЕЙЛЕР на русском, фильм 2021| боевик, MMA <ОПИСАНИЕ:>Больше информации в нашей группе ВК: <LINK> Русский трейлер фильма БОЕЦ БЕЗ ПРАВИЛ 2021 г 🎬 Боец без правил (2021) русский трейлер Notorious Nick (2021)/ США драма, боевик Дата выхода: 7 августа 2021 г (мир) 2 сентября 2021 г (Россия) Ник Ньюэлл, однорукий боец ММА, получает редкую возможность принять участие в чемпионате. Герой жаждет победить не только ради себя, но и ради людей со всего мира, которым знакомы физические трудности. Режиссер: Аарон Леонг Актёры: Элизабет Рём, Кевин Поллак, Коди Кристиан, Бэрри Ливингстон, Энтони Сноу, Сэмюэл Ивэн Хоровиц, Конлан Кисилевич, Марк С. Аллен, Эрик Йорн Сундквист #Боецбезправил #фильм2021 #русскийтрейлер #боиММА"  | ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Дата', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Дата', 'I-Дата', 'O', 'O', 'O', 'O', 'O', 'B-Дата', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Дата', 'O', 'O', 'B-локация', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Дата', 'I-Дата', 'I-Дата', 'I-Дата', 'O', 'O', 'O', 'B-Дата', 'I-Дата', 'I-Дата', 'I-Дата', 'O', 'B-локация', 'O', 'B-персона', 'I-персона', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-персона', 'I-персона', 'O', 'O', 'B-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'I-персона', 'I-персона', 'O', 'B-персона', 'I-персона', 'I-персона', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']  |


## <a name="startup">Запуск</a>

### Последовательные шаги для запуска кода:
1. Склонируйте гит репозиторий;    
```Bash
git clone https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube.git
```

2. перейдите в каталог;    
```Bash
cd 2023-10-hackaton-rutube\dataset
```

3. Создайте виртуальную среду;    
```Bash
python3 -m venv venv
```

4. Активируйте виртуальную среду;    
```Bash
source venb\bin\activate
```
5. Установите необходимые библиотеки;    
```Bash
pip install -r requirements.txt
```

6. Запустите notebook;    
```Bash
jupyter-notebook
```

## <a name="stack">Стек </a>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/scikit.jpg" title="scikit" alt="scikit" width="60" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/spacy.jpg" title="spacy" alt="spacy" width="50" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/torch.jpg" title="torch" alt="torch" width="50" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/transformers.jpg" title="transformers" alt="transformers" width="60" height="40"/>&nbsp;

## <a name="team">Команда </a>

*Состав команды "RGB"*    
*Артем Франчук   
*Виктория Митяева
*София Филина 
*Михаил Нуридинов

## <a name="urls">Ссылки </a>
 
- [ссылка на весы модели](https://disk.yandex.ru/d/oi_83x6jAtDpZA)    
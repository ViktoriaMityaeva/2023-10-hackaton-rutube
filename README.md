| Организатор  | Кейсодержатель |
| ------------- | ------------- |
| <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/cplogo.jpg">  | <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/rutube-logo.jpg">  |
# Распознавание именованных сущностей в названиях и описаниях к видео

## Оглавление
1. [Задание](#zadanie)
2. [Решение](#solution)
3. [Запуск](#startup)
4. [Фичи](#fichi)
5. [Стек](#stack)
6. [Команда](#team)
7. [Ссылки](#urls)

## <a name="zadanie"> Задание </a>

В рамках развития рекомендательной системы и поискового движка RUTUBE важную роль играет работа c контентом, а именно с текстовым названием и описанием к видео. Анализируя данный контент, можно выявлять так называемые именованные сущности и определять, к какому классу они относятся.
Корректное извлечение данных именованных сущностей и распознавание их классов окажет существенную помощь в улучшении качества рекомендаций и поиске.
Участникам хакатона предлагается разработать прототип системы распознавания именованных сущностей в названиях и описаниях к видео.

## <a name="solution">Решение </a>

Решение будет здесь

### Архетиктура модели
<img width="1200" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/arch-model.jpg"> 

<br>
<p>Предобработка текста</p>

| До обработки  | После обработки |
| ------------- | ------------- |
| <img width="100" height="50" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/predobr_text_before.png">  | <img width="100" height="50" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/predobr_text_before.png">  |


<br>
<p>Пример обработки изображения</p>

| До обработки  | После обработки |
| ------------- | ------------- |
| <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/predobr_text_before.png">  | <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/predobr_text_before.png">  |


## <a name="startup">Запуск</a>

### Последовательные шаги для запуска кода:
1. Склонируйте гит репозиторий;
```Bash
git clone https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube.git
```

## <a name="fichi">Фичи </a>

Мы используем комбинацию моделей для распознавания цифр с предварительной предобработкой выравниванием изображения в перспективе и последующей постобработкой в виде эвристик связанных с количеством предсказанных цифр

## <a name="stack">Стек </a>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;

## <a name="team">Команда </a>

*Состав команды "RGB"*    
*Артем Франчук (https://) - All*    
*Виктория Митяева (https://) - All*    
*София Филина (https://) - All*    
*Михаил Нуридинов (https://) - ML-engineer*    

## <a name="urls">Ссылки </a>

- [Гугл диск с материалами](https://)    
- [ссылка на весы модели детекции](https://)    
- [ссылка на весы модели выравнивания](https://)    
- [ссылка на скринкаст](https://)    
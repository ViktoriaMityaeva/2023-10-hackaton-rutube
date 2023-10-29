import spacy

def extract_named_entities(text):
    nlp = spacy.load("ru_core_news_lg")#ru_core_news_lg
    doc = nlp(text)
    
    entities = []
    for ent in doc.ents:
        if ent.label_ in ["PER", "LOC", "DATE", "ORG", "BRAND", "MODEL", "PROJECT", "SEASON", "EPISODE", "LEAGUE", "TEAM", "SPORT", "VIDEO_GAME"]:
            entity = {
                "label": ent.label_,
                "offset": ent.start_char,
                "length": len(ent.text),
                "segment": ent.text
            }
            entities.append(entity)
    return entities

text = "<НАЗВАНИЕ:> Мания/Русский трейлер/2022/Спорт/Драма/Фильм/Новинка/Кино/Премьера/ <ОПИСАНИЕ:>Русский трейлер фильма ""Мания"" 2022 года Дата выхода в РФ – 24 марта 2022 О фильме: Студентка Алекс одержима желанием стать лучшей во всём. Она записывается в университетскую команду по гребле, и вскоре девушке предстоит проверить предел собственных физических Оригинальное название: The Novice Страна: США Дистрибьютор: Capella Film Режиссер: Лорен Хэдэвей Жанр: спорт, драма В ролях: Изабель Фурман, Эми Форсайт, Дилон, Джонатан Черри, Кейт Драммонд"

entities = extract_named_entities(text)
for entity in entities:
    print(entity)

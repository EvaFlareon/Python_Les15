import requests
import chardet


def translate_it(input, output, from_lang, to_lang = 'ru'):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """

    with open(input, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        text = data.decode(result['encoding'])

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    lang = from_lang + '-' + to_lang

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()

    with open(output, 'w') as f:
        f.write(' '.join(response.get('text', [])))

    return ' '.join(response.get('text', []))


a = translate_it('DE.txt', 'DE_RU.txt', 'de')
b = translate_it('ES.txt', 'ES_RU.txt', 'es')
c = translate_it('FR.txt', 'FR_RU.txt', 'fr')
print(a)
print(b)
print(c)

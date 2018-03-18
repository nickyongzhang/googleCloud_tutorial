from google.cloud import translate
import six

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))


example_text ='''Python是纯粹的自由软件， 源代码和解释器CPython遵循 
GPL(GNU General Public License)协议。Python语法简洁清晰，特色之一
是强制用空白符(white space)作为语句缩进。
Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各
种模块（尤其是C/C++）很轻松地联结在一起。常见的一种应用情形是，使用Python
快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，
用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以
用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用
扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现。'''
translate_text('en', example_text)
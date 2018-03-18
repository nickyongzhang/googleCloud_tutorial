import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def language_analysis(text):
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.    
    document = types.Document(
                    content=text,
                    type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment


    entities = client.analyze_entities(document=document).entities

    return sentiment, entities


example_text = 'Python is such a great programming language'
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)

# entity types from enums.Entity.Type
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
               'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
for entity in entities:
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
    print(u'{:<16}: {}'.format('metadata', entity.metadata))
    print(u'{:<16}: {}'.format('salience', entity.salience))
    print(u'{:<16}: {}'.format('wikipedia_url',
          entity.metadata.get('wikipedia_url', '-')))
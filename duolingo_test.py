from dotenv import load_dotenv
import os
import duolingo

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# print(USERNAME, PASSWORD)


lingo  = duolingo.Duolingo(USERNAME, PASSWORD)
skills = lingo.get_learned_skills('la')
words_lists = map(lambda skill: skill['words'], skills)
# flatten them: https://stackoverflow.com/a/952952/3500171
words = [item for sublist in words_lists for item in sublist]

# print(len(skills))
# print(words)

# print(skills[0]['known_lexemes'])

la_to_en_translations = lingo.get_translations(words, source='la', target='en')
en_translation_lists = la_to_en_translations.values()
en_translations = [item for sublist in en_translation_lists for item in sublist]

dirty_en_to_la_translations = lingo.get_translations(en_translations, source='en', target='la')
# remove the empty translations
en_to_la_translations = filter(lambda item: item[1] != [], dirty_en_to_la_translations.items())
print(dict(en_to_la_translations))
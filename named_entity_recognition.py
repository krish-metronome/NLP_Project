from spacy import displacy
import en_core_web_sm

entityTagger = en_core_web_sm.load()

def performNERonEntireText(passage):
    passage = entityTagger(passage)
    print("Displaying all the entities present in the entire corpus:")
    print([(word.text, word.label_) for word in passage.ents])



def extractNERTagsFromRandomPassage(text):
    passage = entityTagger(text)
    displacy.render(passage, jupyter=True, style='ent')
    entity_labels = [word.label_ for word in passage.ents]
    return entity_labels


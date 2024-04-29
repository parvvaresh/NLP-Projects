import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher 

def get_entities(sent):
  Subject = ""
  Object = ""

  prv_token_dep = ""
  prv_token_text = ""

  prefix = ""
  modifier = ""


  for token in nlp(sent):
    if token.dep_ != "punct":
      if token.dep_ == "compound":
        prefix = token.text
        if prv_token_dep == "compound":
          prefix = prv_token_text + " " + token.text
    
    if token.dep_.endswith("mod") == True:
      modifier =  token.text
      if prv_token_dep == "compound":
          modifier = prv_token_text + " " + token.text
    if token.dep_.find("subj") ==  True:
      Subject = modifier + " " + prefix + " " + token.text
      prv_token_dep = ""
      prv_token_text = ""
      prefix = ""
      modifier = ""

    if token.dep_.find("obj") ==  True:
      Object = modifier + " " + prefix + " " + token.text



    prv_token_dep = token.dep_
    prv_token_text = token.text
  return {
      "Subject" : Subject.strip(),
      "object" : Object.strip(),

  }


def get_relation(sent):
  duc = nlp(sent)
  matcher = Matcher(nlp.vocab)

  pattern = [
      {'DEP':'ROOT'}, 
      {'DEP':'prep','OP':"?"},
      {'DEP':'agent','OP':"?"},  
      {'POS':'ADJ','OP':"?"}
  ]
  matcher.add("matching_1", [pattern]) 
  matches = matcher(duc)
  k = len(matches) - 1
  span = duc[matches[k][1]:matches[k][2]] 
  return(span.text)

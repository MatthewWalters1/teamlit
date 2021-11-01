import sys
from google.auth.credentials import AnonymousCredentials
from google.cloud import firestore
from google.cloud.firestore import Client

project_id = "teamlit-dd6f2"

credentials = AnonymousCredentials()
db = Client(project = project_id, credentials = credentials)

def addScore(name, score):
    # Create a name document with a score of score
    try:
        doc_ref = db.collection(u'scores').document(name)
    except:
        print('Could not add {name}\'s score, so the program will exit')
        sys.exit()
    doc_ref.set({
        u'score': score
    })

def getTopScores():
    try:
        scores_ref = db.collection(u'scores')
        query = scores_ref.order_by(u'score', direction=firestore.Query.DESCENDING).limit_to_last(10)
        docs = query.get()
    except:
        print('Could not get and store the top ten scores, so the program will exit')
        sys.exit()

    # Makes a string that contains the top ten list of scores with their players, separated by new lines
    topScores = ''
    for doc in docs:
        score = doc.to_dict().get(u'score')
        topScores += f'{doc.id}: {score}\n'

    # For testing purposes, prints the top scores
    # for doc in docs:
        #print(f'{doc.id} => {doc.to_dict()}')
    
    return topScores


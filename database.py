import sys
from google.auth.credentials import AnonymousCredentials
from google.cloud import firestore
from google.cloud.firestore import Client

project_id = "teamlit-dd6f2"

credentials = AnonymousCredentials()
db = Client(project = project_id, credentials = credentials)

def addScore(name, score):
    # Create an entry in the players collection with this player's new ID
    try:
        id_ref = db.collection(u'ids').document(u'id')
        getID = id_ref.get()
    except:
        print('Could not get the id document, so the program will exit')
        sys.exit()
    newID = getID.to_dict().get(u'nextID')

    # Increment the nextID value in the ids collection id document
    id_ref.set({
        u'nextID': str((int(newID) + 1))
    })
    
    # Create a newID document with a name of name and a score of score
    try:
        doc_ref = db.collection(u'scores').document(newID)
    except:
        print('Could not add scores document for current player, so the program will exit')
        sys.exit()
    doc_ref.set({
        u'name': name,
        u'score': score
    })

def getTopScores():
    try:
        scores_ref = db.collection(u'scores')
        query = scores_ref.order_by(u'score', direction=firestore.Query.DESCENDING).limit(10)
        docs = query.get()
    except:
        print('Could not get and store the top ten scores, so the program will exit')
        sys.exit()

    # Makes a string that contains the top ten list of scores with their players, separated by new lines
    topScores = ''
    for doc in docs:
        name = doc.to_dict().get(u'name')
        score = doc.to_dict().get(u'score')
        topScores += f'{name}: {score}\n'

    # For testing purposes, prints the top scores
    # for doc in docs:
        #print(f'{doc.id} => {doc.to_dict()}')
    
    return topScores


from google.auth.credentials import AnonymousCredentials
from google.cloud.firestore import Client

project_id = "teamlit-dd6f2"

credentials = AnonymousCredentials()
db = Client(project = project_id, credentials = credentials)

# The names of the document, name, and score are user-dependent, but
# for testing purposes this would create a 'test' document with a score of 1000
doc_ref = db.collection(u'scores').document(u'test')
doc_ref.set({
    u'score': 1000
})

scores_ref = db.collection(u'scores')
docs = scores_ref.stream()

# For testing purposes, prints the contents of the 'scores' collection
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')


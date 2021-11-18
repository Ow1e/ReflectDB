from reflect import Database, Identity, String, Value
from datetime import datetime
from random import randint
from tqdm import tqdm

db = Database("data.refldb", "data.refldc", experimental=False)
db.create_all()

class Template(db.Model):
    name = String()
    email = String()
    id = Identity()
    time = Value(10)
    random = Value(15)

def generate():
    return db.dumps(db.refine(Template, name="Owen Shaule", email="ow1e3@protonmail.com", time=datetime.now(), random=randint(1, 100000)))

values = []

value = int(input("Items for the test: "))

for i in range(value):
    values.append(generate())

for i in tqdm(values, desc="Submiting Values"):
    db.publish(i)
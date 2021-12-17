from tqdm import tqdm # Install TQDM for tests
from reflect.database import Database, Identity, String, Value, SubBase

db = Database("data.refldb")
db.create_all()

class Names(db.Model):
    name = String()
    email = String()
    identity = Identity()

people = SubBase("people")

test_amount = 10000

for i in tqdm(range(test_amount)):
    x = db.refine(Names, people, name="Owie", email="Ow1e3@protonmail.com")
    y = db.dumps(x)
    db.publish(y)

with tqdm(total=test_amount) as t:
    db.query()
    t.update(test_amount)
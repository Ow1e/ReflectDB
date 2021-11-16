from tqdm import tqdm # Install TQDM for tests
from reflect.database import Database, Identity, String, Value

db = Database("data.refldb", "data.refldc")
db.create_all()

class Names(db.Model):
    name = String()
    email = String()
    identity = Identity()

test_amount = 10000

for i in tqdm(range(test_amount)):
    x = db.refine(Names, name="Owie", email="Ow1e3@protonmail.com")
    y = db.dumps(x)
    db.publish(y)

with tqdm(total=test_amount) as t:
    db.query()
    t.update(test_amount)
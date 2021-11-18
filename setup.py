from setuptools import setup

LONG_DESCRIPTION = """
# Reflect
A low level RAM free Database System

## Example
```python
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
```
"""

setup(
    name='reflectdb',
    version='0.1.5',    
    description='Low Ram Focused Database System in Python',
    url='https://github.com/Ow1e/ReflectDB',
    author='Owen Shaule',
    author_email='ow1e3@protonmail.com',
    license='',
    keywords=["python", "database"],
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    packages=['reflect'],
    install_requires=[],

    classifiers=[
    ],
)

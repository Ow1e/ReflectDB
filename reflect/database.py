"""
ReflectDB
A light weight Database System for Speeeeeeeeeeeeeeeeeeeed (Without taking Ram)

HAVING A SEPERATE FILE FOR ITERATIONS IS FASTER
YOU CAN CROSS SWITCH MANUALY BUT THERE IS NO BUILT IN WAY
WITHOUT MANUAL TRANSLATION THERE WILL BE A OVERIDE OR ERROR
(TRENDS HAVE THE SAME ISSUE, DO NOT TRANSLATE)

"""

import os

def Value(code, data = None):
    return {
        "value": data,
        "code": code
    }

def Identity():
    return Value(0)

def String(safety=128):
    return Value(1, safety)

class Database:
    path = "database.refl"
    id_keyword = "AUTOFILL"
    future_id = 0
    COMMANDS = [
        "REMOVE"
    ]
    seperate = False
    def __init__(self, path : str, seperate = False):
        self.path = path
        self.seperate = seperate
        if os.path.exists(path) and not seperate:
            with open(self.path) as f:
                self.future_id = int(f.read().split("\n")[1].split(" : ")[1])
                f.close()
        elif seperate:
            if os.path.exists(seperate):
                with open(seperate) as f:
                    self.future_id = int(f.read())
            else:
                with open(seperate, "w") as f:
                    f.write("0")


    def publish(self, content): # New Code, remember to use a seperate interger counter file
        content = content.replace(f"id:{self.id_keyword}", f"id:{self.future_id}")
        if not self.seperate:
            with open(self.path) as f:
                temp = f.readlines()
                f.close()
                temp[1] = "ITERATIONS : "+str(self.future_id + 1)+"\n"
                self.future_id += 1
                with open(self.path, "w") as w:
                    w.writelines(temp)
            with open(self.path, "a") as f:
                f.write(f"\n{content}")
        else:
            with open(self.seperate) as f:
                current = int(f.read())
                new = current+1
                f.close()
                with open(self.seperate, "w") as l:
                    l.write(str(new))
                    self.future_id += 1
            with open(self.path, "a") as f:
                f.write(f"\n{content}")

    def refine(self, model_object, *args, **kwargs):
        variables = []
        for i in dir(model_object):
            if not i.startswith("_"):
                variables.append(i)

        values = {}
        for i in variables:
            values[i] = (getattr(model_object, i))

        out = {}
        try:
            for i in values:
                if values[i]["code"] == 0:
                    if not kwargs.__contains__(i):
                        out["id"] = self.id_keyword
                    else:
                        out["id"] = values[i]["value"]
                elif values[i]["code"] == 1 and type(kwargs[i]) == str:
                    if values[i]["value"] < len(kwargs[i]):
                        raise ValueError("To many Chars compared to specified")
                    else:
                        out[i] = kwargs[i]
                else:
                    out[i] = kwargs[i]
        except KeyError as e:
            raise ValueError("Missing Variable!")

        if len(out) != len(values):
            raise ValueError("Missing Variable!")

        return out
    
    def smart_publish(self, database, **kwargs):
        self.publish(self.dumps(self.refine(database, )))


    def create_all(self):
        if not os.path.exists(self.path):
            if self.seperate:
                start = ["!! ReflectDB !!\n", f"SEPERATE: {self.seperate}"]
            else:
                start = ["!! ReflectDB !!\n", "ITERATIONS : -1"]
            with open(self.path, "w") as f:
                f.writelines(start)
                f.close()

    def dumps(self, object):
        prod = ""
        for i in object:
            prod += f"{i}:{object[i]}; "
        prod = prod.removesuffix(", ")
        return prod

    def loads(self, string : str):
        prod = {}
        identity = -1
        for i in string.split("; "):
            var = i.split(":")
            if var[0] != "id" and len(var) >= 2:
                prod[var[0]] = var[1]
            elif len(var) >= 2:
                identity = int(var[1])
        return identity, prod

    def query(self):
        with open(self.path) as f:
            ids = {}
            for i in f.read().split("\n")[2:]:
                if i.startswith("REMOVE"):
                    data = i.split()
                    ids[int(data[1])] = {}
                else:
                    identity, add = self.loads(i)
                    ids[identity] = add
        return ids

    def remove(self, id : int):
        with open(self.path, "a") as f:
            f.write(f"\nREMOVE "+str(id))

    def save_trend_data(self, i, *args, **kwargs):
        dump = f"id:{i}; "+self.dumps(kwargs)
        self.publish(dump)

    def __repr__(self):
        return "ReflectDB Object"

    class Model:
        # This is for a Model
        def __init__(self):
            print("Variables:")
            variables = ""
            for i in dir(self):
                if not i.startswith("__"):
                    variables += f"{i.upper()}, "
            variables = variables.removesuffix(", ")
            print(variables)


    # NEW TREND SYSTEM
    class Trend:
        iterations = int
        blacklist_dir = [
            "blacklist_dir",
            "iterations"
        ]
        # EXPERIMENTAL
        def __init__(self, start, end):
            print("ReflectDB Model System")
            for i in dir(self):
                if not i.startswith("__") and not i in self.blacklist_dir:
                    attribute = getattr(self, i)
                    self.iterations = start
                    for l in range(start, end):
                        self.iterations = l
                        attribute()
                        

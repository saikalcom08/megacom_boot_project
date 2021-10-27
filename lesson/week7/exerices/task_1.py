class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receive_call(self, call_name): # we receive dictionary
        self.call_name = call_name
        key = list(call_name.keys())
        key = "".join(key)
        print(f"Calling {key}")

    def get_number(self):
        print(self.call_name.get("Kiyal").get("work_number"))

kiyal = {
    "Kiyal": {"work_number": "+996706294910",
              "personal_number": "+996555461278",
              "home_number": "+996500638974"}
    }

phone1 = Phone("+996706294910", "iphone13", "60")
phone2 = Phone("+996555461278", "samsung s9+", "50")
phone3 = Phone("+996500638974", "nokia", "70")

phone1.receive_call(kiyal)
phone1.get_number()


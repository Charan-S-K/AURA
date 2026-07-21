class MemoryExtractor:

    def __init__(self):

        self.store_rules = [
            ("my name is", "name"),
            ("my college is", "college"),
            ("my university is", "university"),
            ("my city is", "city"),
            ("my hometown is", "hometown"),
            ("my favourite language is", "favorite_language"),
            ("my favorite language is", "favorite_language"),
        ]

        self.recall_rules = {
            "what is my name": "name",
            "what's my name": "name",

            "what is my college": "college",
            "which college do i study at": "college",

            "what is my university": "university",

            "what is my city": "city",

            "what is my hometown": "hometown",

            "what is my favorite language": "favorite_language",
            "what's my favorite language": "favorite_language",
        }

    def extract_store(self, message: str):

        text = message.lower()

        for trigger, key in self.store_rules:

            if trigger in text:

                value = message.split(trigger, 1)[1].strip()

                return key, value

        return None

    def extract_recall(self, message: str):

        text = message.lower()

        for question, key in self.recall_rules.items():

            if question in text:

                return key

        return None


memory_extractor = MemoryExtractor()
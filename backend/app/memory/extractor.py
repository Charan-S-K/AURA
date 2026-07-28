class MemoryExtractor:

    def __init__(self):

        self.store_rules = [

            ("i'm studying at", "college"),
            ("i study at", "college"),

            ("i work for", "company"),
            ("i work at", "company"),

            ("i'm from", "hometown"),
            ("i live in", "city"),

            ("my favourite language is", "favorite_language"),
            ("my favorite language is", "favorite_language"),

            ("my birthday is", "birthday"),

            ("my hometown is", "hometown"),
            ("my college is", "college"),
            ("my university is", "university"),
            ("my city is", "city"),
            ("my name is", "name"),

            ("i am an", "profession"),
            ("i'm an", "profession"),

            ("i am a", "profession"),
            ("i'm a", "profession"),

            ("i am ", "name"),
            ("i'm ", "name"),
        ]

        self.recall_rules = {

            "what is my name": "name",
            "what's my name": "name",
            "tell me my name": "name",

            "what is my college": "college",
            "where do i study": "college",

            "where do i work": "company",

            "what is my university": "university",

            "what is my city": "city",
            "where do i live": "city",

            "what is my hometown": "hometown",

            "what is my birthday": "birthday",
            "when is my birthday": "birthday",

            "what is my favorite language": "favorite_language",
            "what's my favorite language": "favorite_language",

            "what is my profession": "profession",
        }

    def extract_store(self, message: str):

        text = message.lower()

        for trigger, key in self.store_rules:

            if trigger in text:

                start = text.index(trigger) + len(trigger)

                value = message[start:].strip()

                return key, value

        return None

    def extract_recall(self, message: str):

        text = message.lower()

        for question, key in self.recall_rules.items():

            if question in text:

                return key

        return None


memory_extractor = MemoryExtractor()
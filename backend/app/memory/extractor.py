import json

from backend.app.services.llm.llm import llm_service


class MemoryExtractor:

    def __init__(self):

        # --------------------------------------------------
        # Explicit and unambiguous memory storage patterns
        # --------------------------------------------------

        self.store_rules = [

            ("my name is", "name"),

            ("my nickname is", "nickname"),

            ("my hometown is", "hometown"),

            ("my college is", "college"),

            ("my university is", "university"),

            ("my city is", "city"),

            ("i live in", "city"),

            ("i'm from", "hometown"),

            ("i study at", "college"),

            ("i'm studying at", "college"),

            (
                "my favourite language is",
                "favorite_language",
            ),

            (
                "my favorite language is",
                "favorite_language",
            ),

            (
                "my favorite food is",
                "favorite_food",
            ),

            (
                "my favourite food is",
                "favorite_food",
            ),

            (
                "my favorite color is",
                "favorite_color",
            ),

            (
                "my favourite color is",
                "favorite_color",
            ),

            (
                "my birthday is",
                "birthday",
            ),

            ("i work at", "company"),

            ("i work for", "company"),
        ]

        # --------------------------------------------------
        # Explicit memory recall patterns
        # --------------------------------------------------

        self.recall_rules = {

            "what is my name": "name",
            "what's my name": "name",
            "tell me my name": "name",

            "what is my nickname": "nickname",
            "what's my nickname": "nickname",

            "what is my college": "college",
            "what's my college": "college",
            "where do i study": "college",

            "what is my university": "university",
            "what's my university": "university",

            "what is my hometown": "hometown",
            "what's my hometown": "hometown",

            "what is my city": "city",
            "what's my city": "city",
            "where do i live": "city",

            "what is my company": "company",
            "what's my company": "company",
            "where do i work": "company",

            "what is my birthday": "birthday",
            "what's my birthday": "birthday",
            "when is my birthday": "birthday",

            "what is my favorite language":
                "favorite_language",

            "what's my favorite language":
                "favorite_language",

            "what is my favourite language":
                "favorite_language",

            "what's my favourite language":
                "favorite_language",

            "what is my favorite food":
                "favorite_food",

            "what's my favorite food":
                "favorite_food",

            "what is my favourite food":
                "favorite_food",

            "what's my favourite food":
                "favorite_food",

            "what is my favorite color":
                "favorite_color",

            "what's my favorite color":
                "favorite_color",

            "what is my favourite color":
                "favorite_color",

            "what's my favourite color":
                "favorite_color",
        }

    # ------------------------------------------------------
    # Store memory
    # ------------------------------------------------------

    def extract_store(
        self,
        message: str,
    ):

        text = message.lower().strip()

        for trigger, key in self.store_rules:

            if text.startswith(trigger):

                value = message[
                    len(trigger):
                ].strip()

                if value:

                    return key, value

        return None

    # ------------------------------------------------------
    # Recall memory
    # ------------------------------------------------------

    def extract_recall(
        self,
        message: str,
    ):

        text = message.lower().strip()

        # --------------------------------------------------
        # Exact / known recall patterns
        # --------------------------------------------------

        for question, key in self.recall_rules.items():

            if question in text:

                return key

        # --------------------------------------------------
        # Natural language recall patterns
        # --------------------------------------------------

        # Favorite color

        if (
            (
                "what color" in text
                or "what colour" in text
            )
            and "like" in text
        ):

            return "favorite_color"

        if (
            (
                "favorite color" in text
                or "favourite color" in text
            )
            and (
                "what" in text
                or "tell" in text
            )
        ):

            return "favorite_color"

        # Favorite food

        if (
            "what food" in text
            and "like" in text
        ):

            return "favorite_food"

        # Favorite language

        if (
            "what language" in text
            and "like" in text
        ):

            return "favorite_language"

        return None


memory_extractor = MemoryExtractor()
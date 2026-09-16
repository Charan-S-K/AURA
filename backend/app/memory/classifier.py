from dataclasses import dataclass
import json

from backend.app.services.llm.llm import llm_service


@dataclass
class MemoryClassification:
    remember: bool
    key: str | None = None
    value: str | None = None


class MemoryClassifier:

    ALLOWED_KEYS = {
        "name",
        "nickname",
        "city",
        "hometown",
        "college",
        "university",
        "company",
        "profession",
        "birthday",
        "favorite_language",
        "favorite_food",
        "favorite_color",
    }

    def classify(self, message: str) -> MemoryClassification:

        prompt = f"""
You are AURA's Memory Classification Engine.

Your job is to determine whether the user's message contains
personal information that AURA should remember.

Allowed memory keys:

{", ".join(sorted(self.ALLOWED_KEYS))}

Rules:

1. Return ONLY valid JSON.
2. Never invent a key.
3. Use only the allowed keys.
4. If there is no useful personal information, return:
   {{"remember": false}}
5. If there is personal information, return:
   {{
       "remember": true,
       "key": "...",
       "value": "..."
   }}
6. Extract only information explicitly stated by the user.
7. Do not guess.
8. Keep the value short and clean.

Examples:

User:
My name is Charan

Output:
{{"remember":true,"key":"name","value":"Charan"}}

User:
My friends call me Charan

Output:
{{"remember":true,"key":"nickname","value":"Charan"}}

User:
I live in Bangalore

Output:
{{"remember":true,"key":"city","value":"Bangalore"}}

User:
I'm from Mysore

Output:
{{"remember":true,"key":"hometown","value":"Mysore"}}

User:
I study at JSSATE

Output:
{{"remember":true,"key":"college","value":"JSSATE"}}

User:
I work at Google

Output:
{{"remember":true,"key":"company","value":"Google"}}

User:
I'm an ISE student

Output:
{{"remember":true,"key":"profession","value":"ISE student"}}

User:
My favorite color is purple

Output:
{{"remember":true,"key":"favorite_color","value":"purple"}}

User:
Tell me a joke

Output:
{{"remember":false}}

User message:

{message}
"""

        try:

            response = llm_service.generate_response(
                message=prompt,
                history=[],
            )

            start = response.find("{")
            end = response.rfind("}") + 1

            if start == -1 or end <= start:
                return MemoryClassification(False)

            data = json.loads(
                response[start:end]
            )

            if data.get("remember") is not True:
                return MemoryClassification(False)

            key = data.get("key")
            value = data.get("value")

            if key not in self.ALLOWED_KEYS:
                return MemoryClassification(False)

            if not isinstance(value, str):
                return MemoryClassification(False)

            value = value.strip()

            if not value:
                return MemoryClassification(False)

            return MemoryClassification(
                remember=True,
                key=key,
                value=value,
            )

        except Exception as e:

            print(
                f"Memory Classifier Error: {e}"
            )

            return MemoryClassification(False)


memory_classifier = MemoryClassifier()
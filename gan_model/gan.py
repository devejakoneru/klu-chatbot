import random

class Generator:
    """
    Generator simulates human-like response generation.
    In future, this will be replaced by a trained neural network.
    """

    def generate(self, base_response: str) -> str:
        variations = [
            base_response,
            "Here is the information you requested:\n" + base_response,
            "According to KL University guidelines:\n" + base_response,
            "Please note the following details:\n" + base_response
        ]
        return random.choice(variations)


class Discriminator:
    """
    Discriminator validates whether the generated response
    is relevant and meaningful.
    """

    def validate(self, response: str) -> bool:
        # Simple validation logic (placeholder)
        if response and len(response) > 20:
            return True
        return False


class GANResponseEngine:
    """
    Combines Generator and Discriminator
    """

    def __init__(self):
        self.generator = Generator()
        self.discriminator = Discriminator()

    def generate_response(self, base_response: str) -> str:
        generated = self.generator.generate(base_response)

        if self.discriminator.validate(generated):
            return generated

        # fallback if discriminator rejects
        return base_response

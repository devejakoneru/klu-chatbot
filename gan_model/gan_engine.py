import torch
from gan_model.basic_gan import train_gan

class GANResponseEnhancer:

    def __init__(self):
        self.generator = train_gan(epochs=200)

    def enhance(self, text):
        noise = torch.randn(1, 20)
        generated_features = self.generator(noise)

        # Just modify style slightly using GAN output
        score = generated_features.mean().item()

        if score > 0:
            return text + "\n\n✨ This response is AI-enhanced using GAN."
        else:
            return text + "\n\n🤖 Generated with adversarial learning mechanism."
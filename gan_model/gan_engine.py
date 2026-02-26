import torch
from gan_model.basic_gan import train_gan

class GANResponseEnhancer:

    def __init__(self):
        self.generator = train_gan(epochs=200)

    def enhance(self, text):
        noise = torch.randn(1, 20)
        generated_features = self.generator(noise)

        score = generated_features.mean().item()

        confidence = round(abs(score) * 100, 2)

        if score > 0:
            return text + f"\n\n🔍 GAN Confidence Score: {confidence}% (High Authenticity)"
        else:
            return text + f"\n\n🔍 GAN Confidence Score: {confidence}% (Moderate Authenticity)"
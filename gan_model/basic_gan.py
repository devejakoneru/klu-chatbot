import torch
import torch.nn as nn
import torch.optim as optim


# ----------------------------
# Generator
# ----------------------------
class Generator(nn.Module):
    def __init__(self, noise_dim=20, output_dim=10):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(noise_dim, 32),
            nn.ReLU(),
            nn.Linear(32, output_dim),
            nn.Tanh()
        )

    def forward(self, z):
        return self.model(z)


# ----------------------------
# Discriminator
# ----------------------------
class Discriminator(nn.Module):
    def __init__(self, input_dim=10):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)


# ----------------------------
# GAN Training Function
# ----------------------------
def train_gan(epochs=500):
    noise_dim = 20
    feature_dim = 10

    G = Generator(noise_dim, feature_dim)
    D = Discriminator(feature_dim)

    criterion = nn.BCELoss()
    g_optimizer = optim.Adam(G.parameters(), lr=0.001)
    d_optimizer = optim.Adam(D.parameters(), lr=0.001)

    for epoch in range(epochs):

        # -----------------
        # Train Discriminator
        # -----------------
        real_data = torch.randn(16, feature_dim)
        real_labels = torch.ones(16, 1)

        fake_noise = torch.randn(16, noise_dim)
        fake_data = G(fake_noise)
        fake_labels = torch.zeros(16, 1)

        d_loss_real = criterion(D(real_data), real_labels)
        d_loss_fake = criterion(D(fake_data.detach()), fake_labels)
        d_loss = d_loss_real + d_loss_fake

        d_optimizer.zero_grad()
        d_loss.backward()
        d_optimizer.step()

        # -----------------
        # Train Generator
        # -----------------
        fake_noise = torch.randn(16, noise_dim)
        fake_data = G(fake_noise)

        g_loss = criterion(D(fake_data), real_labels)

        g_optimizer.zero_grad()
        g_loss.backward()
        g_optimizer.step()

    return G
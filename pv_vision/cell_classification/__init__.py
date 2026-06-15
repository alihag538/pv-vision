import numpy as np
import torch

DATA_PATH = "data"
#MODEL_PATH = "model"
IMG_SIZE = 256
BATCH_SIZE = 16
LEARNING_RATE = 1e-4
NUM_EPOCHS = 50

SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)
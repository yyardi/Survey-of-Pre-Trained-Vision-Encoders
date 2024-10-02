from pathlib import Path

from tqdm import trange
from sklearn.manifold import TSNE
import zarr

import torch
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
from r3m import load_r3m
import mvp
from vip import load_vip


def load_vip_model():
    vip = load_vip().cuda()
    vip.eval()
    return vip


def load_resnet18():
    r3m = load_r3m("resnet18").cuda().eval()
    return r3m


def load_resnet34():
    r3m = load_r3m("resnet34").cuda().eval()
    return r3m


def load_resnet50():
    r3m = load_r3m("resnet50").cuda().eval()
    return r3m


def load_mvp():
    # Load the encoder with pretrained weights
    mvpmodel = mvp.load("vitb-mae-egosoup")
    mvpmodel.freeze()
    return mvpmodel


# Dictionary to store the models
models = {
    "VIP": load_vip_model,
    "ResNet18": load_resnet18,
    "ResNet34": load_resnet34,
    "ResNet50": load_resnet50,
    "MVP": load_mvp,
}
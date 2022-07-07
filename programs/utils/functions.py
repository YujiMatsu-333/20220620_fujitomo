# CopyRight, 2022, Yuji Matsushita, クオリアラボ

import numpy as np

import torch
import torch.nn as nn
from torchvision import models, transforms

class BaseTransform():
  def __init__(self, resize, mean, std):
    self.base_transform = transforms.Compose([
      transforms.Resize(resize),
      transforms.CenterCrop(resize),
      transforms.ToTensor(),
      transforms.Normalize(mean, std)
    ])
  def __call__(self, img):
    return self.base_transform(img)

class Predictor():
  def __init__(self, dict_label):
    self.dict_label = dict_label
  def predict_max(self, out):
    maxid = np.argmax(out.detach().numpy())
    return self.dict_label[maxid]

def predictLabel(img):
  # 予測ラベルの辞書
  dict_label = {
    0:'キッチン',
    1:'トイレ',
    2:'バス',
    3:'バルコニー',
    4:'リビング',
    5:'居室',
    6:'玄関',
    7:'室名札',
    8:'収納',
    9:'洗面所',
    10:'眺望',
    11:'分電盤',
    12:'和室',
    13:'未分類'
  }

  # 画像変換のインスタンスの生成
  resize = 224
  mean = (0.485, 0.456, 0.406)
  std = (0.229, 0.224, 0.225)
  transforms = BaseTransform(resize, mean, std)

  # 予測器のインスタンスの生成
  predictor = Predictor(dict_label)

  # CNNの用意
  net = models.vgg16()
  # VGG16の最後の出力ユニットを14に置き換える
  net.classifier[6] = nn.Linear(in_features=4096, out_features=14)
  path_load_weight = './weights/weights_VGG16_transfer_learning.pth'
  load_weights = torch.load(path_load_weight)
  net.load_state_dict(load_weights)

  # ラベルの予想
  img_transformed = transforms(img)
  input = img_transformed.unsqueeze_(0)
  out = net(input)
  return predictor.predict_max(out)




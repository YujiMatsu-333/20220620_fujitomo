'''
仕分ける画像ファイルを選択し、ファイル名にラベルを追加して保存する。
'''
import tkinter as tk
import os
from PIL import Image

from utils.mainWindow import ApplicationWindow
from utils.functions import predictLabel, reduceImageDataVolume

def main():
  # 出力先の指定
  path_output = '../output/'
  # windowの生成。仕分ける画像を選択し、タプルで返す。
  app = tk.Tk()
  app = ApplicationWindow(master=app)
  app.mainloop()
  tupple_filenames = app.returnTuple()

  for fileName in tupple_filenames:
    # 画像のラベルを返し、保存
    pil_image = Image.open(fileName) # Pillowsで開く
    exif = pil_image.info['exif'] # exif情報を取得
    label = predictLabel(pil_image) # 予測されたラベルの取得
    pil_image = reduceImageDataVolume(pil_image)
    # 画像の名前にラベルを追加して保存
    pil_image.save(path_output + label + '_' + os.path.basename(fileName), exif=exif)

if __name__ == '__main__':
  main()

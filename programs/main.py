'''
仕分ける画像ファイルを選択し、ファイル名にラベルを追加して保存する。
'''
import tkinter as tk
import os
from PIL import Image

from utils.mainWindow import ApplicationWindow
from utils.functions import predictLabel

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
    # 画像の名前にラベルを追加して保存
    pil_image.save(path_output + label + '_' + os.path.basename(fileName), exif=exif)
    # ファイルサイズ縮小
    while os.path.getsize(path_output + label + '_' + os.path.basename(fileName)) > 500000:
      pil_image = Image.open(path_output + label + '_' + os.path.basename(fileName))
      pil_image = pil_image.resize((int(pil_image.size[0]/2), int(pil_image.size[1]/2)))
      pil_image.save(path_output + label + '_' + os.path.basename(fileName), exif=exif)
  print('Classification has compleated!')

if __name__ == '__main__':
  main()

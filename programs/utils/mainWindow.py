# CopyRight, 2022, Yuji Matsushita, クオリアラボ

import tkinter as tk
from tkinter import filedialog
import os

class ApplicationWindow(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.pack()

    self.dir_current = os.getcwd()

    self.master.geometry('300x200')
    self.master.title('画像仕分けアプリ@クオリアラボ')

    self.create_widget()
  
  def create_widget(self):
    self.button_run = tk.Button(self.master, text='画像仕分け開始', command=self.select_files)
    self.button_run.pack()
  
  def select_files(self):
    self.tuple_filenames = filedialog.askopenfilenames(
      filetypes=[("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ],
      initialdir = self.dir_current + '../input/'
    )
    if len(self.tuple_filenames) == 0:
      self.creat_subWindow()
    self.master.destroy()
  
  def creat_subWindow(self):
    subWIn = tk.Toplevel()
    subWIn.geometry('300x100')
    subWIn.title('注意')
    label_sub = tk.Label(subWIn, text='ファイルが選択されておりません')
    label_sub.pack()

  def returnTuple(self):
    if self.tuple_filenames == None:
      return
    return  self.tuple_filenames

    
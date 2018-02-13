# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 10:22:35 2018

@author: Daniel Lee
"""
from GUI import MyGUI
from tkinter import Tk
from Graph import Graph
from FileParser import FileParser
"""
Main driver to run the program. 
"""
def main():
    csvFile = "coinmarket.csv"
    fileParser = FileParser(csvFile)
    graph = Graph(fileParser)
    graph.saveGraph()
    root = Tk()
    #probabilityIncrease, probabilityDecrease = predictor.predict(csvFile)
    gui = MyGUI(root, csvFile)
    gui.appOpen()
    root.mainloop()
    
main()

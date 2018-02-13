# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:18:37 2018

@author: Daniel Lee
"""
import matplotlib.pyplot as plt
from FileParser import FileParser

"""
Creates the graph to show the prices/days of Bitcoin 
"""
class Graph():
    def __init__(self, fileParser):
        #self.__csvFile = csvFile
        self.__fileParser = fileParser
        self.__table = self.__fileParser.parse("graph")
        self.__maxSize = self.__fileParser.getMax()
        self.__price = []
        self.__date = []
        self.__range = 365 #Based on days
        
    def saveGraph(self):
        ctr = []
        fig = plt.figure()
        fig.set_size_inches(7, 5)
        title = "Bitcoin Price Values (USD) Over The Past " + str(self.__range) + " Days"
        for i in range(self.__maxSize - self.__range, self.__maxSize):
            self.__date.append(self.__table.iloc[i, 0])
            self.__price.append(self.__table.iloc[i, 1])
            ctr.append(i)
       
        # plotting the points 
        plt.plot(ctr, self.__price)
        #plt.plot(self.__date, self.__low, label = "Low Points")
        
        plt.xlabel("Past Days")
        plt.xticks([])
        plt.annotate(self.__date[self.__range - 1], xy = (ctr[self.__range - 1], self.__price[self.__range - 1]), xytext = (ctr[self.__range - 2], 5000), arrowprops = dict(arrowstyle = "->")) 
        plt.annotate(self.__date[0], xy = (ctr[0], self.__price[0]), xytext = (ctr[0], 2500), arrowprops = dict(arrowstyle = "->")) 
        plt.ylabel("Price (USD)")
        plt.title(title)
        fig.savefig("Graph.png") #saves it to a png file to use it for the GUI
    
    def update(self, fileParser):
        self.fileParser = fileParser
        self.__table = self.__fileParser.parse("graph")
        self.__maxSize = self.__fileParser.getMax()
        self.__price = []
        self.__date = []
        self.__range = 365 #Based on days


def main():
    fileParser = FileParser("coinmarket.csv")
    graph = Graph(fileParser)
    graph.saveGraph()
    
main()



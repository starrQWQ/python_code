# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:09:12 2019

@author: Administrator
"""
import City

class Individual:
    def __init__(self,city_seq,cities,fit = 0):
        self.city_seq = city_seq.copy()
        self.p = 0
        self.dist = 0
        if fit == 0:
            self.setFit(cities)
        else:
            self.fit = fit
    def get_seq(self):
        return self.city_seq
    def get_dis(self):
        return self.dist
    def get_fit(self):
        return self.fit
    def setFit(self,cities):
        fit = 0
        for i in range(len(self.city_seq[:-1])):
            index_city1 = self.city_seq[i]
            index_city2 = self.city_seq[i+1]
            fit += City.calcDist(cities[index_city1],cities[index_city2])
        self.dist = fit
        self.fit = 1 / fit
    def setP(self,p):
        self.p = p
    
    

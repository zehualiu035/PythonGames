# -*- coding: utf-8 -*-
#Author: zehua liu
#Env python 3
import itertools
import random


class Solve24:
    '''to solve 24 problem'''

    def __init__(self,a,b,c,d):
        self.numList = [a,b,c,d]
        # print(numList)
        self.nList = []
        [self.nList.append(n) for n in list(
            itertools.permutations(self.numList)) if n not in self.nList]
        # print(nList)
        self.operate = ['+', '-', '*', '/']
        self.operateList = list(itertools.product(self.operate, repeat=3))
        # print(operateList)
  
    def Solve(self):
        '''connect all the number and operator to solve 24 problem'''
        # first case: (a?b)?(c?d)
        solveList0 = ['(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] + '(' + str(
            n[2]) + m[2]+str(n[3])+')' for n in self.nList for m in self.operateList]

        # second case:((a?b)?c)?d)
        solveList1 = ['(' + '(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] + str(
            n[2])+')' + m[2]+str(n[3]) for n in self.nList for m in self.operateList]
        # print(solveList1)
        # third case:((a?(b?c)?d)
        solveList2 = ['(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] + '(' + str(
            n[2]) + m[2]+str(n[3])+')' for n in self.nList for m in self.operateList]

        # fourth case:a?((b?c)?d)
        solveList3 = [str(n[0]) + m[0] + '(' + '(' + str(n[1]) + m[1] + str(
            n[2]) + ')' + m[2]+str(n[3])+')' for n in self.nList for m in self.operateList]

        # fourth case:a?(b?(c?d))
        solveList4 = [str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + '(' + str(
            n[2]) + m[2]+str(n[3])+')'+')' for n in self.nList for m in self.operateList]
        #all in one
        allSolves = [solveList0, solveList1,
                     solveList2, solveList3, solveList4]
        tag=False
        for m in allSolves:
            for n in m:
                try:
                    if eval(n)==24:
                        print(n,'=24')
                        tag=True
                except:
                    pass
            if tag==False:
                print('it is hopeless')
        # print(solveList4)
#Solve24().Solve()
Solve24(1,2,3,4).Solve()

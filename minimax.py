# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:01:40 2023

@author: Richard
"""

# ici on va implémenter le minimax avec le BFS car par la suite on va vouloir diminuer le nombre de fils pour un noeuds
# ici le but sera de retourner une action en fonction de l'état
# ON CONSIDERE QUE X CORRESPOND AU  JOUEUR HUMAIN

from morpionGame import morpion

#def heuristic(state):# évalue un state si il est potentiellement gagnant ou perdant#



def minimax(state,player):
    
    
    
    if state.terminalTest():
        #print(i)
        return (state.utility(),)
    
    if player=="X":#correspond au X
        
        best_value = float('-inf')
        actions=state.actions()
        
        bestCombo=(best_value,)
        for action in actions:
            childState=state.result(action,player)
            
            value = minimax(childState, "O")[0]
            if value>best_value:
                best_value=value
                
                bestCombo=(value,action)
                #print(bestAction)
            #best_value = max(best_value, value)
        return  bestCombo#best_value
    else:# correspond au O
        
        best_value = float('inf')
        actions=state.actions()
        
        bestCombo=(best_value,)
        for action in actions:
            childState=state.result(action,player)
            value = minimax(childState, "X")[0]
            if value<best_value:
                best_value=value
                
                bestCombo=(best_value,action)
            #best_value = min(best_value, value)
        return bestCombo
    

def alphabeta(state,player,alpha=float("-inf"),beta=float("inf")):
    
    
    
    if state.terminalTest():
        #print(i)
        return (state.utility(),)
    
    if player=="X":#correspond au X/joueur qui maximise
        
        best_value = float('-inf')
        actions=state.actions()
        
        bestCombo=(best_value,)
        for action in actions:
            childState=state.result(action,player)
            
            value = alphabeta(childState, "O",alpha,beta)[0]
            if value>best_value:
                best_value=value
                
                bestCombo=(best_value,action)
            alpha=max(alpha,value)
            if beta<=alpha:
                break
                
        return  bestCombo
    else:# correspond au O
        
        best_value = float('inf')
        actions=state.actions()
        
        bestCombo=(best_value,)
        for action in actions:
            childState=state.result(action,player)
            value = alphabeta(childState, "X",alpha,beta)[0]
            if value<best_value:
                best_value=value
                
                bestCombo=(best_value,action)
            beta=min(beta,value)
            if beta<=alpha:
                break
                
        return bestCombo
    

emptyBoard=[
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"],
    ]

state=morpion()

print(minimax(state,"max"))
    



    
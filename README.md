# FGO Script

Redesigning the whole script and improve the algorithm. 

## About this branch

__Added__:
1. Servant detection.
2. "Extra Card" detection. When three cards are selected from the same servant, the "Extra Attack"
card now is included in the attack index calculation
3. Multi-Mode supported. Besides the original mode, "Quick Mode" is added for those who would like to use 
"Green Card Team", which means most of the servants in the team have 3 "Quick" cards, so "critical stars" 
could be collected more easily.

__Attention__:
The script is still not tested yet.

> ### About (original branch)
> Besides the original auto battle module, the script now could
automatically select checkpoint, support Servant, and finish 
the battle. AP recovery module is added in order to recover 
AP for longtime running.
> ### Features
> 1. __Auto Battling__: Automatically calculate and select cards which has the maximum
attack.  
> 2. __Auto AP Recovery__: Automatically recover AP when AP is insufficient, allow to manually 
set how many times will be conducted.   
> 3. __Customizable Runtime__: Allow to set how many times it will be played.  
> 4. __Customizable Script__: Can easily add other functions, modify checkpoints to the script.
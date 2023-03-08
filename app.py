

def frequencyComputer(wantedImageFrequency, basePeriodLatchEnableCount, basePeriodOutputEnableCount, columnCount, rowCount, encodingDepth):
    """
    columnCount: Nombre de pixels sur une ligne
    rowCount: Nombre de ligne (pour une matrice de LEDS, la valeur attendue est nombreTotalDeLigne / 2)
    basePeriodLatchEnableCount: Le nombre de periodes de l'horloge de base qu'on veut utiliser pour faire un latch et un output enable.


    Pour afficher une ligne, il faut 'columCount + basePeriodLatchEnableCount' périodes d'horloge.
    Si on tient compte du PWM 8 bits(une ligne est affichée 2**encodingDepth fois),
    pour faire du pwm sur une ligne entière, il faut au total 
    (columnCount + basePeriodLatchEnableCount) * 2**encodingDepth périodes d'horloges.
    
    Une fois le PWM terminé, il faut faire un basePeriodOutputEnableCount.

    Tenant compte de cela, une ligne prend finalement 
    (columnCount + basePeriodLatchEnableCount) * 2**encodingDepth + basePeriodOutputEnableCount périodes d'horloge.

    Du coup, pour aficher une image entière sur la matrice de LEDs, il faut 
    ((columnCount + basePeriodLatchEnableCount) * 2**encodingDepth + basePeriodOutputEnableCount) * rowCount périodes d'horloge.

    On veut faire wantedImageFrequency par seconde donc il faut duration = 1/wantedImageFrequency secondes pour 
    afficher une image

    On a donc l'équation ''' (((columnCount + basePeriodLatchEnableCount) * 2**encodingDepth + basePeriodOutputEnableCount) * rowCount)*p = duration'''
    soit p = duration / (((columnCount + basePeriodLatchEnableCount) * 2**encodingDepth + basePeriodOutputEnableCount) * rowCount)


    
    """

    # la durée théorique qu'il faut pour afficher une image wantedImageFrequency fois par seconde
    duration = 1/wantedImageFrequency
    
    lineDisplayPeriodCount = ((columnCount + basePeriodLatchEnableCount) * 2**encodingDepth + basePeriodOutputEnableCount)
    allRowsDisplayPeriodCount = lineDisplayPeriodCount * rowCount
    
    return allRowsDisplayPeriodCount / duration




if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    wantedImageFrequencies = [30, 60, 70, 120, 200]
    encodingDepths = [3, 4, 5, 6, 7, 8]
    colors = ["red", "blue", "green", "yellow", "black", "purple"]
    
    for index, encodingDepth in enumerate(encodingDepths):
        clockCycles = []
        for imageFrequency in wantedImageFrequencies:
            clock = frequencyComputer(imageFrequency, 2, 2, 32, 8, encodingDepth)
            clockCycles.append(clock)

        plt.semilogy(wantedImageFrequencies, clockCycles, label=f"L={encodingDepth}")

    plt.legend(loc="lower right", ncol=3)
    #plt.legend(bbox_to_anchor=(1.04, 1.0), loc='upper left')
    plt.xlabel('wanted image frequency')
    plt.ylabel('FPGA clock cycle')
    plt.grid(True, which="both")
    plt.show()
    


from Utils import readData2, readData1
from GA import GA

def run():
            fileName = "50p_hard_01_tsp.txt"

            if (fileName != ""):
                print("Marimea populatiei = ")
                marimePopulatie = int(input())
                print("Numarul de generatii = ")
                numarGeneratii = int(input())
                if fileName == "150p_eil51.txt":
                    graph = readData2(fileName)
                else:
                    graph = readData1(fileName)
                ga = GA(marimePopulatie, graph)
                ga.initialization()
                contor = 0
                gen = contor + 1
                contor += 1
                best = ga.getBestChromosome()
                print("generation " + str(gen) + " " + str(best.repres) + " fitness: " + str(best.fitness))
                while (contor < numarGeneratii):
                    ga.oneGenerationElitism()
                    best = ga.getBestChromosome()
                    gen = contor + 1
                    print("generation " + str(gen) + " " + str(best.repres) + " fitness: "+str(best.fitness))
                    contor += 1
run()
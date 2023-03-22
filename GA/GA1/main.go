package main

import (
	"fmt"
	"math/rand"
	"sort"
)

const (
	populationSize = 100
	numGenerations = 1000
	mutationRate   = 0.1
)

type Individual struct {
	x       float64
	fitness float64
}

func main() {
	// Generate initial population
	population := make([]Individual, populationSize)
	for i := 0; i < populationSize; i++ {
		population[i] = Individual{
			x:       rand.Float64() * 5,
			fitness: 0,
		}
	}

	// Evolve population for a fixed number of generations
	for gen := 0; gen < numGenerations; gen++ {
		// Evaluate fitness of each individual
		for i := 0; i < populationSize; i++ {
			population[i].fitness = fitnessFunction(population[i].x)
		}

		// Sort population by fitness
		sortByFitness(population)

		// Print the best individual in the current generation
		fmt.Printf("Generation %d: x = %f, fitness = %f\n", gen, population[0].x, population[0].fitness)

		// Create new population by selecting and breeding individuals
		newPopulation := make([]Individual, populationSize)
		for i := 0; i < populationSize; i++ {
			// Select two parents
			parent1 := selectParent(population)
			parent2 := selectParent(population)

			// Breed two parents to create a child
			child := breed(parent1, parent2)

			// Mutate child with a small probability
			if rand.Float64() < mutationRate {
				child = mutate(child)
			}

			newPopulation[i] = child
		}

		// Replace old population with new population
		population = newPopulation
	}
}

func fitnessFunction(x float64) float64 {
	return x*x - 4*x + 5
}

func sortByFitness(population []Individual) {
	sort.Slice(population, func(i, j int) bool {
		return population[i].fitness < population[j].fitness
	})
}

func selectParent(population []Individual) Individual {
	// Roulette wheel selection
	sumFitness := 0.0
	for _, individual := range population {
		sumFitness += individual.fitness
	}
	r := rand.Float64() * sumFitness
	sumFitness = 0.0
	for _, individual := range population {
		sumFitness += individual.fitness
		if sumFitness >= r {
			return individual
		}
	}
	return population[0]
}

func breed(parent1, parent2 Individual) Individual {
	// Single-point crossover
	child := Individual{
		x:       0.5*parent1.x + 0.5*parent2.x,
		fitness: 0,
	}
	return child
}

func mutate(individual Individual) Individual {
	// Add small amount of Gaussian noise to x
	individual.x += rand.NormFloat64() * 0.1
	return individual
}

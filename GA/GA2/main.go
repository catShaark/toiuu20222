package main

import (
	"fmt"
	"math/rand"
	"sort"
)

const (
	populationSize               = 100
	numGenerations               = 1000
	mutationRate                 = 0.1
	cathegiulai                  = 20
	cathesinhratucathetot        = 30
	cathemoixuathientrongquanthe = 50
)

type thanhphan struct {
	x      float64
	giatri float64
}

func main() {
	// Generate initial population
	fmt.Println("start")
	println(hammuctieu(0))
	population := make([]thanhphan, populationSize)
	for i := 0; i < populationSize; i++ {
		x := rand.Float64() * 5
		population[i] = thanhphan{
			x:      x,
			giatri: hammuctieu(x),
		}
	}
	for gen := 0; gen < numGenerations; gen++ {
		sapxep(population)
		//chon loc
		var newpopopulation = []thanhphan{}

		cathegiulai := chonloc20cathetot(population)
		newpopopulation = append(newpopopulation, cathegiulai...)

		catheduocsinhra := sinhsan30cathe(population)
		newpopopulation = append(newpopopulation, catheduocsinhra...)

		cathengaunhien := sinhngaunhien50cathe()
		newpopopulation = append(newpopopulation, cathengaunhien...)

		fmt.Printf("Sau nam thu %d gia tri cua ham muc tieu = %v, tai x = %v\n", gen, population[0].giatri, population[0].x)
		population = newpopopulation

	}

}
func sinhngaunhien50cathe() (cathemoixuathien []thanhphan) {
	for i := 0; i < cathemoixuathientrongquanthe; i++ {
		x_new := rand.Float64() * 5
		newcathemoixuathien := thanhphan{
			x:      x_new,
			giatri: hammuctieu(x_new),
		}
		cathemoixuathien = append(cathemoixuathien, newcathemoixuathien)

	}
	return
}
func sinhsan30cathe(population []thanhphan) (cathelaitaotucaccathetot []thanhphan) {
	// 10 ca the duoc sinh ra tu ca the tot nhat hien tai
	for i := 0; i < 10; i++ {
		cathehanhphuc := rand.Int()%(cathegiulai-1) + 1
		chil := giaophoi_laitao(population[cathehanhphuc], population[0])
		cathelaitaotucaccathetot = append(cathelaitaotucaccathetot, chil)
	}
	//20 ca the quan he ngau nhien
	for i := 0; i < cathesinhratucathetot-10; i++ {
		cathehanhphuc1 := rand.Int() % cathegiulai
		cathehanhphuc2 := rand.Int() % cathegiulai
		if cathehanhphuc1 == cathehanhphuc2 {
			// tao co hoi cho nguoi ve nhi
			cathehanhphuc2 = 1
		}
		child := giaophoi_laitao(population[cathehanhphuc1], population[cathehanhphuc2])
		cathelaitaotucaccathetot = append(cathelaitaotucaccathetot, child)
	}
	return
}
func chonloc20cathetot(population []thanhphan) (cathetot []thanhphan) {
	for i := 0; i < cathegiulai; i++ {
		cathetot = append(cathetot, population[i])
	}
	return
}
func hammuctieu(x float64) float64 {
	return x*x - 4*x + 5
}
func sapxep(population []thanhphan) {
	sort.Slice(population, func(i, j int) bool {
		return population[i].giatri < population[j].giatri
	})
}
func giaophoi_laitao(parent1, parent2 thanhphan) thanhphan {
	// Single-point crossover
	x_child := 0.5*parent1.x + 0.5*parent2.x

	child := thanhphan{
		x:      x_child,
		giatri: hammuctieu(x_child),
	}
	return child
}

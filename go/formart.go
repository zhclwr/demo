package main 

import "math/rand"
const MaxRand = 8

func StatRandomNumbers(numRands int) (int, int) {
	var a, b int
	for i := 0; i < numRands; i++ {
		if rand.Intn(MaxRand) < MaxRand/2 {
			a = a + 1
		} else {
			b++ 
		}
	}
	return a, b 
}


func main() {
	var a = [...]int{1,2,3}
	for i, v := range a {
		println(i, v)
	}
}

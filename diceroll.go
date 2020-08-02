package main

import (
	"fmt"
	"math/rand"
)

var count1 int = 0
var count2 int = 0
var count3 int = 0

func main() {

	for i := 0; i <= 1000; i++ {
		dice_num := []int{1, 2, 3, 4, 5, 6}
		player1 := rand.Intn(len(dice_num))
		player2 := rand.Intn(len(dice_num))
		// fmt.Println(player1)
		// fmt.Println(player2)
		if player1 > player2 {
			// fmt.Println("Player 1 has won")
			count1 += 1
		} else if player2 > player1 {
			// fmt.Println("Player 2 has won")
			count2 += 1
		} else if player1 == player2 {
			// fmt.Println("Tie")
			count3 += 1
		}
	}
	fmt.Println("PLayer 1 has won many times")
	fmt.Println(count1)
	fmt.Println("PLayer 2 has won many times")
	fmt.Println(count2)
	fmt.Println("Tie has occur times")
	fmt.Println(count3)
}

package main

import (
	"fmt"
	"math/rand"
	
)

var count1 int = 0
var count2 int = 0
var count3 int = 0
// var i int = 0

func main(){

	for j := 0; j <= 10; j++{
		var letters [3]string
		letters[0] = "rock"
		letters[1] = "paper"
		letters[2] = "scissor"

		player1_I := rand.Intn(len(letters))
		player2_I := rand.Intn(len(letters))
		player1 := letters[player1_I]
		player2 := letters[player2_I]

		if player1 == "rock" && player2 == "paper" {
			count2 += 1
		} else if player1 == "rock" && player2 == "scissor" {
			count1 += 1
		} else if player1 == "paper" && player2 == "rock" {
			count1 += 1
		} else if player1 == "paper" && player2 == "scissor" {
			count2 += 1
		} else if player1 == "scissor" && player2 == "paper" {
			count1 += 1
		} else if player1 == "scissor" && player2 == "rock" {
			count2 += 1
		} else if player2 == player1 {
			count3 += 1
		} else {
			fmt.Println("try again")
		}
	}
	fmt.Println(count1)
	fmt.Println("Player 1 won")
	fmt.Println(count2)
	fmt.Println("Player 2 won")
	fmt.Println(count3)
	fmt.Println("TIE occurs")
}
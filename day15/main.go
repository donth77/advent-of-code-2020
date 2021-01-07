package main

import "fmt"

var nums = [7]int{6, 19, 0, 5, 7, 13, 1}

func speak_sequence(finalTurn int) int{
	lastSeen := make(map[int]int)
	prev := nums[len(nums)-1]
	for i := 0; i < len(nums); i++ {
		lastSeen[nums[i]] = i
	}
	for i := len(nums); i < finalTurn; i++ {
		curr := 0
		if val, ok := lastSeen[prev]; ok {
			curr = i-1-val
		} else {
			curr = 0
		}
		lastSeen[prev] = i - 1
		prev = curr
	}
	return prev
}

func main() {
	fmt.Println("Part 1\n", speak_sequence(2020))
	fmt.Println("\nPart 2\n", speak_sequence(30_000_000))
}
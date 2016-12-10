package main

import "fmt"

func main()  {
    mynums := []float64 {1, 2, 3, 4, 5}
    mysums := mySum(mynums)
    fmt.Println("The sum of mynums is ", mysums)
}

func mySum(nums []float64) float64 {
    sum := 0.0
    for _, value := range nums {
        sum += value
    }
    return sum
}

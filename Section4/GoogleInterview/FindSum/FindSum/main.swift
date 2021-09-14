//
//  main.swift
//  FindSum
//
//  Created by Mandha Smitha S on 01/07/2021.
//

/* Given an array of integers and a sum, find if there exist 2 numbers that add up to the sum.*/
/* More info: 1. Array is in memory
              2. Duplicates can happen
 */
/* Example 1: [1, 2, 3, 4], Sum = 8
    Does not exist
 */
/* Example 2: [1, 3, 4, 4], Sum = 8
    Exists
 */

import Foundation

/* Brute force method:
   For each number in the array, find if the complement exists that adds up to the sum. */
func findPair(array: [Int], sum: Int) -> Bool {
    // Array will always have 2 or more integers.
    for i in 0..<(array.count - 1) {
        for j in 1..<array.count {
            if array[i] + array[j] == sum {
                return true
            }
        }
    }
    return false
}

let pairExists = findPair(array: [1, 3, 4, 4], sum: 8)
print(pairExists)


/* Store the complement of the array in a Set before adding. */
func findPair2(array: [Int], sum: Int) -> Bool {
    let mySet = NSMutableSet()
    for i in 0..<array.count {
        if mySet.contains(array[i]) {
            return true;
        }
        mySet.add(sum - array[i])
    }
    return false;
}

let pairExists2 = findPair2(array: [1, 2, 3, 4], sum: 8)
print(pairExists2)

import Data.List

import System.IO  
import Control.Monad
import System.Win32 (COORD(x))

testData :: [Int]
testData = [-1,1000,2000,3000,-1,4000,-1,5000,6000,-1,7000,8000,9000,-1,10000]


groupFirst :: [Int] -> [Int]
groupFirst [] = []
groupFirst (-1:_) = []
groupFirst (x:xs) = x : (groupFirst xs)


groupList :: [Int] -> [[Int]]
groupList [] = []
groupList (x:xs) = if x == (-1) then [groupFirst xs] ++ groupList xs else groupList xs

elfSums :: [Int] -> [Int]
elfSums xs = reverse (sort (map sum (groupList xs)))

topSum :: Int -> [Int] -> Int
topSum a = sum . take a

elfTop :: [Int] -> Int
elfTop xs = topSum 1 (elfSums xs)


elfTop3 :: [Int] -> Int
elfTop3 xs = topSum 3 (elfSums xs)

part1 :: [Int] -> Int 
part1 = elfTop

part2 :: [Int] -> Int
part2 = elfTop3


fileName :: String
fileName = "haskell_day1_input.txt"

main :: IO ()
main = do  
        contents <- readFile fileName
        let list = map (readInt) . words $ contents
        print "Part 1:"
        print (part1 list)
        print "Part 2:"
        print (part2 list)

readInt :: String -> Int
readInt = read
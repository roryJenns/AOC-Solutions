import Data.List

import System.IO  
import Control.Monad
import System.Win32 (COORD(x))

testData :: [Integer]
testData = [-1,1000,2000,3000,-1,4000,-1,5000,6000,-1,7000,8000,9000,-1,10000]


groupFirst :: [Integer] -> [Integer]
groupFirst [] = []
groupFirst (-1:_) = []
groupFirst (x:xs) = x : (groupFirst xs)


groupList :: [Integer] -> [[Integer]]
groupList [] = []
groupList (-1:xs) = [groupFirst xs] ++ groupList xs
groupList (_:xs) = groupList xs


elfSums :: [Integer] -> [Integer]
elfSums xs = reverse (sort (map sum (groupList xs)))

topN :: Integer -> [Integer] -> Integer
topN 0 _ = 0
topN _ [] = 0
topN n (x:xs) = x + topN (n-1) xs

elfTop :: [Integer] -> Integer
elfTop xs = topN 1 (elfSums xs)


elfTop3 :: [Integer] -> Integer
elfTop3 xs = topN 3 (elfSums xs)

part1 :: Integer 
part1 = elfTop testData

part2 :: Integer
part2 = elfTop3 testData


fileName :: String
fileName = "haskell_day1_input.txt"

main :: IO ()
main = do  
        contents <- readFile fileName
        let list = map (toInteger . readInt) . words $ contents
        print (elfTop list)
        print (elfTop3 list)

readInt :: String -> Int
readInt = read
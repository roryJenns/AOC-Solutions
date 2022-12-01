import System.IO  
import Control.Monad
import System.Win32 (COORD(x))


fileName :: String
fileName = "haskell_day1_input.txt"

main :: IO ()
main = do  
        contents <- readFile fileName
        let list = map readInt . words $ contents
        print list

readInt :: String -> Int
readInt = read


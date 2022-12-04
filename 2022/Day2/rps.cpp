#include <iostream>
#include <fstream>

using namespace std;

#define FILE_LINES 3

int main(int argc, char const *argv[])
{
    char first[3];
    char *fileName = "input/test_input.txt";
    int length_of_file = FILE_LINES;

    char data[FILE_LINES][2];
    int i, j;


    ifstream fin(fileName);
    char ch;

    i=0;
    
    while (fin.get(ch)) {
        if (ch == ' ' || ch == '\n'){
            continue;
        }
        data[i/2][i%2] = ch;
        i++;
    }

    for (i=0; i<FILE_LINES; i++) {
        // cout << i << " : " << data[i][0] << data[i][1] << endl;
        printf("%d,%c,%c\n", i, data[i][0], data[i][1]);
    }
    

    return 0;
}

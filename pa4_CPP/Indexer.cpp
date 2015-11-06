#include "Indexer.h"
#include <fstream>
#include <iostream>

using std::ifstream;
using std::ostream;

// Reads content from the supplied input file stream, and transforms the
// content into the actual on-disk inverted index file.
void Indexer::index(ifstream& content, ostream& outfile)
{
    // Fill in this method to parse the content and build your
    // inverted index file.


}

Indexer::Indexer()
{
    ifstream myFile;
    myFile.open("stop_words.txt");
    std::string word;
    if (myFile.is_open()) {
      while (myFile >> word) {
        //add word to set
        stop_words.insert(word);
        //cout << word<< endl;
      }
    }
    myFile.close();
}

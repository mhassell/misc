// a utility to find a word in a file, and print each line where it occurs

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

int main(int argc, char* argv[]){

	if(argc !=3 ){
		std::cout << argc << std::endl;
		std::cout << "Please input a file and a word to search for." << std::endl;
		return 0;
	}
	else{ // find the word (second argument) in the file (first argument)

		std::ifstream file(argv[1]);
		std::vector<std::string> words;
		std::string line;
		while(std::getline(file,line))
			std::istringstream iss(line);

	}

}
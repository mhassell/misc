// a utility to find a word in a file, and print each line where it occurs

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <regex>


int main(int argc, char* argv[]){

	if(argc !=3 ){
		std::cout << argc << std::endl;
		std::cout << "Please input a file and a word to search for." << std::endl;
		return 0;
	}
	else{ // find the word (second argument) in the file (first argument)

		const std::string in(argv[2]);
		std::string reg("("+in+")");
		std::regex e (reg);
		std::cout<< reg << std::endl;
	}

}

/*
void split(const std::string &s, char delim, std::vector<std::string> &words) {
    std::stringstream ss;
    ss.str(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        words.push_back(item);
    }
}

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
			split(line, ' ', words);
			for(int i =0; i<words.size(); i++){
				if(words[i] != " ")
					std::cout << words[i] << '\n' << std::endl;
			}

	}

}
*/
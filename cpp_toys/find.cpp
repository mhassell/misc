// a utility to find a word in a file, and print each line where it occurs

#include <iostream>
#include <string>
#include <fstream>


int main(int argc, char* argv[]){

	if(argc !=3 ){
		std::cout << argc << std::endl;
		std::cout << "Please input a file and a word to search for." << std::endl;
		return 0;
	}
	else{ // find the word (second argument) in the file (first argument)

		const std::string in(argv[2]);
		std::ifstream file(argv[1]);
		std::string line;
		int line_num = 0;
		while(std::getline(file,line)){
			line_num++;
			std::size_t found = line.find(in,0);
			if(found!=std::string::npos){
				std::cout << "Found on line " <<  line_num << "\n\n"<< std::endl;
				std::cout << line << "\n\n" << std::endl;
			}

			line = "";
		}
	}
}
import os 

f1 = open("file1.cpp", "w+")

f1.write("#include <iostream>\n int main()\n{\nstd::cout<< ")

output = input("Enter the sentence to print: ")

f1.write(" \" " + output +   " \" << std::endl;\n}")
f1.close();

os.system("g++ file1.cpp -o file1 & file1")



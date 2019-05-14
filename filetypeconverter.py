infilename=str(input("input a file name, should be .rhtml: ")) #gets name of file to convert
infile = open(infilename, 'r') #opens read only
text = infile.read() #dumps contents into string
infile.close() #close that file
print(text) #show text is read
outfilename=str(input("give a file name to output to, must be .html: ")) #gets name of file to write to
outfile=open(outfilename, 'a+') #create needed html file, read and write access
outfile.write(text) #write text to file
outfile.close() #close file



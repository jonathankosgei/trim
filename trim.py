"""
    Trim takes a file and removes the first `x` characters on each line
    and writes the output to a file or to stdout.   
"""
import sys
import os

class Trim():
    def __init__(self, trim_length = None, file_name = None, output_name = None):
        self.file_name = file_name
        self.trim_length = trim_length
        self.output_name = output_name
        
    def trim_line(self, line):
        # lines shorter that our trim length will totally disappear
        if len(line) <= self.trim_length:
            return ""
        else:
            return line[self.trim_length - 1:]
            
    def trim(self):
        # file_names or trim_length not specified 
        if self.file_name == None or self.trim_length == None:
            return False

        # trim_length should be an integer greater than 0
        try:
            self.trim_length = int(self.trim_length)
            assert(not self.trim_length < 0) 
        except (AssertionError, ValueError, TypeError) as e:
            print("Error: " + str(e))
            return False
            
        # write to output file or std out
        if self.output_name == None:
            out_file = sys.stdout
        else:
            out_file = open(self.output_name, 'a')

        # write line by line to outputfile/stdout
        if os.path.exists(self.file_name) and os.path.isfile(self.file_name):
            [out_file.write(self.trim_line(line)) for line in open(self.file_name, 'r')]
            return True       
        return False


if __name__ == "__main__":
    # get args and initialize trimmer
    usage = "Usage:\tpython trim.py `trim_length` `input_filename` `output_filename`"
    if len(sys.argv) < 3:
        print(usage)
        sys.exit(1)
    trim_length, file_name = sys.argv[1:3]
    out_file = None
    if len(sys.argv) >= 4:
        out_file = sys.argv[3]
    
    # instantiate trimmer and trim
    trimmer = Trim(trim_length=trim_length, file_name=file_name, output_name=out_file)
    if not trimmer.trim():
        print(usage)
        sys.exit(13)
    else:
        sys.exit(0)


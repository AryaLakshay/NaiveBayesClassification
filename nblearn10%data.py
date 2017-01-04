'''
Created on Sep 22, 2016

@author: lakshayarya
'''
'''
Created on Sep 16, 2016

@author: lakshayarya
'''
import sys;
import os;

def main(argv):
    print("Hello");
    '''if len(sys.argv)!=2:
        print("Invalid Syntax");
        sys.exit();'''
        
    #filedir=sys.argv[1];
        
    filedir="/Users/lakshayarya/Desktop/CSCI 544 Assingment-1/Assingment-1/Spam or Ham/train";
    wordCountHamSpam={};
    fspam=0;
    fham=0;
    noSpam=0;
    noHam=0;
    
    if not os.path.isdir(filedir):
        print("Invalid Directory");
        sys.exit();
        
    for root, dirs, files in os.walk(filedir):
        if root.endswith("ham"):
            count=len(files);
            count=(count//10)+1;
            done=0;
            for name in files:
                done=done+1;
                if(done>count):
                    break;
                if name.endswith(".txt"):
                    fham +=1;
                    f=open(root+"//"+name, "r", encoding="latin1");
                    '''mylist = [line.rstrip('\n') for line in f];'''
                    for line in f:
                        for word in line.split():
                            noHam +=1;
                            if word not in wordCountHamSpam:
                                wordCountHamSpam[word] = [1,0];
                            else:
                                wordCountHamSpam[word][0] += 1;
                
                
        elif root.endswith("spam"):
            count=len(files);
            count=(count//10)+1;
            done=0;
            for name in files:
                done=done+1;
                if(done>count):
                    break;
                if name.endswith(".txt"):
                    fspam +=1;
                    f=open(root+"//"+name, "r", encoding="latin1");
                    for line in f:
                        for word in line.split():
                            noSpam +=1;
                            if word not in wordCountHamSpam:
                                wordCountHamSpam[word] = [0,1];
                            else:
                                wordCountHamSpam[word][1] += 1
                                
    outf=open("nbmodel10.txt","w",encoding="latin1");
    
    outf.write(str(fspam));
    outf.write("\n");
    outf.write(str(fham));
    outf.write("\n");
    outf.write(str(noSpam));
    outf.write("\n");
    outf.write(str(noHam));
    outf.write("\n");
    for key, value in wordCountHamSpam.items():
        outf.write(key);
        outf.write(" ");
        outf.write(str(value[0]));
        outf.write(" ");
        outf.write(str(value[1]));
        outf.write("\n");
        
    outf.close();
    print("File Written");                                             
#main(sys.argv[1]);  
main(1);
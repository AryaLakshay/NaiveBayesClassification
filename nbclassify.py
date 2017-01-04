import sys;
import os;
from math import log

def main(argv):
    
    f=open("nbmodel.txt", "r", encoding="latin1");
    
    wordCountHamSpam={};
    count=0;
    fspam=0;
    fham=0;
    nospam=0;
    noham=0;
    for line in f:
        count +=1;
        if count==1:
            fspam=int(line);
        elif count==2:
            fham=int(line);
        elif count==3:
            nospam=int(line);
        elif count==4:
            noham=int(line);
        else:
            splitted = line.split();
            wordCountHamSpam[splitted[0]]=[int(splitted[1]),int(splitted[2])];
            
    '''print(fspam);
    print("\n");
    print(fham);
    print("\n");
    print(nospam);
    print("\n");
    print(noham);
    print("\n");
    for key, value in wordCountHamSpam.items():
        print(key+" "+str(value));'''
        
    #filedir="/Users/lakshayarya/Desktop/CSCI 544 Assingment-1/Assingment-1/Spam or Ham/dev";
    filedir=argv;
    if not os.path.isdir(filedir):
        print("Invalid Directory");
        sys.exit();
    
    outf=open("nboutput.txt", "w", encoding="latin1");
    for root, dirs, files in os.walk(filedir):
            for name in files:
                if name.endswith(".txt"):
                    f=open(root+"//"+name, "r", encoding="latin1");
                    probability_spam=0.0;
                    probability_ham=0.0;
                    for line in f:
                        for word in line.split():
                            if word in wordCountHamSpam:
                                probability_spam += log((wordCountHamSpam[word][1] + 1)/(nospam + len(wordCountHamSpam)))
                                probability_ham += log((wordCountHamSpam[word][0] + 1)/( noham + len(wordCountHamSpam)))
                
          
                    probability_spam +=log(fspam);
                    probability_ham +=log(fham);
                    
                    
                    
                    
                    if probability_ham>probability_spam:
                        outf.write("ham "+root+"/"+name+"\n");
                    else:
                        outf.write("spam "+root+"/"+name+"\n");
                    
    
main(sys.argv[1]);
import sys
import markdown

def to_html(inputfile,outputfile):
    with open(inputfile,"r") as md_file:
        mdcontent = md_file.read()
        html_content = markdown.markdown(mdcontent)
    
    with open(outputfile,"w") as html_file:
        html_file.write(html_content)

def main():
    if sys.argv[1] == "markdown":
        to_html(sys.argv[2],sys.argv[3])
    else: print("Error")

if __name__ == "__main__":
    main()

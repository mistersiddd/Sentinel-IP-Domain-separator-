import validators
import sys

def main():
    maliciousList = open(sys.argv[1])
    ip_list=[]
    domain=[]

    for x in maliciousList:
        if validators.domain(str(x)):
            domain.append(str(x).strip())
        else:
            ip_list.append(str(x).strip())
    if domain:
        print(domain)
        if ip_list:
            print(ip_list)

if __name__ == "__main__":
    main()
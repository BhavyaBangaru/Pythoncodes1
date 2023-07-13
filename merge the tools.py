def merge_the_tools(string,k):
    dict1={}
    for i in range(1,len(string)+1):
        dict1.update({string[i-1]:'0'})
        if i%k==0:
            print("".join(dict1.keys()))
            dict1={}

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
a =[101,124,351,356,456,786,977,1000]

target =124

low,high =0,len(a) -1

while(low <=high):
    mid =(low +high)//2
    if(a[mid] <target):
        low =mid +1
    else:
        high =mid -1

print("Not present in this  array" if(len(a) <=low) else f'{a[low]} present in this array')

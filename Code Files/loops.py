fruits = ''
bucket = []

while fruits != "done":
    fruits = input("Enter fruit in the bucket !! ") 
    if(fruits != 'done'):
        bucket.append(fruits)
    else:
        print(bucket)

# Add fruits in your bucket till you say done
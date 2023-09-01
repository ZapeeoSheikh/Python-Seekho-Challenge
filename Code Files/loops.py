# Add fruits in your bucket till you say done
# While loop
fruits = ''
bucket = []

while fruits != "done":
    fruits = input("Enter fruit in the bucket !! ") 
    if(fruits != 'done'):
        bucket.append(fruits)
    else:
        print(bucket)

# for loops

countries = {
    'symbol' : ['pk', 'ind', 'ch', 'nz', 'sg', 'uae', 'usa', 'aus'],
    'currency' : ['Rs', 'Rs', 'Yun', 'Nz Dollar', 'Sg Dollar', 'Dirham', 'Dollar', 'Aus Dollar']
}

for item in countries['currency']:
    print(item)
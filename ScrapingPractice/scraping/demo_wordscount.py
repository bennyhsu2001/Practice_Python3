try:
    f = open('zen.txt','r',encoding='utf-8-sig')
except FileNotFoundError:
    print("找不到檔案")
except Exception as e:
    print(e)
else:
    # print(f.read())
    words = f.read().split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print(counts)

finally:
    f.close()


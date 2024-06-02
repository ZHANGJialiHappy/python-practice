def consecutive_six(numbers: str):
    count=0
    countConsectiveSix=0
    for char in numbers:
        if char == '6':
            countConsectiveSix+=1
        if char!= '6':
            if countConsectiveSix==2:
                count+=1
            countConsectiveSix=0
    if countConsectiveSix==2:
        count+=1
    return count

if __name__ == "__main__":
   print(consecutive_six("566"))
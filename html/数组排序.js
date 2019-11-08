print = console.log
let arr = ['你', 'b', 'word', 'a', '01', '03', '02','我']
arr.sort((a,b) => {
    numA = Number(a)
    numB = Number(b)
    if (!isNaN(numA) && !isNaN(numB)) {
        return numA - numB
    } else if (!isNaN(numA)) {
        return -1
    } else if(!isNaN(numB)) {
        return 1
    } else {
        return a.charCodeAt() - b.charCodeAt()
    }
})
print(arr)

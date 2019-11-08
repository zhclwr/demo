console.time('time')
let sum = 0
for (let i = 0; i < 40001; i++ ){
    for (let j = 0; j < 40001; j++ ){
        sum += i * j
    }
}
console.log(sum)
console.timeEnd('time')
const fs = require('fs')

const pairs = fs.readFileSync('example.txt','utf-8',(error,data) => {}).split(/\r?\n/gm).map(data => data.split(',').map(data => data.split('-')))

const camp_cleanup = () => {

    let sum = 0
    pairs.map((pair) => {
        const a = pair[0], b = pair[1];
        if (parseInt(a[0]) <= parseInt(b[0]) && parseInt(a[1]) >= parseInt(b[1]) || parseInt(b[0]) <= parseInt(a[0]) && parseInt(b[1]) >= parseInt(a[1]))  {
            sum ++ 
        }
    })
    console.log(sum)
}

const camp_cleanup2 = () => {

    let overlap_sum = 0
    pairs.map((pair) => {
        const a = pair[0], b = pair[1];
        if (parseInt(a[1]) >= parseInt(b[0]) && parseInt(a[1]) <= parseInt(b[1]) || parseInt(a[1]) >= parseInt(b[0]) && parseInt(a[0]) <= parseInt(b[1]))  {
            overlap_sum ++ 
        }
    })
    console.log(overlap_sum)
}
camp_cleanup()
camp_cleanup2()
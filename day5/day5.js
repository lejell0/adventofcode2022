const fs = require('fs')

const input = fs.readFileSync('input.txt').toString()
const [cargo, procedure] = input.split('\n\n');

let stacks = cargo.split('\n').map((line) => line.includes('[')
      ? Array.from(line.matchAll(/([A-Z]+|\s{4})/g)).map((m) => m[0])
      : Array.from(line.matchAll(/(\d+)/g)).map((m) => m[0])
                                    );

stacks = stacks.map((stack, i) => {
    let newStack = [];
    if (i != stack.length) {
    [...Array(stack.length-1).keys()].forEach((it, innerIndex) => {
        let elem = stacks[innerIndex][i];

        if (elem != '    ' ) {
            newStack.push(elem);
        }
    })
}
return newStack
})

// stacks = stacks.filter(e=>e.length)

const moves = procedure.split("\n").map((moveParse) => {
    const [move, from, to] = Array.from(moveParse.matchAll(/(\d+)/g)).map((m) => m[0]).map(Number);
    return {
        move, from: from, to: to
    };
})

moves.map(({ move, from, to }) => {
    // [ [ 'N', 'Z' ], [ 'D', 'C', 'M' ], [ 'P' ] ]
    let resStack = stacks[from -1].splice(0, move)

    stacks[to-1].unshift(...resStack)
    })


const result = stacks.map(arr => arr[0])
console.log(result)
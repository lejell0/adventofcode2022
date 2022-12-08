const fs = require('fs')

const input = fs.readFileSync('input.txt').toString()

let test = ['abcdefg']

const checkRepeats = (subStr) => {
    return /(.).*\1/.test(subStr);
}

let counter = 4
const findMarker = (str) => {
    for (let i = 0; i<str.length; i++) {
        const marker = str.slice(i, i+4);

        if (checkRepeats(marker)) {
            counter++;
        }

        else {
            return counter++;
        }

    }
}

let chrCounter = 14
const findMsg = (str) => {
    for (let i = 0; i<str.length; i++) {
        const marker = str.slice(i, i+14);

        if (checkRepeats(marker)) {
            chrCounter++;
        }

        else {
            return chrCounter++;
        }

    }
}

console.log(findMarker(input))
console.log(findMsg(input))
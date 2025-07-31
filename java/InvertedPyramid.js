
function printNumberDiamond(rows) {

    for (let i = 1; i <= rows; i++) {
        let spaces = ' '.repeat(rows - i);
        let numbers = '';
        for (let j = 1; j <= i; j++) {
            numbers += j;
            
        }
        for (let j = i - 1; j >= 1; j--) {
            numbers += j;
        }
        console.log(spaces + numbers);
    }


    for (let i = rows - 1; i >= 1; i--) {
        let spaces = ' '.repeat(rows - i);
        let numbers = '';
        for (let j = 1; j <= i; j++) {
            numbers += j;
        }
        for (let j = i - 1; j >= 1; j--) {
            numbers += j;
        }
        console.log(spaces + numbers);
    }
}



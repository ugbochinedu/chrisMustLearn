
function printNumberDiamond(rows) {
    for (let i = 1; i <= rows; i++) {
        let spaces = ' '.repeat(rows - i);
        let numbers = '';
        for (let j = 1; j <= 2 * i - 1; j++) {
            numbers += i;
        }
        console.log(spaces + numbers);
    }
    for (let i = rows - 1; i >= 1; i--) {
        let spaces = ' '.repeat(rows - i);
        let numbers = '';
        for (let j = 1; j <= 2 * i - 1; j++) {
            numbers += i;
        }
        console.log(spaces + numbers);
    }
}
NumberDiamond(5);

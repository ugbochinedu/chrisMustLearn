function FloydsTriangle(rows) {
    let num = 1;
    for (let i = 0; i < rows; i++) {
        let row = '';
        for (let j = 0; j <= i; j++) {
            row += num + ' ';
            num++;
        }
        console.log(row);
    }
}

printFloydsTriangle(5);
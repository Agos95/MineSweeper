let board = document.getElementById("board")
let trueBoard = []

function MakeBoard(rows = 9, cols = 9) {
    board.innerHTML = ""
    // create the grid
    for (let i = 0; i < rows; i++) {
        trueBoard.push([])
        let row = board.insertRow(i)
        for (let j = 0; j < cols; j++) {
            trueBoard[i].push(false)
            let cell = row.insertCell(j)
            cell.onclick = function () { ClickCell(this) }
        }
    }
}

function ClickCell(cell) {

}
let DIFFICULTY_LEVEL = {
    0: {
        "level": "Beginner",
        "shape": [9, 9],
        "mines": 10
    },
    1: {
        "level": "Intermediate",
        "shape": [16, 16],
        "mines": 40
    },
    2: {
        "level": "Advanced",
        "shape": [24, 24],
        "mines": 99
    }
}


let board = document.getElementById("board")
let level = null
let [rows, cols] = [null, null]
let mines = null
let trueBoard = null


/**
 * Gets the difficulty level by inspecting the radio selector.
 */
function GetDifficulty() {
    let difficulty = null
    let levels = document.getElementsByName("difficulty")
    for (let x of levels) {
        if (x.checked) {
            difficulty = x.value
            break
        }
    }
    diff = DIFFICULTY_LEVEL[difficulty]
    level = diff["level"]

    rows = diff["shape"][0]
    cols = diff["shape"][1]
    mines = diff["mines"]
    //console.log("rows = " + rows + " | cols = " + cols)
    //console.log("Level = " + level)
    //console.log("mines = " + mines)

}

/**
 * Creates the boards for the game.
 */
function MakeBoard() {
    // clear any previous element
    board.innerHTML = ""
    trueBoard = []
    // create the board
    for (let i = 0; i < rows; i++) {
        trueBoard.push([])
        let row = board.insertRow(i)
        for (let j = 0; j < cols; j++) {
            trueBoard[i].push(0)
            let cell = row.insertCell(j)
            cell.onclick = function () { ClickCell(this) }
        }
    }
    console.log("trueBoard length = " + trueBoard.length)
    console.log("trueBoard el. length = " + trueBoard[0].length)
    //console.log("trueBoard = " + trueBoard.toString())

    // Place Bombs

}

function ClickCell(cell) {

}
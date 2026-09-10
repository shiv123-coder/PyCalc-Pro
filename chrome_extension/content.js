(async function() {
    console.log("PyCalc Pro Auto-Solver Initialized on Sudoku.com");

    // 1. JavaScript Backtracking Sudoku Solver (Runs purely in the browser)
    function solveSudoku(board) {
        let empty = findEmpty(board);
        if (!empty) return true;
        
        let [row, col] = empty;
        for (let num = 1; num <= 9; num++) {
            if (isValid(board, num, row, col)) {
                board[row][col] = num;
                if (solveSudoku(board)) return true;
                board[row][col] = 0; // backtrack
            }
        }
        return false;
    }

    function findEmpty(board) {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (board[i][j] === 0) return [i, j];
            }
        }
        return null;
    }

    function isValid(board, num, row, col) {
        // row
        if (board[row].includes(num)) return false;
        // col
        for (let i = 0; i < 9; i++) {
            if (board[i][col] === num) return false;
        }
        // box
        let boxRow = Math.floor(row / 3) * 3;
        let boxCol = Math.floor(col / 3) * 3;
        for (let i = boxRow; i < boxRow + 3; i++) {
            for (let j = boxCol; j < boxCol + 3; j++) {
                if (board[i][j] === num) return false;
            }
        }
        return true;
    }

    // 2. DOM Extraction Logic for Sudoku.com
    // Target the 81 cells in the grid by trying multiple known class names
    const selectorsToTry = [
        '.game-cell', 
        '.cell', 
        '.sudoku-cell', 
        '.grid-cell', 
        '.game-grid-cell',
        '[data-cell]',
        'table td'
    ];
    
    let cells = null;
    for (let selector of selectorsToTry) {
        let elements = document.querySelectorAll(selector);
        // Sometimes there are multiple boards (e.g., mini-maps). The main board usually has 81.
        if (elements.length >= 81) {
            // If it's more than 81, just take the first 81 (usually the main grid)
            cells = Array.from(elements).slice(0, 81);
            console.log(`PyCalc Pro: Found 81 cells using selector '${selector}'`);
            break;
        }
    }

    if (!cells || cells.length !== 81) {
        alert("PyCalc Pro: Could not find exactly 81 cells on this page. Website DOM might have changed.");
        return;
    }

    let board = [];
    for (let i = 0; i < 9; i++) {
        board.push([0,0,0,0,0,0,0,0,0]);
    }

    let toFill = []; // Track which cells need to be clicked and solved

    cells.forEach((cell, index) => {
        let row = Math.floor(index / 9);
        let col = index % 9;
        
        let val = 0;
        
        // Extract value from cell SVG or class
        // Sudoku.com uses SVG paths, but sometimes includes the number in the HTML or attributes
        // Heuristic 1: Find aria-label
        if (cell.hasAttribute('aria-label') && cell.getAttribute('aria-label').match(/\d/)) {
            val = parseInt(cell.getAttribute('aria-label').replace(/[^\d]/g, ''));
        }
        
        // Heuristic 2: SVG inner text (fallback)
        if (val === 0) {
            let svgTexts = cell.querySelectorAll('text');
            if (svgTexts.length > 0) {
                let text = svgTexts[0].textContent.trim();
                if (text >= '1' && text <= '9') val = parseInt(text);
            }
        }

        // Heuristic 3: Look for a recognizable class like "value-X" inside the cell
        if (val === 0) {
            let innerHtml = cell.innerHTML;
            let match = innerHtml.match(/val(?:ue)?-(\d)/i);
            if (match) val = parseInt(match[1]);
        }
        
        // Heuristic 4: Direct innerText
        if (val === 0) {
            let text = cell.innerText.trim();
            if (text >= '1' && text <= '9') val = parseInt(text);
        }
        
        // Heuristic 5: data-value attribute
        if (val === 0 && cell.hasAttribute('data-value')) {
            let v = parseInt(cell.getAttribute('data-value'));
            if (!isNaN(v) && v >= 1 && v <= 9) val = v;
        }

        board[row][col] = val;
        
        // If the cell is empty or doesn't have a pre-filled class, mark it to be filled
        if (val === 0 || !cell.classList.contains('prefilled')) {
             if (val === 0) {
                 toFill.push({ index: index, row: row, col: col, cellElement: cell });
             }
        }
    });

    console.log("Extracted Board:", JSON.parse(JSON.stringify(board)));

    // 3. Solve the board
    let solved = solveSudoku(board);
    if (!solved) {
        alert("PyCalc Pro: Extracted puzzle appears invalid or has no solution. Extraction may have failed.");
        return;
    }

    console.log("Puzzle Solved!", board);

    // 4. Inject the solved numbers back into the webpage
    // Target the on-screen number pad (sudoku.com specific)
    const numpadItems = document.querySelectorAll('.numpad-item, .game-numpad-button, .numpad-button, .game-numpad .game-cell, .keypad-button, .number-button, [data-action^="number"], [data-value]');
    let numpadMap = {}; 
    numpadItems.forEach(item => {
        let text = item.innerText.trim();
        if (!text) {
             let match = item.innerHTML.match(/val(?:ue)?-(\d)/i);
             if (match) text = match[1];
        }
        if (!text && item.hasAttribute('data-value')) {
             text = item.getAttribute('data-value');
        }
        if (!text && item.hasAttribute('data-action')) {
             let match = item.getAttribute('data-action').match(/\d/);
             if (match) text = match[0];
        }
        
        if (text >= '1' && text <= '9') {
            numpadMap[parseInt(text)] = item;
        }
    });

    if (Object.keys(numpadMap).length === 0) {
        alert("PyCalc Pro: Could not locate the on-screen number pad to input answers.");
        return;
    }

    async function simulateClick(element) {
        element.dispatchEvent(new MouseEvent('pointerdown', { bubbles: true }));
        element.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
        element.dispatchEvent(new MouseEvent('pointerup', { bubbles: true }));
        element.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
        element.click();
    }

    async function fillCells() {
        // Small initial delay before starting
        await new Promise(r => setTimeout(r, 200));

        for (let task of toFill) {
            let correctVal = board[task.row][task.col];
            let numBtn = numpadMap[correctVal];
            
            if (numBtn && task.cellElement) {
                // Select the empty cell
                await simulateClick(task.cellElement);
                await new Promise(r => setTimeout(r, 40)); // Human-like delay
                
                // Click the correct number on the numpad
                await simulateClick(numBtn);
                await new Promise(r => setTimeout(r, 40)); // Human-like delay
            }
        }
        console.log("PyCalc Pro: All cells filled successfully.");
    }

    await fillCells();
})();

document.getElementById('solve-btn').addEventListener('click', async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    
    // Make sure we only execute on sudoku.com
    if (tab.url.includes("sudoku.com")) {
        // Change button text to indicate working state
        const btn = document.getElementById('solve-btn');
        const originalText = btn.innerText;
        btn.innerText = "⏳ Solving...";
        btn.disabled = true;

        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            files: ['content.js']
        }, (results) => {
            btn.innerText = "✅ Solved!";
            setTimeout(() => {
                btn.innerText = originalText;
                btn.disabled = false;
            }, 3000);
        });
    } else {
        alert("This Auto-Solve feature currently only works on sudoku.com");
    }
});

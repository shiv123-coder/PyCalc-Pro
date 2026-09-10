document.getElementById('solve-btn').addEventListener('click', async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    
    // Execute on any website (the content script has universal structural heuristics)
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
});

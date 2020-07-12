const unsetReq = document.querySelector('.unset-req');
unsetReq.addEventListener('click', fetchUnset);

const undoReq = document.querySelector('.undo-req');
undoReq.addEventListener('click', fetchUndo);

const sendReq = document.querySelector('.send-req');
sendReq.addEventListener('click', fetchSend);

function fetchSend() {
    const userName = document.querySelector('#inputName').value;
    const userValue = document.querySelector('#inputValue').value;
    fetch(`https://instantsearch-282800.oa.r.appspot.com/set?name=${userName}&value=${userValue}`)
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}

function fetchUnset() {
    const userName = document.querySelector('#inputName').value;
    fetch(`https://instantsearch-282800.oa.r.appspot.com/unset?name=${userName}`)
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}

function fetchUndo() {
    fetch('https://instantsearch-282800.oa.r.appspot.com/undo')
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}
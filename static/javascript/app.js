const setReq = document.querySelector('.set-req');
setReq.addEventListener('click', fetchSet);

const unsetReq = document.querySelector('.unset-req');
unsetReq.addEventListener('click', fetchUnset);

const undoReq = document.querySelector('.undo-req');
undoReq.addEventListener('click', fetchUndo);

const redoReq = document.querySelector('.redo-req');
redoReq.addEventListener('click', fetchRedo);



function fetchSet() {
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

function fetchRedo() {
    fetch('https://instantsearch-282800.oa.r.appspot.com/redo')
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}
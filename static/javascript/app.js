const setReq = document.querySelector('.set-req');
setReq.addEventListener('click', fetchSet);

const getReq = document.querySelector('.get-req');
getReq.addEventListener('click', fetchGet);

const unsetReq = document.querySelector('.unset-req');
unsetReq.addEventListener('click', fetchUnset);

const numequaltoReq = document.querySelector('.numequalto-req');
numequaltoReq.addEventListener('click', fetchNumequalto);

const undoReq = document.querySelector('.undo-req');
undoReq.addEventListener('click', fetchUndo);

const redoReq = document.querySelector('.redo-req');
redoReq.addEventListener('click', fetchRedo);

const endReq = document.querySelector('.end-req');
endReq.addEventListener('click', fetchEnd);



function fetchSet() {
    const userName = document.querySelector('#inputName').value;
    const userValue = document.querySelector('#inputValue').value;
    fetch(`https://instantsearch-282800.oa.r.appspot.com/set?name=${userName}&value=${userValue}`)
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}

function fetchGet() {
    const userName = document.querySelector('#inputName').value;
    fetch(`https://instantsearch-282800.oa.r.appspot.com/get?name=${userName}`)
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}

function fetchUnset() {
    const userName = document.querySelector('#inputName').value;
    fetch(`https://instantsearch-282800.oa.r.appspot.com/unset?name=${userName}`)
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}

function fetchNumequalto() {
        const userValue = document.querySelector('#inputValue').value;
    fetch(`https://instantsearch-282800.oa.r.appspot.com/numequalto=${userValue}`)
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

function fetchEnd() {
    fetch('https://instantsearch-282800.oa.r.appspot.com/end')
        .then(response => response.text())
        .then(data => document.querySelector('.title').textContent = data)
}
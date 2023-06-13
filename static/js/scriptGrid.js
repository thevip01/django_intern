try {
    document.getElementById('page' + (String(document.location.href).split("/").splice(-1)[0])).classList.add('active')
}
catch { }
document.getElementById('datatable-search-input').addEventListener('input', checksearch);

btn = document.getElementById('search-btn')
btn.addEventListener('click', search)
btn.style.display = 'none'
function checksearch(e) {
    if (e.target.value == '') {
        btn.style.display = 'none'
    }
    else {
        btn.style.display = 'inline-block'

    }
}

function typecheck(value) {
    document.getElementById('searchresult').hidden = true
    let datatable = document.getElementById('datatable')
    datatable.hidden = true
    oldData = datatable.getElementsByTagName('tr')
    for (let a = 1; a < oldData.length; a++) {
        oldData[a].remove()
    }
    if (value != 'id') {
        document.getElementById('datatable-search-input').type = 'text'
        return 0
    }
    document.getElementById('datatable-search-input').type = 'number'

    document.getElementById('searchTableDiv_H4').remove()
}

async function search() {
    searchBy = document.getElementById('searchBy').value
    searchval = document.getElementById('datatable-search-input').value

    let response = await fetch(`http://127.0.0.1:8000/job/search/${searchBy}/${searchval}`)
    let data = await response.json()
    let searchData = data.searchData
    if (searchData.length > 0) {
        document.getElementById('searchresult').hidden = false
        let datatable = document.getElementById('datatable')
        datatable.hidden = false
        oldData = datatable.getElementsByTagName('tr')
        for (let a = 1; a < oldData.length; a++) {
            oldData[a].remove()
        }
        searchData.forEach(item => {
            let myNewTr = document.createElement('tr')
            Object.values(item).map(i => {
                let myNewTd = document.createElement('td')
                myNewTd.innerHTML = i;
                myNewTr.appendChild(myNewTd)
            })
            myNewTr.classList.add('table-primary')
            datatable.appendChild(myNewTr)
        });
    }
    else {
        document.getElementById('searchresult').hidden = false
        searchTableDiv = document.getElementById('searchTableDiv')
        if (document.getElementById('searchTableDiv_H4') != null) {
            document.getElementById('searchTableDiv_H4').remove()
        }
        h4 = document.createElement('h4')
        h4.id = 'searchTableDiv_H4'
        h4.innerHTML = "No Data Found"
        h4.classList.add('w-100')
        h4.classList.add('text-center')
        searchTableDiv.appendChild(h4)
    }
}
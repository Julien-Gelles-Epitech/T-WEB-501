let params = 
{
    table0:{
        rows:0,
        cols:4
    },
    table1:{
        rows:0,
        cols:9
    },
    table2:{
        rows:0,
        cols:6
    },
}

let addbutons = document.getElementsByClassName("add");
let removebutons = document.getElementsByClassName("remove");
let lines = document.getElementsByClassName("line");

async function remove(that) {  
    console.log(that.parentNode.parentNode.name)

    that.parentNode.parentNode.remove();
    // await fetch("/delete_account", {
    //   method: "POST",
    //   headers: {"Content-Type": "application/json"},
    //   body: JSON.stringify({"name" : "chercheur test num1"})
    // })
    // .then((res) => res.json())
    // .then((res) => {return res})

}

function add(that){
    let tr = document.createElement("tr");
    tr.setAttribute("class", "line bg-white border");
    tr.innerHTML = "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'><input class='h-full w-full border border-blue-gray-200 bg-transparent' type='text' value=''/></th>".repeat(that.parentNode.parentNode.cols);
    tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left flex justify-center'><button onclick='remove(this)' class='remove hover:bg-red-600 text-white text-l font-semibold bg-red-500 rounded p-3 '>Supprimer</button></th>"
    that.parentNode.parentNode.parentNode.parentNode.children.item(1).appendChild(tr);
}

async function gettables(){
    await fetch("/people")
    .then((res) => res.json())
    .then((res) => {
        let tr = document.createElement("tr");
        tr.cols = 4;
        tr.innerHTML = "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> username </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> password </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> email </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> companie_siret </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left flex justify-center'> <button onclick='add(this)' class='add hover:bg-green-600 text-white max-w-fit text-l font-semibold bg-green-500 rounded p-3'>Ajouter</button> </th>"
        document.getElementsByTagName("thead")[0].appendChild(tr);

        for (let index = 0; index < res.length; index++) {
            let tr = document.createElement("tr");
            tr.setAttribute("class", "line bg-gray-100 border");

            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].username.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].password.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].email.replace('"', ' ')+'"/></th>'
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'><input class='h-full w-full border border-blue-gray-200 bg-transparent' type='text' value='"+res[index].companie_siret+"'/></th>"
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left flex justify-center'><button onclick='remove(this)' class='remove hover:bg-red-600 text-white text-l font-semibold bg-red-500 rounded p-3 '>Supprimer</button></th>"

            document.getElementsByTagName("tbody")[0].appendChild(tr);
        }
        
    })
    
    await fetch("/advertisement")
    .then((res) => res.json())
    .then((res) => {
        let tr = document.createElement("tr");
        tr.cols = 9;
        tr.innerHTML = "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> ad_id </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> title </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> companie_siret </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> description </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> date </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> salary </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> adress </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> contract </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> category </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left flex justify-center'> <button onclick='add(this)' class='add hover:bg-green-600 text-white max-w-fit text-l font-semibold bg-green-500 rounded p-3'>Ajouter</button> </th>"
        document.getElementsByTagName("thead")[1].appendChild(tr);

        for (let index = 0; index < res.length; index++) {
            let tr = document.createElement("tr");
            tr.setAttribute("class", "line bg-gray-100 border");

            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'><input class='h-full w-full border border-blue-gray-200 bg-transparent' type='text' value='"+res[index].ad_id+"'/></th>"
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].title.replace('"', ' ')+'"/></th>'
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'><input class='h-full w-full border border-blue-gray-200 bg-transparent' type='text' value='"+res[index].companie_siret+"'/></th>"
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].description.replace('"', ' ')+'"/></th>'
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'><input class='h-full w-full border border-blue-gray-200 bg-transparent' type='text' value='"+res[index].date+"'/></th>"
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'><input class='h-full w-full border border-blue-gray-200 bg-transparent' type='text' value='"+res[index].salary+"'/></th>"
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].adress.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].contract.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].category.replace('"', ' ')+'"/></th>'
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left flex justify-center'><button onclick='remove(this)' class='remove hover:bg-red-600 text-white text-l font-semibold bg-red-500 rounded p-3 '>Supprimer</button></th>"

            document.getElementsByTagName("tbody")[1].appendChild(tr);
        }
        
    })

    await fetch("/companie")
    .then((res) => res.json())
    .then((res) => {
        let tr = document.createElement("tr");
        tr.cols = 6;
        tr.innerHTML = "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> companie_siret </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> name </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> adress </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> phone </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> logo </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'> description </th> <th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left flex justify-center'> <button onclick='add(this)' class='add hover:bg-green-600 text-white max-w-fit text-l font-semibold bg-green-500 rounded p-3'>Ajouter</button> </th>"
        document.getElementsByTagName("thead")[2].appendChild(tr);

        for (let index = 0; index < res.length; index++) {
            let tr = document.createElement("tr");
            tr.setAttribute("class", "line bg-gray-100 border");
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left'><input class='h-full w-full border border-blue-gray-200 bg-transparent' type='text' value='"+res[index].companie_siret+"'/></th>"
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].name.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].adress.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].phone.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].logo.replace('"', ' ')+'"/></th>'
            tr.innerHTML += '<th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left"><input class="h-full w-full border border-blue-gray-200 bg-transparent" type="text" value="'+res[index].description.replace('"', ' ')+'"/></th>'
            tr.innerHTML += "<th scope='col' class='text-sm font-medium text-gray-900 px-6 py-4 text-left flex justify-center'><button onclick='remove(this)' class='remove hover:bg-red-600 text-white text-l font-semibold bg-red-500 rounded p-3 '>Supprimer</button></th>"

            document.getElementsByTagName("tbody")[2].appendChild(tr);
        }
        
    })
}  
window.addEventListener("load", gettables);



const buttons = document.getElementsByClassName("more");
function resetbuttons(){
    for (let index = 0; index < buttons.length; index++) {
        buttons[index].classList.remove("hidden");
    }
}
var active = null;
var size;
if (window.innerWidth > 1024) {
    size = 1;
} else {
    size = 0;
}

async function getOneAdvertisement(number){
    await fetch("/advertisement/id="+number)
    .then((res) => res.json())
    .then(((res) => {
        
        active = number;
        let panelcontent = document.getElementsByClassName("panelcontent")[0];
        panelcontent.innerHTML = "";

        let jobs = document.getElementsByClassName("job");
        for (let index = 0; index < jobs.length; index++) {
            jobs[index].classList.remove("hidden");
        }


        let smallpanelcontent = document.getElementsByClassName("plus");
        for (let index = 0; index < smallpanelcontent.length; index++) {
            smallpanelcontent[index].innerHTML = "";
            smallpanelcontent[index].classList.add("hidden");
        }
        smallpanelcontent[number-1].classList.remove("hidden");

        let infosdiv = document.createElement("div");
        infosdiv.setAttribute("class", "w-full flex flex-row items-center");

        let logo = document.createElement("img");
        logo.setAttribute("src", "../static/img/logo.jpg");
        logo.setAttribute("alt", "logo");
        logo.setAttribute("class", "h-24 w-24 m-1");
        infosdiv.appendChild(logo);

        let textdiv = document.createElement("div");
        textdiv.setAttribute("class", "m-3");

        let span1 = document.createElement("span");
        span1.setAttribute("class", "text-blue-500 text-sm");
        span1.innerHTML = res.category;
        textdiv.appendChild(span1);

        let h3 = document.createElement("h3");
        h3.setAttribute("class", "font-bold mt-px");
        h3.innerHTML = res.title;
        textdiv.appendChild(h3);

        let span2 = document.createElement("span");
        span2.setAttribute("class", "text-slate-600 font-bold text-sm");
        span2.innerHTML = "NAME";
        textdiv.appendChild(span2);

        infosdiv.appendChild(textdiv);

        let detailsdiv = document.createElement("div");
        detailsdiv.setAttribute("class", "flex flex-wrap items-center gap-3 mt-2");

        let span3 = document.createElement("span");
        span3.setAttribute("class", "bg-blue-100 text-blue-500 rounded-full px-3 py-1 text-sm");
        span3.innerHTML = res.contract;
        detailsdiv.appendChild(span3);

        let span4 = document.createElement("span");
        span4.setAttribute("class", "text-slate-600 text-sm flex gap-1 items-center");
        span4.innerHTML = "<svg xmlns='http://www.w3.org/2000/svg' class='h-4 w-4' fill='none' viewBox='0 0 24 24' stroke='currentColor' stroke-width='2'><path stroke-linecap='round' stroke-linejoin='round' d='M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z' /> <path stroke-linecap='round' stroke-linejoin='round' d='M15 11a3 3 0 11-6 0 3 3 0 016 0z' /> </svg>" + res.adress;
        detailsdiv.appendChild(span4);

        let span5 = document.createElement("span");
        span5.setAttribute("class", "text-slate-600 text-sm flex gap-1 items-center");
        span5.innerHTML = "$"+ res.salary;
        detailsdiv.appendChild(span5);

        textdiv.appendChild(detailsdiv)
        panelcontent.appendChild(infosdiv);
        let infosdiv2 = infosdiv.cloneNode(true);
        smallpanelcontent[number-1].appendChild(infosdiv2);

        let p = document.createElement("p");
        p.setAttribute("class", "mt-3 text-gray-500 text-sm");
        p.innerHTML = res.description;
        panelcontent.appendChild(p);
        let p2 = p.cloneNode(true);
        smallpanelcontent[number-1].appendChild(p2);

        let button = document.createElement("button");
        button.setAttribute("class", "w-1/3 mt-3 bg-blue-500 text-white font-medium px-4 py-2 rounded-md flex items-center justify-center hover:scale-105 active:bg-blue-600");
        button.innerHTML = "Postuler";
        panelcontent.appendChild(button);
        let button2 = button.cloneNode(true);
        smallpanelcontent[number-1].appendChild(button2);

        let quit = document.createElement("button");
        quit.setAttribute("class", "absolute right-0 w-10 h-10 text-2xl mr-3 text-gray-500");
        quit.setAttribute("id", "quit");
        quit.innerHTML = "X";

        panelcontent.appendChild(quit);

        if (window.innerWidth > 1024) {
            let smallpanelcontent = document.getElementsByClassName("plus");
            for (let index = 0; index < smallpanelcontent.length; index++) {
                smallpanelcontent[index].innerHTML = "";
                smallpanelcontent[index].classList.add("hidden");
                panelcontent.classList.remove("hidden");
                
            }
            let mainpanel = document.getElementsByClassName("mainpanel")[0];
            mainpanel.classList.remove("hidden");
            let mainlist = document.getElementsByClassName("mainlist")[0];
            mainlist.classList.add("w-3/5");

        }else{
            let mainlist = document.getElementsByClassName("mainlist")[0];
            mainlist.classList.remove("w-3/5");
            let mainpanel = document.getElementsByClassName("mainpanel")[0];
            mainpanel.classList.add("hidden");
            document.getElementsByClassName("job")[number-1].classList.add("hidden");
        }
        
    }))
    .then(() => {
        for (let index = 0; index < buttons.length; index++) {
            document.getElementById((index+1).toString()).classList.remove("xl:w-[calc(50%-20px)]");
        }
    })
    .then(() => {
        let quit = document.getElementById("quit");
        quit.addEventListener("click", () => {
            resetbuttons();
            active = null;
            let mainlist = document.getElementsByClassName("mainlist")[0];
            mainlist.classList.remove("w-3/5");
            let mainpanel = document.getElementsByClassName("mainpanel")[0];
            mainpanel.classList.add("hidden");
            for (let index = 0; index < buttons.length; index++) {
                document.getElementById((index+1).toString()).classList.add("xl:w-[calc(50%-20px)]");
            }
        })
    })
    .catch((error) => console.log(error))
}

function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    var items = location.search.substr(1).split("&");
    for (var index = 0; index < items.length; index++) {
        tmp = items[index].split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    }
    return result;
}



async function getAdvertisement(){
    await fetch("/advertisement")
    .then((res) => res.json())
    .then((res) => {
        let title = findGetParameter("title");
        let place = findGetParameter("place");
        const mainlist = document.getElementsByClassName("mainlist")[0];
        res.forEach(element => {
            if (    (title == null) ||  (element.title.toLowerCase().includes(title.toLowerCase())) 
                ){

                let jobdiv = document.createElement("div");
                jobdiv.setAttribute("id", element.ad_id.toString());
                jobdiv.setAttribute("class", "job bg-gradient-to-r from-white to-blue-100 my-2.5 xl:my-0 flex flex-col md:flex-row md:justify-between md:items-center xl:w-[calc(50%-20px)] pr-5 py-4 rounded-md w-full h-min hover:outline outline-blue-500");
                
                let infosdiv = document.createElement("div");
                infosdiv.setAttribute("class", "w-full md:w-3/4 flex flex-row");
                
                let logo = document.createElement("img");
                logo.setAttribute("src", "../static/img/logo.jpg");
                logo.setAttribute("alt", "logo");
                logo.setAttribute("class", "h-24 w-24 m-1");
                
                let textdiv = document.createElement("div");
                
                let span1 = document.createElement("span");
                span1.setAttribute("class", "text-blue-500 text-sm");
                span1.innerHTML = element.category;
                textdiv.appendChild(span1);
                
                let h3 = document.createElement("h3");
                h3.setAttribute("class", "font-bold mt-px");
                h3.innerHTML = element.title;
                textdiv.appendChild(h3);

                let detailsdiv = document.createElement("div");
                detailsdiv.setAttribute("class", "flex items-center gap-3 mt-2");

                let span2 = document.createElement("span");
                span2.setAttribute("class", "bg-blue-100 text-blue-500 rounded-full px-3 py-1 text-sm");
                span2.innerHTML = element.contract;
                detailsdiv.appendChild(span2);

                let span3 = document.createElement("span");
                span3.setAttribute("class", "text-slate-600 text-sm flex gap-1 items-center");
                span3.innerHTML = "<svg xmlns='http://www.w3.org/2000/svg' class='h-4 w-4' fill='none' viewBox='0 0 24 24' stroke='currentColor' stroke-width='2'><path stroke-linecap='round' stroke-linejoin='round' d='M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z' /> <path stroke-linecap='round' stroke-linejoin='round' d='M15 11a3 3 0 11-6 0 3 3 0 016 0z' /> </svg>" + element.adress;
                detailsdiv.appendChild(span3);

                textdiv.appendChild(detailsdiv);

                let p = document.createElement("p");
                p.setAttribute("class", "p1 mt-3 text-gray-500 text-sm");
                p.innerHTML = element.description.substr(0, 80) + "...";
                textdiv.appendChild(p)

                infosdiv.appendChild(logo);
                infosdiv.appendChild(textdiv);
                jobdiv.appendChild(infosdiv);

                let buttondiv = document.createElement("div");
                let button = document.createElement("button");
                button.setAttribute("class", "more mt-3 bg-blue-500 text-white font-medium px-4 py-2 rounded-md flex gap-1 items-center ml-24 md:ml-0 hover:scale-105 active:bg-blue-600");
                button.innerHTML = "See More" + "<svg xmlns='http://www.w3.org/2000/svg' class='h-4 w-4' fill='none' viewBox='0 0 24 24' stroke='currentColor' stroke-width='2'> <path stroke-linecap='round' stroke-linejoin='round' d='M13 7l5 5m0 0l-5 5m5-5H6' /> </svg>";
                buttondiv.appendChild(button);


                jobdiv.appendChild(buttondiv);
                mainlist.appendChild(jobdiv);

                let jobdivplus = document.createElement("div");
                jobdivplus.setAttribute("class", "plus hidden relative bg-gradient-to-r from-white to-blue-100 flex flex-col px-5 py-4 my-2.5 rounded-md w-full");
                mainlist.appendChild(jobdivplus);
            }
        });
        console.log(res);
    })
    .then(() => {
        for (let index = 0; index < buttons.length; index++) {
            buttons[index].param = index.toString();
            buttons[index].addEventListener("click", (button)=>{

                resetbuttons();
                let mainlist = document.getElementsByClassName("mainlist")[0];
                mainlist.classList.add("w-3/5");
                document.getElementById(parseInt(button.target.param)+1).getElementsByClassName("more")[0].classList.add("hidden");
                getOneAdvertisement(parseInt(button.target.param)+1);                
            }); 
        }
        // console.log(document.getElementsByClassName("apply"));
    })
    .then(() => {
        function main_size(){
            let main = document.getElementsByTagName("main")[0];
            let header = document.getElementsByTagName("header")[0];
    
            let size = window.innerHeight - header.offsetHeight -52;
            main.style.height = size+"px";
        }
        main_size();
    
        function job_size(){
            let jobs = document.getElementsByClassName("job");
            
            for (let i = 1; i < jobs.length; i+=2) {
                if (window.innerWidth > 1280) {
                    let max = Math.max(jobs[i-1].offsetHeight, jobs[i].offsetHeight);
                    jobs[i-1].style.height = max+"px";
                    jobs[i].style.height = max+"px";
                }else{
                    jobs[i-1].style.height = "min-content";
                    jobs[i].style.height = "min-content";
                }
            }
            
        }
        job_size();
    
        window.addEventListener("resize", (event) => {
            job_size();
            main_size();
        });
    })
    .catch((error) => console.log(error))
}
window.addEventListener("load", getAdvertisement);

window.addEventListener("resize", () => {
    if (window.innerWidth > 1024 && size == 0) {
        size = 1;
        if (active != null) { 
            getOneAdvertisement(active)
        }
    }
    if (window.innerWidth <= 1024 && size == 1) {
        size = 0;
        if (active != null) { 
            getOneAdvertisement(active)
        }
    }

})
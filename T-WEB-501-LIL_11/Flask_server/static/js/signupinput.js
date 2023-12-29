window.addEventListener("load", () => {
    const verif = document.getElementsByClassName("verif");
    const data = document.getElementsByClassName("data");
    console.log(data[0]);

    data[0].addEventListener("input", ()=>{
        if (data[0].value.length > 3){
            verif[0].classList.add("hidden");
            verif[1].classList.remove("hidden");
        }else{
            verif[1].classList.add("hidden");
            verif[0].classList.remove("hidden");
        }
    })
    data[1].addEventListener("input", ()=>{
        if (data[1].value.length > 3){
            verif[2].classList.add("hidden");
            verif[3].classList.remove("hidden");
        }else{
            verif[3].classList.add("hidden");
            verif[2].classList.remove("hidden");
        }
    })
    data[2].addEventListener("input", ()=>{
        if (data[2].value.length > 3){
            verif[4].classList.add("hidden");
            verif[5].classList.remove("hidden");
        }else{
            verif[5].classList.add("hidden");
            verif[4].classList.remove("hidden");
        }
        if (data[2].value == data[3].value){
            verif[6].classList.add("hidden");
            verif[7].classList.remove("hidden");
        }
        else{
            verif[7].classList.add("hidden");
            verif[6].classList.remove("hidden");
        }
    })
    data[3].addEventListener("input", ()=>{
        if (data[3].value == data[2].value){
            verif[6].classList.add("hidden");
            verif[7].classList.remove("hidden");
        }else{
            verif[7].classList.add("hidden");
            verif[6].classList.remove("hidden");
        }
    })

    if (data.length == 5) {
        data[4].addEventListener("input", ()=>{
            if (data[4].value.length > 3){
                verif[8].classList.add("hidden");
                verif[9].classList.remove("hidden");
            }else{
                verif[9].classList.add("hidden");
                verif[8].classList.remove("hidden");
            }
        })
    }

});
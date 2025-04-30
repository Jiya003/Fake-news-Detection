document.addEventListener("DOMContentLoaded",()=>{
    const resultBox=document.querySelector('.result');
    if (resultBox){
        resultBox.style.opacity=0;
        setTimeout(()=>{
            resultBox.style.transition="opacity 0.8s ease";
            resultBox.style.opacity=1;
        },200);
    }
});

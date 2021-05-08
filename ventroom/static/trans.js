window.onload=() =>{
    const transelem=document.querySelector(".transition");
    const anchors=document.querySelectorAll("a");
    setTimeout(() => {
        transelem.classList.remove('is-active')
    },500);

    for (let i=0;i<anchors.length;i++)
    {
        const anchor=anchors[i];
        anchor.addEventListener('click', e=>{
            e.preventDefault();
            let target=e.target.href;
            transelem.classList.add('is-active');
            setTimeout(() => {
                window.location.href=target;
            }, 1000);
        });
    }
}

window.onscroll = function() {myFunction()};

var navbar = document.querySelector("nav");


function myFunction() {
  if (window.pageYOffset > 0) {
    navbar.classList.add("sticky")
  } 
  else {
    navbar.classList.remove("sticky");
  }
}

const animin=document.querySelectorAll(".anim");
observer=new IntersectionObserver((entries)=>
{
    entries.forEach(entry=>{
        if(entry.intersectionRatio > 0)
        {
            entry.target.style.animation="anim1 0.6s forwards ease-out";
        }
        else
        {
            entry.target.style.animation="none";
        }
    })
})
animin.forEach(eachanim=>{
    observer.observe(eachanim)   
})

let mouseCursor = document.querySelector('.fancyCursor');
let navlinks = document.querySelectorAll('.NavBar a');
let hlink = document.querySelectorAll('.eventreg-mainform a');
let plink = document.querySelectorAll('.participantreg a');
let Halink = document.querySelectorAll('.host-access a');
let hbtn = document.querySelectorAll('.HostButton a')
window.addEventListener('mousemove',cursor);

function cursor(e){
    console.log(e);
       mouseCursor.style.top=e.pageY+'px';
       mouseCursor.style.left=e.pageX + 'px';
}
navlinks.forEach(link => {
    link.addEventListener('mouseleave',()=>{
        mouseCursor.classList.remove("link-grow");
        mouseCursor.classList.remove("hoverd-link");
    });
    link.addEventListener('mouseover',()=>{
        mouseCursor.classList.add("link-grow");
        mouseCursor.classList.add("hoverd-link");
    });
});
hlink.forEach(link=>{
    link.addEventListener('mouseleave',()=>{
        mouseCursor.classList.remove("link-grow");
        mouseCursor.classList.remove("hoverd-link");
    });
    link.addEventListener('mouseover',()=>{
        mouseCursor.classList.add("link-grow");
        mouseCursor.classList.add("hoverd-link");
    });
});
plink.forEach(link=>{
    link.addEventListener('mouseleave',()=>{
        mouseCursor.classList.remove("link-grow");
        mouseCursor.classList.remove("hoverd-link");
    });
    link.addEventListener('mouseover',()=>{
        mouseCursor.classList.add("link-grow");
        mouseCursor.classList.add("hoverd-link");
    });
});
Halink.forEach(link=>{
    link.addEventListener('mouseleave',()=>{
        mouseCursor.classList.remove("link-grow");
        mouseCursor.classList.remove("hoverd-link");
    });
    link.addEventListener('mouseover',()=>{
        mouseCursor.classList.add("link-grow");
        mouseCursor.classList.add("hoverd-link");
    });
});
hbtn.forEach(link=>{
    link.addEventListener('mouseleave',()=>{
        mouseCursor.classList.remove("link-grow");
        mouseCursor.classList.remove("hoverd-link");
    });
    link.addEventListener('mouseover',()=>{
        mouseCursor.classList.add("link-grow");
        mouseCursor.classList.add("hoverd-link");
    });
});
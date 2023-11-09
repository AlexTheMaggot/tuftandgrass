window.addEventListener('load', () => {
    let slider = document.getElementById('slider');
    let slides = slider.children
    let inf_cyc_1 = true;
    for (let step = 0; step < 5; step++) {
        for (let slide of slides) {
            let new_slide = slide.cloneNode(true)
            slider.appendChild(new_slide)
        }
    }
});



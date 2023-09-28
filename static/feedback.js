
const ratingCircles = document.querySelectorAll('.rating-circle');

ratingCircles.forEach(circle => {
    circle.addEventListener('click', () => {
        // Remove selected class from all circles
        ratingCircles.forEach(c => {
            c.classList.remove('selected');
        });

        // Add selected class to the clicked circle
        circle.classList.add('selected');

        // Get the selected score from the data attribute
        const selectedScore = circle.getAttribute('data-score');

        // You can use the selectedScore value as needed (e.g., submit it with a form)
        console.log('Selected Score:', selectedScore);
    });
});

const ratingCircles1 = document.querySelectorAll('.rating-circle-1');

ratingCircles1.forEach(circle => {
    circle.addEventListener('click', () => {
        // Remove selected class from all circles
        ratingCircles1.forEach(c => {
            c.classList.remove('selected');
        });

        // Add selected class to the clicked circle
        circle.classList.add('selected');

        // Get the selected score from the data attribute
        const selectedScore = circle.getAttribute('data-score');

        // You can use the selectedScore value as needed (e.g., submit it with a form)
        console.log('Selected Score:', selectedScore);
    });
});



// Handle cipher algorithm selection
document.getElementById('algorithm').addEventListener('change', function() {
    // Hide all cipher info boxes
    document.querySelectorAll('.cipher-info').forEach(box => box.classList.add('d-none'));
    // Show the selected cipher info box
    const selectedInfo = document.getElementById('info-' + this.value);
    if (selectedInfo) {
        selectedInfo.classList.remove('d-none');
    }

    if (learningModeActive) {
        learningModes.forEach(mode => mode.classList.add('d-none'));
        const learningMode = document.getElementById(`learning-${this.value}`);
        if (learningMode) {
            learningMode.classList.remove('d-none');
            animateLearningSteps();
        }
    }
});

// Fake coordinates update
function updateCoordinates() {
    const lat = Math.floor(Math.random() * 90);
    const long = Math.floor(Math.random() * 180);
    const coords = `COORDINATES: ${lat}° ${Math.floor(Math.random() * 60)}' ${Math.floor(Math.random() * 60)}"N, ${long}° ${Math.floor(Math.random() * 60)}' ${Math.floor(Math.random() * 60)}"E`;
    document.getElementById('coordinates').textContent = coords;
}
setInterval(updateCoordinates, 3000);
updateCoordinates();

// Typewriter effect with sound
function typeWriter(text, element, sound, speed = 50) {
    let i = 0;
    element.textContent = '';
    
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            if (text.charAt(i) !== ' ') {
                sound.currentTime = 0;
                sound.play();
            }
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typewriter effect if result exists
document.addEventListener('DOMContentLoaded', function() {
    const resultText = document.querySelector('.result-text');
    const typewriterElement = document.querySelector('.typewriter-text');
    const typeSound = document.getElementById('typeSound');
    
    if (resultText && typewriterElement) {
        const text = resultText.textContent;
        resultText.style.display = 'none';
        typeWriter(text, typewriterElement, typeSound);
    }
});

// Add sound toggle
let isSoundEnabled = true;
const typeSound = document.getElementById('typeSound');
typeSound.volume = 0.5; // Reduce volume to 20%

document.addEventListener('keydown', function(e) {
    if (e.key === 'm' || e.key === 'M') {
        console.log('Sound toggle triggered');
        isSoundEnabled = !isSoundEnabled;
        typeSound.volume = isSoundEnabled ? 0.5 : 0;
    }
});

// Learning Mode Functionality
const learningToggle = document.getElementById('learningToggle');
const learningModes = document.querySelectorAll('.learning-mode');
let learningModeActive = false;

learningToggle.addEventListener('click', () => {
    learningModeActive = !learningModeActive;
    learningToggle.classList.toggle('active');
    
    // Show/hide learning mode for current cipher
    const currentCipher = document.getElementById('algorithm').value;
    const currentLearningMode = document.getElementById(`learning-${currentCipher}`);
    
    learningModes.forEach(mode => mode.classList.add('d-none'));
    if (learningModeActive && currentLearningMode) {
        currentLearningMode.classList.remove('d-none');
        animateLearningSteps();
    }
});

// Animate learning steps
function animateLearningSteps() {
    const steps = document.querySelectorAll('.learning-step');
    steps.forEach((step, index) => {
        setTimeout(() => {
            step.classList.add('visible');
        }, index * 500);
    });
}

// Practice Challenge
const practiceAnswers = {
    'caesar': {
        message: 'KHOOR',
        answer: 'HELLO',
        hint: 'Each letter is shifted 3 positions forward in the alphabet! Try moving each letter back 3 positions.'
    },
    'atbash': {
        message: 'SVOOL',
        answer: 'HELLO',
        hint: 'Replace each letter with its opposite in the alphabet (A→Z, B→Y, etc.). Try writing the alphabet and matching each letter with its opposite!'
    },
    'morse': {
        message: '.... . .-.. .-.. ---',
        answer: 'HELLO',
        hint: 'Each letter is represented by dots and dashes. Look for patterns - H is ...., E is ., L is .-.., O is ---'
    },
    'binary': {
        message: '01001000 01000101 01001100 01001100 01001111',
        answer: 'HELLO',
        hint: 'Each letter is represented by 8 bits (binary digits). Try looking for repeating patterns - LL will have the same code!'
    },
    'pigpen': {
        message: '⊓|⊐⊏⊐⊐⊗',
        answer: 'HELLO',
        hint: 'Each symbol represents a letter based on its position in a grid. Look for patterns in the symbols!'
    }
};

function updatePracticeChallenge(cipher) {
    const practiceMessage = document.getElementById('practice-message');
    const practiceAnswer = document.getElementById('practice-answer');
    const practice = practiceAnswers[cipher];
    
    if (practice) {
        practiceMessage.textContent = practice.message;
        if (practiceAnswer) {
            practiceAnswer.value = ''; // Clear previous answer
        }
        // Hide any previous success stamp
        const successStamp = document.querySelector('.success-stamp');
        if (successStamp) {
            successStamp.classList.remove('visible');
        }
    }
}

// Initialize practice challenge on page load
document.addEventListener('DOMContentLoaded', function() {
    // ... existing DOMContentLoaded code ...
    
    // Initialize practice challenge for the currently selected cipher
    const selectedCipher = document.getElementById('algorithm').value;
    if (selectedCipher) {
        updatePracticeChallenge(selectedCipher);
    }
});

// Update practice challenge when cipher changes
document.getElementById('algorithm').addEventListener('change', function() {
    // ... existing cipher change code ...
    updatePracticeChallenge(this.value);
});

// Handle practice answer with improved feedback
document.getElementById('practice-answer')?.addEventListener('input', function() {
    const cipher = document.getElementById('algorithm').value;
    const practice = practiceAnswers[cipher];
    const successStamp = document.querySelector('.success-stamp');
    
    if (practice) {
        if (this.value.toUpperCase() === practice.answer) {
            successStamp.textContent = '✨ Great job! ✨';
            successStamp.classList.add('visible');
            // Play success sound or animation
            setTimeout(() => {
                successStamp.classList.remove('visible');
            }, 2000);
        }
    }
});

// Show hint with improved formatting
document.getElementById('showHint')?.addEventListener('click', function() {
    const cipher = document.getElementById('algorithm').value;
    const practice = practiceAnswers[cipher];
    
    if (practice) {
        alert(`🎯 Practice Mission Hint:\n\n${practice.hint}`);
    }
}); 
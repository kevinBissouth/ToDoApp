// Attendre 5 secondes puis afficher la vraie page
setTimeout(() => {
    document.getElementById('loadingPage').classList.remove('hidden');
    document.getElementById('presentationPage').classList.add('blur-lg');
}, 1000); // 5000 ms = 5 secondes

// Attendre 5 secondes puis afficher la vraie page
setTimeout(() => {
    document.getElementById('loadingPage').classList.add('hidden');
    document.getElementById('presentationPage').classList.remove('blur-lg');
    document.getElementById('presentationPage').classList.remove('pointer-events-none');
}, 13000); // 5000 ms = 5 secondes
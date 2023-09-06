function updateDateTime() {
    var currentDate = new Date();
    var options = { year: 'numeric', month: 'long', day: 'numeric' };
    document.getElementById('current-date').textContent = currentDate.toLocaleDateString('en-US', options);

    var currentTime = new Date();
    var timeOptions = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
    document.getElementById('current-time').textContent = currentTime.toLocaleTimeString('en-US', timeOptions);
}

// Update date and time immediately and then every second
updateDateTime();
setInterval(updateDateTime, 1000);
const seatGrid = document.getElementById('seat-grid');
for (let i = 0; i < 20; i++) {
    const seat = document.createElement('div');
    seat.className = 'seat';
    seat.id = 'seat' + i;
    seat.onclick = () => selectSeat(i);
    seatGrid.appendChild(seat);
}

let selectedSeat = null;

// Select a seat
function selectSeat(seatNumber) {
    if (selectedSeat !== null) {
        document.getElementById('seat' + selectedSeat).classList.remove('selected');
    }
    selectedSeat = seatNumber;
    document.getElementById('seat' + seatNumber).classList.add('selected');
}

// Set timer for the seat
function setTimer() {
    const minutes = document.getElementById('timer-input').value;
    if (selectedSeat === null || !minutes) {
        alert("Please select a seat and enter time in minutes.");
        return;
    }
    const expiration = new Date(new Date().getTime() + minutes * 60000).toUTCString();
    document.cookie = "seat" + selectedSeat + "=" + minutes + ";expires=" + expiration + ";path=/";
    alert("Timer set for seat " + selectedSeat + " for " + minutes + " minutes.");
}
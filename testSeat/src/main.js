function selectSeat(element, seatId) {
    let time = prompt("How many hours/minutes? (format: HH:MM)");
    if (time) {
      let [hours, minutes] = time.split(':').map(t => parseInt(t));
      let totalSeconds = hours * 3600 + minutes * 60;
      element.classList.add('active');
      countdown(element, totalSeconds);
    }
  }

  function countdown(element, seconds) {
    let timerElement = document.createElement('div');
    timerElement.classList.add('timer');
    element.appendChild(timerElement);

    let interval = setInterval(() => {
      let hours = parseInt(seconds / 3600);
      let minutes = parseInt((seconds % 3600) / 60);
      let remainingSeconds = seconds % 60;
      timerElement.textContent = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
      seconds--;

      if (seconds < 0) {
        clearInterval(interval);
        element.classList.remove('active');
        element.removeChild(timerElement);
      }
    }, 1000);
  }
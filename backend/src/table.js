document.addEventListener("DOMContentLoaded", function () {
    fetch("src/TestData.csv") // csv file
      .then((response) => response.text())
      .then((csvText) =>
        Papa.parse(csvText, {
          header: true,
          complete: function (results) {
            populateTable(results.data);
          },
        })
      );
  });

  function populateTable(usersData) {
    var userDataContainer = document.getElementById("userData");

    usersData.forEach(function (user) {
      var row = document.createElement("tr");

      // Add data cells
      row.innerHTML = `
          <td>${user.PID}</td>
          <td>${user.Name}</td>
          <td>${user["Time In"]}</td>
          <td>${user["Total Hours"]}</td>
          <td>${user["Extra Time"]}</td>
          <td class="tally">${generateTally()}</td>
          <td>${generateDropdown()}</td>
      `;

      userDataContainer.appendChild(row);
    });
  }

  function generateTally() {
    var tallyHtml = "";
    for (var i = 0; i < 5; i++) {
      tallyHtml +=
        '<span class="tally-dot" onclick="toggleTally(this)"></span>';
    }
    return tallyHtml;
  }

  function generateDropdown() {
    return `
      <select class="dropdown">
          <option value="a1">A1</option>
          <option value="a2">A2</option>
          <option value="a3">A3</option>
          <option value="a4">A4</option>
          <option value="a5">A5</option>
          <option value="a1">B1</option>
          <option value="b2">B2</option>
          <option value="b3">B3</option>
          <option value="b4">B4</option>
          <option value="b5">B5</option>
          <option value="c1">C1</option>
          <option value="c2">C2</option>
          <option value="c3">C3</option>
          <option value="c4">C4</option>
          <option value="c5">C5</option>
          <option value="c6">C6</option>
          <option value="d1">D1</option>
          <option value="d2">D2</option>
          <option value="d3">D3</option>
          <option value="d4">D4</option>
          <option value="d5">D5</option>
          <option value="d6">D6</option>
          <option value="e1">E1</option>
          <option value="e2">E2</option>
          <option value="e3">E3</option>
          <option value="e4">E4</option>
      </select>
  `;
  }

  function toggleTally(element) {
    element.classList.toggle("active");
  }
  
  async function loadCSVData(filePath) {
      const response = await fetch(filePath);
      const data = await response.text();
  return Papa.parse(data, { header: true }).data;
}


  function parseCSV(data) {
  const lines = data.split("\n").filter(line => line.trim());
  const headers = lines[0].split(",").map(header => header.trim()); 
  return lines.slice(1).map(line => {
      const values = line.split(",");
      if (values.length !== headers.length) {
          throw new Error('Mismatched headers and values in CSV row');
      }
      return headers.reduce((object, header, index) => {
          object[header] = values[index] && values[index].trim(); 
          return object;
      }, {});
  });
}


function createOverstaySeverityBarChart(data) {
  const severityCounts = { 'Severe': 0, 'Moderate': 0, 'Light': 0 };

  data.forEach(item => {
      severityCounts['Severe'] += parseInt(item['Severe'], 10);
      severityCounts['Moderate'] += parseInt(item['Moderate'], 10);
      severityCounts['Light'] += parseInt(item['Light'], 10);
  });

  const trace = {
      x: Object.keys(severityCounts),
      y: Object.values(severityCounts),
      type: 'bar'
  };

  const layout = {
      title: 'Overstay Severity Counts',
      xaxis: { title: 'Severity' },
      yaxis: { title: 'Count' },
      paper_bgcolor: 'rgba(0,0,0,0)',
          plot_bgcolor: '#1a1e23',
          font: {
              color: '#fff' 
          },
          xaxis: {
              title: 'Time In',
              gridcolor: '#444', 
              linecolor: '#444',
              tickcolor: '#fff' 
          },
          yaxis: {
              title: 'Extra Time (Minutes)',
              gridcolor: '#444',
              linecolor: '#444',
              tickcolor: '#fff'
          },
          showlegend: false
  };

  // Plotly.newPlot('overstaySeverityBarChart', [trace], layout);
}
function createTimeInVsOverstaySeverityHeatmap(data) {
  const timeSlots = {};
  const severityLevels = ['Severe', 'Moderate', 'Light'];

  data.forEach(item => {
      const timeSlot = getTimeSlot(item['Time In']);
      if (!timeSlots[timeSlot]) {
          timeSlots[timeSlot] = { 'Severe': 0, 'Moderate': 0, 'Light': 0 };
      }
      severityLevels.forEach(level => {
          timeSlots[timeSlot][level] += parseInt(item[level], 10);
      });
  });

  const xValues = Object.keys(timeSlots);
  const yValues = severityLevels;
  const zValues = yValues.map(severity => xValues.map(timeSlot => timeSlots[timeSlot][severity]));

  const trace = {
      x: xValues,
      y: yValues,
      z: zValues,
      type: 'heatmap'
  };

  const layout = {
      title: 'Heatmap of Time In vs Overstay Severity',
      xaxis: { title: 'Time Slot' },
      yaxis: { title: 'Overstay Severity' },
      paper_bgcolor: 'rgba(0,0,0,0)',
          plot_bgcolor: '#1a1e23',
          font: {
              color: '#fff' 
          },
          xaxis: {
              title: 'Time In',
              gridcolor: '#444', 
              linecolor: '#444',
              tickcolor: '#fff' 
          },
          yaxis: {
              title: 'Extra Time (Minutes)',
              gridcolor: '#444',
              linecolor: '#444',
              tickcolor: '#fff'
          },
          showlegend: false
  };

  // Plotly.newPlot('timeInVsOverstaySeverityHeatmap', [trace], layout);
}
function getTimeSlot(timeIn) {
  const date = new Date(timeIn);
  const hours = date.getHours();
  const startTime = hours.toString().padStart(2, '0') + ':00';
  const endTime = (hours + 1).toString().padStart(2, '0') + ':00';
  return startTime + '-' + endTime;
}

function createTimeSeriesPlot(data) {
  const parsedData = data.map(item => ({
      timeIn: new Date(item['Time In']),
      totalHours: parseFloat(item['Total Hours (H)'])
  })).sort((a, b) => a.timeIn - b.timeIn);

  const trace = {
      x: parsedData.map(item => item.timeIn),
      y: parsedData.map(item => item.totalHours),
      mode: 'lines',
      type: 'scatter'
  };

  const layout = {
      title: 'Time Series of Time In vs Total Hours',
      xaxis: { title: 'Time In' },
      yaxis: { title: 'Total Hours' },
      paper_bgcolor: 'rgba(0,0,0,0)',
          plot_bgcolor: '#1a1e23',
          font: {
              color: '#fff' 
          },
          xaxis: {
              title: 'Time In',
              gridcolor: '#444', 
              linecolor: '#444',
              tickcolor: '#fff' 
          },
          yaxis: {
              title: 'Extra Time (Minutes)',
              gridcolor: '#444',
              linecolor: '#444',
              tickcolor: '#fff'
          },
          showlegend: false
  };

  Plotly.newPlot('timeSeriesDiv', [trace], layout);
}

function createAnomalyDetectionPlot(data) {
  const extraTimeData = data.map(item => {
      const extraTimeString = item['Extra Time (Minutes)'].trim();
      const extraTimeValue = parseFloat(extraTimeString);
      return isNaN(extraTimeValue) ? null : extraTimeValue;
  }).filter(item => item !== null); 

  const zScores = calculateZScores(extraTimeData);

  const anomalies = extraTimeData.filter((val, index) => Math.abs(zScores[index]) > 2);

  const trace = {
      x: data.map(item => new Date(item['Time In'])),
      y: extraTimeData,
      mode: 'markers',
      type: 'scatter',
      marker: {
          color: zScores.map(z => Math.abs(z) > 2 ? 'red' : 'blue'),
          size: 12
      },
      text: zScores.map((z, index) => `Z-score: ${z.toFixed(2)}, Extra Time: ${extraTimeData[index]}`)
  };

  const layout = {
      title: 'Anomaly Detection in Extra Time',
      xaxis: { title: 'Time In' },
      yaxis: { title: 'Extra Time (Minutes)' },
      showlegend: false,
      paper_bgcolor: 'rgba(0,0,0,0)',
          plot_bgcolor: '#1a1e23',
          font: {
              color: '#fff' 
          },
          xaxis: {
              title: 'Time In',
              gridcolor: '#444', 
              linecolor: '#444',
              tickcolor: '#fff' 
          },
          yaxis: {
              title: 'Extra Time (Minutes)',
              gridcolor: '#444',
              linecolor: '#444',
              tickcolor: '#fff'
          },
  };

  console.log("Extra Time Data:", extraTimeData);
console.log("Z-Scores:", zScores);
  Plotly.newPlot('anomalyDetectionDiv', [trace], layout);
}

  
function calculateZScores(data) {
  const mean = data.reduce((acc, val) => acc + val, 0) / data.length;
  const std = Math.sqrt(data.map(val => (val - mean) ** 2).reduce((acc, val) => acc + val, 0) / data.length);
  return data.map(val => (val - mean) / std);
}

document.addEventListener('DOMContentLoaded', async () => {
  const data = await loadCSVData('src/TestData.csv');	
  createOverstaySeverityBarChart(data);
  createTimeInVsOverstaySeverityHeatmap(data);
  createTimeSeriesPlot(data);
  createAnomalyDetectionPlot(data);
  
});


